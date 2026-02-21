from repositories.data_repository import DataRepository

class DataService:

    def __init__(self):
        self.repo = DataRepository()

    def save_records(self, records: list[dict]):
        self.repo.create_table()
        self.repo.insert_records(records)

    def list_records(self):
        self.repo.create_table()
        records = self.repo.fetch_all()
        return records
    
    def clear_records(self):
        self.repo.create_table()
        self.repo.clear()