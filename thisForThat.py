def getJSONObject(u, text=""):
    import requests, json

    u += text
    
    r = requests.get(u)

    byteData = r.content
    stringData = byteData.decode("utf8")

    jsonData = json.loads(stringData)

    return jsonData

def getInfoFromJSON(jsonData):
    import json

    this = jsonData.get("this")
    that = jsonData.get("that")

    output = "It's " + this + " for " + that + "!"

    return output

def censorText(jsonData):
    import json

    output = jsonData.get("result")

    return output

    
    



def interface():
    import PySimpleGUI as sg
    
    thisURL = "http://itsthisforthat.com/api.php?json"
    censorURL = "https://www.purgomalum.com/service/json?text="

    layout = [
        [sg.Text("It's this for that")],
        [sg.Text("This is an idea generator which gives an idea in the format its blank for blank. For example it's Twitter for education.")],
        [sg.Text(" " * 256, key = "idea")],
        [sg.Button("Generate Idea")]
        ]

    window = sg.Window("This For That", layout, element_justification = 'c')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == "Generate Idea":
            jsonItem = getJSONObject(thisURL)

            toUpdate = getInfoFromJSON(jsonItem)

            jsonItem = getJSONObject(censorURL, toUpdate)

            toUpdate = censorText(jsonItem)

            window.Element("idea").Update(toUpdate)
        
    window.close()

interface()
