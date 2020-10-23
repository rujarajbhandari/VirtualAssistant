import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import wolframalpha
client = wolframalpha.Client("25G3YG-PP4WXRR9HE")

import wikipedia

#import Simple GUI for python
import PySimpleGUI as sg

#sg.theme_previewer()
#Define the window's contents
sg.theme('Light Blue')
layout = [[sg.Text("How can I help you today?")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Virtual Assistant', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    res = client.query(values['-INPUT-'])
    wolframalpha_res = next(res.results).text
    wiki_res = wikipedia.summary(values['-INPUT-'], sentences=1)
    sg.popup("Wolframalpha Result for " + values['-INPUT-'] + ":\n" + wolframalpha_res, "Wikipedia Result for "+ values['-INPUT-'] + ":\n" + wiki_res)


# Finish up by removing from the screen
window.close()

