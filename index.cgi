#!/usr/local/bin/python
# -*- coding: utf-8 -*- 

import cgi
import MySQLdb

# Для преобразования символов unicode  
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

# Данные для доступа к БД
db_addr = 'MYSQL_SERVER_IP_ADDRESS'
db_user = 'DATABASE_USERNAME'
db_user_passwd = 'DATABASE_PASSWORD'
db_name = 'DATABASE_NAME'

# Пути к текстовым файлам
keywords = open('keywords.txt', 'r').read().splitlines()
keywords_custom = open('keywords_custom.txt', 'rw').read().splitlines()

form = cgi.FieldStorage()
rem_str = form.getvalue('rem_str')
add_str = form.getvalue('add_str')

def mysql(self):
    try:
        db = MySQLdb.connect(db_addr, db_user, db_user_passwd, db_name)
    except MySQLdb.DatabaseError, err:
        print '<b>', err, '</b><audio src=\"alarm.wav\" autoplay></audio>'
    cursor = db.cursor()
    query = str(self)
    cursor.execute(query)
    query = cursor.fetchall()
    db.close()
    return query

def check_support_new():
    query = mysql('SELECT * FROM `ticket` WHERE ticket_state_id = 1 AND queue_id=5;') 
    for s in query:
        ticket = s[1], s[2].decode('utf-8').upper(), s[18].upper()
        print ticket[0], '|', ticket[1], '|', ticket[2], '<br>'
        for key in keywords:
            check = ticket[1].find(key.decode('utf-8').upper()), ticket[2].find(key.decode('utf-8').upper())
            for c in check:
                if c > 0:
                     print '<span style="font-size:18px;"><b>', ticket[0], '|', ticket[1], '|', ticket[2], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'
        for key in keywords_custom:
            check = ticket[1].find(key.decode('utf-8').upper()), ticket[2].find(key.decode('utf-8').upper())
            for c in check:
                if c > 0:
                     print '<span style="font-size:18px;"><b>', ticket[0], '|', ticket[1], '|', ticket[2], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'

def check_service_new():
    query = mysql('SELECT * FROM `ticket` WHERE ticket_state_id = 1 AND queue_id=6;')  
    for s in query:
        ticket = s[1], s[2].decode('utf-8').upper(), s[18].upper()
        print ticket[0], '|', ticket[1], '|', ticket[2], '<br>'
        for key in keywords:
            check = ticket[1].find(key.decode('utf-8').upper()), ticket[2].find(key.decode('utf-8').upper())
            for c in check:
                if c > 0:
                     print '<span style="font-size:18px;"><b>', ticket[0], '|', ticket[1], '|', ticket[2], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'
        for key in keywords_custom:
            check = ticket[1].find(key.decode('utf-8').upper()), ticket[2].find(key.decode('utf-8').upper())
            for c in check:
                if c > 0:
                     print '<span style="font-size:18px;"><b>', ticket[0], '|', ticket[1], '|', ticket[2], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'

def check_abuse_new():
    query = mysql('SELECT * FROM `ticket` WHERE ticket_state_id = 1 AND queue_id=18;')  
    for s in query:
        ticket = s[1], s[2].decode('utf-8').upper(), s[18].upper()
        print ticket[0], '|', ticket[1], '|', ticket[2], '<br>'
        for key in keywords:
            check = ticket[1].find(key.decode('utf-8').upper()), ticket[2].find(key.decode('utf-8').upper())
            for c in check:
                if c > 0:
                     print '<span style="font-size:18px;"><b>', ticket[0], '|', ticket[1], '|', ticket[2], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'
        for key in keywords_custom:
            check = ticket[1].find(key.decode('utf-8').upper()), ticket[2].find(key.decode('utf-8').upper())
            for c in check:
                if c > 0:
                     print '<span style="font-size:18px;"><b>', ticket[0], '|', ticket[1], '|', ticket[2], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'

def check_support_open():
    query = mysql('SELECT * FROM `ticket` WHERE ticket_state_id = 4 AND queue_id=5;')  
    for s in query:
        print s[1], '<br>'
        for key in keywords_custom:
            if s[1] == key:
                print '<span style="font-size:18px;"><b>', s[1], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'

def check_service_open():
    query = mysql('SELECT * FROM `ticket` WHERE ticket_state_id = 4 AND queue_id=6;')  
    for s in query:
        print s[1], '<br>'
        for key in keywords_custom:
            if s[1] == key:
                print '<span style="font-size:18px;"><b>', s[1], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'

