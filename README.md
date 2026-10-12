# Radioactive Decay Simulator

A Python project comparing theoretical radioactive decay with a stochastic simulation of individual decay events.

**Author:** Derek Dong Han Li

## Overview

Radioactive decay is random at the individual-nucleus level, but the expected behaviour of a population follows an exponential relationship.

This project models both behaviours and plots them together. It explores how a simulated population fluctuates around the theoretical prediction and how the initial population affects the relative size of those fluctuations.

## Features

- Calculates the decay constant from a user-defined half-life.
- Calculates the theoretical number of remaining radioactive nuclei over time.
- Simulates random decay events using binomial sampling.
- Plots theoretical and simulated results together.
- Exports results to a CSV file.
- Includes basic mathematical and simulation validation checks.
- Uses a fixed random seed for reproducible results.

## Requirements

- Python 3
- NumPy
- Matplotlib

Install the required packages:

```bash
python -m pip install numpy matplotlib
```

The project also uses Python’s built-in `math` module.

## Running the Simulator

Run the script from a terminal:

```bash
python decay_simulator.py
```

The program runs its validation checks and displays a graph. With the current execution order, close the graph window to let the program finish exporting `results.csv`.

The CSV is saved in the current working directory with these columns:

```text
time,theoretical_atoms,simulated_atoms
```

The time column uses the time unit selected in the program.

## Configuration

Edit these settings inside `main()`:

```python
initial_atoms = 1000
half_life = 10.0
duration = 50.0
number_of_steps = 500
time_unit = "days"
```

| Setting | Meaning |
|---|---|
| `initial_atoms` | Initial number of radioactive nuclei; use a positive integer |
| `half_life` | Time required for the expected population to decrease by half |
| `duration` | Total simulated time |
| `number_of_steps` | Number of time intervals; use a positive integer |
| `time_unit` | Unit displayed on the graph |

Half-life and duration must use the same unit. Changing `time_unit` changes the label only; it does not convert numerical values.

The default values are illustrative and do not represent a particular isotope.

## Mathematical Model

The decay constant is:

```text
λ = ln(2) / T½
```

The expected remaining population is:

```text
N(t) = N₀ × exp(−λt)
```

Where:

- `N₀` is the initial population.
- `N(t)` is the expected population at time `t`.
- `T½` is the half-life.
- `λ` is the decay constant, in inverse time units.

For each simulation interval, the probability that a remaining nucleus decays is:

```text
p = 1 − exp(−λΔt)
```

The number of decays is sampled from a binomial distribution:

```text
decayed nuclei ~ Binomial(previous population, p)
new population = previous population − decayed nuclei
```

This keeps simulated counts as whole numbers and prevents a nucleus from decaying more than once.

## Validation

The included checks verify that:

- The theoretical population at time zero equals the initial population.
- One half-life leaves half the expected population.
- Two half-lives leave one-quarter of the expected population.
- The simulated population starts at the specified initial count.
- Simulated counts never become negative or increase.

For the default settings, 50 days equals five half-lives:

```text
N(50) = 1000 × (1/2)⁵ = 31.25
```

The theoretical value can be fractional because it is an expectation. The simulated result is an integer and varies with the random seed.

These checks confirm basic consistency; they do not constitute a full statistical validation of the simulation.

## Reproducibility

The simulation uses `seed=42` by default. Keeping the same seed, inputs, and software environment reproduces the same random sequence. Changing the seed produces another realization of the decay process.

## Assumptions and Limitations

- The sample contains one radioactive isotope.
- Nuclei decay independently with a constant decay constant.
- No new parent nuclei enter the sample.
- Radioactive daughter products and decay chains are not tracked.
- Results describe remaining nuclei, not radiation dose, shielding, or health effects.
- The model is an educational simulation and has not been validated for operational nuclear engineering use.

## Possible Extensions

- Run repeated simulations and compare their average with the theoretical curve.
- Plot the spread of results across multiple runs.
- Add isotope presets with referenced half-life data.
- Model parent–daughter decay chains.
- Add activity calculations with explicit unit conversion.