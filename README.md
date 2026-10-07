# Python Project Template

A simple template for Python data-processing projects.

The template provides a basic structure for organising data loading, processing, parameters, helper functions, and project documentation.

## Project structure

```text
.
├── data/                   # Input and output data
│   └── input/
│   └── output/
├── docs/                   # Project documentation
├── src/
│   └── utilities/
│       ├── helpers.py      # Helper functions
│       ├── load.py         # Data loading
│       ├── parameters.py   # Project parameters
│       └── processing.py  # Main data processing
├── .gitignore
├── LICENSE
├── README.md
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
└── setup.py                # Package configuration
```

## Getting started

Clone the repository and create a Python environment:

```bash
git clone <repository-url>
cd <project-name>

python -m venv .venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running the project

The main entry point is:

```bash
python main.py
```

The `main.py` file creates the processing class and runs the main project workflow.

## Project organisation

### `main.py`

The main entry point for running the project.

### `src/utilities/load.py`

Contains the class and functions used to load data.

### `src/utilities/processing.py`

Contains the main processing workflow that takes the loaded data and produces outputs.

### `src/utilities/helpers.py`

Contains reusable helper functions used throughout the project.

### `src/utilities/parameters.py`

Contains project parameters, including environmental parameters, file paths, data structures, and other configuration values.

### `data/`

Used to store project data. Data files are excluded from version control.

## Using this template

This repository is intended to be used as a starting point for new Python projects.

When starting a new project:

1. Copy or use this repository as a GitHub template.
2. Rename the project and update the project metadata.
3. Add the required dependencies to `requirements.txt`.
4. Add project-specific parameters to `parameters.py`.
5. Implement the data-loading functionality in `load.py`.
6. Implement the processing workflow in `processing.py`.
7. Update `main.py` with the required arguments.
8. Add project-specific documentation to `docs/`.

## Running the code

Once the environment has been activated and the dependencies installed, run the project from the root directory:

```bash
python main.py
```

The `main.py` file is the main entry point for the project. It creates the `ProcessingClass`, which loads the required data and runs the main processing workflow.

Before running the project, add the required arguments to `main.py`:

```python
def main():
    result = processing.ProcessingClass(
        # Add required arguments
    )


if __name__ == "__main__":
    main()
```

The project can then be run with:

```bash
python main.py
```

### Development workflow

A typical workflow when using this template is:

1. Add project parameters to `src/utilities/parameters.py`.
2. Add data-loading functionality to `src/utilities/load.py`.
3. Add reusable functions to `src/utilities/helpers.py`.
4. Add the main processing workflow to `src/utilities/processing.py`.
5. Pass the required arguments to `ProcessingClass` in `main.py`.
6. Run the project with:

```bash
python main.py
```

## License

This project is licensed under the MIT License. See `LICENSE` for details.