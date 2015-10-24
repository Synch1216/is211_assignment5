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
    def __init__(self):
        self.timestamp = seconds
        self.second= process_time

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


def simulateOneServer(url):
    server = Server()
    print_queue = Queue()

    waiting_times= []

    for line in url:
        time = int(line[0])
        queue.enqueue(line)

        print ('time')

def main():
    url_parser = argparse.ArgumentParser()
    url_parser.add_argument("--file", help='url', type=str)
    args= url_parser.parse_args()

    url = csv.reader(urllib2.urlopen(args))
    simulateOneServer(url)




if __name__ == '__main__':
    main()


