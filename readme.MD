# Yelp Business Search Application

This Python project queries the Yelp API for businesses (such as barbers) in a specified location (e.g., NYC) and filters the results to display businesses with a rating greater than 4.5. The project demonstrates how to interact with the Yelp API and handle API responses in Python.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Usage](#usage)
4. [Features](#features)
5. [Error Handling](#error-handling)
6. [Contributing](#contributing)
7. [License](#license)

## Installation

### Prerequisites

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)
- A [Yelp API Key](https://docs.developer.yelp.com/docs/fusion-authentication) (for accessing the Yelp API)

### Setup

- Clone this repository:

  ```bash
  git clone https://github.com/BaconPancakez/py_velp
  cd py_velp
  ```

- Create and activate a virtual environment:

  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

- Install the required dependencies from `requirements.txt`:

  ```bash
  pip install -r requirements.txt
  ```

- Add your Yelp API Key in a `config.py` file:

  Create a `config.py` file in the root directory of the project with the following content:

  ```python
  # config.py
  api_key = 'YOUR_YELP_API_KEY'
  ```

  Replace `'YOUR_YELP_API_KEY'` with your actual Yelp API Key.

## Configuration

The `config.py` file contains sensitive configurations like your API key. Ensure this file is listed in `.gitignore` to prevent accidental exposure of sensitive data.

## Usage

Run the script to perform the specified task (e.g., searching businesses):

```bash
python3 app.py
```
