from django.db import models

QUESTIONS = [
    {
        'likes': 5,
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answer_number': question_id * question_id,
        'tags': ['tag' for i in range(question_id)],
        'photos': f"img/Avatar{question_id}.jpg",
    } for question_id in range(12)
]

ANSWERS = [
    {
        'photos': f"img/Avatar{answer_id}.jpg",
        'id': answer_id,
        'likes': 5,
        'text': f'Text of answer #{answer_id}',
    } for answer_id in range(12)
]

HOTQUESTIONS = [
    {
        'likes': 5,
        'id': question_id,
        'title': f'Question #{question_id}',
        'text': f'Text of question #{question_id}',
        'answer_number': question_id * question_id,
        'photos': f"img/Avatar{question_id}.jpg",
    } for question_id in range(6)
]

TAGS = [
    {
        'id': tag_id,
        'title': f'Tag #{tag_id}',
    } for tag_id in range(3)
]
