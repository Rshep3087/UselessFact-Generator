import PySimpleGUI as sg
import requests
from loguru import logger

def get_fact():
	r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
	return r.json().get("text")


layout = [[sg.Text('Useless Fact:', size=(12,2)), sg.Text("Select Get Useless Fact Button for a Useless Fact", size=(75,2), key="-FACT-")],
          [sg.Button('Get Useless Fact'), sg.Exit()]]
		 

window = sg.Window("Useless Fact Generator", layout, finalize=True)

while True:
    event, values = window.read()
    logger.info(event, values)
    if event is None or event == "Exit":
        break
    if event == "Get Useless Fact":
        fact = get_fact()
        window["-FACT-"].update(fact)
		
window.close()
