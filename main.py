from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

todos = []

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo added", "todo": todo}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_single(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}

@app.put("/todos/{todo_id}")
def update(todo_id: int, updated: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated
            return {"message": "Todo updated", "todo": updated}
    return {"message": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted"}
    return {"message": "Todo not found"}
