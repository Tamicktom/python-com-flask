import pytest
import requests

BASE_URL="http://localhost:5000"

tasks = []

class TestClass:
    def test_create_task(self):
        task = {
                "title": "task de teste",
                "description": "description de teste",
                "completed": False
                }

        response = requests.post(f"{BASE_URL}/tasks", json=task)

        assert response.status_code == 201
        print(response)
