__author__ = 'malcolmbarnes'
__author__ = 'malcolmbarnes'

import csv
import urllib2
import argparse


# Designed the server based on the Printer Class from the text, and likewise with the Response Class.
class Server:
    def __init__(self):
        self.current_task = None
        self.time_remaining= 0

    def tick (self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
        # if self.time_remaining <= 0:
            # self.current_task= None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining= new_task.get_pages() * 60/ self.page_rate

class Request:
    def __init__(self, arrival, duration):
        self.timestamp = arrival
        self.process_time= duration

    def get_stamp(self):
        return self.timestamp

    def get_time(self):
        return self.process_time

    def wait_time(self, current_time):
        return current_time - self.timestamp

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self, items)


def simulateOneServer():
    server = Server()
    print_queue = Queue()

    waiting_times= []
    t= []

    with open('/Users/malcolmbarnes/Desktop/therequests.csv') as csvfile:
        reader= csv.reader(csvfile, delimiter=',')
        for row in reader:
            print row

def main():
    simulateOneServer()




if __name__ == '__main__':
    main()



