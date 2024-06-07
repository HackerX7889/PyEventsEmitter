DEFAULT_LISTNER_COUNT = 10

class Disposable:
    """
    Represents a disposable object.
    """
    pass

class AbortSignal:
    """
    Represents an abort signal.

    This class is used to indicate whether an operation should be aborted.
    """

    def __init__(self, aborted: bool):
        """
        Initializes a new instance of the AbortSignal class.

        Args:
            aborted (bool): True if the operation should be aborted; otherwise, False.
        """
        self.aborted = aborted