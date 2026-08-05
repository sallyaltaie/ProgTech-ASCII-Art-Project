# Den tar text från användare
# load image cat.png as cat
# session.load_image(...)

class CommandParser:
    """ Parse and execute commands for ASCII Art Studio """

    def __init__(self, session):
        """ Initialize a parser connected to a session."""
        self.session = session

    def execute(self, command):
        """ Parse and execute one command. """
        words = command.split()

        if len(words) == 0:
            return ""

        command_name =  words[0]

        if command_name == "info":
            return self.session.info()

        if command_name == "render":
            return self._execute_render(words)

        return "Unknown command"

    def _execute_render(self, words):
        """ Execute a render command. """
        if len(words) == 1:
            return self.session.render()

        if len(words) == 2:
            return self.session.render(words[1])

        return "Invalid render command."