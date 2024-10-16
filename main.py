#verison_settings
app_develop = 'Mexpy'
version_app = '0.0.2-B'
#verison_settings

import array
import codecs
import datetime
import importlib
from json import dumps
import os
import random
import socket
import sys
import threading
import time
from urllib import response
from zoneinfo import ZoneInfo
import zoneinfo
from bottle import route, run, template, request, WSGIRefServer, ServerAdapter, Bottle
import pymysql
import hashlib
import requests
import json
from cheroot.wsgi import Server as CherryPyWSGIServer
from cherrypy.process.servers import ServerAdapter
import secrets
import string
from pyfiglet import Figlet, fonts, FigletFont
import colorama
from colorama import Fore, Back, Style
from configparser import ConfigParser
import urllib

#connect_to_off
close_key = 'wiLK6QR9N0j8lKOJ0GFacQu0Gc0z5C95PdF92yEUFA6hJcJMseIzZP7ZHsj0GySHRLru4ikFxwjahI9P2kLmCVdIHRskGPQcMuIpkhaqMb1CnqmaWTDvCSRZs3HX2e0IYJCQkUwYkhU160ginaE5T2cscBU7voeUaBc0li0bXnUJbHKwycIWORecGgTwgVbsIlSNvK0dKsolwksnFwmDHtWUukt7aXawHsYfVMC16VrggIZG4hMBP02neFa4Ppl4Dr'

close_hash512_key_object = hashlib.sha512(close_key.encode('utf-8'))
close_hash512_key = close_hash512_key_object.hexdigest()

open_key = '6uX5l0GL66kdQkNb9YahNoivOjwQojtWKxZ21K1zzzT8qnIyZQMjonld6i2agDkSpjf0Zvm3J91EwzGnLAn5XbPLuRCNVGtD0QtRwm6XxCG6JHfXZEs5QANYdvJC9sAX2QCuJtP9oAyBtSa6XZ0s8LloFv0pp2axrJfCSLfr0AmCTJMYHaKw80qJ2ta6JSTF0L6nm2fibjXuGa76cbSD4MwuAzHxzM6r14YIb8VmWglLRYsedFS4bqhBk1kibEfqU4OPdjb97aTZXMqa9jp0XhX3qu6eFvEVAxhZOZprw5l8NUpBFdhCW9cxsD2aBsQk5lMT8w9XTiEVNZB26qVoyCV3RLbadS7w5CvTcQMTyyN2En4NQPjsd7uiCxoVF3qHVlmmSGMBDd35DTtt7IFAJ5uWU77UlDSLBr4AFwktd2dhX5qQ21kfDo04uD4Xy4nuOJ3Gl9h57sJNS5ZwDL7AS9QXNh8jfkrB1eoEqPBwdsjx0Jc7fhF5Sz5IBaIv3y63FHBmoduLXglPV7EVD0iZIZCesPwcvWGmL36I1I7R2KuBJZQcoPevFNtkdIZDGgvEpJXrVOn3ijNixMQS66LiIqLqkQ8OQV3ktOzuMrQ2rF8S1gspEHsRltDedqNbJ3Yf4adVNP4'

private_app_key = "0i4rbOaj99XfSWB487JZUCHIvXThxsRj80EQNHWY3x5ZMV6qw3AhhqQEgPpbLxX8StEsSc04EP7lKhStGMRtycTIkfcCFz6UM6sbq8KVwJKMG1cebqP6fulC9JhbxjZq8KrbzxI0Likx1zsxrAXhlKmhg6xQB7YszaHTLn0jDyUDLQfN9DSv2vGF8Wqo3J3aMJQbWhTGZ5cm4jbVdjkviBACfHxbAsFQryxfICkMK9dC8hNKWy2TKKiLhbOa4G80g7n1L3drHNAqd9qOjDTlisuJNnujlQlApRwUAtWNTvVD13uN9V8iTbJlC3FJXc1uOjUZjSZIpzWqAmB4gWpTvzNkRfla9BLu7A1xBocCtnkSXCLhULK9AhWLAVb8GuRe4Ysr9Knvw6w39lDaAGgxKK8GAVeIs4lLraYRSxlbZEUoIofcAJU6TNiyzLfNyIrX6xgd4bSKk88ipPWv021CgYY8HkqYtg4yEJMgkvznEVEV0cSnRwxdP60oO1tRQDFiZZyctKFIP3hCWcR7Q453NhYLOnWcyl0MVQBiBHoDcRG88TYU8LCYF4GUzAgcFhUHDLIaiQf6p3CjSeOeJLtK0eHAnQbh6cafg0hIqyJA0zmQzzyr20r4x2iixIJoVFRhevwGM1yUjoFyHm"
#connect_to_off

# determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    name_script = os.path.basename(__file__)
    application_path = os.path.dirname(sys.executable).replace(name_script, '')
elif __file__:
    name_script = os.path.basename(__file__)
    application_path = os.path.dirname(__file__).replace(name_script, '')

sys.path.insert(1, application_path)

app = Bottle()

hash_to_web_private = "wlTYdxGTZIudHsgBSkTSlaDJlyiPaMiHqPOkBjNfgNxVJfHtfUnrQmoPkThieqBVxQtuTsECBVQZiGNTabofaBHBHotVNKbPndICPFJIOwfvIxmSuOQphlGpsWzlxowq"
status_its_server = 'none'

def check_languages():
    languages_array = ['russian', 'english']

    select_lang = f'{config_init("no_child")[20]}'

    if(select_lang == ''):
        select_lang = 'english'

    i = 0
    for l in languages_array:
        i += 1
        if(l == select_lang):
            path = application_path + '/languages/'
            languages = [e for e in os.listdir(path) if os.path.isfile(path + e)]

            count_lang = len(next(os.walk(path))[2])
            i = 0
            for i, lang in enumerate(languages):
                i += 1
                if(lang == select_lang + '.ini'):
                    print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The language you selected "{Fore.LIGHTYELLOW_EX}{select_lang}{Fore.LIGHTWHITE_EX}"')
                    return select_lang
                elif(i >= count_lang):
                    print(f'{Fore.LIGHTRED_EX}[Error] The language you selected is not in "languages/{Fore.RED}{select_lang}.ini{Fore.LIGHTRED_EX}"')
                    print(Style.RESET_ALL)
                    return sys.exit()
        elif(i >= len(languages_array)):
            print(f'{Fore.LIGHTRED_EX}[Error] Language not found - {Fore.RED}{select_lang}{Fore.LIGHTRED_EX}"')
            print(Style.RESET_ALL)
            return sys.exit()

