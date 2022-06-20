# Sigrid's Cool Eye dot py
An exercise in becoming your ideal self via the magic of VTube Studio and Python.
 
# Setup
1. Install python [Download](https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe)
2. In the terminal, navigate to where `main.py` is and run the command `pip install -r requirements.txt` (you may need to add pip to your PATH variable if the command is not recognized).
3. Run VTube Studio! Approve the plugin authentication request from the UI.
4. Run the command `py main.py` to begin the infinite loop. Precc CTRL+C a few times to kill the process.
 
# Customization
Inside `main.py` you'll see a function `pickRandomExpressionFile()` that randomly chooses an expression file from a predefined list. Simply replace the contents of that list with your eyeball expressions. You can also tweak the timing interval in the main loop function by altering the `time.sleep()` values.
 
In addition, once you hook up your voice recognition library (Python can do that???), there's a boolean flag `cycleRandomly` that you'll want to set to `False` when you say a keyword. This will stop the random cycling, allowing you time to invoke ` await func.setexstate(...)` yourself with the desired expression. Just make sure to set it back to `True` when you're done~!

