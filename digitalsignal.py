"""digital signal file."""


class DigitalSignal:
    """digital signal most basic abstraction."""
    signal_as_array: [float]

    def __init__(self, sample_rate: float):
        self.sample_rate = sample_rate

    def set_signal_array(self, signal):
        """overwrite signal array value"""
        self.signal_as_array = signal
