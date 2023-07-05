import subprocess
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


def makeDumpCommand(dbName,host,sourcePort,destFolder):
    destPath='{cwd}/{destFolder}'.format(cwd=os.getcwd(),destFolder=destFolder)
    uri='--uri=mongodb://{host}:{port}/{DB}'.format(host=host,port=sourcePort,DB=dbName)
    print('dvbdjb')
    outputDir='--out={dp}'.format(dp=destPath)
    print('outputDIR' + outputDir)
    return ['mongodump',uri,outputDir]
try:
    mongoclient=pymongo.MongoClient("localhost", 27017)
  
    databaseName=os.getenv('DATABASE_NAME')
    collections=mongoclient.get_database(databaseName).list_collection_names()
    print(collections)
    host=os.getenv('HOST')
    outputDir=os.getenv('DESTINATION_DIR')
    sourcePort=os.getenv('SOURCE_PORT')
    dumpCMD=makeDumpCommand(databaseName,host,sourcePort,outputDir)
    print(dumpCMD)
    for name in collections:
        dumpCMD_copy=dumpCMD.copy()
        dumpCMD_copy.extend(['--collection',name])
        print(dumpCMD_copy)

        subprocess.call(dumpCMD_copy)
except Exception as e:
    print(e)
