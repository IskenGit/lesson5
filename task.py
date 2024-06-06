class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False  # False означает, что задача не выполнена

    def mark_as_completed(self):
        self.status = True

    def __repr__(self):
        status = "Выполнено" if self.status else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
        print(f"Добавлена задача: {description} с сроком выполнения: {deadline}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print(f"Задача '{self.tasks[index].description}' отмечена как выполненная.")
        else:
            print("Неверный индекс задачи.")

    def get_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.status]
        return pending_tasks

    def display_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx}: {task}")

# Пример использования
manager = TaskManager()
manager.add_task("Закончить проект", "2024-06-15")
manager.add_task("Подготовить презентацию", "2024-06-10")

print("\nВсе задачи:")
manager.display_tasks()

print("\nОтметим первую задачу как выполненную.")
manager.mark_task_completed(0)

print("\nТекущие задачи:")
for task in manager.get_pending_tasks():
    print(task)
