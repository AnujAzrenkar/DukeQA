import sys
import configparser
import mysql.connector

config = configparser.ConfigParser()
config.read('config.ini')



if len(sys.argv)==3: 
    param = sys.argv[1]
    project = sys.argv[2]
    if param == '-p' and project == 'mcc':
     dbase = config['mysqlDB']['db2']
     print(dbase)	
    elif param == '-p' and  project == 'jc': 
     dbase = config['mysqlDB']['db1']
     print(dbase)
    else:
     print("Use proper command")
else:
    print("Use proper command")

cnx = mysql.connector.connect(user=config['mysqlDB']['user'],
                              password=config['mysqlDB']['pass'],
                              host=config['mysqlDB']['host'],
                              port=config['mysqlDB']['port'],
                              database=dbase)

try:
    cursor = cnx.cursor()
    cursor.execute("""
		SELECT u.id, u.email, u.first_name, u.last_name, GROUP_CONCAT( sg.event_id) AS 'Events', GROUP_CONCAT(sg.user_ip) AS 'User_ip' FROM users u JOIN sendgrid_events_users sg ON sg.user_id = u.id WHERE  u.is_subscribed =1 AND u.is_active=1 GROUP BY sg.user_id
	""")
    result = cursor.fetchall()
    print(result)
finally:
    cnx.close()