def check_date_time_to_type():
    if(config_init('no_child')[22] != 'system'):
        count_zones = len(aviable_zones)-1
        for i, zone in enumerate(aviable_zones):
            if(i <= count_zones and zone == config_init('no_child')[22]):
                if(int(config_init('no_child')[23]) == 12):
                    datetime_type = datetime.datetime.now(tz=ZoneInfo(config_init('no_child')[22])).strftime("%d-%m-%Y %I:%M:%S %p")
                    print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time zone you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[22]}{Fore.LIGHTWHITE_EX}"')
                    print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time format you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[23]} AM/PM{Fore.LIGHTWHITE_EX}"')
                    return datetime_type
                elif(int(config_init('no_child')[23]) == 24):
                    datetime_type = datetime.datetime.now(tz=ZoneInfo(config_init('no_child')[22])).strftime("%d-%m-%Y %H:%M:%S")
                    print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time zone you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[22]}{Fore.LIGHTWHITE_EX}"')
                    print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time format you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[23]} H{Fore.LIGHTWHITE_EX}"')
                    return datetime_type
                else:
                    print(f'{Fore.LIGHTRED_EX}[Error] {Fore.LIGHTWHITE_EX}Time Format "{Fore.RED}{config_init("no_child")[23]}{Fore.LIGHTWHITE_EX}" not found.')
                    print(f'{Fore.LIGHTYELLOW_EX}[Help] {Fore.LIGHTWHITE_EX}Available Time Formats:\t{Fore.LIGHTGREEN_EX}12 {Fore.LIGHTWHITE_EX}| {Fore.LIGHTGREEN_EX}24')
                    print(Style.RESET_ALL)
                    return sys.exit()
            elif(i >= count_zones and zone != config_init('no_child')[22]):
                print(f'{Fore.LIGHTRED_EX}[Error] {Fore.LIGHTWHITE_EX}TimeZone "{Fore.RED}{config_init("no_child")[22]}{Fore.LIGHTWHITE_EX}" not found.')
                print(f'{Fore.LIGHTYELLOW_EX}[Help] {Fore.LIGHTWHITE_EX}List of available TimeZones.')
                for i, zone in enumerate(aviable_zones):
                    print(f'{Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}{i}{Fore.LIGHTWHITE_EX}] {Fore.LIGHTGREEN_EX}{zone}')
                print(Style.RESET_ALL)
                return sys.exit()
    else:
        if(int(config_init('no_child')[23]) == 12):
            datetime_type = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time zone you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[22]}{Fore.LIGHTWHITE_EX}"')
            print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time format you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[23]} AM/PM{Fore.LIGHTWHITE_EX}"')
            return datetime_type
        elif(int(config_init('no_child')[23]) == 24):
            datetime_type = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time zone you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[22]}{Fore.LIGHTWHITE_EX}"')
            print(f'{Fore.GREEN}[Setting] {Fore.LIGHTWHITE_EX}The time format you have chosen "{Fore.LIGHTYELLOW_EX}{config_init("no_child")[23]} H{Fore.LIGHTWHITE_EX}"')
            return datetime_type
        else:
            print(f'{Fore.LIGHTRED_EX}[Error] {Fore.LIGHTWHITE_EX}Time Format "{Fore.RED}{config_init("no_child")[23]}{Fore.LIGHTWHITE_EX}" not found.')
            print(f'{Fore.LIGHTYELLOW_EX}[Help] {Fore.LIGHTWHITE_EX}Available Time Formats:\t{Fore.LIGHTGREEN_EX}12 {Fore.LIGHTWHITE_EX}| {Fore.LIGHTGREEN_EX}24')
            print(Style.RESET_ALL)
            return sys.exit()

def date_time_to_type():
    if(config_init('no_child')[22] != 'system'):
        if(int(config_init('no_child')[23]) == 12):
            datetime_type = datetime.datetime.now(tz=ZoneInfo(config_init('no_child')[22])).strftime("%d-%m-%Y %I:%M:%S %p")
            return datetime_type
        elif(int(config_init('no_child')[23]) == 24):
            datetime_type = datetime.datetime.now(tz=ZoneInfo(config_init('no_child')[22])).strftime("%d-%m-%Y %H:%M:%S")
            return datetime_type
        else:
            print(f'{Fore.LIGHTRED_EX}[Error] {Fore.LIGHTWHITE_EX}Time Format "{Fore.RED}{config_init("no_child")[23]}{Fore.LIGHTWHITE_EX}" not found.')
            print(f'{Fore.LIGHTYELLOW_EX}[Help] {Fore.LIGHTWHITE_EX}Available Time Formats:\t{Fore.LIGHTGREEN_EX}12 {Fore.LIGHTWHITE_EX}| {Fore.LIGHTGREEN_EX}24')
            print(Style.RESET_ALL)
            return sys.exit()
    else:
        if(int(config_init('no_child')[23]) == 12):
            datetime_type = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
            return datetime_type
        elif(int(config_init('no_child')[23]) == 24):
            datetime_type = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            return datetime_type
        else:
            print(f'{Fore.LIGHTRED_EX}[Error] {Fore.LIGHTWHITE_EX}Time Format "{Fore.RED}{config_init("no_child")[23]}{Fore.LIGHTWHITE_EX}" not found.')
            print(f'{Fore.LIGHTYELLOW_EX}[Help] {Fore.LIGHTWHITE_EX}Available Time Formats:\t{Fore.LIGHTGREEN_EX}12 {Fore.LIGHTWHITE_EX}| {Fore.LIGHTGREEN_EX}24')
            print(Style.RESET_ALL)
            return sys.exit()

def checking_config():
    print('')

def checking_activate():
    responses = requests.get(f'http://api.mexpy.ru/managment/activation.php?hash={close_hash512_key}&key={open_key}&host={config_init("no_child")[13]}&port={config_init("no_child")[14]}&activate={config_init("no_child")[21]}').json()
    if(responses['checking_activate'][0]['status'] == 'ok'):
        print(f'Добро пожаловать, Уважаемый {responses["checking_activate"][0]["name"]}!')
        print(f'Ваш ключ активации актуален, до окончания активированной версии осталось {responses["checking_activate"][0]["end_day_key"]} дня(-ей), {responses["checking_activate"][0]["end_hours_key"]} часа(-ов), {responses["checking_activate"][0]["end_minutes_key"]} минут(-а,-ы), {responses["checking_activate"][0]["end_seconds_key"]} секунд(-а,-ы). Дата окончания {responses["checking_activate"][0]["end_fulldate_key"]} [TimeZone: Europe/Moscow] Местное время - {datetime.datetime.now(tz=ZoneInfo(responses["checking_activate"][0]["timezone"])).strftime("%d-%m-%Y %H:%M:%S")}.')
        return 'activate'
    elif(responses['checking_activate'][0]['status'] == 'end'):
        print(f'Ваш ключ закончился')
        return 'no_activate'
    elif(responses['checking_activate'][0]['status'] == 'key invalid'):
        print(f'Ключ не был найден')
        return 'no_activate'

