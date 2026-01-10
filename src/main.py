from flask import Flask, jsonify, request
from models.task import Task, CreateTaskSchema

app = Flask(__name__)

tasks = []

@app.get("/task")
def index_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
            "tasks": task_list,
            "total": len(tasks)
            }

    return jsonify(output)

@app.post("/task")
def store_task():
    data = request.get_json()

    parsedData = CreateTaskSchema.model_validate(data)

    id = len(tasks) + 1

    task = Task(
            id,
            parsedData.title,
            parsedData.description,
            parsedData.completed
            )

    tasks.append(task)

    print(tasks)

    return jsonify({
        "message": "Task criada com sucesso"
        })

if __name__ == "__main__":
    app.run(debug=True)
