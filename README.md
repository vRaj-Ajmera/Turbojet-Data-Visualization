# Turbojet Data Visualization

Welcome to the Turbojet Data Visualization project! This README will guide you through setting up your development environment and running the project.

## Table of Contents
- [File Structure](#file-structure)
- [Integration Overview](#integration-overview)
- [Editing Instructions](#editing-instructions)
- [Running Instructions](#running-instructions)

## File Structure

```
turbojet_project/
│
├── main.py
│
├── gui/
│   └── turbojet_gui.py
│
├── model/
│   └── turbojet_model.py
│
└── utils/
    ├── general_analysis.py
    └── unit_conversions.py
```

## Integration Overview

In this project, the GUI (`turbojet_gui.py`) interacts with the underlying model (`turbojet_model.py`) to calculate engine performance metrics such as thrust and TSFC (Thrust Specific Fuel Consumption). Here's a brief overview of how this integration works:

1. **GUI Interaction**: The GUI collects user inputs, such as Mach number, total temperature, total pressure, turbine inlet temperature, and other relevant parameters.

2. **Model Calculation**: The GUI creates a TurbojetModel object, passing the user inputs to it. Inside the TurbojetModel class (`turbojet_model.py`), the calculations are performed using a `general_analysis` object. This object contains methods for various mathematical calculations required for determining engine performance metrics.

3. **Data Processing**: After the model completes the calculations using the `general_analysis` object, it returns the calculated thrust and TSFC values to the GUI.

4. **Visualization**: The GUI utilizes the returned data to create graphical representations of the engine's performance metrics. This may involve plotting graphs, displaying numerical values, or generating other types of visualizations to help users understand the turbojet engine's performance characteristics.

## Editing Instructions

To contribute to this project, follow these steps:

1. **Clone the Repository**: Open your IDE and clone the repository.
2. **Create a New Branch**: If you want to edit or add files, create a new branch. All changes should be made in this branch.
3. **Edit and Test**: Make your changes in this branch and test them using the main file.
4. **Create a Pull Request**: Once you're finished and everything is working as expected, create a pull request to merge your branch with main.

## Running Instructions

To run the project:

- **Run the Main File**: Start by running the main file (main.py). You can debug and test the project from there.

Happy coding!
