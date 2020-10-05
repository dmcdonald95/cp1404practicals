
HEX_COLOUR_NAMES = {"chocolate": "#d2691e", "blue1": "#0000ff", "antiquewhite": "#faebd7", "darkgoldenrod1": "#ffb90f",
                    "darkgreen": "#006400", "darkorange": "#ff8c00", "darkorchid": "#9932cc", "dimgray": "#696969",
                    "honeydew1": "#f0fff0", "purple": "#a020f0"}
user_colour = input("Pick a colour: ")
while user_colour != "":
    if user_colour in HEX_COLOUR_NAMES:
        print(user_colour, "is", HEX_COLOUR_NAMES[user_colour])
    else:
        print("Invalid colour")
    user_colour = input("Pick a colour: ")
