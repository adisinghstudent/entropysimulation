import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate entropy
def calculate_entropy(states):
    probabilities = np.bincount(states) / len(states)
    probabilities = probabilities[probabilities > 0]
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

# Function to simulate the system
def simulate_system(num_particles, num_states):
    states = np.random.randint(0, num_states, num_particles)
    return states

# Streamlit app
st.title("Entropy Simulation")

st.sidebar.header("Simulation Parameters")

# User inputs
num_particles = st.sidebar.slider("Number of Particles", 10, 1000, 100)
num_states = st.sidebar.slider("Number of States", 2, 10, 4)
num_iterations = st.sidebar.slider("Number of Iterations", 1, 100, 10)

# Initialize variables
entropies = []
states = simulate_system(num_particles, num_states)

# Simulate the system over iterations
for _ in range(num_iterations):
    states = simulate_system(num_particles, num_states)
    entropy = calculate_entropy(states)
    entropies.append(entropy)

# Plot the results
fig, ax = plt.subplots()
ax.plot(entropies, marker='o')
ax.set_title("Entropy Over Time")
ax.set_xlabel("Iteration")
ax.set_ylabel("Entropy")

# Show plot in Streamlit
st.pyplot(fig)

# Display the final entropy
st.write(f"Final Entropy: {entropies[-1]:.4f}")

# Display the final state distribution
fig, ax = plt.subplots()
ax.hist(states, bins=np.arange(num_states + 1) - 0.5, edgecolor='black')
ax.set_title("Final State Distribution")
ax.set_xlabel("State")
ax.set_ylabel("Count")

# Show plot in Streamlit
st.pyplot(fig)

#Nice
