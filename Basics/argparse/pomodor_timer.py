import argparse
import time



def main():
    parser = argparse.ArgumentParser(description="Pomodoro Timer")
    parser.add_argument("minutes",type=int,help="Minutes to focus")
    args = parser.parse_args()

    seconds = args.minutes * 60

    while seconds:
        mins,secs = divmod(seconds,60)
        print(f"\rTime remaining: {mins:02d}:{secs:02d}",end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up! Take a break.")


if __name__ == "__main__":
    main()
