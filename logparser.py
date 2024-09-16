import argparse
import subprocess

def run_script(script, file):
    try:
        subprocess.run(["python3", script, file])
    except Exception as e:
        print(f"Error running {script}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Command line controller.')

    parser.add_argument('--ipv4', '-ip', action='store_true', help='Run ipv4_count.py')
    parser.add_argument('--status', '-s', action='store_true', help='Run http_status.py')
    parser.add_argument('--method', '-m', action='store_true', help='Run http_method.py')
    parser.add_argument('file', type=str, help='File to be analyzed')

    args = parser.parse_args()

    if args.ipv4:
        run_script('ipv4_count.py', args.file)
    elif args.status:
        run_script('http_status.py', args.file)
    elif args.method:
        run_script('http_method.py', args.file)
    else:
        print("Please specify a valid flag! -> (-ip, -s, -m)")

if __name__ == "__main__":
    main()