def checking_supported():
    responses = requests.get(f'http://api.mexpy.ru/managment/check_supported.php?hash={close_hash512_key}&key={open_key}&host={config_init("no_child")[13]}&port={config_init("no_child")[14]}&activate={config_init("no_child")[21]}&version={version_app}&app={activate_app}').json()
    if(responses['checking_supported'][0]['status'] == 'support'):
        return 'support'
    elif(responses['checking_supported'][0]['status'] == 'no support'):
        return 'no_support'
    elif(responses['checking_supported'][0]['status'] == 'key not found'):
        sys.exit()
    elif(responses['checking_supported'][0]['status'] == 'key invalid'):
        sys.exit()
    elif(responses['checking_supported'][0]['status'] == 'key end'):
        sys.exit()

def checking_update():
    if(config_init('no_child')[24] == 'YES'):
        responses = requests.get(f'http://api.mexpy.ru/managment/check_updates.php?hash={close_hash512_key}&key={open_key}&host={config_init("no_child")[13]}&port={config_init("no_child")[14]}&activate={config_init("no_child")[21]}&version={version_app}&app={activate_app}&support={support_app}').json()
        if(responses['checking_updates'][0]['status'] == 'new_update'):
            if(responses['checking_updates'][0]['type'] == 'activate'):
                print(f'\nДоступна новая лицензионная версия для обновления:\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_app')

            elif(responses['checking_updates'][0]['type'] == 'free'):
                print(f'\nДоступна новая общедоступная/бесплатная версия для обновления:\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_app')

            elif(responses['checking_updates'][0]['type'] == 'none_activate_to_update_free'):
                print(f'\nНе было найдено поддерживаемых лицензионных версий, просьба обновиться до последней общедоступной/бесплатной версии, иначе вы не сможете пользоваться сервером.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

            elif(responses['checking_updates'][0]['type'] == 'new_update_activate_to_free'):
                print(f'\nВаш ключ активации недействителен, но при этом у вас лицензионная версия сервера. Вы не можете использовать лицензионную версию сервера без валидного ключа активации. Можете обновить программу до последней общедоступной/бесплатной версии.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

            elif(responses['checking_updates'][0]['type'] == 'new_update_free_to_free'):
                print(f'\nВаша версия сервера более не поддерживается нашими серверами, но были найдены общедоступные/бесплатные версии для обновления вашего сервера.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

            elif(responses['checking_updates'][0]['type'] == 'new_activate_to_update_nosup'):
                print(f'\nВаша версия более не поддерживается, но была найдена поддерживаемя лицензионная версия.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

        elif(responses['checking_updates'][0]['status'] == 'none_updates'):
            if(responses['checking_updates'][0]['type'] == 'activate'):
                print(f'\nНе было найдено валидных лицензионных версий сервера для обновления.')
                return 1

            elif(responses['checking_updates'][0]['type'] == 'free'):
                print(f'\nНе было найдено валидных общедоступных/бесплатных версий сервера для обновления.')
                return 1

            elif(responses['checking_updates'][0]['type'] == 'none_free_to_closing_activate'):
                print(f'\nВерсия вашего сервера более не поддерживается нашими серверами, при попытке найти новые версии для обновления лицензионной версии не было найдено поддерживаемых версий, после была произведена попытка поиска общедоступных/бесплатных поддерживаемых версий, которые так же не были найдены.\nЕсли вы видите данное сообщение, мы уже работаем над выпуском новой версии, и данные меры были предприняты в срочных целях, о которых мы вас оповестим по окончанию работ.\nПросим прощения за доставленные неудобства.')
                sys.exit()
            elif(responses['checking_updates'][0]['type'] == 'none_free_to_closing_free'):
                print(f'\nВерсия вашего сервера более не поддерживается нашими серверами, при попытке найти новые версии для обновления лицензионной версии не было найдено поддерживаемых версий, после была произведена попытка поиска общедоступных/бесплатных поддерживаемых версий, которые так же не были найдены.\nЕсли вы видите данное сообщение, мы уже работаем над выпуском новой версии, и данные меры были предприняты в срочных целях, о которых мы вас оповестим по окончанию работ.\nПросим прощения за доставленные неудобства.')
                sys.exit()

            elif(responses['checking_updates'][0]['type'] == 'none_update_activate_to_free'):
                print(f'\nТак как у вас лицензионная версия сервера, но ваш ключ является невалидным, мы вынуждены обновить ваш сервер на общедоступную/бесплатную версию. Но при поиске поддерживаемых общедоступных/бесплатных версий, не было найдено поддерживаемых версий.')
                sys.exit()

        elif(responses['checking_updates'][0]['status'] == 'error'):
            if(responses['checking_updates'][0]['type'] == 'free'):
                if(responses['checking_updates'][0]['message'] == 'version_not_found'):
                    print(f'Version Not Found')
                    sys.exit()

            elif(responses['checking_updates'][0]['type'] == 'activate'):
                print('')
                sys.exit()

    elif(config_init('no_child')[24] == 'NO'):
        print(f'Поиск обновлений был пропущен всвязи со значением конфигурации...')
        responses = requests.get(f'http://api.mexpy.ru/managment/check_updates.php?hash={close_hash512_key}&key={open_key}&host={config_init("no_child")[13]}&port={config_init("no_child")[14]}&activate={config_init("no_child")[21]}&version={version_app}&app={activate_app}&support={support_app}').json()
        
        if(responses['checking_updates'][0]['status'] == 'new_update'):
            if(responses['checking_updates'][0]['type'] == 'none_activate_to_update_free'):
                print(f'\nНе было найдено поддерживаемых лицензионных версий, просьба обновиться до последней общедоступной/бесплатной версии, иначе вы не сможете пользоваться сервером.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

            elif(responses['checking_updates'][0]['type'] == 'new_update_activate_to_free'):
                print(f'\nВаш ключ активации недействителен, но при этом у вас лицензионная версия сервера. Вы не можете использовать лицензионную версию сервера без валидного ключа активации. Можете обновить программу до последней общедоступной/бесплатной версии.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

            elif(responses['checking_updates'][0]['type'] == 'new_update_free_to_free'):
                print(f'\nВаша версия сервера более не поддерживается нашими серверами, но были найдены общедоступные/бесплатные версии для обновления вашего сервера.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

            elif(responses['checking_updates'][0]['type'] == 'new_activate_to_update_nosup'):
                print(f'\nВаша версия более не поддерживается, но была найдена поддерживаемя лицензионная версия.\nПоследняя Версия: {responses["checking_updates"][0]["last_version"]}\nНазвание версии: {responses["checking_updates"][0]["last_version_name"]}\nОписание доработок: {responses["checking_updates"][0]["last_version_desc"]}\nДата релиза: {responses["checking_updates"][0]["last_version_published"]}')
                commands_update('update_nosupport')

        elif(responses['checking_updates'][0]['status'] == 'none_updates'):
            if(responses['checking_updates'][0]['type'] == 'none_free_to_closing_activate'):
                print(f'\nВерсия вашего сервера более не поддерживается нашими серверами, при попытке найти новые версии для обновления лицензионной версии не было найдено поддерживаемых версий, после была произведена попытка поиска общедоступных/бесплатных поддерживаемых версий, которые так же не были найдены.\nЕсли вы видите данное сообщение, мы уже работаем над выпуском новой версии, и данные меры были предприняты в срочных целях, о которых мы вас оповестим по окончанию работ.\nПросим прощения за доставленные неудобства.')
                sys.exit()
            elif(responses['checking_updates'][0]['type'] == 'none_free_to_closing_free'):
                print(f'\nВерсия вашего сервера более не поддерживается нашими серверами, при попытке найти новые версии для обновления лицензионной версии не было найдено поддерживаемых версий, после была произведена попытка поиска общедоступных/бесплатных поддерживаемых версий, которые так же не были найдены.\nЕсли вы видите данное сообщение, мы уже работаем над выпуском новой версии, и данные меры были предприняты в срочных целях, о которых мы вас оповестим по окончанию работ.\nПросим прощения за доставленные неудобства.')
                sys.exit()

            elif(responses['checking_updates'][0]['type'] == 'none_update_activate_to_free'):
                print(f'\nТак как у вас лицензионная версия сервера, но ваш ключ является невалидным, мы вынуждены обновить ваш сервер на общедоступную/бесплатную версию. Но при поиске поддерживаемых общедоступных/бесплатных версий, не было найдено поддерживаемых версий.')
                sys.exit()

        elif(responses['checking_updates'][0]['status'] == 'error'):
            if(responses['checking_updates'][0]['type'] == 'free'):
                if(responses['checking_updates'][0]['message'] == 'version_not_found'):
                    print(f'Version Not Found')
                    sys.exit()

            elif(responses['checking_updates'][0]['type'] == 'activate'):
                print('')
                sys.exit()

    else:
        print(f'Неверное значение конфига автообновления.')
    return 1

def commands_update(type):
    if(type == 'update_app'):
        while True:
            user_input = input(f'/Y(/YES) - Update | /N(/NO) - Start APP >>> ')
            user_input = user_input.upper()
            if(user_input == '/Y' or user_input == '/YES'):
                print(f'Тут должен быть этап обновления...')
                req = urllib.request.Request('http://api.mexpy.ru/managment/skinsgtasampstandart.rar', method='HEAD')
                f = urllib.request.urlopen(req)
                url_file_size = int(f.headers['Content-Length'])

                def dlProgress(count, blockSize, totalSize):
                    percent = int(count*blockSize*100/totalSize)
                    sys.stdout.write(f"\r{percent}%/100% | {count*blockSize}/{totalSize}")
                    sys.stdout.flush()

                urllib.request.urlretrieve('http://api.mexpy.ru/managment/skinsgtasampstandart.rar', application_path + '/express-transit.png', reporthook=dlProgress)
                sys.exit()
                #break
            elif(user_input == '/N' or user_input == '/NO'):
                print(f'Сервер продолжил включение без обновления...')
                return 1
    elif(type == 'update_nosupport'):
        while True:
            user_input = input(f'/Y(/YES) - Update | /N(/NO) - Stop APP >>> ')
            user_input = user_input.upper()
            if(user_input == '/Y' or user_input == '/YES'):
                print(f'Тут должен быть этап обновления...')
                sys.exit()
                #break
            elif(user_input == '/N' or user_input == '/NO'):
                print(f'Сервер выключен')
                sys.exit()

def generate_alphanum_crypt_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    crypt_rand_string = ''.join(secrets.choice(
        letters_and_digits) for i in range(length))
    return crypt_rand_string

def set_language():
    language_section = language.upper()

    translate = ConfigParser()
    translate.read(f"{application_path}/languages/{language}.ini", encoding='utf-8')

    return [language_section, translate]

def output_head():
    preview_text = Figlet(font='small')
    print(f'{Fore.LIGHTMAGENTA_EX}{preview_text.renderText("Develop by " + app_develop)}\n{Fore.CYAN}{preview_text.renderText("Version: " + version_app)}')
    print(Style.RESET_ALL)

def initilize_its_server():
    path = application_path + '/servers/'
    servers = [e for e in os.listdir(path) if os.path.isdir(path + e)]

    count_servers = len(next(os.walk(path))[1])
    i = 0
    for i, item in enumerate(servers):
        i += 1
        if(item == config_init("no_child")[1]):
            if(config_init("no_child")[1] == config_init("no_child")[0]):
                if(config_init("no_child")[16] == config_init("no_child")[15]):
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}[{Fore.LIGHTBLUE_EX}{config_init("no_child")[1]}{Fore.LIGHTWHITE_EX}] Проиницилизорован как основной сервер Управления.')
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Поиск и подключение дочерних внутренних серверов:')
                    
                    pth = application_path + '/servers/'
                    folders = [e for e in os.listdir(pth) if os.path.isdir(pth + e)]

                    servers = ''
                    for n, item_child in enumerate(folders):
                        if(item_child != config_init("no_child")[1]):
                            servers += f'\n{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] \t\t{Fore.LIGHTWHITE_EX}"{Fore.LIGHTCYAN_EX}{item_child}{Fore.LIGHTWHITE_EX}" - Дочерний'
                    if(servers == ''):
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Дочерние внутренние сервера не были подключены.')
                    else:
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] \t{Fore.LIGHTWHITE_EX}"{Fore.LIGHTBLUE_EX}{config_init("no_child")[1]}{Fore.LIGHTWHITE_EX}" - Основной {servers}')
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Дочерние сервера подключены.')

                    return 'main'
                else:
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Ошибка...] Сервер {item} указан как глобальный, но секретный ключ в настройках сервера отличается от ключа в глобальных настройках.')
                    return server.stop()
            else:
                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.CYAN}{config_init("no_child")[1]} {Fore.LIGHTWHITE_EX}Проиницилизорован как удалённый сервер Управления зависящий от {Fore.LIGHTBLUE_EX}{config_init("no_child")[0]}{Fore.LIGHTWHITE_EX}.')
                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.CYAN}{config_init("no_child")[1]} {Fore.LIGHTWHITE_EX}Отправка запроса к основному серверу {Fore.LIGHTBLUE_EX}{config_init("no_child")[0]} {Fore.LIGHTWHITE_EX}на взаимную связь.')
                try:
                    requests.post(config_init("no_child")[3])
                except requests.exceptions.ConnectionError:
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [ОШИБКА!] Подключение к основному серверу не удалось.')
                    return server.stop()
                else: 
                    sha512_server_key_its = hashing('no_password','no_command','no_key_main_server',config_init("no_child")[16])[4]
                    sha512_server_key_main = hashing('no_password','no_command',config_init("no_child")[15],'no_key_its_server')[3]
                    private_key_its_server_sha512 = hashing(config_init("no_child")[1],'no_command','no_key_main_server','no_key_its_server')[0]

                    pth = application_path + '/servers/'
                    folders = [e for e in os.listdir(pth) if os.path.isdir(pth + e)]

                    child_servers = ''
                    for n, item in enumerate(folders):
                        if(item != config_init("no_child")[1]):
                            child_servers += f'{item}:'
                    if(child_servers == ''):
                        child_servers = 'none'

                    url = f'{config_init("no_child")[3]}/managment/connects_servers_line/line_to_conn/{config_init("no_child")[1]}/{config_init("no_child")[0]}/{sha512_server_key_its}/{sha512_server_key_main}/{private_key_its_server_sha512}/{config_init("no_child")[12]}/{config_init("no_child")[14]}/{child_servers}'
                    responses = requests.post(url).json()
                    answer = responses[0]['connects'][0]['answer']
                    if(responses[0]['connects'][0]['status'] == 'success'):
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}{answer}')
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Иницилизация дочерних серверов зависящих от "{Fore.CYAN}{config_init("no_child")[1]}{Fore.LIGHTWHITE_EX}" к "{Fore.LIGHTBLUE_EX}{config_init("no_child")[0]}{Fore.LIGHTWHITE_EX}".')
                        print(f"{responses[0]['connects'][0]['servers_child']}")
                        return 'child-remote'
                    elif(responses[0]['connects'][0]['status'] == 'error'):
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [ОШИБКА!] Подключение к серверу {config_init("no_child")[0]} - {config_init("no_child")[3]} не удалось.\nОтвет основного сервера: {answer}')
                        return server.stop()
                    else:
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [ОШИБКА!] Произошла непредвиденная ошибка во время получения ответа от сервера. Проверьте настройки для подключения.')
                        return server.stop()
        elif(i > count_servers):
            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [ОШИБКА!] Во время иницилизации в директории серверов не было найдено глобального сервера "{config_init("no_child")[1]}".')
            return server.stop()

def check_connection_mysql(host_name, user_name, user_password, data_base):
    try:
        pymysql.connect(host=host_name, user=user_name, passwd=user_password, database=data_base, cursorclass=pymysql.cursors.DictCursor)
        return print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}База данных MYSQL успешно подключается.')
    except Exception as e:
        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTRED_EX}[ОШИБКА!] {Fore.WHITE}Подключение к базе данных не удалось.\n{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTRED_EX}[ОШИБКА!]{Fore.RED}', e)
        print(Style.RESET_ALL)
        server.stop()
        return sys.exit()

