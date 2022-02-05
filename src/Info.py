import GameBoard as gb

def check(parsedInput, settings):
    if len(parsedInput) != 3:
        print("ERROR, Info command - Invalid arguments.")
        return 84
    if parsedInput[1] not in settings.keys():
        print("ERROR, Info command - Invalid key.")
        return 84
    return 0

def run(parsedInput):
    key = parsedInput[1]
    value = parsedInput[2]
#    print("Before", gb.settings)
    gb.settings[key] = int(value)
#    print("After", gb.settings)

def InfoCmd(parsedInput, Gboard):
    if check(parsedInput, gb.settings) != 84:
        run(parsedInput)