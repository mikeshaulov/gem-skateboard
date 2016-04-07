from gemsdk import *
from Tkinter import *
import time

master = Tk()
canvas_center = 250
w = Canvas(master, width=canvas_center * 2, height=100)
w.pack()

def onStatusUpdate(st):
    print 'status update', st
    return 0

def onCombinedData(quaternions,acceleration):
    w.delete(ALL)
    w.create_rectangle(canvas_center, 10, canvas_center + 100 * acceleration[0], 30, fill="red")
    w.create_rectangle(canvas_center, 40, canvas_center + 100 * acceleration[1], 60, fill="green")
    w.create_rectangle(canvas_center, 70, canvas_center + 100 * acceleration[2], 90, fill="blue")
    print acceleration[0],acceleration[1],acceleration[2]
    return 0

if __name__ == '__main__':


    print 'starting program'
    gemMgr = GemManager()
    gem = gemMgr.Gems.values()[0]
    res = gem.setCallbacks(onStatusUpdate,onCombinedData)
    print 'Set on Status Change Result', res
    gem.connect()
    mainloop()
    #raw_input('waiting\n')