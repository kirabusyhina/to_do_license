from license_db import validate_license

def main_program():
    """
    Simple To-Do Manager (file-based).
    Stores tasks in tasks.txt located next to the executable (or script).
    """
    import os
    from pathlib import Path

    tasks_path = Path(os.getcwd()) / "tasks.txt"

    def load_tasks() -> list[str]:
        if not tasks_path.exists():
            return []
        lines = tasks_path.read_text(encoding="utf-8").splitlines()
        return [ln.strip() for ln in lines if ln.strip()]

    def save_tasks(tasks: list[str]) -> None:
        tasks_path.write_text("\n".join(tasks) + ("\n" if tasks else ""), encoding="utf-8")

    def show_tasks(tasks: list[str]) -> None:
        print("\n=== Your tasks ===")
        if not tasks:
            print("(No tasks yet)")
            return
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")

    while True:
        tasks = load_tasks()

        print("\n=== To-Do Manager ===")
        print("1) Add task")
        print("2) Show tasks")
        print("3) Delete task")
        print("4) Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            text = input("Task text: ").strip()
            if not text:
                print("Task cannot be empty.")
                continue
            tasks.append(text)
            save_tasks(tasks)
            print("Saved.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if not tasks:
                continue
            raw = input("Enter task number to delete: ").strip()
            try:
                idx = int(raw)
            except ValueError:
                print("Not a number.")
                continue
            if idx < 1 or idx > len(tasks):
                print("Invalid task number.")
                continue
            removed = tasks.pop(idx - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")

        elif choice == "4":
            print("Goodbye.")
            return

        else:
            print("Invalid option. Choose 1-4.")

def main():
    print("=== Licensed Application ===")
    user_email = input("Enter your email: ").strip()
    license_key = input("Enter license key: ").strip()

    ok, msg = validate_license(license_key, user_email)
    if not ok:
        print("\nACCESS DENIED:", msg)
        input("\nPress Enter to exit...")
        return

    print("\nACCESS GRANTED:", msg)
    main_program()
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
