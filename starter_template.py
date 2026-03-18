import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="A brief description of the tool")
    
    # Add arguments
    parser.add_argument("name", help="The name of the user")
    parser.add_argument("-g", "--greeting", default="Hello", help="The greeting to use")

    args = parser.parse_args()

    # Logic
    print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    main()