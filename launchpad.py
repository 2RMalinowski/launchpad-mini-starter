import rtmidi

grid = ['x', 'x', 'o', 'o', 'o', 'o', ' ', 'x', 'o']

def midi_acces():
    mo = rtmidi.MidiOut()
    for port_no in range(mo.get_port_count()):
            port_name = mo.get_port_name(port_no)
            print("MIDI out:", port_name)
            if port_name.find('Launchpad Mini') > -1:
                midi_port = mo.open_port(port_no)
    return midi_port

def reset():
    midi_acces().send_message([0xB0, 00, 00])


def display_grid(key, color, hex = 0x90):
    light_grid = midi_acces().send_message
    for key in range(2, 115, 16):
        light_grid([hex, key, color])
    for key in range(5, 118, 16):
        light_grid([hex, key, color])
    for key in range(32, 40):
        light_grid([hex, key, color])
    for key in range(80, 88):
        light_grid([hex, key, color])
    return light_grid


def get_index_symbol(mylist):
    for i, el in enumerate(mylist): 
        display_board(i, el)
    return
    

def display_board(index_nr, element):
        index_nr = convert_to_lp_nr(index_nr)
        if el x:
                sdasda
        send 


def display_color(gamelist):
    for item in gamelist:
        if item == 'x':
            color = 11
        if item == 'o':
            color = 48
        if item == ' ':
            color = 0
    return color

print(display_color(grid))

# def get_loc(num):
#     pos_dict = {
#         1: 96,
#         2: 99,
#         3: 102,
#         4: 48,
#         5: 51,
#         6: 54,
#         7: 0,
#         8: 3,
#         9: 6,}
#     loc = pos_dict.get(num)
#     retu1rn int(loc)


def display_boxes(list, color, hex = 0x90):
    light_box = midi_acces().send_message
    for loc in list:    
        loc1 = loc + 1
        loc2 = loc + 16
        loc3 = loc + 17
        light_box([hex, loc, color])
        light_box([hex, loc1, color])
        light_box([hex, loc2, color])
        light_box([hex, loc3, color])

    return light_box

display_grid(0x90, 0, 17)
color = random.choice([11, 48])
display_box(0x90, mygrid, color)



# [index + 1 for index, value in enumerate(grid) if value == 'x']

# response = ask_number()
# print(response)
# loc = get_loc(response)
# print(loc)
# color = random.choice([11, 48])
# display_box(0x90, loc, color)



# response = ask_number()
# print(response)
# loc = get_loc(response)
# print(loc)
# color = 11
# display_box(0x90, loc, color)
#display_box(0x90, 0, 11)
#display_box(0x90, 51, 48)
