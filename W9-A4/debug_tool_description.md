# VS Code Integrated Debug Tool (Python Debugger)

## Overview

VS Code has a built-in Python Debugger that allows us to observe the program's execution in real time, helping locate and fix bugs. The screenshot shows the debugger catching an exception while running `W8-A3/main.py`.

## How It Works

### 1. Setting Breakpoints

In the code editor, click to the left of a line number to set a breakpoint (shown as a red dot). When the program reaches that line, it automatically pauses so you can inspect the current state. In the screenshot, the program paused at line 126 where `exit(1)` is called.

### 2. Starting a Debug Session

Click the green play button in the top toolbar (or press F5) and select the "Python Debugger: Current File" configuration to launch the current Python file in debug mode. The debugger automatically runs the startup command in the terminal and connects to your program.

### 3. Variables Panel

The Variables panel on the left side displays the values of all variables in the current scope in real time. In the screenshot, we can see:
- `CV_PDF_PATH = 'docs/Yaohui_AI.pdf'`
- `JD_FILE_PATH = 'docs/sample_jd.txt'`

This lets you inspect variable values directly without adding `print()` statements.

### 4. Call Stack

The Call Stack panel shows the chain of function calls that led to the current execution point. In the screenshot, the program is at the `<module>` level of `main.py`, line 126.

### 5. Watch Expressions

You can add custom expressions in the Watch panel. The debugger will automatically evaluate and display the results of these expressions each time the program pauses.

### 6. Breakpoints Panel

The Breakpoints panel provides centralised management of all breakpoints. You can also tick "Raised Exceptions" or "Uncaught Exceptions" to make the debugger pause automatically when an exception is thrown. In the screenshot, "Uncaught Exceptions" is enabled, so the debugger paused when `exit(1)` raised a `SystemExit` exception and displayed the exception details.

### 7. Debug Control Buttons

The top toolbar provides several key control buttons:
- **Continue**: Resume execution until the next breakpoint
- **Step Over**: Execute the current line and move to the next one
- **Step Into**: Step into the function called on the current line
- **Step Out**: Step out of the current function
- **Restart**: Restart the debug session
- **Stop**: Terminate the debug session

## What Happened in the Screenshot

The program checks whether the file `docs/Yaohui_AI.pdf` exists. Since the file was not found, it printed "CV file not found" and called `exit(1)`. Because "Uncaught Exceptions" was enabled in the Breakpoints panel, the debugger automatically paused when the `SystemExit` exception was raised and displayed an exception popup, allowing the developer to examine the error and the current variable state.
