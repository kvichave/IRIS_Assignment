import pandas as pd

class ExcelProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.excel = pd.read_excel(file_path, sheet_name=None, header=None)

    def list_tables(self):
        return list(self.excel.keys())

    def get_row_names(self, table_name: str):
        if table_name not in self.excel:
            raise ValueError("Invalid table name")
        df = self.excel[table_name].dropna(how='all', axis=1).dropna(how='all', axis=0)
        return df.iloc[:, 0].dropna().tolist()

    def sum_row_values(self, table_name: str, row_name: str):
        if table_name not in self.excel:
            raise ValueError("Invalid table name")
        df = self.excel[table_name].dropna(how='all', axis=1).dropna(how='all', axis=0)
        row = df[df.iloc[:, 0] == row_name]
        if row.empty:
            raise ValueError("Row name not found")
        values = pd.to_numeric(row.iloc[0, 1:], errors='coerce').fillna(0)
        return float(values.sum())
