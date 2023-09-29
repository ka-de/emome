"""
This module defines a GUI application that displays a grid of emojis and allows
the user to copy them to the clipboard by clicking on them. The emojis are
organized into seven sets, and the user can switch between them using keyboard
shortcuts. The application is built using PyQt5 and pyperclip libraries.
"""
from PyQt5.QtWidgets import QPushButton
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
)
from PyQt5.QtGui import QIcon, QPalette, QColor
import pyperclip
import keyboard

# Define seven sets of emojis as simple lists
emojis_set1 = ["👾", "🍕", "🔥", "😢", "😄", "⭐", "❤️", "👍", "🐙"]
emojis_set2 = ["🚀", "🌈", "🎉", "😎", "🌸", "🐶", "🐱", "🍔", "☕"]
emojis_set3 = ["🦊", "🐻", "🐯", "🐺", "🐑", "🐗", "🦄", "🦉", "🦌"]
emojis_set4 = ["🚗", "🚲", "🚁", "🐍", "✈️", "🚀", "🚂", "🚢", "🚤"]
emojis_set5 = ["🎮", "🕹️", "👾", "🎲", "🎯", "🎳", "🎰", "🃏", "🕶️"]
emojis_set6 = ["🎶", "🎵", "🎷", "🎸", "🎤", "🎹", "🥁", "🎺", "🎻"]
emojis_set7 = ["🍉", "🍇", "🍓", "🍍", "🍊", "🍋", "🥭", "🍎", "🍏"]


class EmojiButton(QPushButton):
    """
    A custom QPushButton that displays an emoji symbol and copies it to the
    clipboard when clicked.

    Attributes:
        emoji_symbol (str): The emoji symbol to be displayed on the button.

    Methods:
        __init__(self, emoji_symbol, parent=None): Initializes the EmojiButton
        object.
        copy_to_clipboard(self): Copies the emoji symbol to the clipboard and
        toggles the visibility of the window.
    """

    def __init__(self, emoji_symbol, parent=None):
        super().__init__(emoji_symbol, parent)
        self.emoji_symbol = emoji_symbol
        self.clicked.connect(self.copy_to_clipboard)

    def copy_to_clipboard(self):
        """
        Copies the emoji symbol to the clipboard.

        This method uses the pyperclip module to copy the emoji symbol to the
        clipboard. After copying, it toggles the visibility of the window.

        Args:
            None

        Returns:
            None
        """
        pyperclip.copy(self.emoji_symbol)
        self.window().toggle_visibility()


