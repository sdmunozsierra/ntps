# Network Traffic Proxy System GUI
Version 1.0.0
March 17, 2019

Team 5
Isai Gonzalez, Julio De La Cruz, Oscar Galindo, Alan Caldelas, Sergio Sierra

* This is just the graphical user interface, no implementation is included.
* There are some samples used in lists and such to show an early idea of how it can be implemented.

* The program uses PyQt5 for the graphical elements.
* To run the GUI, use python to run the NTPS.py file. The other files included are overlays like the "Create/Edit Hook Window". These files must be in the same directory.
* We did not include error overlays as there would be no way to trigger them in this version of the project.

## Run
To run the app run the following command in a terminal:
```python __main__.py```

## Requirements
This project requires python 3 and modules listed below that can be installed via `pip install "packagename"`.

### Pip
* pytest - Required for running tests.
* freezegun - Required for running tests that are based on time module.

## Testing

To run tests via pytest type ```python -m pytest -v Tests/``` in a terminal in the root directory.

Test cases are divided in Blackbox and Whitebox testing.
The syntax for test files is as follows:
```test_*CLASS_NAME*_*TEST_NAME*```
