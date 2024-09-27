import argparse
import subprocess

def run_script(script, file):
    try:
        subprocess.run(["python3", script, file])
    except Exception as e:
        print(f"Error running {script}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Command line controller.')

    parser.add_argument('-ip', '--ipv4', action='store_true', help='counts unique IP addresses')
    parser.add_argument('-s', '--status', action='store_true', help='counts HTTP status codes')
    parser.add_argument('-m', '--method', action='store_true', help='counts HTTP methods')
    parser.add_argument('-x', '--extension', action='store_true', help='counts various File Extensions')
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