def create_connection(host_name, user_name, user_password, data_base):
    db_connect = None
    try:
        db_connect = pymysql.connect(host=host_name, user=user_name, passwd=user_password, database=data_base, cursorclass=pymysql.cursors.DictCursor)
        return db_connect
    except Exception as e:
        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [ОШИБКА!] Подключение к базе данных не удалось.\nОшибка -', e)
        return server.stop()

def config_init(server):

    config = ConfigParser()
    config.read(f"{application_path}/config.ini", encoding='utf-8')

    its_server_fullhost = f"{config.get('ITS', 'protocol')}://{socket.gethostbyname(config.get('ITS', 'host'))}:{config.get('ITS', 'port')}"
    its_server = f"{config.get('ITS', 'server')}"
    its_server_protocol = f"{config.get('ITS', 'protocol')}"
    its_server_host = f"{socket.gethostbyname(config.get('ITS', 'host'))}"
    its_server_port = f"{config.get('ITS', 'port')}"
    its_server_key = f"{config.get('ITS', 'secret_key')}"

    main_server_fullhost = f"{config.get('MAIN', 'protocol')}://{socket.gethostbyname(config.get('MAIN', 'host'))}:{config.get('MAIN', 'port')}"
    main_server = f"{config.get('MAIN', 'server')}"
    main_protocol = f"{config.get('MAIN', 'protocol')}"
    main_host = f"{socket.gethostbyname(config.get('MAIN', 'host'))}"
    main_port = f"{config.get('MAIN', 'port')}"
    main_secret_key = f"{config.get('MAIN', 'secret_key')}"

    hash_api = f"{config.get('KEYS', 'hash_api')}"
    key_api = f"{config.get('KEYS', 'key_api')}"

    autocheck_updates = f"{config.get('APP', 'autocheck_updates')}"
    autocheck_updates = autocheck_updates.upper()

    language = f"{config.get('APP', 'language')}"
    key_activation_cfg = f"{config.get('APP', 'key_activation')}"

    timezone = f"{config.get('APP', 'timezone')}"
    format_time = f"{config.get('APP', 'format_time')}"

    key_activation_obj_sha512 = hashlib.sha512(private_app_key.encode('utf-8') + key_activation_cfg.encode('utf-8'))
    key_activation = key_activation_obj_sha512.hexdigest()

    if(key_activation_cfg == ''):
        key_activation = 'none'
    
    if(its_server == main_server):
        db_host = config.get('MYSQL', 'host')
        db_user = config.get('MYSQL', 'user')
        db_pass = config.get('MYSQL', 'password')
        db_base = config.get('MYSQL', 'database')
    else:
        db_host = 'none'
        db_user = 'none'
        db_pass = 'none'
        db_base = 'none'

    if(server != 'no_child'):
        child_server = f"{server}"
        child_server_key = f"{its_server_key}"
    else:
        child_server = f"none"
        child_server_key = f"none"
    
    return [main_server,                        #название главного сервера -                0
            its_server,                         #название основного сервера -               1
            child_server,                       #название дочернего сервера -               2
            main_server_fullhost,               #полный адрес работы главного сервера -     3
            its_server_fullhost,                #полный адрес работы основного сервера -    4
            db_host,                            #хост базы данных mysql -                   5
            db_user,                            #пользователь базы данных mysql -           6
            db_pass,                            #пароль базы данных mysql -                 7
            db_base,                            #название БД базы данных mysql -            8
            main_protocol,                      #протокол адреса API глобального сервера -  9
            main_host,                          #хост адреса API глобального сервера -      10
            main_port,                          #порт адреса API глобального сервера -      11
            its_server_protocol,                #протокол адреса API основного сервера -    12
            its_server_host,                    #хост адреса API основного сервера -        13
            its_server_port,                    #порт адреса API основного сервера -        14
            main_secret_key,                    #секретный ключ глобального сервера -       15
            its_server_key,                     #секретный ключ основного сервера -         16
            child_server_key,                   #секретный ключ дочернего сервера -         17
            hash_api,                           #публичный ключ шифрования для ссылок -     18
            key_api,                            #набор символов для удлиненния url -        19
            language,                           #выбранный язык для локализации -           20
            key_activation,                     #ключ активации сервера -                   21
            timezone,                           #временная зона выбранная пользователем -   22
            format_time,                        #формат времени 12/24 -                     23
            autocheck_updates]                  #автопоиск обновлений -                     24

