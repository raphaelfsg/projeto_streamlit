import pyodbc

server = 'mysqlserver.cskdto84k8kb.sa-east-1.rds.amazonaws.com,3306' 
database = 'project_user' 
username = 'subadmin' 
password = 'streamlit22' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()