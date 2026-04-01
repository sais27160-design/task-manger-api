from sqlalchemy.orm import Session
from .models.task_orm import TaskORM

class TaskRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def create(self, user_id: int, title: str, description: str | None):
        task = TaskORM(user_id=user_id, title=title, description=description, done=False)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_all(self):
        return self.db.query(TaskORM).all()

    def update(self, task_id: int, done: bool):
        task = self.db.get(TaskORM, task_id)
        if task:
            task.done = done
            self.db.commit()
            self.db.refresh(task)
        return task

    def delete(self, task_id: int):
        task = self.db.get(TaskORM, task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
        return task
    
    def get_by_id(self, task_id: int):
        return self.db.query(TaskORM).filter(TaskORM.id == task_id).first()


    def save(self, task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task