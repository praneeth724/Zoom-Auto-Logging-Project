import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)

def meeting():
    open_link('https://us05web.zoom.us/j/86479150393?pwd=Q1FUV0pWZkNEUFU2S2ZBZ1BCN3lEQT09')

schedule.every().friday.at("09:15").do(meeting)


while 1:
    schedule.run_pending()
    time.sleep(9.30)
