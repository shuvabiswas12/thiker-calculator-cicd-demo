# CICD-Python Calculator Application

## Overview
The CICD-Python project is a simple calculator application designed for Windows OS. It provides a graphical user interface (GUI) for performing basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Project Structure
```
CICD-Python
├── app.py               # Main entry point for the calculator application
├── app_test.py          # Unit tests for the calculator application
├── calculator
│   ├── __init__.py      # Marks the calculator directory as a package
│   ├── gui.py           # GUI layout and behavior
│   └── core.py          # Core logic for arithmetic operations
├── requirements.txt      # Lists project dependencies
└── README.md            # Documentation for the project
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd CICD-Python
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the calculator application, execute the following command:
```
python app.py
```

## Testing
To run the unit tests for the calculator application, use:
```
pytest app_test.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.