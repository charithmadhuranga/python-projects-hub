import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Bulk rename files in a folder")
    parser.add_argument("dir",help="Directory path")
    parser.add_argument("prefix",help="New prefix for files")
    args = parser.parse_args()

    path = Path(args.dir)
    for i,file in enumerate(path.iterdir()):
        if file.is_file():
            new_name = f"{args.prefix}_{i}{file.suffix}"
            file.rename(path/new_name)
    print("Renaming complete")

if __name__ == "__main__":
    main()