def hashing(password,command,key_main_server,key_its_server):
    hash_private_md5 = hashlib.md5(hash_to_web_private.encode('utf-8'))
    hash_private_md5_result = hash_private_md5.hexdigest()
    hash_private_sha512 = hashlib.sha512(hash_private_md5_result.encode('utf-8'))
    hash_private = hash_private_sha512.hexdigest()

    hash_objects_pass_sha = hashlib.sha512(password.encode('utf-8'))
    hex_digs_sha = hash_objects_pass_sha.hexdigest()
    hash_objects_pass_md5 = hashlib.md5(hex_digs_sha.encode('utf-8'))
    hash_pass_md5 = hash_objects_pass_md5.hexdigest()
    hash_objects_pass_md5_sha = hashlib.sha512(hash_pass_md5.encode('utf-8'))
    hash_pass = hash_objects_pass_md5_sha.hexdigest()

    hash_api_sha512 = hashlib.sha512(config_init('no_child')[18].encode('utf-8'))
    hash_api_sha512_result = hash_api_sha512.hexdigest()

    hash_api_sha256 = hashlib.sha256(config_init('no_child')[18].encode('utf-8'))
    hash_api_sha256_result = hash_api_sha256.hexdigest()

    password_check = hash_private + hash_pass + hash_api_sha512_result

    hash_command_sha512 = hashlib.sha512(command.encode('utf-8'))
    hash_command_input = hash_command_sha512.hexdigest()

    hash_command_input1 = hash_command_input + hash_private

    key_main_server_sha512 = hashlib.sha512(key_main_server.encode('utf-8'))
    key_main_server_sha512_result = key_main_server_sha512.hexdigest()

    key_its_server_sha512 = hashlib.sha512(key_its_server.encode('utf-8'))
    key_its_server_sha512_result = key_its_server_sha512.hexdigest()
    
    return [password_check, hash_api_sha256_result, hash_command_input1, key_main_server_sha512_result, key_its_server_sha512_result]

