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
    if args.command == "remove" or args.command == "list" or args.command == "show" or args.command=="edit":

        return args, file_path
    string = f"""\n{args.title}:{args.content}"""
    return args, string, file_path


def checkIfRepeated(integer, filePath):
    with open(filePath, "r") as file:
        lines = file.readlines()
        num = 0
        for i in lines:

            num = num+1
            if type(integer) == int:
                if int(integer) > len(lines):
                    return "no"

                print(int(integer), num, i)
            return "yes "
            # return "yes"
        #     if i.split(":")[0] == string.split(":")[0]:
        #         return "yes"
        # return "no"


def add(name):
    with open(dataBase()[2], "a") as file:
        file.write(name)


def edit(num, content,filePath):
     if checkIfRepeated(num,filePath) == "yes":
            print(f"✅ Note number '{num}' updated successfully!")
     else:
         print(f"❌ Error: Note number '{num}' not found!")
     with open(filePath, "r") as file:
        lines = file.readlines() 
       
        with open(filePath, "w") as file:
            for line in lines:
                print("line",line)
                print(num)
                name = lines[num-1].split(":")[0]
                if line.startswith(name + ":"):  # Find the note
 
                    file.write(
                        f"\n {name}:{content} ")
                else:
                    file.write(line)  # Keep other lines unchanged

       


def remove(integer, filePath):
    if checkIfRepeated(integer, dataBase()[1]) == "no":
        print(f"❌ Error: Note number {integer} not found!")
        return

    else:
        if integer == "all":
            with open(filePath, "r") as file:
                lines = file.readlines()
            with open(filePath, "w") as file:
                file.writelines("")
                print(f"✅ everything removed succesfully")
                return

        with open(filePath, "r") as file:
            lines = file.readlines()
            name = lines[int(integer)-1]
            print(name, "namo")
            new_lines = [
                line for line in lines if not line.startswith(name.split(":")[0]+":")]
            print(new_lines, "new")
        with open(filePath, "w") as file:
            file.writelines(new_lines)
            print(
                f"✅ note {integer} `{name.split(":")[0]}` removed successfully!")


def listFn(filePath):
    with open(filePath, "r") as file:
        lines = file.readlines()
        num = 0
        for i in lines:
            num += 1
            print(num, i.split(":")[0])


def show(filePath, args):
    with open(filePath, "r") as file:
        lines = file.readlines()

        if args.number > len(lines):
            print(
                """this is a very big number there is no note to this number please write 
python3 engine.py list""".capitalize())
            return

        print(lines[args.number-1])


def start():
    if dataBase()[0].command == "add":
        add(dataBase()[1])
    if dataBase()[0].command == "edit":
        edit(dataBase()[0].number, dataBase()[0].content, dataBase()[1])
    if dataBase()[0].command == "remove":
        remove(dataBase()[0].title, dataBase()[1])
    if dataBase()[0].command == "list":
        listFn(dataBase()[1])
    if dataBase()[0].command == "show":
        show(dataBase()[1], dataBase()[0])


start()
