def check(parsedInput):
    if len(parsedInput) != 1:
        print("ERROR Board command - No arguments expected.")
        return 84
    return 0

def run():
    print("Programme ended")
    exit(0)

def EndCmd(parsedInput, unused):
    if check(parsedInput) != 84:
        run()