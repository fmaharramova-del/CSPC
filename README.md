# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- A radioactive decay simulation (pure-Python loop and vectorized NumPy versions), tested against the analytical decay law with pytest.

**Speed comparison (loop vs NumPy):**
- loop  : 2.8656 s
- numpy : 0.0003 s
- speed-up: 9270.2x faster

**Tests:** all passing? yes

**Conclusion:**
- NumPy's vectorized operations vastly outperform pure-Python loops when working with large arrays, because they push the loop into pre-compiled C code instead of Python's interpreter. Writing and running tests against the known analytical law (N0 * e^(-λt)) gave confidence that the simulation is correct, not just fast. The biggest challenge was remembering to activate the conda environment before running scripts.


---

## PW1 - Lab B: Data, Plotting, and Automation

**What the data showed:**
- The observed decay counts start high and drop off sharply within the first few time steps, then flatten out near zero — a classic exponential decay shape.

**Did it match the analytical law?**
- Yes. Plotting the observed points next to the analytical curve N0*exp(-λt) on shared axes showed the same overall shape and scale, confirming the data is consistent with exponential decay.

**Snakemake pipeline:**
- The Snakefile defines one rule that regenerates figure.png from decay_observed.csv by running plot.py, only rebuilding it when the input or script has changed.



---

## PW2 --- Lab A: Motion from Tracking Data

**Mean acceleration measured:**
- -8.58 m/s² (expected about -9.81). The standard deviation was 28.7 m/s², so individual values are very scattered. The mean is pulled away from -9.81 partly by the noisy values at the ends of the data.

**Why the acceleration was noisy:**
- Differentiation divides the difference between neighbouring noisy measurements by a small time step (0.1 s), so every derivative amplifies the noise. Acceleration needed two derivatives, so it is much noisier than the position, which looked smooth.

**What integrating back showed:**
- Integrating the noisy acceleration twice recovered the position with a maximum difference of 0.78 m from the original. Integration is a sum, so random errors partly cancel: integration suppresses noise, the opposite of differentiation.

**Figure:** `PW2/Lab A/motion.png` shows position (smooth), velocity (slightly rough) and acceleration (very noisy, around the dashed -9.81 line).