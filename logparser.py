import argparse
import subprocess

"""
Rather than have all the different functions in one file,
I found breaking the different functions up across multiple files
to be more modular and easier to read.

All files follow the same format: define regex, open file, search line by line,
if there's a match, append matched string to dictionary with count. Then print
results.
"""

def run_script(script, file): # For creating a subprocess to run the selected function.
    try:
        subprocess.run(["python", script, file])
    except Exception as e:
        print(f"Error running {script}: {e}")

def main(): # Defines command line controller arguments.
    parser = argparse.ArgumentParser(description='Command line controller.')

    parser.add_argument('-ip', '--ipv4', action='store_true', help='counts unique IP addresses.')
    parser.add_argument('-s', '--status', action='store_true', help='counts HTTP status codes.')
    parser.add_argument('-m', '--method', action='store_true', help='counts HTTP methods.')
    parser.add_argument('-x', '--extension', action='store_true', help='counts various file extensions.')
    parser.add_argument('file', type=str, help='File to be analyzed')

    args = parser.parse_args()

    if args.ipv4:
        run_script('ipv4_count.py', args.file)
    elif args.status:
        run_script('http_status.py', args.file)
    elif args.method:
        run_script('http_method.py', args.file)
    elif args.extension:
        run_script('file_ext.py', args.file)
    else:
        print("Please specify a valid flag! -> (-ip, -s, -m...)")

if __name__ == "__main__":
    main()