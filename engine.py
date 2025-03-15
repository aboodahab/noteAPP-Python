import argparse
from pathlib import Path


def welcome():
    file_path = Path("notes.txt")
    file_path.touch(exist_ok=True)
# makes new file if the file doesn't exsit
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
    list_parser = subparsers.add_parser(
        "list", help="shows the notes without the content ")

    remove_parser = subparsers.add_parser("remove", help="remove note ")
    remove_parser.add_argument(
        "title", type=str, help="title of removed note")

    edit_parser = subparsers.add_parser("edit", help="edit note")
    edit_parser.add_argument("number", type=int, help="number of the  note")
    edit_parser.add_argument(
        "content", type=str, help="the new content of the edit note")
    show_parser = subparsers.add_parser("show")
    show_parser.add_argument(
        "number", type=int, help="number of the note that is removed")
    args = parser.parse_args()
    if args.command == "remove" or args.command == "list" or args.command == "show" or args.command == "edit":

        return args, file_path
    string = f"""\n{args.title}:{args.content}"""
    return args, string, file_path


def readFile(filePath):
    with open(filePath, "r") as file:
        lines = file.readlines()
    return lines


def getNumNotes(content):
    size = len(content)
    print(size)
    return size


def noteIndexExists(content, integer):
    for line in content:
        nameOfNote = line.split(":")[0]
        integerNoteName = content[integer-1].split(":")[0]
        if nameOfNote == integerNoteName:
            print(nameOfNote, integerNoteName)
            return True


def add(name):
    with open(dataBase()[2], "a") as file:
        file.write(name)


def edit(num, content, filePath):
    if num > getNumNotes(readFile(dataBase()[1])):
        print("that is a very big note number please type (python3 engine.py list) to know the notes and their number")
        return
    if noteIndexExists(readFile(filePath), num) == True:
        print(f"✅ Note number '{num}' updated successfully!")
    else:
        print(f"❌ Error: Note number '{num}' not found!")
    with open(filePath, "r") as file:
        lines = file.readlines()

        with open(filePath, "w") as file:
            for line in lines:
                name = lines[num-1].split(":")[0]
                if line.startswith(name + ":"):  # Find the note

                    file.write(f"{name}:{content}\n")
                else:
                    file.write(line)  # Keep other lines unchanged


def remove(integer, filePath):

    if integer == "all":
        with open(filePath, "w") as file:
            file.writelines("")
            print(f"✅ everything removed succesfully")
            return
    if noteIndexExists(readFile(dataBase()[1]), int(integer)) != True:
        print(f"❌ Error: Note number {integer} not found!")
        return

    else:

        with open(filePath, "r") as file:
            lines = file.readlines()
            name = lines[int(integer)-1]
            new_lines = [
                line for line in lines if not line.startswith(name.split(":")[0]+":")]
        with open(filePath, "w") as file:
            file.writelines(new_lines)
            print(
                f"✅ note {integer} `{name.split(":")[0]}` removed successfully!")


def listFn():

    num = 0
    for i in readFile(dataBase()[1]):
        num += 1
        print(num, i.split(":")[0].strip())


def show(args):

    if args.number > len(readFile(dataBase()[1])):
        print(
            """this is a very big number there is no note to this number please write 
python3 engine.py list""".capitalize())
        return

    print(readFile(dataBase()[1])[args.number-1])


def start():
    if dataBase()[0].command == "add":
        add(dataBase()[1])
    if dataBase()[0].command == "edit":
        edit(dataBase()[0].number, dataBase()[0].content, dataBase()[1])
    if dataBase()[0].command == "remove":
        remove(dataBase()[0].title, dataBase()[1])
    if dataBase()[0].command == "list":
        listFn()
    if dataBase()[0].command == "show":
        show(dataBase()[0])


start()
