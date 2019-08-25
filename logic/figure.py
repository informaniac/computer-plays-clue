class Figure:
    """
    Representation of a game figure
    """

    def __init__(self, name, start_position):
        """
        Constructor

        :param name: name of the figure
        :type name: str
        :param start_position: initial position (room identifier) of the figure
        :type start_position: str
        """
        self.name = name
        self.position = start_position

    def __str__(self):
        return self.name

    def move_to(self, position):
        """

        :param position: new position (room) of the figure
        :type position: str
        """
        self.position = position