def start_server_app():
    if(status_its_server == 'main'):
        @app.route('/managment/connects_servers_line/<api>/<server_name>/<main_server_name>/<key_server_sha512>/<key_main_sha512>/<private_key_sha512>/<protocol_req>/<port_req>/<child_servers>', method='POST')
        def connects_servers_line(api,server_name,main_server_name,key_server_sha512,key_main_sha512,private_key_sha512,protocol_req,port_req,child_servers):
            server_ip_request = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')

            if(api == 'line_to_conn'):
                with open(f'{application_path}/general/servers.json', 'r', encoding='utf-8') as f:
                    text = json.load(f)
                for txt in text['servers']:
                    name = f"{txt['name']}"
                    protocol = f"{txt['protocol']}"
                    host_and_domain = f"{txt['host']}"
                    port = f"{txt['port']}"
                    secret_key_server = f"{txt['secret_key']}"

                with open(f'{application_path}/config.json', 'r', encoding='utf-8') as f:
                    text = json.load(f)
                for txt in text['main']:
                    secret_key_main = f"{txt['secret_key']}"
                    server_main = f"{txt['server']}"

                    host = socket.gethostbyname(host_and_domain)

                    if(server_ip_request == host):
                        if(name == server_name and
                        protocol_req == protocol and
                        port_req == port and
                        hashing('no_password','no_command',secret_key_main,secret_key_server)[3] == key_main_sha512 and
                        hashing('no_password','no_command',secret_key_main,secret_key_server)[4] == key_server_sha512 and
                        main_server_name == server_main):
                            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Сервер] Подключён удалённый сервер {server_name} - {protocol}://{host}:{port}.')
                            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Сервер] Иницилизация дочерних серверов {server_name}.')
                            сh_srv = child_servers.split(':')

                            child_servers_text = ''
                            child_servers_text_js = ''

                            if(child_servers != 'none'):
                                if(child_servers != 'none'):
                                    for i in range(len(сh_srv)-1):
                                        child_servers_text += f'\n<{date_time_to_type()}> [Сервер] \t\t{Fore.LIGHTWHITE_EX}"{сh_srv[i]}" - Дочерний'
                                        child_servers_text_js += f'\n<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] \t\t{Fore.LIGHTWHITE_EX}"{Fore.LIGHTCYAN_EX}{сh_srv[i]}{Fore.LIGHTWHITE_EX}" - Дочерний'
                                
                                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Сервер] \t{Fore.LIGHTWHITE_EX}"{server_name}" - Основной {child_servers_text}\n')
                            else:
                                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Сервер] У сервера {server_name} не было обнаружено подключенных дочерних серверов.')

                            json_request = [{
                                        "connects": [
                                            {
                                                "api": api,
                                                "answer": f'Сервер {server_name} успешно был подключён к {server_main}, и проиницилизирован как удалённый.',
                                                "server_name": server_name,
                                                "servers_child": f'<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] \t{Fore.LIGHTWHITE_EX}"{Fore.CYAN}{server_name}{Fore.LIGHTWHITE_EX}" - Основной {child_servers_text_js}',
                                                "host": f'{protocol}://{host}:{port}',
                                                "status": 'success',
                                            }
                                        ]}]
                            response.content_type = 'application/json'
                            return dumps(json_request)
                        else:
                            json_request = [{
                                        "connects": [
                                            {
                                                "api": api,
                                                "answer": f'Параметры удалённого сервера передаваемые глобальному для связки не соответствуют указанным на глобальном сервере в списке разрешённых удалённых серверов. Сервер - {server_name}',
                                                "server_name": server_name,
                                                "host": f'{protocol}://{host}:{port}',
                                                "status": 'error',
                                            }
                                        ]}]
                            response.content_type = 'application/json'
                            return dumps(json_request)
                    else:
                        json_request = [{
                                    "connects": [
                                        {
                                            "api": api,
                                            "answer": 'IP адрес с которого отправлен запрос, не соответствует ни одному из серверов в списке главного.',
                                            "server_name": server_name,
                                            "host": f'{protocol}://{host}:{port}',
                                            "status": 'error',
                                        }
                                    ]}]
                        response.content_type = 'application/json'
                        return dumps(json_request)

    elif(status_its_server == 'main'):
        @app.route('/managment/authentication/<api>/<server_connect>/<login>/<password>/<hash_public_sha256>/<key_long>', method='POST')
        def authentication(api,server_connect,login,password,hash_public_sha256,key_long):
            client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
            if(api == "auth" or api == "auth_to_system"):
                if(hash_public_sha256 == hashing('none_password','none_command','none_key_main','none_key_server')[1] and key_long == config_init("no_child")[19]):
                    db_connect = create_connection(config_init('no_child')[5], config_init('no_child')[6], config_init('no_child')[7], config_init('no_child')[8])
                    db_request = db_connect.cursor()
                    search_account = db_request.execute(f"SELECT * FROM users WHERE login = '{login}'")
                    if(search_account > 0):
                        db_request.execute(f"SELECT * FROM users WHERE login = '{login}'")
                        output = db_request.fetchall()
                        for row in output:
                            if(password == hashing(row['password'],'none_command','none_key_main','none_key_server')[0]):
                                json_request = [{
                                                "authentication": [
                                                    {
                                                        "id": row['id'],
                                                        "login": row['login'],
                                                        "ip_last": row['ip_last'],
                                                        "ip_reg": row['ip_reg'],
                                                        "city_last": row['city_last'],
                                                        "city_reg": row['city_reg'],
                                                        "date_last": row['date_last'],
                                                        "date_reg": row['date_reg'],
                                                        "rang": row['rang'],
                                                        "name": row['name'],
                                                        "api": api,
                                                        "status": "success"
                                                    }
                                                ]
                                            }]
                                response.content_type = 'application/json'
                                if(api == "auth"):
                                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Авторизация] : [{row["rang"]}] {row["name"]}(login: {row["login"]}; ip: {client_ip}) Успешно авторизовался в Панели Управления.')
                                """elif(api == "auth_to_system"):
                                    print(f'')"""
                                return dumps(json_request)
                            else:
                                json_request = [{ "authentication": [ { "login": login, "api": "auth", "status": "invalid password" } ] }]
                                response.content_type = 'application/json'
                                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Авторизация] : С IP {client_ip} была произведена неудачная попытка в аккаунт {login}. Не правильно введённый пароль.')
                                return dumps(json_request)
                    else:
                        json_request = [{ "authentication": [ { "login": login, "api": "auth", "status": "invalid login" } ] }]
                        response.content_type = 'application/json'
                        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Авторизация] : С IP {client_ip} была произведена неудачная попытка авторизации. Был введён несуществующий логин {login}.')
                        return dumps(json_request)
                else:
                    json_request = [{ "authentication": [ { "login": login, "api": "auth", "status": "invalid public_key" } ] }]
                    response.content_type = 'application/json'
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Авторизация] : С IP {client_ip} был отправлен неверно составленный POST запрос. Публичный ключ несоответствует серверному. Указанный логин: {login}.')
                    return dumps(json_request)
            else:
                json_request = [{ "authentication": [ { "login": 'none', "api": "none", "status": "invalid api" } ] }]
                response.content_type = 'application/json'
                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Неверный запрос] : С IP {client_ip} был отправлен неверно составленный POST запрос. API Указанный в запросе отсутствует на сервере.')
                return dumps(json_request)

    @app.route('/managment/commands/<api>/<login>/<password>/<server_select>/<command>/<args>/<command_private_key_sha512>/<hash_public_sha256>/<key_long>', method='POST')
    def commands(api,login,password,server_select,command,args,command_private_key_sha512,hash_public_sha256,key_long):
        client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')

        #генерация переменной выбранного сервера, или же для переадресации#
        server_host = config_init('no_child')[4]
        #генерация переменной выбранного сервера, или же для переадресации#

        if(api == "commands"):
            command_slash = "/" + command
            if(args != 'args_none'):
                hash_on_command = f'{command} {args}'
            else:
                hash_on_command = command
            if(hashing('none_password',hash_on_command,'none_key_main','none_key_server')[2] == command_private_key_sha512):
                hash_api_sha256_result = hashing('none_password','none_command','none_key_main','none_key_server')[1]
                url = f'{config_init("no_child")[3]}/managment/authentication/auth_to_system/{config_init("no_child")[0]}/{login}/{password}/{hash_api_sha256_result}/{config_init("no_child")[19]}'
                responses = requests.post(url).json()

                if(responses[0]['authentication'][0]['api'] == 'auth_to_system' and responses[0]['authentication'][0]['status'] == 'success'):
                    #команды сервера#
                    path = application_path + '/servers/'
                    servers = [e for e in os.listdir(path) if os.path.isdir(path + e)]

                    count_servers = len(next(os.walk(path))[1])
                    i = 0
                    for i, item in enumerate(servers):
                        i += 1
                        if(item == server_select):
                            select_commands = importlib.import_module(f'servers.{server_select}.commands')
                            return select_commands.command_request(api,login,server_select,command,args,command_slash,client_ip,date_time_to_type(),server_host,config_init('no_child')[1],config_init('no_child')[0],application_path,'/general/','/servers/','config.json','/help.json')
                        elif(i > count_servers):
                            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Сервер] Непредвиденная ошибка несовпадения сервера')
                            json_request = [{
                                            "commands": [
                                                {
                                                    "login": login,
                                                    "api": "commands",
                                                    "answer": f'Непредвиденная ошибка несовпадения сервера.',
                                                    "command": command_slash,
                                                    "server_select": server_select,
                                                    "server_to": server_select,
                                                    "client_ip": client_ip,
                                                    "status": "closed",
                                                    "server_host": server_host
                                                }
                                            ]}]
                            response.content_type = 'application/json'
                            return dumps(json_request)
                    #команды сервера#
                else:
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Коммандер] : Во время исполнения команды {command_slash} произошла ошибка авторизации пользователя {login}.')
                    json_request = [{
                                    "commands": [
                                        {
                                            "login": login,
                                            "api": "commands",
                                            "answer": f'При обмене информации с сервером, не было найдено аккаунтов с переданным логином.',
                                            "command": command_slash,
                                            "server_select": server_select,
                                            "server_to": server_select,
                                            "client_ip": client_ip,
                                            "status": "closed",
                                            "server_host": server_host
                                        }
                                    ]}]
                    response.content_type = 'application/json'
                    return dumps(json_request) 
            else:
                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Коммандер] : Во время исполнения команды {command_slash} произошло несовпадение хеша команды. Введённый логин: {login}')
                json_request = [{
                                "commands": [
                                    {
                                        "login": login,
                                        "api": "commands",
                                        "answer": f'Ошибка хеша во время обмена информацией.',
                                        "command": command_slash,
                                        "server_select": server_select,
                                        "server_to": server_select,
                                        "client_ip": client_ip,
                                        "status": "closed",
                                        "server_host": server_host
                                    }
                                ]}]
                response.content_type = 'application/json'
                return dumps(json_request)  
        else:
            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Коммандер] : С IP {client_ip} был отправлен неверно составленный POST Запрос.')
            json_request = [{
                            "commands": [
                                {
                                    "login": 'none',
                                    "api": "commands",
                                    "answer": f'Произошла ошибка, был отправлен неверно составленный POST Запрос, или же отсутствие передаваемого API.',
                                    "command": 'none',
                                    "server_select": server_select,
                                    "server_to": server_select,
                                    "client_ip": client_ip,
                                    "status": "closed",
                                    "server_host": server_host
                                }
                            ]}]
            response.content_type = 'application/json'
            return dumps(json_request)

    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Подключение точек соединений для API прошло успешно.')
    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Проверка работоспособности API сервиса методом POST.')
    try:
        requests.post(config_init('no_child')[4])
        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}API сервисы успешно принимают запросы POST методом.')
    except requests.exceptions.ConnectionError:
        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> [Ошибка] API сервер не отвечает.')
        return server.stop()
    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTGREEN_EX}[{set_language()[1].get(set_language()[0], "server_is_running")}] {Fore.LIGHTWHITE_EX}Сервер {Fore.CYAN}{config_init("no_child")[1]} {Fore.LIGHTWHITE_EX}работает по адресу {Fore.YELLOW}{config_init("no_child")[4]}\n')
    #for thread in threading.enumerate():
    #    print(thread.name)
    print(Style.RESET_ALL)
    while True:
        command = input(f'[{set_language()[1].get(set_language()[0], "enter_command")}] >>> ')
        if(command == '/stop'):
            server.stop()
            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTRED_EX}[{set_language()[1].get(set_language()[0], "shutdown")}] {Fore.LIGHTWHITE_EX}Сервер {Fore.LIGHTBLUE_EX}{config_init("no_child")[1]} {Fore.RED}выключен{Fore.LIGHTWHITE_EX}, и адрес {Fore.YELLOW}{config_init("no_child")[4]} {Fore.RED}деактивирован{Fore.LIGHTWHITE_EX}.\n')
            print(Style.RESET_ALL)
            break

