import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.notes = ""

    def mark_completed(self):
        self.completed = True

    def add_note(self, note):
        self.notes = note

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        notes_str = f" - Notes: {self.notes}" if self.notes else ""
        return f"[{status}] {self.description}{notes_str}"


class ToDoApp:
    def __init__(self):
        self.tasks = []
        self.history = []  # To keep track of changes for undo

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.history.append(("add", task))
        print("Task added successfully!")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.history.append(("complete", index))
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    def add_note_to_task(self, index, note):
        if 0 <= index < len(self.tasks):
            self.tasks[index].add_note(note)
            self.history.append(("note", index, self.tasks[index].notes))
            print("Note added to task!")
        else:
            print("Invalid task number!")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.history.append(("delete", removed_task))
            print("Task deleted successfully!")
        else:
            print("Invalid task number!")

    def undo_last_action(self):
        if not self.history:
            print("No actions to undo.")
            return

        action = self.history.pop()
        if action[0] == "add":
            self.tasks.remove(action[1])
            print("Undo: Task addition undone.")
        elif action[0] == "complete":
            self.tasks[action[1]].completed = False
            print("Undo: Task completion undone.")
        elif action[0] == "note":
            self.tasks[action[1]].notes = ""
            print("Undo: Task note undone.")
        elif action[0] == "delete":
            self.tasks.append(action[1])
            print("Undo: Task deletion undone.")

    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if not results:
            print("No tasks found with the given keyword.")
        else:
            print("\nSearch Results:")
            for task in results:
                print(task)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
            return
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def export_tasks(self, filename="tasks_export.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(str(task) + "\n")
        print(f"Tasks exported to {filename}")

    def show_statistics(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks if task.completed)
        print("\n--- Statistics ---")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        if total_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100
            print(f"Completion rate: {completion_rate:.2f}%")

    def run(self):
        while True:
            print("\n--- To-Do App ---")
            print("1. Add Task")
            print("2. Complete Task")
            print("3. Add Note to Task")
            print("4. Delete Task")
            print("5. Undo Last Action")
            print("6. Search Tasks")
            print("7. Show Tasks")
            print("8. Export Tasks")
            print("9. Show Statistics")
            print("10. Exit")
            choice = input("Choose an option (1-10): ")

            if choice == "1":
                description = input("Enter the task description: ")
                self.add_task(description)
            elif choice == "2":
                try:
                    index = int(input("Enter the task number to mark as completed: ")) - 1
                    self.complete_task(index)
                except ValueError:
                    print("Please enter a valid number!")
            elif choice == "3":
                try:
                    index = int(input("Enter the task number to add a note: ")) - 1
                    note = input("Enter the note: ")
                    self.add_note_to_task(index, note)
                except ValueError:
                    print("Please enter a valid number!")
            elif choice == "4":
                try:
                    index = int(input("Enter the task number to delete: ")) - 1
                    self.delete_task(index)
                except ValueError:
                    print("Please enter a valid number!")
            elif choice == "5":
                self.undo_last_action()
            elif choice == "6":
                keyword = input("Enter the keyword to search for: ")
                self.search_tasks(keyword)
            elif choice == "7":
                self.display_tasks()
            elif choice == "8":
                filename = input("Enter the filename to export tasks (default: tasks_export.txt): ")
                if not filename:
                    filename = "tasks_export.txt"
                self.export_tasks(filename)
            elif choice == "9":
                self.show_statistics()
            elif choice == "10":
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate and run the app
if __name__ == "__main__":
    app = ToDoApp()
    app.run()
