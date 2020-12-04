# CS4900-CompGeo
Computational Geometry Practice in Python for CS 4900 at WMU.

# Usage: Generic

The following are setup and usage instructions for development outside of a dedicated IDE like [PyCharm](https://www.jetbrains.com/pycharm/). Note that this application requires the following:

1. **Python 3.8.x** or above.
2. **pip 20.x** or above (installed by default when you install Python 3 >= 3.4 or when working in a virtual environment created by virtualenv or venv).

## Getting Started

After cloning this repository, cd to **CompGeo/** and run the included
bash script **compgeo_init.sh**:

```bash
cd CompGeo/
bash compgeo_init.sh
```
This will create a virtual environment named **venv** and install the
dependencies listed in **requirements.txt**.

If you elect to set up your development environment manually, run the following:

```bash
cd CompGeo/
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## PyTest Unit Testing

This application uses [PyTest](https://docs.pytest.org/en/stable/) for unit testing. To run, simply enter the following while in the **CompGeo** directory:

```bash
cd CompGeo/
pytest
```

This will invoke Pytest over all of the files matching the naming convention **test_[name].txt,** which are all stored in the **test/** directory/ies.

## Updating Dependencies

Whenever you update or add dependencies via pip3, while venv is active, output the installed packages into **requirements.txt:**

```bash
pip3 freeze > requirements.txt
```

Make sure you are currently working from the virtual environment. Otherwise, you will output Python packages installed globally on your machine rather than those in the virtual environment.

## Exiting

Exit from the virtual environment by running **deactivate:**
```bash
deactivate
```

# Usage: PyCharm

TODO: Add instructions