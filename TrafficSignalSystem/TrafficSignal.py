from abc import ABC, abstractmethod
from enum import Enum
import time
import threading


class Direction(Enum):
    NORTH = "North"
    EAST = "East"
    SOUTH = "South"
    WEST = "West"


class SignalState(ABC):
    @abstractmethod
    def handle(self, controller):
        pass


class GreenState(SignalState):
    def handle(self, controller):
        direction = controller.current_direction
        duration = controller.durations[direction]["green"]
        print(f"[{direction.value}] GREEN light ON for {duration}s.")
        time.sleep(duration)
        controller.set_state(YellowState())


class YellowState(SignalState):
    def handle(self, controller):
        direction = controller.current_direction
        duration = controller.durations[direction]["yellow"]
        print(f"[{direction.value}] YELLOW light ON for {duration}s.")
        time.sleep(duration)
        controller.set_state(RedState())


class RedState(SignalState):
    def handle(self, controller):
        direction = controller.current_direction
        duration = controller.durations[direction]["red"]
        print(f"[{direction.value}] RED light ON for {duration}s.")
        time.sleep(duration)
        controller.next_direction()
        controller.set_state(GreenState())


class TrafficSignalController:
    def __init__(self, durations):
        self.directions = list(Direction)
        self.current_direction_index = 0
        self.durations = durations
        self.state = GreenState()
        self.override_state = None
        self.running = True

    @property
    def current_direction(self):
        return self.directions[self.current_direction_index]

    def next_direction(self):
        self.current_direction_index = (self.current_direction_index + 1) % len(self.directions)

    def set_state(self, state):
        self.state = state

    def manual_override(self, direction, state_name):
        print(f"⚠️ MANUAL OVERRIDE: Forcing {direction.value} to {state_name.upper()} state")
        self.current_direction_index = self.directions.index(direction)
        states = {"green": GreenState(), "yellow": YellowState(), "red": RedState()}
        self.override_state = states[state_name.lower()]

    def run(self):
        while self.running:
            if self.override_state:
                self.override_state.handle(self)
                self.override_state = None
            else:
                self.state.handle(self)

    def stop(self):
        self.running = False
