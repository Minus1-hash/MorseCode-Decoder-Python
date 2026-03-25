sprite = Sprite('Tobi')
m  = {
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}


morseinput = input("Enter the 4-digit Morse code (: ")


morselist = morseinput.split()

pin = ""
for code in morselist:
    if code in m:
        pin += m[code]
    else:
        pin += "?"


print("Decoded PIN:", pin)