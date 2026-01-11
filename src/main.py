from flask import Flask, jsonify, request
from models.task import Task, CreateTaskSchema

app = Flask(__name__)

tasks = []
task_id = 0

@app.get("/tasks")
def index_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
            "tasks": task_list,
            "total": len(tasks)
            }

    return jsonify(output)

@app.get("/tasks/<int:id>")
def show_task(id: int):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Task não encontrada"}), 404

@app.put("/tasks/<int:id>")
def update_task(id: int):
    task: None | CreateTaskSchema = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if (task is None):
        return jsonify({"message": "Task não encontrada"}), 404

    data = request.get_json()

    parsedData = CreateTaskSchema.model_validate(data)

    task.title = parsedData.title
    task.description = parsedData.description
    task.completed = parsedData.completed

    return jsonify({"message": "Task atualizado com sucesso"}), 200

@app.post("/tasks")
def store_task():
    data = request.get_json()

    parsedData = CreateTaskSchema.model_validate(data)

    id = task_id + 1

    task = Task(
            id,
            parsedData.title,
            parsedData.description,
            parsedData.completed
            )

    tasks.append(task)

    return jsonify({
        "message": "Task criada com sucesso",
        "id": task.id
        }), 201

@app.delete("/tasks/<int:id>")
def delete_task(id: int):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            break

    return jsonify({
        "message": "Task deletada com sucesso"
        })

if __name__ == "__main__":
    app.run(debug=True)
