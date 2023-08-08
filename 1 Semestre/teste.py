'''
    Site: https://acervolima.com/automacao-gui-usando-python/
'''

# import pyautogui 

#código para mover o mouse
# pyautogui.moveTo(519, 1060, duration= 1)

#código para simular um click
# pyautogui.click()


# pyautogui.moveTo(1717, 352, duration = 1)

# pyautogui.click()



import pyautogui
# moving the cursor left 498 px & down
# 998px from it's current position
pyautogui.moveRel(-498, 996, duration=1)

pyautogui.click()

pyautogui.moveTo(1165,637, duration = 1)

# right clicks at the present cursor
# location
pyautogui.click(button="right")

pyautogui.moveTo(1207,621, duration = 1)

pyautogui.click()