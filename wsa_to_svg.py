# Takes WSA as input an returns the svg code generated from it
def generate_svg_code(wsa, max_size):
    #Initialize svg with sizes according to wsa matrix size and size of one cell
    svg = '<svg width="%d" height="%d">' % (wsa.ncols*max_size, wsa.nrows*max_size)
    #Add code of each cell
    svg += generate_cells_svg(wsa.cells, max_size)
    #We need to close svg code and to return it
    return svg + '</svg>'


def generate_cells_svg(cells, max_size):
    cells_svg = ''
    x = 0
    y = 0
    for row in cells:
        for cell in row:
            cells_svg += generate_cell_svg(cell, max_size, x, y)
            x += max_size
        y += max_size
        x = 0
    return(cells_svg)

def generate_cell_svg(cell, max_size ,x ,y):
    cell_svg = ''
    cell_svg += get_shape(cell.shape, cell.size, max_size, x, y)
    cell_svg += get_color_code(cell.color)
    cell_svg += '/>'
    return(cell_svg)


def get_color_code(color):
    return ' style="fill:rgb(%d,%d,%d);"' % (color[0],color[1],color[2])

def get_shape(shape, size, max_size, x, y):
    shape_svg = ''
    center = max_size / 2
    if shape == 'c':
        shape_svg += '<circle cx="%d" cy="%d" r="%d"' % (x+center,y+center,size*center)
    elif shape == 'etb':
        shape_svg += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d"' % (x + center, y + center, size * center, size*(center-10))
    elif shape == 'elf':
        shape_svg += '<ellipse cx="%d" cy="%d" rx="%d" ry="%d"' % (x + center, y + center, size * (center-10), size *center)
    elif shape == 's':
        x_coord = x + center*(1-size)
        y_coord = y + center*(1-size)
        s_size = 2*(center-(x_coord-x))
        shape_svg += '<rect x="%d" y="%d" width="%d" height="%d"' %(x_coord, y_coord, s_size, s_size)
    elif shape == 'sr':
        x_coord = x + center * (1 - size)
        y_coord = y + center * (1 - size)
        s_size = 2 * (center - (x_coord - x))
        shape_svg += '<rect x="%d" y="%d" width="%d" height="%d" rx="%d" ry="%d"' % (x_coord, y_coord, s_size, s_size, 10, 10)
    elif shape == 'r':
        x_coord = x + center * (1 - size)
        y_coord = y + center/4
        s_size_x = 2 * (center - (x_coord - x))
        s_size_y = center/2
        shape_svg += '<rect x="%d" y="%d" width="%d" height="%d"' % (
        x_coord, y_coord, s_size_x, s_size_y)
    elif shape == 'd':
        x_coord = x + center * (1 - size)
        y_coord = y + center * (1 - size)
        s_size = 2 * (center - (x_coord - x))
        shape_svg += '<rect x="%d" y="%d" width="%d" height="%d" transform="rotate(45 %d %d)"' % (x_coord, y_coord, s_size, s_size, x+center, y+center)
    elif shape == 'dr':
        x_coord = x + center * (1 - size)
        y_coord = y + center * (1 - size)
        s_size = 2 * (center - (x_coord - x))
        shape_svg += '<rect x="%d" y="%d" width="%d" height="%d" transform="rotate(45 %d %d)" rx="%d" ry="%d"' % (
        x_coord, y_coord, s_size, s_size, x+center, y+center, 10, 10)
    return shape_svg

    