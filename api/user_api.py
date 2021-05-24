import azure.functions as func
from .http_asgi import AsgiMiddleware
import fastapi, os, sys
from fastapi import Form, Depends
from typing import Optional
from azure.cosmosdb.table.tableservice import TableService

root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from functions.createTable import createTable as funcCreateTable
from functions.deleteTable import deleteTable as funcDeleteTable

app = fastapi.FastAPI()


async def con_parameters(conn_string: Optional[str] = Form(None), acc_name: Optional[str] = Form(None), 
                acc_key: Optional[str] = Form(None), sas_token: Optional[str] = Form(None)):
    return  {   "conn_string": conn_string,
                "acc_name": acc_name, 
                "acc_key": acc_key, 
                "sas_token": sas_token  }

def getTableService(connection_parameters):
    table_service = None
    if connection_parameters['conn_string']!=None:
        table_service = TableService(connection_string=connection_parameters['conn_string'])
    elif connection_parameters['acc_name']!=None:
        if connection_parameters['acc_key']!=None:
            table_service = TableService(account_name=connection_parameters['acc_name'], account_key=connection_parameters['acc_key'])
        elif connection_parameters['sas_token']!=None:
            table_service = TableService(account_name=connection_parameters['acc_name'], account_key=connection_parameters['sas_token'])
    return table_service

@app.post('/createTable')
async def create_table(tableName: str = Form(...), con_params: dict = Depends(con_parameters)):
    table_service = getTableService(con_params)
    if table_service != None:
        response = funcCreateTable(tableName, table_service)
    else:
        response = {"message": "Missing key authentication data", "status": 400}
    return response

@app.post('/deleteTable')
async def delete_table(tableName: str = Form(...), con_params: dict = Depends(con_parameters)):
    table_service = getTableService(con_params)
    if table_service != None:
        response = funcDeleteTable(tableName, table_service)
    else:
        response = {"message": "Missing key authentication data", "status": 400}
    return response

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)