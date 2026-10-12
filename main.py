import math
import struct
import wave

import numpy as np


def note_to_freq(note_offset: int, base_freq: float = 440.0) -> float:
    """Calculates pitch frequency in Hz using equal temperament formula:

    f = base_freq * (2 ** (n / 12))
    """
    return base_freq * (2.0 ** (note_offset / 12.0))


def generate_sine_wave(
    frequency: float, duration: float, sample_rate: int = 44100
) -> np.ndarray:
    """Generates a continuous sine wave array for a given frequency and duration."""
    # Compute total samples and time array
    total_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, total_samples, endpoint=False)

    # Calculate floating-point sine wave values using math.sin in a vector-friendly way
    # sin(2 * pi * f * t)
    angular_freq = 2.0 * math.pi * frequency
    waveform = np.sin(angular_freq * t)

    return waveform


def export_wav(
    filename: str, waveform: np.ndarray, sample_rate: int = 44100
) -> None:
    """Normalizes floating-point audio data (-1.0 to 1.0) and exports to 16-bit .wav."""
    # Scale float values (-1.0 to 1.0) to 16-bit signed integer range (-32767 to 32767)
    max_amplitude = 32767
    scaled_data = (waveform * max_amplitude).astype(np.int16)

    # Open .wav file for writing (1 channel, 2 bytes per sample, 44.1kHz)
    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit (2 bytes)
        wav_file.setframerate(sample_rate)

        # Convert integers to raw binary PCM data
        raw_bytes = bytearray()
        for sample in scaled_data:
            raw_bytes.extend(struct.pack("<h", sample))

        wav_file.writeframes(raw_bytes)


def main():
    sample_rate = 44100  # Standard CD-quality audio rate
    note_duration = 0.5  # Half-second per note

    # Define a simple C Major Scale relative to A4 (440 Hz)
    # Semitone offsets relative to A4 (A4 = 0)
    c_major_offsets = {
        "C4": -9,
        "D4": -7,
        "E4": -5,
        "F4": -4,
        "G4": -2,
        "A4": 0,
        "B4": 2,
        "C5": 3,
    }

    print("Generating C Major Scale audio...")
    audio_segments = []

    for note, offset in c_major_offsets.items():
        freq = note_to_freq(offset)
        print(f"Synthesizing {note}: {freq:.2f} Hz")
        wave_data = generate_sine_wave(freq, note_duration, sample_rate)
        audio_segments.append(wave_data)

    # Concatenate all note arrays into one continuous stream
    full_song = np.concatenate(audio_segments)

    # Save to file
    output_filename = "c_major_scale.wav"
    try:
        export_wav(output_filename, full_song, sample_rate)
        print(f"\nSuccess! Audio saved to '{output_filename}'")
    except OSError as e:
        print(f"Error saving wave file: {e}")


if __name__ == "__main__":
    main()
