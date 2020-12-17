def calculate(lenght, step, load):
    if not lenght and not step and not load:
        parametrs = {
            "main_beam_height": 0,
            "secondary_beam_height": 0,
            "main_height": 0,
            "hole_height": 0,
            "hole_width": 0,
        }
    else:
        if lenght < step:
            temp = lenght
            lenght = step
            step = temp

        main_beam_height = beam_height(lenght, step, load)
        secondary_beam_height = beam_height(step, 2.5, load)
        main_heigh = main_beam_height + 140
        if main_beam_height > 300:
            hole_height = main_beam_height - 300
        else:
            hole_height = 0

        if hole_height >= 700:
            hole_width = hole_height + 300
        elif hole_height >= 450:
            hole_width = hole_height + 200
        elif hole_height >= 250:
            hole_width = hole_height + 100
        elif hole_height > 0:
            hole_width = hole_height + 50
        else:
            hole_width = 0

        parametrs = {
            "main_beam_height": main_beam_height,
            "secondary_beam_height": secondary_beam_height,
            "main_height": main_heigh,
            "hole_height": hole_height,
            "hole_width": hole_width,
        }
    return parametrs


def beam_height(l, b, load):
    h_list = [i for i in range(200, 1500, 50)]
    load = (9.81 * load) / 1000
    M = ((b * load * 1.2) * l * l) / 8
    W = M * 100 / 24
    h_beam = 1.1 * ((W * 161) ** (1 / 3)) * 10
    main_h = 0
    for h in h_list:
        if h_beam < h:
            if h == 200:
                main_h = h
                break
            else:
                main_h = h - 50
                break
    if main_h == 0:
        main_h = h_list[-1]
    return main_h
