"""Test cases for little_computer."""

import unittest
from little_computer.components import Register


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
