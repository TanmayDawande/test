import subprocess
import pandas as pd
import pyautogui
import time
from datetime import datetime

def sign_in(id, password):
    subprocess.call('C:\\Users\\om\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')

    time.sleep(5)
    #below code will open zoom, provide the id and password
    pyautogui.click(x=821, y=380, clicks=1, interval=1, button='left')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(id)
    time.sleep(1)
    pyautogui.click(x=1010, y=676, clicks=1, interval=1, button='left')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(password)
    time.sleep(1)
    pyautogui.press('enter')


df = pd.read_csv('Tanmay.csv')
while True:

    now = datetime.now().strftime("%H:%M")
    if now in str(df['timings']):

        row = df.loc[df["timings"] == now]
        m_id = str(row.iloc[0,1])
        m_password = str(row.iloc[0,2])

        sign_in(m_id, m_password)
        time.sleep(60)
