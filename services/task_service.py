from repositories.task_repository import TaskRepository 
from services.models.task_rule import TaskRule

class TaskService:
    def __init__(self, repo: TaskRepository, rule: TaskRule):
        self.repo = repo
        self.rule = rule

    def create_task(self, user_id: int, title: str, description: str | None = None):
        tasks = self.repo.get_all()
        user_tasks = [t for t in tasks if t.user_id == user_id and not t.done]
        if len(user_tasks) >= self.rule.max_open_tasks_per_user:
            raise ValueError("Maximum open tasks reached for user")
        return self.repo.create(user_id, title, description)

    def get_tasks(self):
        return self.repo.get_all()

    def update_task(self, task_id: int, title=None, description=None, done=None):
        task = self.repo.get_by_id(task_id)
        if not task:
            return None

        if title is not None:
            task.title = title

        if description is not None:
             task.description = description

        if done is not None:
            task.done = done

        return self.repo.save(task)

    def delete_task(self, task_id: int):
        return self.repo.delete(task_id)