from pydantic import BaseModel

# class for Smart home
class SmartHome():
    def __init__(self, state: int, room: str, floor: int, mood: str) -> None:
        self.state = state
        self.room = room
        self.floor = floor
        self.mood = mood

    # Är belysningen av eller på
    def light_switch(self, state: int, room: str, floor: int):
    
        pass

    # Mood lighting profiler
    def mood(self, room: str, floor: int, mood: str):

        pass

    # Schemaläggning av belysning
    def scheduling():

        pass