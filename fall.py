from pydantic import BaseModel

# class for Smart home
class SmartHome():
    def __init__(self, state: int, room: str, floor: int, mood: str, time: int, day: str) -> None:
        self.state = state
        self.room = room
        self.floor = floor
        self.mood = mood
        self.time = time
        self.day = day

    # Är belysningen av eller på
    def light_switch(self, state: int, room: str, floor: int):
        # state == 1 = ON, state == 2 = OFF
        new_light_switch_state = light_switch(state: 1, room: 'bedroom', floor: 2)

        return new_light_switch_state
       # pass

    # Mood lighting profiler
    def mood_profile(self, room: str, floor: int, mood: str):
        
        new_mood_profile = mood_profile(room: 'bedroom', floor: 2, mood: 'Funky')

        return new_mood_profile
       # pass

    # Schemaläggning av belysning
    def scheduling(self, room: str, floor: int, mood: str, time: int, day: str):

        new_schedule = schedule(room: 'bedroom', floor: 2, mood: 'Funky', time: 6, day: 'Wednesday')

        return new_schedule
       # pass