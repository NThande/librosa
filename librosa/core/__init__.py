#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Core IO and DSP
===============

Audio loading
-------------
.. autosummary::
    :toctree: generated/

    load
    stream
    to_mono
    resample
    get_duration
    get_samplerate

Time-domain processing
----------------------
.. autosummary::
    :toctree: generated/

    autocorrelate
    lpc
    zero_crossings
    mu_compress
    mu_expand

Signal generation
-----------------
.. autosummary::
    :toctree: generated/

    clicks
    tone
    chirp

Spectral representations
------------------------
.. autosummary::
    :toctree: generated/

    stft
    istft
    reassigned_spectrogram

    cqt
    icqt
    hybrid_cqt
    pseudo_cqt

    vqt

    iirt

    fmt

    magphase

Phase recovery
--------------
.. autosummary::
    :toctree: generated/

    griffinlim
    griffinlim_cqt


Harmonics
---------
.. autosummary::
    :toctree: generated/

    interp_harmonics
    salience

    phase_vocoder


Magnitude scaling
-----------------
.. autosummary::
    :toctree: generated/

    amplitude_to_db
    db_to_amplitude
    power_to_db
    db_to_power

    perceptual_weighting
    frequency_weighting
    multi_frequency_weighting
    A_weighting
    B_weighting
    C_weighting
    D_weighting

    pcen

Time unit conversion
--------------------
.. autosummary::
    :toctree: generated/

    frames_to_samples
    frames_to_time
    samples_to_frames
    samples_to_time
    time_to_frames
    time_to_samples

    blocks_to_frames
    blocks_to_samples
    blocks_to_time

Frequency unit conversion
-------------------------
.. autosummary::
    :toctree: generated/

    hz_to_note
    hz_to_midi
    midi_to_hz
    midi_to_note
    note_to_hz
    note_to_midi

    key_to_notes
    key_to_degrees

    hz_to_mel
    hz_to_octs
    mel_to_hz
    octs_to_hz

    A4_to_tuning
    tuning_to_A4


Frequency range generation
--------------------------
.. autosummary::
    :toctree: generated/

    fft_frequencies
    cqt_frequencies
    mel_frequencies
    tempo_frequencies
    fourier_tempo_frequencies


Pitch and tuning
----------------
.. autosummary::
    :toctree: generated/

    estimate_tuning
    pitch_tuning
    piptrack


Miscellaneous
-------------
.. autosummary::
    :toctree: generated/

    samples_like
    times_like

    get_fftlib
    set_fftlib
"""

from .time_frequency import *  # pylint: disable=wildcard-import
from .audio import *  # pylint: disable=wildcard-import
from .spectrum import *  # pylint: disable=wildcard-import
from .pitch import *  # pylint: disable=wildcard-import
from .constantq import *  # pylint: disable=wildcard-import
from .harmonic import *  # pylint: disable=wildcard-import
from .fft import *  # pylint: disable=wildcard-import


__all__ = [_ for _ in dir() if not _.startswith('_')]