class EmojiWindow(QMainWindow):
    """
    A class representing the main window of the Emome application.

    Attributes:
    - current_emojis (list): A list of strings representing the current set of
    emojis displayed in the window.
    - emoji_buttons (list): A list of EmojiButton objects representing the
    buttons displaying the emojis in the window.

    Methods:
    - __init__(self): Initializes the EmojiWindow object.
    - initUI(self): Initializes the user interface of the Emome application.
    - shift_key_pressed(self, e): A method that is called when the shift key is
    pressed. Changes the current set of emojis to emojis_set2.
    - shift_key_released(self, e): A method that is called when the shift key is
    released. Changes the current set of emojis to emojis_set1.
    - ctrl_key_pressed(self, e): A method that is called when the ctrl key is
    pressed. Changes the current set of emojis to emojis_set3.
    - ctrl_key_released(self, e): A method that is called when the ctrl key is
    released. Changes the current set of emojis to emojis_set1.
    - alt_key_pressed(self, e): A method that is called when the alt key is
    pressed. Changes the current set of emojis to emojis_set4.
    - alt_key_released(self, e): A method that is called when the alt key is
    released. Changes the current set of emojis to emojis_set1.
    - ctrl_alt_pressed(self): A method that is called when the ctrl and alt
    keys are pressed together. Changes the current set of emojis to emojis_set7.
    - ctrl_shift_pressed(self): A method that is called when the ctrl and shift
    keys are pressed together. Changes the current set of emojis to emojis_set5.
    - alt_shift_pressed(self): A method that is called when the alt and shift
    keys are pressed together. Changes the current set of emojis to emojis_set6.
    - update_buttons(self): A method that updates the text of the emoji buttons
    to match the current set of emojis.
    - toggle_visibility(self): A method that toggles the visibility of the
    EmojiWindow object.
    """

    def __init__(self):
        super().__init__()

        self.current_emojis = emojis_set1

        self.initUI()

    def initUI(self):
        """
        Initializes the user interface of the Emome application.

        Sets the window title and icon, creates the central widget, and adds the
        emoji buttons to the grid layout. Also sets up keyboard shortcuts to
        toggle different sets of emojis and to toggle the visibility of the
        application.
        """
        self.setWindowTitle("Emome")

        # Set the application icon with the ICO file (wolf.ico)
        # Replace 'wolf.ico' with the actual file name
        self.setWindowIcon(QIcon('wolf.ico'))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(central_widget)
        grid_layout.setHorizontalSpacing(20)

        emoji_buttons = []

        for i, emoji_symbol in enumerate(self.current_emojis):
            row, col = divmod(i, 3)
            button = EmojiButton(emoji_symbol, self)
            font = button.font()
            font.setPointSize(font.pointSize() + 18)
            button.setFont(font)
            button.setFixedSize(120, 120)
            # Set button background color to #6e6a86
            button.setStyleSheet("background-color: #6e6a86;")
            emoji_buttons.append(button)
            grid_layout.addWidget(button, row, col)

        self.emoji_buttons = emoji_buttons

        keyboard.on_press_key('shift', self.shift_key_pressed)
        keyboard.on_release_key('shift', self.shift_key_released)

        # Detect the Ctrl key press and release to toggle the third set
        keyboard.on_press_key('ctrl', self.ctrl_key_pressed)
        keyboard.on_release_key('ctrl', self.ctrl_key_released)

        # Detect the Alt key press and release to toggle the fourth set
        keyboard.on_press_key('alt', self.alt_key_pressed)
        keyboard.on_release_key('alt', self.alt_key_released)

        # Detect Ctrl + Alt key combination to toggle the seventh set
        keyboard.add_hotkey('ctrl+alt', self.ctrl_alt_pressed)

        # Detect Ctrl + Shift key combination to toggle the fifth set
        keyboard.add_hotkey('ctrl+shift', self.ctrl_shift_pressed)

        # Detect Alt + Shift key combination to toggle the sixth set
        keyboard.add_hotkey('alt+shift', self.alt_shift_pressed)

        keyboard.add_hotkey('ctrl+alt+e', self.toggle_visibility)

    def shift_key_pressed(self, e):
        if not e.is_keypad:
            if self.current_emojis is not emojis_set2:
                self.current_emojis = emojis_set2
                self.update_buttons()

    def shift_key_released(self, e):
        if not e.is_keypad:
            if self.current_emojis is not emojis_set1:
                self.current_emojis = emojis_set1
                self.update_buttons()

    def ctrl_key_pressed(self, e):
        if not e.is_keypad:
            if self.current_emojis is not emojis_set3:
                self.current_emojis = emojis_set3
                self.update_buttons()

    def ctrl_key_released(self, e):
        if not e.is_keypad:
            if self.current_emojis is not emojis_set1:
                self.current_emojis = emojis_set1
                self.update_buttons()

    def alt_key_pressed(self, e):
        if not e.is_keypad:
            if self.current_emojis is not emojis_set4:
                self.current_emojis = emojis_set4
                self.update_buttons()

    def alt_key_released(self, e):
        if not e.is_keypad:
            if self.current_emojis is not emojis_set1:
                self.current_emojis = emojis_set1
                self.update_buttons()

    def ctrl_alt_pressed(self):
        if self.current_emojis is not emojis_set7:
            self.current_emojis = emojis_set7
            self.update_buttons()

    def ctrl_shift_pressed(self):
        if self.current_emojis is not emojis_set5:
            self.current_emojis = emojis_set5
            self.update_buttons()

    def alt_shift_pressed(self):
        if self.current_emojis is not emojis_set6:
            self.current_emojis = emojis_set6
            self.update_buttons()

    def update_buttons(self):
        for i, emoji_symbol in enumerate(self.current_emojis):
            self.emoji_buttons[i].emoji_symbol = emoji_symbol
            self.emoji_buttons[i].setText(emoji_symbol)

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    emoji_window = EmojiWindow()

    # Set the application background color to #191724
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(25, 23, 36))
    app.setPalette(palette)

    emoji_window.show()
    sys.exit(app.exec_())