def begin():
    try:
        server.start()
    except:
        server.stop()

def shutdown():
    server.stop()
    sys.exit()

def checking_running_cherry(host):
    timestamp_start = int(time.time())
    timestamp_end = timestamp_start + 5*60

    push_10s = False
    push_30s = False
    push_5m = False

    datetime_end = datetime.datetime.fromtimestamp(timestamp_end)

    check = True
    while check:
        try:
            try:
                responses = requests.post(f'{config_init("no_child")[4]}/check_run/{gen_code1}/{gen_code2}/{gen_code3}').json()
            except requests.exceptions.ConnectionError:
                if(timestamp_start + 10 <= int(time.time()) and push_10s == False):
                    push_10s = True
                    print(f'\n{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Слишком долгое подключение, можете нажать CTRL + C для завершения работы, или продолжайте ждать если уверены в правильности настроек и доступности.')
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Продолжение подключения... [CTRL + C] для завершения.')
                elif(timestamp_start + 30 <= int(time.time()) and push_30s == False):
                    push_30s = True
                    print(f'\n{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Запуск веб-сервера занимает слишком много времени.')
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Если до {datetime_end} ничего не изменится, то сервер будет автоматически выключен.')
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Советуем проверить конфигурацию сервера и доступность хоста:порта.')
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Продолжение подключения... [CTRL + C] для завершения.\n')
                elif(timestamp_end <= int(time.time()) and push_5m == False):
                    push_5m = True
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTRED_EX}[Выключение сервера...] {Fore.LIGHTWHITE_EX}Попытки подключиться к {Fore.YELLOW}{host} {Fore.LIGHTWHITE_EX}продлились 5 минут. Сервер был выключен, проверьте доступность и правильность хоста.')
                    shutdown()
            except requests.exceptions.JSONDecodeError:
                print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTRED_EX}[Выключение сервера...] {Fore.LIGHTWHITE_EX}Во время обмена сгенерированными ключами веб-сервера с сервером, произошла непредвиденная ошибка.')
                shutdown()
            else:
                if(responses[0]['answer'][0]['status'] != 'ok'):
                    print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.LIGHTRED_EX}[Выключение сервера] {Fore.LIGHTWHITE_EX}Во время обмена сгенерированными ключами веб-сервера с сервером, произошла непредвиденная ошибка.')
                    shutdown()
                else:
                    check = False
                    return True
        except KeyboardInterrupt:
            print('Сервер был выключен вручную.')
            shutdown()

