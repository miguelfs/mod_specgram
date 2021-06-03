# (wip) TCC - Modulation Spectrogram Transform

### How this repository is organized:
___
- `poc/` : Holds Jupyter Notebooks sandboxes
- `lib/`: Implementation. Basically taking what works from `poc/` and making a package of it.
- `samples/`: Short audio samples.


### How to run it:
___
There's a `requirements.txt` file with all the used packages and subsequent versions.
I recommend using `venv` to open it. You can follow the instructions [here][1].

### References:
___

[Exploitation of Spectral Redundancy in Cyclostationary Signals (1991), Gardner](https://ui.adsabs.harvard.edu/abs/1991ISPM....8...14G/abstract)

[A Scalable and Progressive Audio Codec (2001), Atlas](https://ieeexplore.ieee.org/document/940358)

[Joint Acoustic and Modulation Frequency (2003), Atlas](https://link.springer.com/article/10.1155/S1110865703305013)

[Feasability of single channel speaker separation on modulation frequency analysis (2007), Schimmel & Atlas](https://www.semanticscholar.org/paper/Feasibility-of-Single-Channel-Speaker-Separation-on-Schimmel-Atlas/18fa2fd19a602757853c9fd3b454625d4df87ef7)

[Amplitude Modulation Spectrogram based features for robust speech recognition in noisy and reverberant environments (2011), Moritz](https://ieeexplore.ieee.org/document/5947602)

[Fundamentals of Music Processing: Audio, Analysis, Algorithms, Applications (2016), Muller](https://www.springer.com/gp/book/9783319357652#otherversion=9783319219448)

[1]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/