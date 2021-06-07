import logging

def deleteTable(tableName, table_service):
    if tableName:
        try:
            result = table_service.delete_table(tableName)
            if result:
                ret = f"Table has been deleted!!"
            else:
                ret = 'Resource not found'
            return {"message": ret, "status": 200}
        except Exception as e:
            return {"message": f"{e}", "status": 400}
