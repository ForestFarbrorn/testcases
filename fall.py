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
        # state == 1 = ON, state == 2 = OFF
        state == 1
        room == 'bedroom'
        floor == 2

       # pass

    # Mood lighting profiler
    def mood_profile(self, room: str, floor: int, mood: str):
        
       # pass

    # Schemaläggning av belysning
    def scheduling():

       # pass