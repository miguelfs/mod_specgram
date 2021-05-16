"""signal file."""

from enum import Enum
from numpy import sin, pi, arange

from digitalsignal import DigitalSignal


class Shape(Enum):
    """pre-defined common signal shapes"""
    SINE = 1


class AudioSignal(DigitalSignal):
    """audio signal abstraction. duration must be in seconds."""

    def __init__(self, sample_rate: float, frequency: float, amplitude: float, duration: float):
        super().__init__(sample_rate)
        self.frequency = frequency
        self.amplitude = amplitude
        self.shape = Shape.SINE
        self.duration = duration
        self.signal_as_array = self.get_signal()

    def get_signal(self):
        """generate an array signal"""
        if self.shape != Shape.SINE:
            raise Exception("not mapped shape. lol.")
        n = self.sample_rate * self.duration
        t = arange(n) / self.sample_rate
        return self.amplitude * sin(2 * pi * self.frequency * t)
