import sys
import mouse
import keyboard
import clipboard
import pyautogui
import pyperclip
from time import sleep, time
from rich import print
from win10toast import ToastNotifier
from pynput.keyboard import Key, Controller
toaster = ToastNotifier()


keyboard.add_abbreviation("ik", "ilungakadiongo@gmail.com")


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


def on_press(key):
    try:
        print(f"alphanumeric {key} pressed")
        if key == Key.esc:
            print("ESC pressed, must exit")
            sleep(10)
    except AttributeError:
        print("special key {0} pressed".format(key))
        if key == Key.esc:
            print("ESC pressed, must exit")
            sleep(10)


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
    start_time = time()
    done = 0
    moved = False
    for i in range(100):
        
        if moved is not True:
            moved = move_to_delete_button()
        if moved:
            mouse.click("left")
            sleep(0.7)
            keyboard.send("tab")
            keyboard.send("enter")
        else:
            print("Mouse not moved to delete button, so can't click")
            break
        
        # sleep(1)
        keyboard.press("ctrl")
        keyboard.send("s")
        keyboard.release("ctrl")
        sleep(1)

        keyboard.send("enter")

        keyboard.press("ctrl")
        keyboard.send("c")
        keyboard.release("ctrl")
        data: str = clipboard.paste()
        if data != "Unposted":
            print(f"Something went wrong we quit, in in clipboard={data}")
            break

        # move_save = move_to_save()

        # if move_save:
        #     mouse.click("left")
        #     # sleep(1)
        #     keyboard.send("enter")
        # else:
        #     print("Impossible d'enregister, on continue")

        # if is_error_dialog():
        #     keyboard.send("enter")
        #     continue
        # else:
        #    print("No error dialog")

        print(f"Ligne {done} done successfully.")
        done += 1
        sleep(0.7)
    else:
        print(f"Finished {done} rows!")
        print("--- %s seconds ---" % (time() - start_time))
        # toaster.show_toast(f"Finished {done} rows!")
        keyboard.unhook_all()


start = pyautogui.confirm("Shall I proceed?")
if start is not None:
    sleep(5)
    # listener = k2.Listener(on_press=on_press)
    # listener.start()
    main()

else:
    print("The program can't start")


# toast("Hello", "Hello from Python", audio={"src": "ms-winsoundevent:Notification.Looping.Alarm", "loop": "true"})
