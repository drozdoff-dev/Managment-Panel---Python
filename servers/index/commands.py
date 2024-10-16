from urllib import response
import requests
import threading
import time
import datetime
import importlib
import os
import sys
import pymysql
import hashlib
import json
from json import dumps

def command_request(api,login,server_select,command,args,command_slash,client_ip,timerequest,server_host,its_server,main_server,dir,path_global,path_servers,name_file_cfg_servers,name_file_help_servers):
    sys.path.insert(1, dir)
    #команды сервера#
    if(command_slash == "/test1"):
        if(args == 'args_none'):
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": 'test1',
                                    "command": command_slash,
                                    "server_select": server_select,
                                    "server_to": server_select,
                                    "client_ip": client_ip,
                                    "status": "ok",
                                    "server_host": server_host
                                }
                            ]}]
            response.content_type = 'application/json'
            return dumps(json_request)
    elif(command_slash == "/test2"):
        if(args == 'args_none'):
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": 'test2',
                                    "command": command_slash,
                                    "server_select": server_select,
                                    "server_to": server_select,
                                    "client_ip": client_ip,
                                    "status": "ok",
                                    "server_host": server_host
                                }
                            ]}]
            response.content_type = 'application/json'
            return dumps(json_request)
    #команды сервера#

    #неизвестная команда#
    else:
        select_commands_global = importlib.import_module(f'general.commands')
        return select_commands_global.command_request(api,login,server_select,command,args,command_slash,client_ip,timerequest,server_host,its_server,main_server,dir,path_global,path_servers,name_file_cfg_servers,name_file_help_servers)
    #неизвестная команда#