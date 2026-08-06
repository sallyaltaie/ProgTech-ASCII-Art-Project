from session import Session
from command_parser import CommandParser


def main():
    """Start the ASCII Art Studio."""
    
    session = Session()
    parser = CommandParser(session)

    print("============================")
    print("Welcome to ASCII Art Studio!")
    print("============================")
    print("Type a command or 'quit' to exit.")
    print()

    while True:
        command = input("Command: ")
        result = parser.execute(command)

        if result == "quit":
            break

        if result != "":
            print(result)

    print("Bye!")


if __name__ == "__main__":
    main()