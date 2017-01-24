"""
Author:YCY
Time:
Description: Read DBSettings From a xml File. Connect to DB and Throw some related Exceptions.
"""
import time

from JSYOptimalControl.assist import Log

import xml.etree.ElementTree as ET
import cx_Oracle


class DB(object):
    @classmethod
    def get_connect_object(cls):
        tree = ET.parse('../dbset.xml')
        root = tree.getroot()
        connect_string = ""
        conn = ""
        # Parse XML and Get ConnectString
        for database in root.findall('DataBase'):
            if database.get('name') == 'Oracle':
                host_ip = database.find('HostIP').text
                db_source = database.find('DBSource').text
                username = database.find('UserName').text
                password = database.find('PassWord').text
                connect_string = username + '/' + password + '@' + host_ip + '/' + db_source
        try:
            conn = cx_Oracle.connect(connect_string)
        except Exception as e:
            # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  " + str(e))
            Log.write_log(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  " + str(e))

        return conn


if __name__ == '__main__':
    conn1 = DB.get_connect_object()
    print(conn1)




