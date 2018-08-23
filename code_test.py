import numpy as np
import pyodbc
import psycopg2

def get_connection(p):
    if(p is not None):
        con = pyodbc.connect(p)
    else:
        con = pyodbc.connect('connection string')
    return(con)