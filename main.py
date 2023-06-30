import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)

def meeting():
    open_link('https://us05web.zoom.us/j/86479150393?pwd=Q1FUV0pWZkNEUFU2S2ZBZ1BCN3lEQT09')#YOUR ZOOM LINK PASTE

schedule.every().friday.at("09:15").do(meeting)#MEETING TIME AND DATE INSERT


while 1:
    schedule.run_pending()
    time.sleep(1)
