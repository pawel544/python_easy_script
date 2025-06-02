import pyautogui
from datetime import datetime
import os
import shutil
import time
import PySimpleGUI as sg




if not os.path.exists("screens"):
    fol=os.mkdir("screens")
screenshot_count = 0


layout=[[sg.Text("Screen Shot")],
        [sg.Text('Podaj liczbe zrzótów'),sg.Input()],
        [sg.Text("Podaj opóźnienie"),sg.Input()],
        [sg.Text(key='-OUTPUT-')],
        [sg.Button("Wyślij"), sg.Button("EXIT")]



        ]
window= sg.Window("Screen Shot",layout, size=(550,550), resizable=True )




def save_screenshot(screenshot_count,today_str,values,window):
    try:
        time.sleep(int(values[1]))
    except ValueError:
        print(window['-OUTPUT-'].update(f"Opóźnienie musi być liczbą"))
        return
    try:
        screenshot_path=pyautogui.screenshot(f'screenshot_{today_str}_{screenshot_count}.png')
        src_path=os.path.abspath(f'screenshot_{today_str}_{screenshot_count}.png')
        dest_dir=os.path.abspath("screens")
        shutil.move(src_path, dest_dir)
        window['-OUTPUT-'].update(f"Utworzono zrzut screenshot_{today_str}_{screenshot_count}.png.")
    except Exception as e:
        window['-OUTPUT-'].update(f"Wystąpił nieoczekiwany błąd {e}")
def take_screenshots(screenshot_count,values):
    try:
        num_screenshots = int(values[0]) if values[0].strip().isdigit() else 1
    except ValueError:
        window['-OUTPUT-'].update(f"Ilość zrzutów musi być liczbą")
        return
    try:
        for x  in range(num_screenshots):

            dat= datetime.now()
            today_str= dat.strftime("%Y_%m_%d")
            screenshot_count+=1
            folder = os.path.join("screens",f'screenshot_{today_str}_{screenshot_count}.png')
            if os.path.exists(folder):
                continue
            save_screenshot(screenshot_count, today_str, values, window)
    except Exception as e:
        window['-OUTPUT-'].update(f"Wystąpił nieoczekiwany błąd {e}")
while True:
    try:
        screenshot_count = len(os.listdir("screens"))
        event, values =window.read()
        print(event, values)
        if event== sg.WIN_CLOSED or event == "EXIT":
            break
        if event == "Wyślij":
            take_screenshots(screenshot_count,values)
    except Exception as e:
        window['-OUTPUT-'].update(f"Wystąpił nieoczekiwany błąd {e}")
window.close()
