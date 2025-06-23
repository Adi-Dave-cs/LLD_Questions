import threading
import time
from TrafficSignal import TrafficSignalController, Direction

if __name__ == "__main__":
    durations = {
        Direction.NORTH: {"green": 3, "yellow": 2, "red": 1},
        Direction.EAST:  {"green": 3, "yellow": 2, "red": 1},
        Direction.SOUTH: {"green": 3, "yellow": 2, "red": 1},
        Direction.WEST:  {"green": 3, "yellow": 2, "red": 1},
    }

    controller = TrafficSignalController(durations)

    # Run in background thread
    signal_thread = threading.Thread(target=controller.run)
    signal_thread.start()

    # Simulate manual override after 10 seconds
    time.sleep(10)
    controller.manual_override(Direction.SOUTH, "green")

    # Stop after some time
    time.sleep(15)
    controller.stop()
    signal_thread.join()
