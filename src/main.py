from flask import Flask, request
from models.task import Task, CreateTaskSchema

app = Flask(__name__)

tasks = []

@app.get("/task")
def index_tasks():
    return tasks

@app.post("/task")
def store_task():
    data = request.get_json()

    parsedData = CreateTaskSchema.model_validate(data)

    id = tasks.__len__() + 1

    task = Task(
            id,
            parsedData.title,
            parsedData.description,
            parsedData.completed
            )

    tasks.append(task)

    print(tasks)

    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
