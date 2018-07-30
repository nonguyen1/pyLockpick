# pyLockpick

This is my solution for solving the lock pick problem created by HackMIT 2018
puzzle#3.

## The challenge goeas as follows: 

You'be been recruited to be trained to be the master lock picker. We present
you the finest lockpicking training program, the Lockpick Simulator 3000.

Your mission is to acheive more than a golden number lockpicks under 20
seconds. Get a 100 lockpicks, and you will unlock the answer.

__FOR MAC USERS open the application by using ./lockpick__

## How to use:
Make sure you have the required modules installed by using the following
command: 

```
pip install -r requirements.txt
```

Open lockpick program with the following settings: 
- lowest resolution (640 X 400)
- Ultra graphics settings
- Window mode enabled

Place the lockpick application in the far left corner.

Once the applications is loaded and placed in the corner, run the script using
the command

```
python pyLock.py
```

You can then start the lock pick program and the locks should begin picking.

There should be no output to the terminal. I avoided using
prints because depending on your cpu speed, print statements may reduce
efficiency. This is to ensure the program will complete 100 lockpicks in 20
seconds.

