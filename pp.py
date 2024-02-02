import win32api , win32con ,win32gui ,win32ui
import time 
import pyautogui
from win32dic import VK_CODE
import pygetwindow as gw
#window = "WhatsApp"


    
    



def main(spam,message):
    
    start_time = time.time()
    bring_window_to_front("WhatsApp")
    # print(f"awawdwadawdwd{gw.getActiveWindow()}")
    active_window = get_focused_window_title()
    
    if active_window == "WhatsApp":
        active = True
        while active:
            KeyClick('5')
            KeyClick('enter')
            message += 1
            active_window = get_focused_window_title()
            if active_window == "WhatsApp":
                active = True
            else:
                active = False


    else:

        active = False
        
            
    time_mess = time.time() - start_time
    if time_mess > 60:
        time_mess /= 60
        if time_mess > 60:
            time_mess /= 60
            time_mess = f"[{int(time_mess)}] hours"
        else:
            time_mess = f"[{int(time_mess)}] min"
    else:
        time_mess = f"[{int(time_mess)}] sec"


    
        



    print(f"[{message}] messages sent in {time_mess}")



#####################################
##############FUNCTIONS##############
#####################################
    

def bring_window_to_front(window_title):

    try:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(hwnd)
            print(f"Window '{window_title}' brought to front.")
        else:
            print(f"Window '{window_title}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def is_window_active(activeWindow):
    active_window = get_focused_window_title()

    if active_window == activeWindow:
        active = True
    else:
        active = False

def get_focused_window_title():
    while True:
        focused_window = gw.getActiveWindow()
        if focused_window:
            return focused_window.title
                  
def KeyClick(key):
    try:
        win32api.keybd_event(VK_CODE[key], 0, 0, 0)
        time.sleep(0.08)  # You may need to adjust this delay based on your requirements
        win32api.keybd_event(VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
    except KeyError:
        print(f"Key {key} not found in VK_CODE dictionary.")

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)



if __name__ == "__main__":
    #spam = input("what letter wolud u like to spam: ")
    #du = int(input(f"minute u want to sppam [{spam}]:"))
    spam = "5"
    

    message = 0
    main(spam,message)
       
