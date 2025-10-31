# Define task processing - Backup | Update | Analytics | Clean Logs

class TaskQueue:
    def __init__(self):
        self.task = []
    
    def add_task(self, task):
        print(f"Adding task: {task}")
        self.task.append(task)

    def process_task(self):
        while self.task:
            task = self.task.pop(0)
            print(f"Processing task: {task}")
        print("All Task processed...")

def main():
    task_queue = TaskQueue()
    tasks = ["Backup Database", "Update Software", "Run Analytics", "Clean Logs"]

    for task in tasks:
        task_queue.add_task(task)

    task_queue.process_task()

if __name__ == "__main__":
    main()

# Example
# task_queue = TaskQueue()
# task_queue.add_task("Backup Database")
# task_queue.add_task("Update Software")
# task_queue.process_task()

