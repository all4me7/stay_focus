from my_modules import always_on, desktop_switcher
from threading import Thread


def always_on_runner():
    always_on.run()


def desktop_switcher_runner():
    desktop_switcher.run()


def main():
    thread_always_on = Thread(target=always_on_runner, args=())
    thread_always_on.start()

    thread_desktop_switcher = Thread(target=desktop_switcher_runner, args=())
    thread_desktop_switcher.start()


if __name__ == "__main__":
    print("Running...")
    main()
