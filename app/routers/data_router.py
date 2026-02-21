from fastapi import APIRouter
from services.data_service import DataService
from processor.csv_processor import read_csv, filter_data, calculate_average, write_csv
from app.schemas.data_schema import ProcessResponse, RecordsListResponse

router = APIRouter()
service = DataService()

@router.post("/process", response_model=ProcessResponse)
def process_data(threshold: float = 15, input_path: str = "data/sample_data.csv"):

    data = read_csv(input_path)
    filtered = filter_data(data, threshold)
    service.save_records(filtered)
    average = calculate_average(filtered)

    output_path = "data/filtered_output.csv"
    write_csv(output_path, filtered)

    return ProcessResponse(
        filtered_count=len(filtered),
        average=average,
        output_file=output_path
    )

@router.get("/records", response_model=RecordsListResponse)
def list_records():
    records = service.list_records()

    formatted = [
        {"id": r[0], "record_id": r[1], "value": r[2]}
        for r in records
    ]

    return RecordsListResponse(records=formatted)

@router.delete("/records")
def clear_records():
    service.clear_records()
    return {"message": "All records cleared"}