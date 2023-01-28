import mouse
import keyboard
import pyautogui
from time import sleep, time
from rich import print
from win10toast import ToastNotifier
toaster = ToastNotifier()

# left click
# mouse.click('right')
keyboard.add_abbreviation("ik", "ilungakadiongo@gmail.com")

print(mouse.get_position())


def move_to_journal() -> bool:
    journal_button = None
    try:
        for o in range(3):
            journal_button = pyautogui.locateOnScreen("journal_button.PNG")
            if journal_button is not None:
                break
            else:
                pass
        if journal_button is not None:
            center_jb = pyautogui.center(journal_button)
            pyautogui.moveTo(center_jb)
            return True
        else:
            print("Can't locate journal button")
            return False
    except BaseException:
        print("An exception occurred")
        return False


def is_error_dialog():
    for o in range(3):
        error_dialog = pyautogui.locateOnScreen("error_dialog.PNG")
        if error_dialog is not None:
            break
        else:
            pass
    try:
        if error_dialog is not None:
            return True
        else:
            return False
    except BaseException as e:
        print(f"An exception occurred {e}")
        return False


def move_to_delete_button() -> bool:
    delete_button = None
    try:
        for o in range(3):
            delete_button = pyautogui.locateOnScreen("button_delete.PNG")
            if delete_button is not None:
                break
        if delete_button is not None:
            center = pyautogui.center(delete_button)
            pyautogui.moveTo(center)
            return True
        else:
            print("Can't locate delete button")
            return False
    except BaseException as be:
        print({be})
        return False


def move_to_save():
    save_button = None
    try:
        for o in range(3):
            save_button = pyautogui.locateOnScreen("save_button.PNG")
            if save_button is not None:
                break
            else:
                pass
        if save_button is not None:
            center = pyautogui.center(save_button)
            pyautogui.moveTo(center)
            return True
        else:
            print("Can't locate save button")
            return False
    except BaseException as be:
        print({be})
        return False
    

def main():
    print("Program start in 5 seconds ...")
    # sleep(5)
    start_time = time()
    done = 0
    moved = False
    for i in range(1000):
        # go to delete button
        pyautogui.moveTo(x=355,y=91)
        mouse.click("left")
        sleep(.5)
        
        # go to journal
        pyautogui.moveTo(x=1036,y=588)
        mouse.click("left")
        sleep(.5)        
        
        # keyboard.send("tab")
        # keyboard.send("enter")
        
        # go to save button
        keyboard.press('ctrl')
        keyboard.send('s') 
        keyboard.release("ctrl")
        keyboard.send("enter")
        sleep(.5)
        
        #  click ok after save
        pyautogui.moveTo(x=1146,y=608)
        mouse.click("left")
        # sleep(0.5)
        # move_save = move_to_save()

        print(f"Done {done}")
        done += 1
        sleep(0.7)
    else:
        print(f"Finished {done} rows!")
        print("--- %s seconds ---" % (time() - start_time))
        toaster.show_toast(f"Finished {done} rows!")
        keyboard.unhook_all()


start = pyautogui.confirm('Shall I proceed?')
if start is not None:
    sleep(5)
    main()
    # print(mouse.get_position())
else: 
    print("The program can't start")


# toast("Hello", "Hello from Python", audio={"src": "ms-winsoundevent:Notification.Looping.Alarm", "loop": "true"})
