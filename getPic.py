#!/usr/bin/env python
#encoding:UTF-8

import re
import urllib
import threading
import time
import Queue
import sys

def getHtml(url):
    status = urllib.urlopen(url).getcode()
    print 'urlopen.getcode status:', status
    if status != 200:
        print "can't reach url:",url
        exit()

    page = urllib.urlopen(url).read()
    return page

#get url of pics
def getUrl(html):
    pattern = r'http://.*?\.jpg!mid'
    imgre = re.compile(pattern)
    imglist = re.findall(imgre, html)
    return imglist

class getImg(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.start()

    def run(self):
        global count
        while(True):
            imgurl = self.queue.get()
            urllib.urlretrieve(imgurl, '%s.jpg' % count)
            count += 1
            if self.queue.empty():
                break
            self.queue.task_done()


def main():
    global count
    #url = "http://girl-atlas.com/a/10130205170100000231"
    url = sys.argv[1]
    print "get all pics from:",url

    html = getHtml(url)
    imglist = getUrl(html)
    threads = []
    count = 0
    queue = Queue.Queue()

    for i in range(len(imglist)):
        queue.put(imglist[i])

    for i in range(4):
        thread = getImg(queue)
        threads.append(thread)

if __name__ == '__main__':
    main()
    print "Down"
    
