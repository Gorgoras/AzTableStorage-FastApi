import time, logging

def truncateTable(tableName, table_service):
    if tableName:
        try:
            table_service.delete_table(tableName)
            time.sleep(1)
            existe = False
            while(not existe):
                logging.info("Attempting to create")
                time.sleep(5)
                existe = table_service.create_table(tableName)

            logging.info("Done!!")
            ret = 'Table has been truncated!'
            return {"message": ret, "status": 200}
        except Exception as e:
            return {"message": f"{e}", "status": 400}
