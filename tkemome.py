"""
This script creates a GUI application that allows the user to select and copy emojis to
the clipboard. The GUI contains two sets of emojis, and the user can switch between them
by pressing the Shift key. The GUI also includes a hotkey (Ctrl+Alt+E) to toggle the
visibility of the window.

The script imports the following modules:
- tkinter: for creating the GUI
- pyperclip: for copying text to the clipboard
- keyboard: for registering hotkeys and listening for key events

The script defines the following functions:
- copy_to_clipboard: copies the given emoji to the system clipboard
- toggle_visibility: toggles the visibility of the root window between iconic and deiconified states
- update_buttons: updates the text and command of each emoji button in the GUI
- shift_key_handler: a function that handles the shift key press event and updates the current
                     set of emojis accordingly

The script creates a main window using tkinter, and configures the grid layout to have equal
weight for equal spacing. It then creates buttons for each emoji using the grid layout, and
registers a hotkey to toggle window visibility. Finally, it starts listening for Shift key
state changes and enters the main loop to display the GUI.
"""
import tkinter as tk
import pyperclip
import keyboard

# Define two sets of emojis as simple lists
emojis_set1 = ["👾", "🍕", "🔥", "😢", "😄", "⭐", "❤️", "👍", "🐙"]
emojis_set2 = ["🚀", "🌈", "🎉", "😎", "🌸", "🐶", "🐱", "🍔", "☕"]

current_emojis = emojis_set1  # Start with set 1


def copy_to_clipboard(emoji):
    """
    Copies the given emoji to the system clipboard.

    Args:
        emoji (str): The emoji to be copied to the clipboard.

    Returns:
        None
    """
    pyperclip.copy(emoji)


def toggle_visibility():
    """
    Toggles the visibility of the root window between iconic and deiconified states.
    """
    if root.state() == 'iconic':
        root.deiconify()
    else:
        root.iconify()


def update_buttons():
    """
    Updates the text and command of each emoji button in the GUI.

    For each emoji button, the text is set to the corresponding emoji symbol
    from the `current_emojis` list, and the command is set to a lambda function
    that copies the emoji symbol to the clipboard and minimizes the GUI window.

    Args:
        None

    Returns:
        None
    """
    for i, emoji_symbol in enumerate(current_emojis):
        emoji_buttons[i]['text'] = emoji_symbol
        emoji_buttons[i]['command'] = lambda e=emoji_symbol: [
            copy_to_clipboard(e), root.iconify()]


def shift_key_handler(e):
    """
    A function that handles the shift key press event and updates the current
    set of emojis accordingly.

    Args:
        e: The event object representing the shift key press.

    Returns:
        None
    """
    global current_emojis
    if keyboard.is_pressed('shift'):
        if current_emojis is not emojis_set2:
            current_emojis = emojis_set2
            update_buttons()
    else:
        if current_emojis is not emojis_set1:
            current_emojis = emojis_set1
            update_buttons()


# Create the main window
root = tk.Tk()
root.title("Emome")

# Configure grid columns to have equal weight for equal spacing
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Create buttons for each emoji using the grid layout
emoji_buttons = []
for i, emoji_symbol in enumerate(current_emojis):
    row, col = divmod(i, 3)
    button = tk.Button(root, text=emoji_symbol, font=(
        "Arial", 36), command=lambda e=emoji_symbol: [copy_to_clipboard(e), root.iconify()])
    emoji_buttons.append(button)
    button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10)

# Register the hotkey (Ctrl+Alt+E) to toggle window visibility
keyboard.add_hotkey('ctrl+alt+e', toggle_visibility)

# Start listening for Shift key state changes
keyboard.hook(shift_key_handler)

# Start the main loop
root.mainloop()
