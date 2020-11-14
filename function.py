
def fill_area_code(area):
    if len(area) == 2:
        correct_area_code = '0{}'.format(area)
    elif len(area) == 1:
        correct_area_code = '00{}'.format(area)
    elif len(area) == 3:
        correct_area_code = area
    else:
        correct_area_code = area[-3:]
    return correct_area_code

def correct_lenght(lenght):
    if lenght == '':
        correct_lenght = 0
    elif float(lenght) < 0:
        correct_lenght = 0
    else:
        correct_lenght = float(lenght)
    return correct_lenght