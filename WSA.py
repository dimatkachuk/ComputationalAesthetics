class WSA:
    def __init__(self, cells, nrows, ncols):
        self.cells = cells
        self.nrows = nrows
        self.ncols = ncols

    def __str__(self):
        str = ''
        for row in self.cells:
            for elem in row:
                str += elem.__str__() + ' '
            str += '\n'
        return str





class Cell:
    def __init__(self, size, shape='s', color=(255,255,255)):
        self.size = size
        self.shape = shape
        self.color = color

    def __str__(self):
        return '(%s,%s,%s)' % (self.size, self.shape, self.color)


def generate_wsa(cases, shapes, colors):
    height, width = get_wsa_size(cases)
    cells = []
    for case in cases.keys():
        cells.append(get_wsa_row(cases[case], shapes, colors, width))
    return WSA(cells, height, width)


def get_wsa_size(cases):
    height = len(cases.keys())
    width = 0
    for case in cases.keys():
        width = len(cases[case]) if len(cases[case]) > width else width
    return (height,width)

def get_wsa_row(case, shapes, colors, max_width):
    row = []
    # Add each task to WSA row (case)
    for task in case:
        cell = Cell(task['timestamp'], shapes[task['activity']], colors[task['performer']])
        row.append(cell)
    # If number of tasks less than maximum width of WSA, add empty cells
    for iter in range(max_width-len(case)):
        row.append(Cell(1.0))
    return row