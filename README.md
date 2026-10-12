# Harmonic Signal Generator

> A programmatic audio synthesis engine for generating uncompressed numerical waveforms and musical scales using mathematical pitch formulation and vectorized array processing.

---

## Overview / Value Proposition

Manual audio prototyping and procedural sound effect generation often require heavy third-party audio synthesis suites or bloated multimedia frameworks. This tool solves this operational friction by providing a transparent, dependency-minimal Python engine that calculates precise logarithmic pitch offsets and exports raw pulse-code modulation (PCM) audio streams directly to disk. It enables developers and sound engineers to programmatically generate test tones, musical scales, and raw acoustic buffers with complete control over sample rates and bit depths.

---

## Under the Hood / How It Works

The execution pipeline operates across three distinct computational stages:

1. **Pitch Calculation:** Frequencies are derived using the equal temperament tuning standard ($f = 440 \cdot 2^{n/12}$), converting semitone offsets relative to A4 into precise hertz values.
2. **Vectorized Waveform Generation:** Time domains are discretized using linear spacing arrays. Angular frequencies are computed and passed into trigonometric sine functions to construct continuous floating-point wave arrays spanning $[-1.0, 1.0]$.
3. **Quantization & PCM Export:** Floating-point amplitudes are scaled to signed 16-bit integer boundaries ($\pm 32767$), packed into binary byte structures using format strings (`<h`), and wrapped into standard uncompressed `.wav` containers via Python's built-in `wave` module.

---

## Key Features

* **Equal Temperament Frequency Resolution:** Dynamically maps arbitrary semitone intervals to precise acoustic frequencies.
* **Vectorized Array Operations:** Leverages high-performance array broadcasting for rapid sample generation.
* **Uncompressed Audio Serialization:** Converts floating-point buffers into standard 16-bit mono PCM wave files without lossy compression.
* **Modular Architecture:** Separates mathematical frequency calculation, wave synthesis, and file IO into distinct, testable functions[cite: 1].

---

## Tech Stack & Core Dependencies Breakdown

* **Python 3.10+:** Target runtime environment utilizing modern type hinting conventions.
* **`numpy`:** Selected for high-performance array manipulation, linear space generation, and efficient memory block concatenation.
* **`math`:** Utilized for high-precision transcendental operations (`math.sin`) and mathematical constants.
* **`wave` & `struct`:** Standard library modules responsible for container formatting, header writing, and binary byte packing.

---

## Environment & Web-Based Quick Start

You can run and test this repository entirely inside your browser using GitHub Codespaces without installing local development tooling.

### 1. Launch via GitHub Codespaces
Click the **Code** dropdown on the repository main page, select the **Codespaces** tab, and click **Create codespace on main**.

### 2. Manual Environment Setup (Terminal)
If operating inside a remote or virtual environment, execute the following commands:

```bash
# Clone the repository
git clone [https://github.com/your-username/harmonic-signal-generator.git](https://github.com/your-username/harmonic-signal-generator.git)
cd harmonic-signal-generator

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install numpy
```

### 3. Execution

Run the main script to generate the sample C Major scale audio file:

```bash
python main.py
```

This outputs a file named c_major_scale.wav in the root directory.

## Repository Structure

```bash
harmonic-signal-generator/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
├── main.py
└── c_major_scale.wav
```

## Roadmap

**[ ] Type Stubs & Strict Static Analysis:** Introduce strict mypy type checking configurations and comprehensive docstring annotations.

**[ ] Polyphonic Chord Synthesis:** Extend the generation pipeline to mix multiple frequency arrays simultaneously for chord progression rendering.

**[ ] Structured Logging Integration:** Replace standard print statements with formatted logging outputs to capture pipeline execution metrics and telemetry.