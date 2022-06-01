from time import sleep
import mouse
import keyboard


class DataContainer:
    SLEEP_TIME: int = 60
    SHIFT_BUTTON: str = "shift"
    LOOP_TIME: float = 0.05
    SPACE_BUTTON: str = "space"


def run() -> None:
    try:
        while True:
            first_mouse_position: tuple[int, int] = mouse.get_position()
            sleep(DataContainer.SLEEP_TIME)
            second_mouse_position: tuple[int, int] = mouse.get_position()
            if first_mouse_position == second_mouse_position:
                for _ in range(100):
                    sleep(DataContainer.LOOP_TIME)
                    if keyboard.is_pressed(hotkey=DataContainer.SPACE_BUTTON):
                        break
                    else:
                        keyboard.press_and_release(DataContainer.SHIFT_BUTTON)
            else:
                pass
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
