# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import time
import sys

class Countdown:
    def __init__(self, seconds):
        self.seconds = seconds

    def _format_time(self, seconds):
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

    def start(self):
        try:
            total = self.seconds
            while total > 0:
                time_str = self._format_time(total)
                # Overwrite the line to create a digital clock effect
                sys.stdout.write(f"\rTime remaining: {time_str}")
                sys.stdout.flush()
                time.sleep(1)
                total -= 1
            
            # Final 00:00:00
            sys.stdout.write(f"\rTime remaining: 00:00:00\n")
            print("Time's up!")
            
            # Optional: Beep on completion (cross-platform attempt)
            # This prints the ASCII Bell character
            sys.stdout.write('\a') 
            sys.stdout.flush()
            
        except KeyboardInterrupt:
            print("\nCountdown stopped.")

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
