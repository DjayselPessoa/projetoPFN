import PySimpleGUI as sg


class FirstScreen:
    def __init__(self):
        self.layout = [
            [sg.Text('Welcome to the App!')],
            [sg.Text('There are no saved files.', font=('Helvetica', 14), justification='center')],
            [sg.Text('Please fill out the form below to get started.')],
            [sg.Text('Name'), sg.InputText()],
            [sg.Text('Email'), sg.InputText()],
            [sg.Button('Submit')]
        ]

        self.window = sg.Window('First Screen', self.layout)

    def read(self):
        event, values = self.window.read()
        if event == sg.WINDOW_CLOSED:
            return None
        if event == 'Submit':
            name, email = values[0], values[1]
            # Do something with name and email
            return name, email

    def close(self):
        self.window.close()
