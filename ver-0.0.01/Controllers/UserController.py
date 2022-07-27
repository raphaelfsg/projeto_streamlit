import services.database as db

def incluir() {
    count = cursor.execute("""
    INSERT INTO project_user (Name, ProductNumber, StandardCost, ListPrice, SellStartDate) 
    VALUES (?,?,?,?,?)""",
    'SQL Server Express New 20', 'SQLEXPRESS New 20', 0, 0, CURRENT_TIMESTAMP).rowcount
    cnxn.commit()
}

