import argparse
import yml
import sys
sys.path.append('C:/DukeQA/UnitIV - Structured Flow/modules')
from modules.config_module import MainConfig
from modules import unsubscribe_module

#Using the argparse python library for custom commands 
#creating a simple instance and using it
parser = argparse.ArgumentParser()
parser.add_argument("-p","--project",help="project can have value 'mcc' or 'jc'")
args = parser.parse_args()


dbname = a[args.project]['databases[1]']
user = a[args.project]['username']
password = a[args.project]['password']

mysql.createConnection(dbname, user, password)

unsubscribe_module.run()

database.closeConnector()
