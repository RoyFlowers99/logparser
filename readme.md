# LogParser

**LogParser** is a simple Python tool that scans log files to identify and count different unique values such as IP addresses and HTTP statuses & methods.

## Features
- **IP Address Counting**: Detects and counts the occurrences of each unique IP address in the log file.
- **HTTP Status Code Detection**: Detects and counts HTTP status codes (e.g., 200, 404, 500).
- **HTTP Method Analysis**: Finds and counts the occurrences of HTTP methods (e.g., GET, POST, DELETE).

## Requirements
- Python 3.x

## Installation
1. Clone the repository:

   ```git clone https://github.com/royflowers99/logparser.git```

2. Navigate into the project directory:

    ```cd logparser```

2. Ensure Python 3 is installed on your system.

    ```python3 --version```

## Usage

Run the program from the command line, specifying the log file and the type of analysis you want to perform:

```python3 logparser.py [OPTIONS] <logfile>```

#### Options:

`--help` or `-h` for the full list of current options.

#### Examples:

To count IP addresses:

`python3 logparser.py -ip /path/to/access.log`

To analyze HTTP status codes:

`python3 logparser.py -s /path/to/access.log`

To count HTTP methods:

`python3 logparser.py -m /path/to/access.log`

## License

This project is licensed under the MIT License.
