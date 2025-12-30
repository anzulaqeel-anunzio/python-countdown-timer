# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from timer.core import Countdown

def parse_time(time_str):
    """Parse string like '10', '1m', '1h30m' into seconds."""
    total_seconds = 0
    current_num = ""
    
    # Simple logic: If it's just a number, assume seconds (or minutes? let's stick to explicit or standard args)
    # Actually, simpler is: if arg is int, assume seconds. If contains m/h/s, parse it.
    
    if time_str.isdigit():
        return int(time_str)

    # Simple parser for 1h30m10s
    for char in time_str:
        if char.isdigit():
            current_num += char
        else:
            if not current_num:
                continue
            val = int(current_num)
            current_num = ""
            if char == 's':
                total_seconds += val
            elif char == 'm':
                total_seconds += val * 60
            elif char == 'h':
                total_seconds += val * 3600
                
    if current_num: # trailing number without unit, assume seconds? or ignore.
        total_seconds += int(current_num)
        
    return total_seconds

def main():
    parser = argparse.ArgumentParser(description="CLI Countdown Timer")
    parser.add_argument("time", help="Time to count down (e.g., '10', '1m', '5m30s')")
    parser.add_argument("--minutes", "-m", action="store_true", help="Interpret pure number as minutes instead of seconds")

    args = parser.parse_args()

    seconds = 0
    if args.time.isdigit():
        val = int(args.time)
        if args.minutes:
            seconds = val * 60
        else:
            seconds = val
    else:
        seconds = parse_time(args.time)

    if seconds <= 0:
        print("Invalid time duration.")
        sys.exit(1)

    print(f"Starting countdown for {seconds} seconds...")
    timer = Countdown(seconds)
    timer.start()

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