def check_abuse_open():
    query = mysql('SELECT * FROM `ticket` WHERE ticket_state_id = 4 AND queue_id=18;')  
    for s in query:
        print s[1], '<br>'
        for key in keywords_custom:
            if s[1] == key:
                print '<span style="font-size:18px;"><b>', s[1], '</b><audio src=\"alarm.wav\" autoplay></audio></span><br>'

def remove_string(string):
    rst = []
    with open('keywords_custom.txt') as fd:
        t = fd.read()
        for line in t.splitlines():
            if line != string:
                rst.append(line)
    with open('keywords_custom.txt', 'w') as fd:
        fd.write('\n'.join(rst))
        fd.write('\n')

def add_string(add_str):
    rst = []
    with open('keywords_custom.txt') as fd:
        t = fd.read()
        for line in t.splitlines():
            rst.append(line)
    with open('keywords_custom.txt', 'w') as fd:
        fd.write('\n'.join(rst))
        fd.write(add_str + '\n')
        fd.write('\n')                                                                                                                                           

print 'Content-type: text/html'
print ''
print '<html>'
print '<head>'
print '<title>OTRS Monitoring</title>'
print '<meta http-equiv="refresh" content="60" >'
print '</head>'
print '<body>'

print '<table cellpadding="0" cellspasing="0" width="100%">'
print '<tr><td colspan="3" height="50" align="left" style="border:#dedbde 1px solid;"><img style="padding:5px;" src="http://freehost.com.ua/images/logo.png"></td></tr>'
print '<tr><td width="15%" align="center" valign="top" style="border:#dedbde 1px solid; padding-bottom:5px;"><div style="padding:3px;border-bottom:#dedbde 1px solid;background:#f7f7f7;">Статические ключевики:</div><div style="border-bott\
om:#dedbde 1px solid; padding-bottom:5px;">'
for key in keywords:
    print key, '<br>'
print '</div><div style="padding:3px; margin-top:2px;margin-bottom:5px; border-bottom:#dedbde 1px solid;background:#f7f7f7;border-top:#dedbde 1px solid;">Открытые тикеты в support:</div>'
check_support_open()
print '</td>'
print '<td width="70%" align="left" valign="top" style="border:#dedbde 1px solid;">' 
print '<div style="width:33%; float:left;"><div style="text-align:center;padding:3px; border-bottom:#dedbde 1px solid;background:#f7f7f7;">Новые тикеты в abuse:</div>'
print '<div style="font-size:12px;padding:3px;">'  
check_abuse_new()
print '</div>'
print '</div>'
print '<div style="width:33%; float:left;"><div style="text-align:center;padding:3px; border-left:#dedbde 1px solid; border-bottom:#dedbde 1px solid;background:#f7f7f7;">Новые тикеты в service:</div>'
print '<div style="font-size:12px;padding:3px;">'
check_service_new()
print '</div>'
print '</div>'
print '<div style="width:33%; float:left;"><div style="text-align:center;padding:3px; border-left:#dedbde 1px solid; border-bottom:#dedbde 1px solid;background:#f7f7f7;">Новые тикеты в support:</div>'
print '<div style="font-size:12px;padding:3px;">'
check_support_new()
print '</div>'
print '</div>'
print '</td>'
print '<td width="15%" align="center" valign="top" style="border:#dedbde 1px solid;padding-bottom:5px;"><div style="padding:3px;border-bottom:#dedbde 1px solid; background:#f7f7f7;">Динамические ключевики:</div><div style="border-bottom:#dedbde 1px solid; padding-bottom:5px;">'

for key in keywords_custom:
    if key:
        print key, '<a href="index.cgi?rem_str=' + key + '">Удалить</a><br>'
print '<form action="index.cgi" method="get" style="padding:0; margin:0;">'
print '<input type="text" name="add_str"><input type="submit" value="Добавить">'
print '</form>'                               
if rem_str:
    remove_string(rem_str)
    print '<script language="JavaScript" type="text/javascript">'
    print 'function redirect() {location="index.cgi";} setTimeout("redirect()", 1);'
    print '</script>'
if add_str:
    add_string(add_str)
    print 'ok'
    print '<script language="JavaScript" type="text/javascript">'
    print 'function redirect() {location="index.cgi";} setTimeout("redirect()", 1);'
    print '</script>'
print '</div><div style="padding:3px; margin-top:2px;margin-bottom:5px; border-bottom:#dedbde 1px solid;background:#f7f7f7;border-top:#dedbde 1px solid;">Открытые тикеты в service:</div>'
check_service_open()
print '</td>'
print '</tr></table>'

print '</body>'
print '</html>'
