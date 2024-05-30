# Python Socket Translator

This project is a simple translator (English to Portuguese) implemented in Python that uses sockets for communication and the [translators](https://github.com/uliontse/translators) library for translation.

## Requirements

- Python 3.x
- `translators` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/devthiart/python-translator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-translator
    ```

3. Install the required dependencies:

    ```bash
    pip install translators
    ```

4. Configure IP address in `server.py` and `client.py` files.

    server.py (line 28):
    ```bash
    # put your computers IP address here:
    server.bind(('YOUR_IP_HERE', 12345))
    ```

    client.py (line 6):
    ```bash
    # put your computers IP address here:
    client.connect(('YOUR_IP_HERE', 12345))
    ```

## Usage

1. Start the server:

    ```bash
    python server.py
    ```

2. In another terminal, start the client and request a translation:

    ```bash
    python client.py
    ```

3. Follow the prompts to enter the text you want to translate to portuguese.
