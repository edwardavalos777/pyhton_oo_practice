"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    class SerialGenerator:
        """A machine to create unique incrementing serial numbers.

    Attributes:
        start (int): The starting value of the serial number.

    Methods:
        generate(): Generates the next serial number and returns it.
        reset(): Resets the serial number back to its starting value.
    """

    def __init__(self, start=0):
         """Initializes the serial number with the given start value.

        Args:
            start (int): The starting value of the serial number.
        """
         self.serial_number = start

    def generate(self):
        """Generates the next serial number and returns it."""
        serial = self.serial_number
        self.serial_number += 1
        return serial

    def reset(self):
        """Resets the serial number back to its starting value."""
        self.serial_number = 0


    serial = SerialGenerator(start=100)

    serial_number = serial.generate()

    serial.reset()

