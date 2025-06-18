
def mymyname_writer():
    import pyautogui
    str=input('Enter line: ')

    pos=pyautogui.position()

    for letter in str:
        if letter == " ":
            pyautogui.moveTo(x=pos[0]+30, y=pos[1])
        elif letter.upper() == "A":
            pyautogui.dragTo(x=pos[0]+25, y=pos[1]-100)
            pyautogui.dragTo(x=pos[0]+50, y=pos[1])
            pyautogui.moveTo(x=pos[0]+12, y=pos[1]-50)
            pyautogui.dragTo(x=pos[0]+38, y=pos[1]-50)
            pyautogui.moveTo(x=pos[0]+70, y=pos[1])
            pos=pyautogui.position()
        elif letter.upper() == "N":
            pyautogui.dragRel(xOffset=0, yOffset=-100)
            pyautogui.dragTo(x=pos[0]+50, y=pos[1])
            pyautogui.dragRel(xOffset=0, yOffset=-100)
            pyautogui.moveTo(x=pos[0]+70, y=pos[1])
            pos=pyautogui.position()
        elif letter.upper() == "M":
            pyautogui.dragRel(xOffset=0, yOffset=-100)
            pyautogui.dragRel(xOffset=25, yOffset=50)
            pyautogui.dragRel(xOffset=25, yOffset=-50)
            pyautogui.dragRel(xOffset=0, yOffset=100)
            pyautogui.moveTo(x=pos[0]+70, y=pos[1])
            pos=pyautogui.position()


# --------------------------------------------------------------------------------------------------


def myname_writer():
    import pyautogui


    # Draws my name -- "NAMAN"
            
    pyautogui.sleep(5) # It waits for 5 seconds so that you can switch the screen to MS Paints
    pos=pyautogui.position()

    # To draw "N"
    pyautogui.dragRel(xOffset=0, yOffset=-100)
    pyautogui.dragTo(x=pos[0]+50, y=pos[1])
    pyautogui.dragRel(xOffset=0, yOffset=-100)
    pyautogui.moveTo(x=pos[0]+70, y=pos[1])
    pos=pyautogui.position()
    # # time.sleep(3)

    # To draw "A"
    pyautogui.dragTo(x=pos[0]+25, y=pos[1]-100)
    pyautogui.dragTo(x=pos[0]+50, y=pos[1])
    pyautogui.moveTo(x=pos[0]+12, y=pos[1]-50)
    pyautogui.dragTo(x=pos[0]+38, y=pos[1]-50)
    pyautogui.moveTo(x=pos[0]+70, y=pos[1])
    pos=pyautogui.position()

    # To draw "M"
    pyautogui.dragRel(xOffset=0, yOffset=-100)
    pyautogui.dragRel(xOffset=25, yOffset=50)
    pyautogui.dragRel(xOffset=25, yOffset=-50)
    pyautogui.dragRel(xOffset=0, yOffset=100)
    pyautogui.moveTo(x=pos[0]+70, y=pos[1])
    pos=pyautogui.position()

    # To draw "A"
    pyautogui.dragTo(x=pos[0]+25, y=pos[1]-100)
    pyautogui.dragTo(x=pos[0]+50, y=pos[1])
    pyautogui.moveTo(x=pos[0]+12, y=pos[1]-50)
    pyautogui.dragTo(x=pos[0]+38, y=pos[1]-50)
    pyautogui.moveTo(x=pos[0]+70, y=pos[1])
    pos=pyautogui.position()

    # To draw "N"
    pyautogui.dragRel(xOffset=0, yOffset=-100)
    pyautogui.dragTo(x=pos[0]+50, y=pos[1])
    pyautogui.dragRel(xOffset=0, yOffset=-100)
    pyautogui.moveTo(x=pos[0]+70, y=pos[1])
    pos=pyautogui.position()

if __name__=="__main__":
    myname_writer()