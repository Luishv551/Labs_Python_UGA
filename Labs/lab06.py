def rectangle (lenght,width):

    perimeter = 2 * (lenght + width)
    area = (lenght * width)
    if lenght == width:
        print (f'The perimeter of the rectangle is {perimeter} and the area is {area}. This is a Square')
    else:
        print (f'The perimeter of the rectangle is {perimeter} and the area is {area}. This is not a Square')

def cuboid (lenght,width, height):
    edge_lenght = 4 * (lenght + width + height)
    surface_area = 2 * (lenght * width + lenght * height + width * height)
    volume = lenght * width * height

    if lenght == width == height:
        print (f'The edge lenght of the cuboid is {edge_lenght}, the surface area is {surface_area} and the volume is {volume}. This is a Cube')
    else:
        print (f'The edge lenght of the cuboid is {edge_lenght}, the surface area is {surface_area} and the volume is {volume}. This is not a Cube')

var = input('Insert R for Retangle and C for Cuboid ')

if var == 'r' or var == 'R':
    lenght = int (input('Insert the Lenght:\n'))
    width = int (input('Insert the Width:\n'))
     
    rectangle(lenght, width)
else:
    lenght = int (input('Insert the Lenght:\n'))
    width = int (input('Insert the Width:\n'))
    height = int (input('Insert the Height:\n'))

    cuboid(lenght, width, height)
