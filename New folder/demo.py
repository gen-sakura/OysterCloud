import pypyodbc as odbc
import pandas as pd
#from credential import username, password

# Login Authentication DO NOT CHANGE
username = 'azureuser'
password = 'Oysterboys2023'

# Connect to Azure SQL Server
server = 'oystersqlserver.database.windows.net'
database = 'OysterSensorsData'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:oystersqlserver.database.windows.net,1433;Database=OysterSensorsData;Uid=azureuser;Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30'
conn = odbc.connect(connection_string)

# Query the database
sql = '''
SELECT TOP (1000) * FROM [dbo].[DataTable]
'''
cursor = conn.cursor()
cursor.execute(sql)

# Save query results to Pandas dataframe
dataset = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame(dataset, columns=columns)
print(df)