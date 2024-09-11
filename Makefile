# Detect platform
ifeq ($(OS),Windows_NT)
    PYTHON = python
    PIP = pip
else
    PYTHON = python3
    PIP = pip3
endif

# Default target
all: install run

# Install dependencies
install:
	$(PIP) install -r requirements.txt

# Run the script
run:
	$(PYTHON) main.py

# Clean up temporary files
clean:
	rm -rf output/
