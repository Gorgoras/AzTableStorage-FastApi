def deleteTable(tableName, table_service):
    if tableName:
        try:
            table_service.delete_table(tableName)
            ret = f"Table deleted!!"
            return {"message": ret, "status": 200}
        except:
            return {"message": "Error", "status": 400}
