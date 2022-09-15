from random import randrange
from signal import alarm
from socket import AF_KEY
import sys


def solution(sleep_time,alarms):
    # chage everything to minutes
    # pick the min one that is the wake up time
    # chage to time format
    # sleep_time = [1, 6, 13]
    res = sys.maxsize
    sleep_time_in_mins = sleep_time[1] * 60 + sleep_time[2]

    for alarm in alarms:
        my_alarm =alarm[0] * 60 + alarm[1]
        if  my_alarm + sleep_time_in_mins > 1440:
            res =  min(res,(1440 - sleep_time_in_mins) + my_alarm)
        else:
            res = min(res, (alarm[0] * 60 + alarm[1]) - sleep_time_in_mins )
    
    print(res // 60 , res % 60)

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        sleep_time = list(map(int, input().split()))
        alarms = []
        for _ in range(sleep_time[0]):
            alarms.append(list(map(int, input().split())))  

        solution(sleep_time,alarms)