# PyAutoGUI notes
Jul 24, 2018

## Pauses and Fail-Safes
- Use ```pyautogui.PAUSE = 1.5``` to wait 1.5 seconds after each PyAutoGUI
function call, so you can have a window to stop an out-of-control program.

- Use ```SHFT-OPT-Q``` to log out when mouse is unresponsive or uncontrollable.

- Use the fail-safe feature. When you move the mouse quickly to the upper
  corner of the screen, PyAutoGUI will throw a FailSafeException. You can
  choose to handle this or not. Or you can turn it off completly.
  pyautogui. ```FailSafeException = False```.
