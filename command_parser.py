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

        if command_name == "load":
            return self._execute_load(words)

        if command_name == "set":
            return self._execute_settings(words)

        if command_name == "render":
            return self._execute_render(words)

        if command_name == "save":
            return self._execute_save(words)

        if command_name == "quit":
            return "quit"
            
        return "Unknown command"

    def _execute_load(self, words):
        """ Execute a load image command."""

        if len(words) == 3:
            object_type = words[1]
            filename = words[2]

            if object_type == "image":
                self.session.load_image(filename)
                return "Image loaded."

            if object_type == "session":
                self.session.load_session(filename)
                return "Session loaded."

        if len(words) == 5:
            object_type = words[1]
            filename = words[2]
            keyword = words[3]
            alias = words[4]

            if object_type == "image" and keyword == "as":
                 self.session.load_image(filename, alias)
                 return "Image loaded."

            return "Invalid load command."

    def _execute_set(self, words):
        """Execute a set command."""

        if len(words) == 4:
            image_key = words[1]
            setting = words[2]
            value = words[3]

            try:
                if setting == "width" or setting == "height":
                    value = int(value)
                else:
                    value = float(value)

            except ValueError:
                return "Value must be a number."

            return self.session.set_image_settings(image_key, setting, value)
        
        return "Invalid set command."

    def _execute_render(self, words):
        """ Execute a render command. """

        if len(words) == 1:
            return self.session.render()

        if len(words) == 2:
            image_key = words[1]
            return self.session.render(image_key)

        if len(words) == 4:
            image_key = words[1]
            keyword = words[2]
            filename = words[3]

            if keyword == "to":
                return self.session.render_to_file(image_key, filename)

        return "Invalid render command."

    def _execute_save(self, words):
        """Execute a save session command."""

        if len(words) == 4:
            object_type = words[1]
            keyword = words[2]
            filename = words[3]

            if object_type == "session" and keyword == "as":
                self.session.save_session(filename)
                return "Session saved."

        return "Invalid save command."