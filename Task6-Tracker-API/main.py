from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from typing import Annotated
from typing import List, Optional
from datetime import date, datetime
from uuid import UUID, uuid4

app = FastAPI()

# In-memory storage
users_db = {}
tasks_db = {}

# ----------------------------
# 🧩 Pydantic Models
# ----------------------------
class UserCreate(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20)]
    email: EmailStr
    email: EmailStr

class UserRead(BaseModel):
    id: UUID
    username: str
    email: EmailStr

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: UUID

    @validator('due_date')
    def due_date_must_be_future(cls, v):
        if v < date.today():
            raise ValueError("Due date must be today or in the future")
        return v

class Task(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    due_date: date
    status: str
    user_id: UUID

class TaskStatusUpdate(BaseModel):
    status: str

    @validator("status")
    def validate_status(cls, v):
        allowed = {"pending", "in-progress", "completed"}
        if v not in allowed:
            raise ValueError(f"Status must be one of {allowed}")
        return v

# ----------------------------
# 🧑‍💻 User Endpoints
# ----------------------------

@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    user_id = uuid4()
    user_data = UserRead(id=user_id, **user.dict())
    users_db[user_id] = user_data
    return user_data

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: UUID):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ----------------------------
# ✅ Task Endpoints
# ----------------------------

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    if task.user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    task_id = uuid4()
    task_data = Task(
        id=task_id,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status="pending",
        user_id=task.user_id
    )
    tasks_db[task_id] = task_data
    return task_data

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: UUID):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: UUID, update: TaskStatusUpdate):
    task = tasks_db.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.status = update.status
    tasks_db[task_id] = task
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: UUID):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return [task for task in tasks_db.values() if task.user_id == user_id]
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    task = tasks_db.pop(task_id, None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task