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
        if type(value) == int:
            self.value = value
        else:
            raise ValueError("Only integers can be stored in registers. " + str(value) + " is of type " +
                             type(value).__name__)


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
        if type(value) == int:
            self.value = value
        else:
            raise ValueError("Only integers can be stored in memory. "+str(value)+" is of type "+type(value).__name__)


class Memory:
    """A Memory Bank."""

    def __init__(self, size=100):
        """Initialise memory."""
        self.size = size
        self.values = []

        for n in range(size):
            self.values.append(MemoryLocation())

    def get(self, address):
        """Get value from memory."""
        if address >= self.size or address < 0:
            raise KeyError("Attempted to read memory location "+str(address)+" in memory of size "+str(self.size))
        return self.values[address].get()

    def set(self, address, value):
        """Set value in memory."""
        if address >= self.size or address < 0:
            raise KeyError("Attempted to write memory location "+str(address)+" in memory of size "+str(self.size))
        self.values[address].set(value)
