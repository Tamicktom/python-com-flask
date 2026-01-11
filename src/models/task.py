from pydantic import BaseModel

class CreateTaskSchema(BaseModel):
    title: str
    description: str
    completed: bool

class Task:
    def __init__(self, id, title, description, completed = False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
                "id": self.id,
                "title": self.title,
                "description": self.description,
                "completed" : self.completed
                }

if __name__ == "__main__":
    pass
