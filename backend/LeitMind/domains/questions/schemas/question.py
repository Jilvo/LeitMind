from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question_id: int
    text: str
    answers: list[str]
    correct_answer: int
    category: int
    explanation: str
    # image_path: Optional[str]
    # difficulty: int
    # user_id: int

class QuestionUpdateRequest(BaseModel):
    text: str
    answers: list[str]
    correct_answer: int
    category: int
    explanation: str
class CategoryRequest(BaseModel):
    name: str
    description: str


class ValidateRequest(BaseModel):
    question_id: int
    answer_id: int
    user_id: int
