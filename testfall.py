from unittest.mock import MagicMock
from fall import SmartHome

def test_light_switch(mocker):
        
        
        assert isinstance(state == 1)
        assert state == 1

        assert isinstance(room == 'bedroom')
        assert room == 'bedroom'

        assert isinstance(floor == 2)
        assert floor == 2

def test_mood_profile(mocker):
    
    mock_mood_profile = mocker.patch.object(SmartHome, 'mood_profile')
    get_mood_profile = new_mood_profile(mood = 'Funky')

    mock_instance.assert_called_once()
    assert mood == 'Funky'

def test_scheduling(mocker):
      
def test_get_all_questions_returns_list(mocker):
    mock_db_instance = mocker.patch.object(
        QuestionDB, 
        'get_all_questions', 
        return_value=[Question(qid=0, question_text='Test question', answer_text='Test answer')]
    )

    questions = get_all_questions()

    assert isinstance(questions, list)
    assert len(questions) == 1
    assert questions[0].question_text == 'Test question'
    assert questions[0].answer_text == 'Test answer'
    mock_db_instance.assert_called_once()