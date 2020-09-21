from sense_hat import SenseHat

sense = SenseHat()
sense.low_light = True

sense.clear()

sense.show_letter("S")

index = 1

while True:
    selection = False
    events = sense.stick.get_events()
    for event in events:
        if event.action != "released":
            index+=1
            if index %2 == 0:
                sense.show_letter("S")
            else:
                sense.show_letter("B")
