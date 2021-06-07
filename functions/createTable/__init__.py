def createTable(tableName, table_service):
    if tableName:
        try:
            table_service.create_table(tableName)
            ret = f"Table has been created!!"
            return {"message": ret, "status": 200}
        except Exception as e:
            return {"message": f"{e}", "status": 400}
