class TaskManager:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n--------------------------")
        print("1. View")
        print("2. Add")
        print("3. Mark Complete")
        print("4. Delete")
        print("5. Exit")
        print("\n")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to do.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def add_task(self):
        task = input("Enter a new task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def mark_complete(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to mark as complete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks.pop(task_num - 1)
                print("Task marked as complete!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks.pop(task_num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")
            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                self.add_task()
            elif choice == "3":
                self.mark_complete()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again!")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
