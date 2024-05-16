import pyodbc


class DBUtil:
    @staticmethod
    def getDBConn():
        try:
            connection = pyodbc.connect(
                "DRIVER={SQL Server};" "SERVER=SaiGanesh;" "DATABASE=LoanManagement;"
            )
            print("Connection to MSSQL Server successful")
            return connection
        except pyodbc.OperationalError as e:
            print(f"The error '{e}' occurred")
