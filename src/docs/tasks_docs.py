class TaskMetadata:
    class Create:
        summary = "Create a new task"
        description = "Add a new task to the task list."

    class List:
        summary = "List all tasks"
        description = "Retrieve a list of all existing tasks."

task_metadata = TaskMetadata()

task_fields = {
    "title": "Short title of the task",
    "description": "Detailed description of the task",
    "completed": "Completion status of the task",
}

task_example = {
    "title": "Write migration scripts",
    "description": "Create Alembic migrations for initial schema",
    "completed": False,
}