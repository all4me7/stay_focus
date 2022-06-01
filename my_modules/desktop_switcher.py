from pyvda import VirtualDesktop as desktop
from pyvda import AppView as view
import keyboard
import time


class DataContainer:
    FIRST_DESKTOP: int = 1
    SECOND_DESKTOP: int = 2
    ACTIVATION_HOTKEY_1: str = "ctrl+alt"
    ACTIVATION_HOTKEY_2: str = "ctrl+win+alt"
    TIME_VALUE: float = 0.5


def move_window() -> None:
    current_desktop: int = desktop.current().number
    window: object = view.current()

    if current_desktop == DataContainer.FIRST_DESKTOP:
        window.move(desktop(DataContainer.SECOND_DESKTOP))
        time.sleep(DataContainer.TIME_VALUE)
    else:
        window.move(desktop(DataContainer.FIRST_DESKTOP))
        time.sleep(DataContainer.TIME_VALUE)


def desktop_switch() -> None:
    current_desktop: int = desktop.current().number

    if current_desktop == DataContainer.FIRST_DESKTOP:
        desktop(DataContainer.SECOND_DESKTOP).go()
        time.sleep(DataContainer.TIME_VALUE)
    else:
        desktop(DataContainer.FIRST_DESKTOP).go()
        time.sleep(DataContainer.TIME_VALUE)


def run():
    keyboard.add_hotkey(DataContainer.ACTIVATION_HOTKEY_1, desktop_switch)
    keyboard.add_hotkey(DataContainer.ACTIVATION_HOTKEY_2, move_window)
    keyboard.wait()


if __name__ == "__main__":
    run()
