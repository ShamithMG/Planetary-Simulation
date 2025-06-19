# N-Body Planetary Orbit Simulation

## Description

This project is a Python application that simulates and visualizes the orbits of an arbitrary number of planets. It features a scalable, object-oriented design where each planetary body is an instance of a class, allowing the system to be easily configured to handle any number of orbits.
This project was developed as part of the "first year computing final assignment," extending the original scope from a 2- or 3-body problem to a an N-body simulation.

## Key Features

* **Scalable N-Body Design:** Utilizes a class-based architecture to simulate an arbitrary number of planets.
* **Modular & Organized:** The code is separated into logical components: a main application with the UI, a simulation engine, and a constants file.
* **Standalone Demo:** Runs out-of-the-box with placeholder data, generating procedural circular orbits for demonstration purposes.

## File Structure

* `main.py`: The main application entry point.
* `body_physics.py`: Contains the core classes and functions for the physics simulation. This is where the `Planet` class and the trajectory calculation logic reside.
* `rendering_orbit.py`: Contains functions to draw and animate orbit.
* `planetary_data.py`: A centralized file for storing the position, velcoity and mass for each star and planet in the solar system
* `CONSTANTS.py`: A centralized file for storing physical and simulation constants.

* `FinalAssessment.ipynb`: Initial submission for this assignment

## Prerequisites

To run this simulation, you will need Python 3 and the following libraries:

* `numpy`
* `matplotlib`
* `IPython` : Jupyter NB
