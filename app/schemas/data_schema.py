from pydantic import BaseModel
from typing import List

class ProcessResponse(BaseModel):
    filtered_count: int
    average: float
    output_file: str

class RecordResponse(BaseModel):
    id: int
    record_id: str
    value: float

class RecordsListResponse(BaseModel):
    records: List[RecordResponse]