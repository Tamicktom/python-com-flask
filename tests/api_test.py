import requests

BASE_URL="http://localhost:5000"

tasks = []

class TestClass:
    def test_create_task(self):
        body = {
                "title": "title de teste",
                "description": "description de teste",
                "completed": False
                }

        response = requests.post(f"{BASE_URL}/tasks", json=body)

        assert response.status_code == 201
        
        response_json = response.json()

        assert "message" in response_json
        assert "id" in response_json

        tasks.append(response_json["id"])

    def test_get_tasks(self):
        response = requests.get(f"{BASE_URL}/tasks")
        assert response.status_code == 200

        response_json = response.json()

        assert "tasks" in response_json
        assert "total" in response_json

    def test_get_task(self):
        if tasks:
            task_id = tasks[0]
            response = requests.get(f"{BASE_URL}/tasks/{task_id}")
            assert response.status_code == 200

            response_json = response.json()

            assert "id" in response_json
            response_task_id = response_json["id"]
            assert response_task_id == task_id
            assert "title" in response_json
            assert "description" in response_json
            assert "completed" in response_json

    def test_update_task(self):
        if tasks:
            task_id = tasks[0]
            
            body = {
                    "title": "task atualizada",
                    "description": "task atualizada na descrição",
                    "completed": True
                    }

            response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=body)
            assert response.status_code == 200

            response_json = response.json()

            assert "id" in response_json
            response_task_id = response_json["id"]
            assert response_task_id == task_id

            assert "title" in response_json
            response_task_title = response_json["title"]
            assert response_task_title == body["title"]

            assert "description" in response_json
            response_task_description = response_json["description"]
            assert response_task_description == body["description"]

            assert "completed" in response_json
            response_task_completed = response_json["completed"]
            assert response_task_completed == body["completed"]

    def test_delete_task(self):
        if tasks:
            task_id = tasks[0]

            response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
            assert response.status_code == 200
