
def completa_codigo_de_area(area):
    if len(area) == 2:
        codigo_area_correto = '0{}'.format(area)
    elif len(area) == 1:
        codigo_area_correto = '00{}'.format(area)
    elif len(area) ==3 :
        codigo_area_correto = area
    else:
        codigo_area_correto = area[-3:]
    return codigo_area_correto
