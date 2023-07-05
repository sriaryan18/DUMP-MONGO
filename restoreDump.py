from dotenv import load_dotenv
import os
import subprocess
load_dotenv()

# mongorestore --gzip --db restore2 dumpDirectory/

#  mongorestore --gzip --uri=mongodb://0.tcp.in.ngrok.io:17122/restore3 dumpDirectory/KonverseDB/ --numInsertionWorkersPerCollection=2

def makeRestoreCommad(dbName,host,sourcePort):
    uri='--uri=mongodb://{host}:{port}/{DB}'.format(host=host,port=sourcePort,DB=dbName) if not os.getenv('RESTORE_URI') else os.getenv('RESTORE_URI')
    dumpLocation='{}/{}'.format(os.getenv('DESTINATION_DIR'),os.getenv('DATABASE_NAME'))
    return ['mongorestore','--gzip',uri,'--numInsertionWorkersPerCollection={worker}'.format(worker=os.getenv('WORKER')),dumpLocation]


try:
    dbName=os.getenv('restore3')
    sourcePort=os.getenv('RESTORE_PORT')
    host=os.getenv('RESTORE_HOST')
    restoreCMD=makeRestoreCommad(dbName,host,sourcePort)
    subprocess.call(restoreCMD)

except Exception as e:
    print("=================================")
    print(e)
    print("==================================")
