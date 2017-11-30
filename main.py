import WSA as wsa
import wsa_to_svg as svg
import csv_to_wsa as csv

start = '<!DOCTYPE html> \
<html> \
	<head> \
    <!-- META TAGS --> \
      <meta charset="UTF-8"> \
      <meta name="viewport" content="width=device-width, initial-scale=1.0"> \
      <!-- keywords for search engines--> \
      <meta name="keywords" content="..."> \
      <!-- description for search engines--> \
      <meta name="description" content="..."> \
    <!----------------> \
    <!-- Page TITLE --> \
      <title> Generator </title> \
    <!----------------> \
    <!-- LINKS --> \
      <!-- stylesheet links --> \
      <!-- fonts links --> \
      <link href="https://fonts.googleapis.com/css?family=Dosis|Josefin+Sans|Just+Another+Hand|Montserrat|Pacifico|Saira+Extra+Condensed|Sedgwick+Ave+Display" rel="stylesheet"> \
    <!-----------> \
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script> \
  </head> \
	<body>'

end = '</body> \
</html>'



def generate_index(file, svg):
    f = open(file, 'w')
    f.write(start)
    f.write(svg)
    f.write(end)


if __name__ == "__main__":
    dict, unique_elements = csv.read_csv('test_logs/log-ws.csv')
    colors = csv.get_colors(unique_elements['performers'])
    shapes = csv.get_shapes(unique_elements['activities'])
    csv.convert_timestamps(dict)
    w = wsa.generate_wsa(dict, shapes, colors)
    svg_wsa = svg.generate_svg_code(w,50)
    generate_index('index.html', svg_wsa)
