from MainViewNew import FirstScreen
import PySimpleGUI as sg


class App:
    def __init__(self):
        self.current_screen = None
        self.screens = {
            'first': FirstScreen()
        }

    def run(self):
        self.current_screen = 'first'
        while self.current_screen is not None:
            screen = self.screens[self.current_screen]
            result = screen.read()
            if result is not None:
                self.handle_result(result)
            screen.close()

    def handle_result(self, result):
        # Do something with the result
        print(result)
        self.current_screen = None

if __name__ == '__main__':
    app = App()
    app.run()
