import signal
import sys

class GracefulKiller:
    def __init__(self):
        self.kill_now = False
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        print("\n🛑 Shutdown signal received. Finishing current step...")
        self.kill_now = True




# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/