from unittest.mock import MagicMock
from fall import SmartHome, mood_profile

def test_light_switch(mocker):
        
        
        assert isinstance(state == 1)
        assert state == 1

        assert isinstance(room == 'bedroom')
        assert room == 'bedroom'

        assert isinstance(floor == 2)
        assert floor == 2

def test_mood_profile(mocker):
    
    mock_mood_profile = mocker.patch.object(SmartHome, 'mood_profile')
    set_mood_profile = mood_profile 

    assert isinstance()

def test_scheduling(mocker):