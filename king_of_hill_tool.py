# coding:utf-8
'''king_of_hill_tool.py

It send request for ctf that is 'king of hill.
Implement to use it, when you want use this module.
'''

import requests
import sched
import time
import datetime


class KingOfHillTool():
    ''' The base class of KingOfHillTool.

    Needs implementing following methods to use it:
        * self.task
        * self.measure_connection_time
    '''

    def __init__(self, url, schedule_list, over_time=0):
        ''' The constractor that set up own instance variable.

        Arguments:
            'url'(str): target url string
            'schedule_list'(list in time):
                list that has times object that are sending schedules.
        '''
        # set base config
        self.url = url
        self.schedule_list = schedule_list
        self.over_time = over_time

        # set time
        self.connection_time = self.measure_connection_time()
        print('[Info] The connection time is ' + str(self.connection_time))

    def run(self):
        ''' The main method.

        Loop that culcurate the time to next schedule,
        and waiting then, running 'self.task()'.
        '''
        print('[Info] Start')

        for schedule in self.schedule_list:
            # calculate time to the next schedule
            wait_time = schedule - datetime.datetime.now()
            wait_time = wait_time.total_seconds() - self.connection_time
            wait_time -= self.over_time

            # waiting
            print('[Info] Now time is {}'.format(datetime.datetime.now()))
            print('[Info] Next schedule is {}'.format(schedule))
            print('[Info] Next schedule is {} second before'.format(wait_time))
            time.sleep(wait_time)

            # run task
            print('[Info] The task start !')
            self.task()

    def task(self):
        ''' Run the lootine when the schedule_list called.

        It need implementing.
        '''
        # no implement error(not implement yet)
        print('[Error] You need implementing')
        raise

    def measure_connection_time(self):
        ''' Measure time to connect target.

        It need implementing.
        '''
        # no implement error(not implement yet)
        print('[Error] You need implementing')
        raise
