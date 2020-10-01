"""This module will contain classes for the various components which make up the CPU."""


class Register:
    """A CPU register."""

    def __init__(self):
        """Initialise Register."""
        self.value = 0

    def get(self):
        """Get value stored in register."""
        return self.value

    def set(self, value):
        """Set value stored in register."""
        self.value = value


class MemoryLocation:
    """A single location in memory."""

    def __init__(self):
        """Initialise class."""
        self.value = 0

    def get(self):
        """Get value in memory location."""
        return self.value

    def set(self, value):
        """Set value in memory location."""

