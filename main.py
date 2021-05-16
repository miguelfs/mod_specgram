"""main file"""
from audiosignal import AudioSignal


def main():
    """ do all the stuff :) """
    fs = 8000
    mod_freq = 2
    carr_freq = 800
    modulator = AudioSignal(fs, mod_freq, 1, 4)
    carrier = AudioSignal(fs, carr_freq, 1, 4)


if __name__ == "__main__":
    main()
