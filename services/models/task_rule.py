from dataclasses import dataclass

@dataclass(slots=True)
class TaskRule:
    max_open_tasks_per_user: int = 20