if __name__ == '__main__':
    aviable_zones = zoneinfo.available_timezones()  #запись в массив всех временных зон
    output_head()                                   #вывод заголовка с версией приложения и шапкой разработчика
    language = check_languages()                    #проверка доступности выбранного языка и установка его для всех текстов
    check_date_time_to_type()                       #проверка правильности введёного часового пояса и типа суток, далее установка на весь выводимый текст
    checking_config()                               #проверка всех конфигов на правильность введённых данных + наличие всех директорий и конфигов
    activate_app = checking_activate()              #проверка и установка приложению статуса "активированного", либо же "не активированного"
    support_app = checking_supported()              #проверка нынешней версии приложения на дальнейшую работоспособность
    checking_update()                               #проверка новых обновлений учитывая конфиги пользователя и проверки активированной и поддерживаемой версии приложения



    print(f'\n{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Происходит выделение адреса {Fore.YELLOW}{config_init("no_child")[4]} {Fore.LIGHTWHITE_EX}в параллельный поток.')
    server = CherryPyWSGIServer((config_init('no_child')[13], int(config_init('no_child')[14])),app,server_name=config_init('no_child')[1],numthreads=30)
    threading.Thread(target=begin).start()

    gen_code1 = generate_alphanum_crypt_string(random.randint(32, 512))
    gen_code2 = generate_alphanum_crypt_string(random.randint(32, 512))
    gen_code3 = generate_alphanum_crypt_string(random.randint(32, 512))

    @app.route('/check_run/<code1>/<code2>/<code3>', method='POST')
    def check_run(code1,code2,code3):
        if(code1 == gen_code1 and code2 == gen_code2 and code3 == gen_code3):
            json_request = [{
                            "answer": [
                                {
                                    "status": 'ok'
                                }
                            ]}]
            response.content_type = 'application/json'
            return dumps(json_request)

    if(checking_running_cherry(config_init("no_child")[4]) == True):
        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Адрес {Fore.YELLOW}{config_init("no_child")[4]} {Fore.LIGHTWHITE_EX}успешно привязан к серверу {Fore.LIGHTBLUE_EX}{config_init("no_child")[1]}{Fore.LIGHTWHITE_EX}.')
        status_its_server = initilize_its_server()

        if(status_its_server == 'main'):
            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Проверка подключения к базе данных MYSQL.')
            check_connection_mysql(config_init('no_child')[5], config_init('no_child')[6], config_init('no_child')[7], config_init('no_child')[8])
        elif(status_its_server == 'child-remote'):
            print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Проверка подключения к базе данных MYSQL пропущена, ведь сервер является дочерним.')
        print(f'{Fore.LIGHTYELLOW_EX}<{date_time_to_type()}> {Fore.GREEN}[{set_language()[1].get(set_language()[0], "starting")}] {Fore.LIGHTWHITE_EX}Подключение точек соединений для API.')
        start_server_app()