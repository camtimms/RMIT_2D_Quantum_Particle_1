# Free Particle Evolution in 2D using the Schrödinger Equation

This repository contains Python code for simulating the free-particle time evolution in two-dimensional space using the time-dependent Schrödinger equation in momentum space.

The simulation visualizes how a Gaussian wave packet evolves over time. It uses a Fourier transform approach and plots the absolute value of the wave function at several time intervals.

## 📄 Contents

- `2D_Quantum_Particle_1.py`: The main Python script that runs the simulation.
- `Quantum_Physics_Comp_Report_1.pdf`: A report detailing the physics and computational methods used in this project.
- `example_code/`: A folder containing auxiliary code snippets used during development.
- `plots/`: A folder containing `.png` files of the visualized wavefunction over time.

## 🧠 Author

**Campbell Timms**

---

## 🧪 Project Description

The wave function of a free particle in 2D space is initialized as a normalized Gaussian function. It is evolved in time by applying the free-particle propagator in Fourier space.

The physical parameters include:

- Grid size: `N = 100`
- Real-space scaling: `L = 2`
- Gaussian width: `σ = 0.1`
- Time evolution step: `Δt = 200`
- Electron mass: `m ≈ 9.11 × 10⁻³¹ kg`
- Reduced Planck’s constant: `ħ ≈ 1.05 × 10⁻³⁴ J·s`
- Wave vector: `k = 100`

## 📊 Simulation Overview

The wave function is evolved using the following approach:

1. **Initialization**:
    - Create a 2D Gaussian wave packet centered in the grid.
    - Normalize the wave function.

2. **Fourier Transformation**:
    - Apply the 2D Fourier transform to switch to momentum space.
    - Construct a phase factor from the free-particle propagator.

3. **Time Evolution**:
    - Multiply by the phase factor in momentum space.
    - Inverse Fourier transform to return to real space.
    - Plot the probability density (magnitude squared of the wave function).

4. **Multiple Time Steps**:
    - Repeat the process to visualize wavefunction evolution over increasing times.

Each frame shows the wave function dispersing over time in arbitrary spatial units.

## 📷 Example Output

Output images are saved in the `plots/` folder. Each `.png` shows a heatmap of the wave function amplitude at different time steps.

## ▶️ How to Run

Ensure you have the following Python packages installed:

```bash
pip install numpy matplotlib
