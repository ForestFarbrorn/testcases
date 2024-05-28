from pydantic import BaseModel

# class for Smart home
class SmartHome():
    def __init__(self, state: int, room: str, floor: int, mood: str, time_am: int, time_pm: int) -> None:
        self.state = state
        self.room = room
        self.floor = floor
        self.mood = mood
        self.time_am = time_am
        self.time_pm = time_pm

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
    def scheduling(self, room: str, floor: int, mood: str, time_am: int, time_pm: int):

        new_schedule = schedule(room: 'bedroom', floor: 2, mood: 'Funky', time_am: 6, time_pm: 9)

        return new_schedule
       # pass