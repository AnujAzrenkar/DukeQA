import os
import yaml
import mysql.connector

class MainConfig:
   def gen_config(self):
       try:
           with open("config.yml", 'r') as ymlfile:
               main_config = yaml.load(ymlfile)

       except Exception as ex:
           print(str(ex))

       finally:
           return main_config