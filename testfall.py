from unittest.mock import MagicMock
from fall import SmartHome

def test_light_switch(mocker):
        
        mock_light_switch = mocker.patch.object(SmartHome, 'light_switch')
        get_light_switch = light_switch(state = 1)
        
        assert isinstance(state = 1)
        assert get_light_switch.light_switch(state = 1)

        assert isinstance(room == 'bedroom')
        assert room == 'bedroom'

        assert isinstance(floor == 2)
        assert floor == 2

def test_mood_profile(mocker):
    
    mock_mood_profile = mocker.patch.object(SmartHome, 'mood_profile')
    get_mood_profile = new_mood_profile(mood = 'Funky')

    mock_instance.assert_called_once()

def test_scheduling(mocker):
      
        mock_scheduling = mocker.patch.object(SmartHome, 'scheduling')
        get_schedule = new_schedule(room: 'bedroom', floor: 2, mood: 'Funky', time: 6, day: 'Wednesday')

        mock_instance.assert_called_once()