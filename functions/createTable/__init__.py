def createTable(tableName, table_service):
    if tableName:
        try:
            table_service.create_table(tableName)
            ret = f"Table created!!"
            return {"message": ret, "status": 200}
        except:
            return {"message": "Error", "status": 400}
