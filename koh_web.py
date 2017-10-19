# coding:utf-8
''' koh_web.py
    This module is implemented 'KingOfHillTool'.
    It send HTTPS Request to hack and check connection speed.
'''

import datetime
import time
import requests

import koh_tool


class KoH_Web(koh_tool.KingOfHillTool):
    ''' It is implemented 'KingOfHillTool'.

        It send HTTPS Request to hack and check connection speed.
    '''

    def task(self):
        ''' It is implemented 'KingOfHillTool.task()' to send https request.

            Send HTTPS Request to attack ctf server .
        '''
        # send https request
        payload = {'key': 'value'}
        response = requests.post(self.url, data=payload)
        print(response.text)

        # save file
        _file = open('index.html', 'wb')
        _file.write(response.content)
        _file.close()

    def measure_connection_time(self):
        ''' It is implemented 'KingOfHillTool.measure_connection_time'
            to send https request.

            Send HTTPS requests to measure connection time.
        '''

        # start couting
        start_time = time.time()

        # test to send https request
        payload = {'hoge': 'spam'}
        response = requests.post(self.url, data=payload)

        # stop counting
        connection_time = time.time() - start_time
        connection_time /= 2

        return connection_time


if __name__ == '__main__':
    # schedule list
    schedule_list = [
        #datetime.datetime(yy, mm, dd, hh, mm, ss)
    ]

    # start koh_web
    koh_web = KoH_Web('https://example.com', schedule_list)
    koh_web.run()
