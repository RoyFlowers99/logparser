# LogParser

**LogParser** is a simple Python tool that scans log files to identify and count different unique values such as IP addresses, HTTP statuses & methods, and file extensions.

## Features
- **IP Addresses**: Detects and counts the occurrences of each unique IP address in the log file.
- **HTTP Status Codes**: Detects and counts HTTP status codes (e.g., 200, 404, 500).
- **HTTP Methods**: Finds and counts the occurrences of HTTP methods (e.g., GET, POST, DELETE).
- **File Extensions**: Finds and counts occurrences of file extensions (e.g. .html, .cpp, .json)

## Requirements
- Python 3.x

## Installation
1. Clone the repository:

   ```git clone https://github.com/royflowers99/logparser.git```




## Usage

Navigate into the project directory:

```cd logparser```

Run the program from the command line, specifying the log file and the type of analysis you want to perform:

```python logparser.py [OPTION] <logfile>```

#### Options:

`--help` or `-h` for the full list of current options.

#### Example:

To count IP addresses:

`python logparser.py -ip /path/to/access.log`


## License

This project is licensed under the MIT License.
