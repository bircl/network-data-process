# ov Exercise - Birkan

This project involves processing poles and lines data. 
The script snaps lines to the nearest pole points and populates missing pole height data from the nearest available pole.

## Project Structure

- `data/`: Directory containing the input data files.
  - `input_data.gpkg`: GeoPackage file containing `poles` and `lines` layers.
- `output/`: Directory where the processed data will be saved.
- `main.py`: The main Python script that performs the processing.
- `requirements.txt`: Python dependencies required to run the script.
- `Makefile`: A makefile to automate the installation of dependencies and execution of the script.

## Prerequisites

- Python 3.9.7 or later
- A virtual environment is recommended

## Setup and Installation

*!! make sure you are in the project directory*

1. **Create a Virtual Environment** (optional)
    ```bash
    python3 -m venv ov_birkan
    source ov_birkan/bin/activate  # On Windows: ov_birkan\Scripts\activate
    ```

2. **Install Dependencies**:
    To install all required dependencies, run:
    ```bash
    pip install -r requirements.txt
    ```

    Alternatively, use the `Makefile`:
    ```bash
    make install
    ```

3. **Input Data**:
    - Make sure `input_data.gpkg` that contains `poles` and `lines` layers in the `data/` directory.

## Running the Script

You can run the script using the following command:

```bash
python3 main.py   # On Windows: python main.py
```

Alternatively, you can use the `Makefile`:
```bash
make run
```


### Troubleshooting
If you encounter any issues, ensure that:

 - You have the correct version of Python installed.
 - All dependencies are installed correctly (check `requirements.txt`).
 - You have the input data file input_data.gpkg in the correct location.