"""
Radioactive Decay Simulator
Author: Derek Dong Han Li

Compare theoretical radioactive decay with a random simulation.

Use the same time unit for half-life, duration, and time step.
"""

import numpy as np
import matplotlib.pyplot as plt
import math


def calculate_decay_constant(half_life):
    """Calculate decay constant: lambda = ln(2) / half-life."""
    x = math.log(2) / half_life
    return x


def theoretical_decay(initial_atoms, decay_constant, times):
    """Calculate expected remaining atoms: N(t) = N0 * exp(-lambda * t)."""
    l = []
    for t in times:
        l.append(initial_atoms * math.exp(-decay_constant * t))
    return np.array(l)


def simulate_decay(initial_atoms, decay_constant, times, seed=42):
    """Simulate how many atoms remain at each time."""
    rng = np.random.default_rng(seed)

    remaining = np.zeros(len(times), dtype=int)
    remaining[0] = initial_atoms

    for index in range(1, len(times)):
        time_step = times[index] - times[index - 1]

        # Formula: probability = 1 - exp(-lambda * time_step)
        prob = 1 - math.exp(-decay_constant * time_step)

        # Use rng.binomial(previous_atom_count, probability).
        previous_atoms = remaining[index - 1]
        decayed_atoms = rng.binomial(previous_atoms, prob)

        remaining[index] = previous_atoms - decayed_atoms

    return remaining


def plot_results(times, theoretical, simulated, time_unit):
    """Plot the theoretical curve and simulated atom counts."""
    plt.figure(figsize=(10, 6))

    plt.plot(times, theoretical, label="Theoretical", linewidth=2)
    plt.step(
        times,
        simulated,
        where="post",
        label="Simulated",
        linestyle="--",
        alpha=0.8
    )

    plt.xlabel(f"Time ({time_unit})")
    plt.ylabel("Remaining atoms")
    plt.title("Radioactive Decay: Theory and Simulation")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def export_results(times, theoretical, simulated):
    """Save time, theoretical counts, and simulated counts to CSV."""
    results = np.column_stack((times, theoretical, simulated))

    np.savetxt(
        "results.csv",
        results,
        delimiter=",",
        header="time,theoretical_atoms,simulated_atoms",
        comments="",
        fmt=["%.6f", "%.6f", "%d"]
    )


def validate_model():
    """Check known decay results and basic simulation constraints."""
    initial_atoms = 1000
    half_life = 10.0
    decay_constant = calculate_decay_constant(half_life)

    times = np.array([0.0, half_life, 2 * half_life])
    theoretical = theoretical_decay(
        initial_atoms, decay_constant, times
    )

    assert np.isclose(theoretical[0], 1000)
    assert np.isclose(theoretical[1], 500)
    assert np.isclose(theoretical[2], 250)

    simulated = simulate_decay(initial_atoms, decay_constant, times)

    assert simulated[0] == initial_atoms
    assert np.all(simulated >= 0)
    assert np.all(np.diff(simulated) <= 0)

    print("All validation checks passed.")


def main():
    # Example values, not tied to a specific isotope.
    initial_atoms = 1000000
    half_life = 10.0
    duration = 50.0
    number_of_steps = 500
    time_unit = "days"

    if initial_atoms <= 0 or half_life <= 0 or duration <= 0:
        raise ValueError("Atom count, half-life, and duration must be positive.")

    times = np.linspace(0, duration, number_of_steps + 1)

    decay_constant = calculate_decay_constant(half_life)
    theoretical = theoretical_decay(initial_atoms, decay_constant, times)
    simulated = simulate_decay(initial_atoms, decay_constant, times)

    validate_model()
    plot_results(times, theoretical, simulated, time_unit)
    export_results(times, theoretical, simulated)


if __name__ == "__main__":
    main()