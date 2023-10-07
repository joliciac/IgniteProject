
# class Task:
#     def __init__(self, description):
#         self.description = description
#         self.is_completed = False

# class ToDoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, task):
#         self.tasks.remove(task)

#     def list_tasks(self):
#         for i, task in enumerate(self.tasks, 1):
#             status = "Done" if task.is_completed else "Not Done"
#             print(f"{i}. [{status}] {task.description}")

#     def mark_completed(self, task):
#         task.is_completed = True

# def main():
#     todo_list = ToDoList()

#     while True:
#         print("\nTo-Do List Menu:")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. List Tasks")
#         print("4. Mark Task as Completed")
#         print("5. Quit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             description = input("Enter task description: ")
#             task = Task(description)
#             todo_list.add_task(task)
#         elif choice == "2":
#             todo_list.list_tasks()
#             task_index = int(input("Enter task number to remove: ")) - 1
#             task_to_remove = todo_list.tasks[task_index]
#             todo_list.remove_task(task_to_remove)
#         elif choice == "3":
#             todo_list.list_tasks()
#         elif choice == "4":
#             todo_list.list_tasks()
#             task_index = int(input("Enter task number to mark as completed: ")) - 1
#             task_to_complete = todo_list.tasks[task_index]
#             todo_list.mark_completed(task_to_complete)
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        print("\nTasks:")
        for i, task in enumerate(self.tasks, 1):
            status = "Done" if task.completed else "Not Done"
            print(f"{i}. [{status}] {task.description}")
            
    def remove_task(self, task):
        self.tasks.remove(task)

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True

    def recommend_resources(self, study_topic):
        resources = {
                   "Math": ["Khan Academy: Math Tutorials", "MIT OpenCourseWare: Introduction to Calculus"],
        "Programming": [
            "Codecademy: Learn Python",
            "edX: Java Programming Fundamentals",
            "Learn Python: Learnpython.org",
            "W3Schools: Python Tutorial",
            "Youtube - Programming with Mosh: https://youtu.be/kqtD5dpn9C8?si=Y4aYXevbIW_nLF3y ",
        ],
        "Python": [
            "Codecademy: Learn Python",
            "edX: Python for Data Science",
            "Python.org: Official Python Documentation",
            "Real Python: Python Tutorials",
            "Coursera - Python for Everybody: https://www.coursera.org/specializations/python",
        ],
        "Java": [
            "edX: Java Programming Fundamentals",
            "Java.com: Official Java Documentation",
            "Codecademy: Learn Java",
            "Coursera - Java Programming and Software Engineering Fundamentals: https://www.coursera.org/specializations/java-programming",
            "Youtube - Bro Code: https://youtu.be/xk4_1vDrzzo?si=bWYf7vC3mb26Zxws",
        ],
        "Web Development": [
            "MDN Web Docs: Web Development Tutorials",
            "W3Schools: Web Development Resources",
            "FreeCodeCamp: Full Stack Web Development Certification",
            "Coursera - Web Design for Everybody: https://www.coursera.org/specializations/web-design",
        ],
        "Database Management": [
            "Coursera - Database Management Essentials: https://www.coursera.org/specializations/database-management",
            "SQLZoo: Interactive SQL Tutorial",
            "w3resource: SQL Tutorial",
        ],
        "Software Design": [
            "Coursera - Software Design and Architecture: https://www.coursera.org/specializations/software-design-architecture",
            "Clean Code: A Handbook of Agile Software Craftsmanship (Book)",
            "Udacity - Software Architecture Nanodegree: https://www.udacity.com/course/software-architecture-nanodegree--nd803",
        ],
        "Data Structures and Algorithms": [
            "Coursera - Algorithms Specialization: https://www.coursera.org/specializations/algorithms",
            "GeeksforGeeks: Data Structures and Algorithms",
            "LeetCode: Coding Challenges and Algorithms Practice",
            "HackerRank: Data Structures and Algorithms",
        ],
        "Interview Questions": [
            "interview.io: https://interviewing.io/",
            "Book by Gayle Laackmann: Cracking the Coding Interview",

        ],
        }

        if study_topic in resources:
            print(f"\nRecommended Resources for {study_topic}:")
            for i, resource in enumerate(resources[study_topic], 1):
                print(f"{i}. {resource}")
        else:
            print("No recommendations available for this topic.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Complete Task")
        print("5. Get Study Recommendations")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.list_tasks()
        elif choice == "4":
            todo_list.list_tasks()
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == "5":
            study_topic = input("Enter your study topic: ")
            todo_list.recommend_resources(study_topic)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
