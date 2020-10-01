"""Test cases for little_computer."""

import unittest
from little_computer.components import Register, MemoryLocation, Memory


class TestComponents(unittest.TestCase):
    """Test cases for little_computer.components."""

    def test_Register(self):
        """Test Register class."""
        a = Register()
        b = Register()

        a.set(5)

        self.assertEqual(a.get(), 5)

        a.set(6)
        b.set(2)

        self.assertEqual(a.get(), 6)
        self.assertEqual(b.get(), 2)

    def test_MemoryLocation(self):
        """Test MemoryLocation class."""
        a = MemoryLocation()
        b = MemoryLocation()

        a.set(13)
        b.set(256)

        self.assertEqual(a.get(), 13)
        self.assertEqual(b.get(), 256)

        b.set(5)

        self.assertEqual(b.get(), 5)

    def test_Memory(self):
        """Test Memory class."""
        a = Memory(10)

        a.set(5, 10)
        a.set(7, 45)
        a.set(3, 578)

        self.assertEqual(a.get(5), 10)
        self.assertEqual(a.get(7), 45)
        self.assertEqual(a.get(3), 578)

        with self.assertRaises(KeyError):
            a.set(10, 5)


if __name__ == "__main__":
    unittest.main()
