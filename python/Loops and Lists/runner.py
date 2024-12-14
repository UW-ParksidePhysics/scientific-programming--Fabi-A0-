import os

def list_files(extension=".py"):
    """Lists all files with the given extension in the current directory."""
    return [f for f in os.listdir() if f.endswith(extension)]

def main():
    files = list_files(".py")
    if not files:
        print("No Python files found.")
        return

    print("Select a file to run:")
    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")

    try:
        choice = int(input("\nEnter the number of the file to run: ")) - 1
        if 0 <= choice < len(files):
            os.system(f"python3 {files[choice]}")
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()
