import mysql.connector
from modules.config_module import MainConfig

class DatabaseConf:
   config=MainConfig().gen_config()
   global cnx
   global  cursor
   print config

   def create_conn(self):
       #readConfig();
       cnx = mysql.connector.connect(user=self.config['db_config']['username'],
                             password=self.config['db_config']['password'],
                             host=self.config['db_config']['host'],
                             port=self.config['db_config']['port'],
                             database=self.config['db_config']['databases'][1])
       cursor = cnx.cursor()

   def runUnsubYahoo(self):
       cursor.execute("""select count(*) from users where email like '%yahoo.com' """)
       result = cursor.fetchall()
       print result

   def close_conn(self):
       self.cnx.close()