import pypyodbc as odbc
import pandas as pd
#from credential import username, password

# Login Authentication DO NOT CHANGE
username = 'azureuser'
password = 'Oysterboys2023'

# Connect to Azure SQL Server via connection string (find this in connection strings > ODBC)
server = 'oystersqlserver.database.windows.net'
database = 'OysterSensorsData'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:oystersqlserver.database.windows.net,1433;Database=OysterSensorsData;Uid=azureuser;Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
conn = odbc.connect(connection_string)

# Query the database
def query(query, conn=conn):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor

# Save query results to Pandas dataframe
def dataset_to_df(cursor):
    columns = [column[0] for column in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)

def get_top_1000_rows():
    sql = '''
    SELECT TOP (1000) * FROM [dbo].[DataTable]  
    '''
    row_cursor = query(sql)
    return dataset_to_df(row_cursor)

top_1000_rows = get_top_1000_rows()
print(top_1000_rows)