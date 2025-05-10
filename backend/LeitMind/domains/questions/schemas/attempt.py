from pydantic import BaseModel

class AttemptRequest(BaseModel):
    question_id: int
    answer_id: int
    user_id: int
    attempt_id: int

