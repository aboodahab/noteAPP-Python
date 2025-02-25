import argparse
from pathlib import Path


def welcome():
    file_path = Path("notes.txt")
    file_path.touch(exist_ok=True)  # إنشاء الملف إذا لم يكن موجودًا

    print(f"welcome in notes.py")


welcome()


def dataBase():
    file_path = "notes.txt"


    parser = argparse.ArgumentParser(
        description="simple notes app made by python!")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="adds new note")
    add_parser.add_argument("title", type=str, help="new note title")
    add_parser.add_argument("content", type=str, help="the new note content")

    remove_parser = subparsers.add_parser("remove", help="remove note ")
    remove_parser.add_argument(
        "title", type=str, help="title of removed note")

    edit_parser = subparsers.add_parser("edit", help="edit note")
    edit_parser.add_argument("title", type=str, help="title of the note")
    edit_parser.add_argument(
        "content", type=str, help="the new content of the edit note")

    args = parser.parse_args()
    if args.command == "remove":

        return args, file_path
    string = f"""{args.title}:"{args.content}"\n"""
    return args, string, file_path


def checkIfRepeated(string, filePath):
    with open(filePath, "r") as file:
        for i in file.readlines():
            if i.split(":")[0] == string.split(":")[0]:
                print("yes")
                return "yes"
        print("no")
        return "no"


def add(name):
    if checkIfRepeated(name, dataBase()[2]) == "yes":
        print("this title is used!!")
        with open(dataBase()[2], "r") as file:
            print(file.readlines())
        return

    with open(dataBase()[2], "a") as file:
        file.write(name)
    with open(dataBase()[2], "r") as file:
        print(file.readlines())


def edit(name, content):
    with open(dataBase()[2], "r") as file:
        lines = file.readlines()  # Read all lines

        with open(dataBase()[2], "w") as file:
            for line in lines:
                if line.startswith(name + ":"):  # Find the note

                    file.write(
                        f"{name}: {content}\n")
                else:
                    file.write(line)  # Keep other lines unchanged

        if checkIfRepeated(dataBase()[1], dataBase()[2]) == "yes":
            print(f"✅ Note '{name}' updated successfully!")
        else:
            print(f"❌ Error: Note '{name}' not found!")


def remove(name, filePath):
    if checkIfRepeated(name, dataBase()[1]) == "no":
        print(f"❌ Error: Note '{name}' not found!")
        return
    else:

        with open(filePath, "r") as file:
            lines = file.readlines()
            new_lines = [
                line for line in lines if not line.startswith(name+":")]
            print(new_lines, "new")
        with open(filePath, "w") as file:
            file.writelines(new_lines)
            print(f"✅ note {name} removed successfully!")


def start():
    if dataBase()[0].command == "add":
        add(dataBase()[1])
    if dataBase()[0].command == "edit":
        edit(dataBase()[0].title, dataBase()[0].content)
    if dataBase()[0].command == "remove":
        remove(dataBase()[0].title, dataBase()[1])


start()
