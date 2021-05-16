from librosa import stft
from numpy import conjugate, zeros_like


def get_mod_specgram(signal):
    """generate a modulation spectrogram, like Atlas(2003)"""
    D = stft(signal)
    D_conj = D * conjugate(D)
    P = zeros_like(D)
    ETA, OMEGA = P.shape
    max_row, max_column = D.shape
    for max_column in range(0, max_column):
        for eta in range(0, ETA):
            for omega in range(0, OMEGA):
                if omega - eta / 2 > 0 and omega + eta / 2 < max_column:
                    P[eta, omega] = P[eta, omega] + D[omega - eta / 2] * D_conj[omega + eta / 2]
    return P
