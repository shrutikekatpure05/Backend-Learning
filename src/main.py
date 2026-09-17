from fastapi import FastAPI

app = FastAPI()


@app.get("/api/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Complete API documentation"},
        {"id": 2, "title": "Test login endpoint"},
        {"id": 3, "title": "Fix dashboard bug"},
    ]


@app.get("/api/tasks/{task_id}")
def get_task(task_id: int):
    tasks = [
        {"id": 1, "title": "Complete API documentation"},
        {"id": 2, "title": "Test login endpoint"},
        {"id": 3, "title": "Fix dashboard bug"},
    ]

    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"message": "Task not found"}
