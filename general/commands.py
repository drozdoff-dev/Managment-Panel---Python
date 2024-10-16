from concurrent.futures import ThreadPoolExecutor, as_completed
import socket
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
from requests.exceptions import HTTPError
import queue
import json
from json import dumps

def command_request(api,login,server_select,command,args,command_slash,client_ip,timerequest,server_host,its_server,main_server,dir,path_global,path_servers,name_file_cfg_servers,name_file_help_servers):
    sys.path.insert(1, dir)
    #команды сервера#
    if(command_slash == "/help"):
        if(args == 'args_none'):

            #выборка глобальных команд
            commands_global = ''
            path_help_global = dir + f'{path_global}'
            with open(f'{path_help_global}{name_file_help_servers}', 'r', encoding='utf-8') as f:
                global_help = json.load(f)
            for help_gl in global_help['commands']:
                commands_global += f"{help_gl['command']} - {help_gl['description']}\n"
            #выборка глобальных команд

            #выборка команд сервера клиента
            commands_server = ''
            path_help_server = dir + f'{path_servers}{server_select}'
            with open(f'{path_help_server}{name_file_help_servers}', 'r', encoding='utf-8') as f:
                server_help = json.load(f)
            for help_srv in server_help['commands']:
                commands_server += f"{help_srv['command']} - {help_srv['description']}\n"
            #выборка команд сервера клиента

            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": '\n[ОБЩИЕ]\n'
                                                + f'{commands_global}'
                                                + f'\n[Команды СУ - {server_select}]\n'
                                                + f'{commands_server}',
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
        else:
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": f'Вы передали аргументы команде, которая их не воспринимает. Ваши аргументы {args}',
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

    elif(command_slash == "/leave" or command_slash == "/quit" or command_slash == "/q"):
        if(args == 'args_none'):
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": f'Goodbye {login}',
                                    "command": command_slash,
                                    "server_select": server_select,
                                    "server_to": server_select,
                                    "client_ip": client_ip,
                                    "status": "quit",
                                    "server_host": server_host
                                }
                            ]}]
            print(f'<{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}> [Выход] : Пользователь {login} вышел из Панели Управления.')
            response.content_type = 'application/json'
            return dumps(json_request)
        else:
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": f'Вы передали аргументы команде, которая их не воспринимает. Ваши аргументы {args}',
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

    elif(command_slash == "/server_select" or command_slash == "/select_server"):
        if(args != 'args_none'):
            if(server_select == args):
                json_request = [{
                        "commands": [
                            {
                                "login": login,
                                "api": "commands",
                                "answer": f'Вы и так подключены к серверу [{args}]. /servers - для списка серверов.',
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
            else:
                pth = dir + path_servers
                folders = [e for e in os.listdir(pth) if os.path.isdir(pth + e)]

                count_servers = len(next(os.walk(pth))[1]) - 1
                i = 0
                for i, item in enumerate(folders):
                    i += 1
                    if(item == args):
                        print(f'<{timerequest}> {login} подключился к серверу управления "{args}".')
                        json_request = [{
                                "commands": [
                                    {
                                        "login": login,
                                        "api": "commands",
                                        "answer": f'Вы подключились к серверу управления - {args}.',
                                        "command": command_slash,
                                        "server_select": args,
                                        "server_to": server_select,
                                        "client_ip": client_ip,
                                        "status": "ok",
                                        "server_host": server_host
                                    }
                                ]}]
                        response.content_type = 'application/json'
                        return dumps(json_request)
                    elif(i > count_servers):
                        json_request = [{
                                "commands": [
                                    {
                                        "login": login,
                                        "api": "commands",
                                        "answer": f'Вы ввели несуществующий сервер [{args}]. /servers - для списка серверов.',
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
        else:
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": f'Вы не передали аргументы команде, которой они обязательны. Пример - {command} [text]',
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
    elif(command_slash == "/servers"):
        if(args == 'args_none'):
            pth = dir + path_servers
            folders = [e for e in os.listdir(pth) if os.path.isdir(pth + e)]

            servers = ''
            for n, item in enumerate(folders):

                pth_serv = dir + f'{path_servers}{item}'
                with open(f'{pth_serv}{name_file_cfg_servers}', 'r', encoding='utf-8') as f:
                    load_cfg = json.load(f)
                for cfg_serv in load_cfg['host']:
                    server_fullhost = f"{cfg_serv['head']}://{cfg_serv['host']}:{cfg_serv['port']}"
                    server_host_check = f"{cfg_serv['host']}"
                    server_port_check = f"{cfg_serv['port']}"

                if(item == main_server):
                    servers += f"[{n + 1}] - {item} ({check_to_connect_servers(server_fullhost)}) - Основной сервер управления\n"
                else:
                    servers += f"[{n + 1}] - {item} ({check_to_connect_servers(server_fullhost)}) - Дочерний сервер управления\n"

            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": f'Список серверов:\n{servers}',
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
        else:
            json_request = [{
                            "commands": [
                                {
                                    "login": login,
                                    "api": "commands",
                                    "answer": f'Вы передали аргументы команде, которая их не воспринимает. Ваши аргументы {args}.',
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
        json_request = [{
                        "commands": [
                            {
                                "login": login,
                                "api": "commands",
                                "answer": f'Команды {command} несуществует. Используется /help для просмотра доступных команд.',
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
    #неизвестная команда#

def check_to_connect_servers(host):
    try:
        requests.post(host)
        return 'Доступен'
    except requests.exceptions.ConnectionError:
        return 'Недоступен'
        