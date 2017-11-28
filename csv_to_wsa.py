import random
import WSA as wsa
import wsa_to_svg as svg


def read_csv(file):
    output = {}
    input = open(file, 'r')
    unique_elems = {
        'activities': [],
        'performers': []
    }
    for row in input.readlines():
        c,a,p,state,t = row.split(';')
        if state == 'starts':
            if a not in unique_elems['activities']:
                unique_elems['activities'].append(a)
            if p not in unique_elems['performers']:
                unique_elems['performers'].append(p)
            if c in output.keys():
                output[c].append(get_object(a,p,int(t.strip()),False))
            else:
                output.update({c:[get_object(a,p,int(t.strip()),False)]})
        else:
            for elem in output[c]:
                if elem['completed'] == False and elem['activity'] == a and elem['performer'] == p:
                    elem['timestamp'] = int(t.strip()) - elem['timestamp']
                    elem['completed'] = True
    input.close()
    return output, unique_elems

def get_object( activity, performer, timestamp, completed):
    return {'activity': activity, 'performer': performer, 'timestamp': timestamp, 'completed': completed}


def get_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def get_colors(performers):
    colors = {}
    for performer in performers:
        r,g,b = get_rgb()
        colors.update({performer:(r,g,b)})
    return colors

def get_shapes(activities, init_shapes=['c', 'etb', 'elf', 's', 'sr', 'r', 'd', 'dr']):
    shapes = {}
    for elem in range(len(activities)):
        shapes.update({activities[elem]:init_shapes[elem]})
    return shapes

def convert_timestamps(cases):
    for case in cases.keys():
        max_time = 0
        for task in cases[case]:
            max_time = task['timestamp'] if task['timestamp'] > max_time else max_time
        for task in cases[case]:
            task['timestamp'] = round(task['timestamp']/max_time,2)



if __name__ == "__main__":
    dict, unique_elements = read_csv('test_logs/log-ws.csv')
    #for case in dict.keys():
    #    print(dict[case])
    #print(unique_elements)
    colors = get_colors(unique_elements['performers'])
    #print(colors)
    shapes = get_shapes(unique_elements['activities'])
    #print(shapes)
    convert_timestamps(dict)
    w = wsa.generate_wsa(dict, shapes, colors)
    print(w)
    svg_wsa = svg.generate_svg_code(w,50)
    print(svg_wsa)
