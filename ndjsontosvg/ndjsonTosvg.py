#! /usr/bin/python3

def write_header(f):
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    f.write('<!--Created with ndjsontosvg (https:https://github.com/thompson318/ndjsontosvg) \n')
    f.write('\tfrom the simplified Google quickdraw data set.-->\n')
    f.write('<svg width="256" height="256"\n')
    f.write('\txmlns="http://www.w3.org/2000/svg">\n')
    f.write('\txmlns:ndjsontosvg="https://github.com/thompson318/ndjsontosvg"\n')
    f.write('\txmlns:quickdraw="https://quickdraw.withgoogle.com/data"\n')
    f.write('\txmlns:scikit-surgery="https://doi.org/10.1007/s11548-020-02180-5">\n\n')


import ndjson

data = None
with open('cat_200.ndjson') as f:
    data = ndjson.load(f)

print(len(data))

for index, item in enumerate(data):
    if 'drawing' not in item:
        raise KeyError("Item has no drawing data")
        
    outfilename = 'cat_{:04d}.svg'.format(index)
    with open(outfilename, 'w') as f:
        drawing = item.get('drawing')
        write_header(f)
        f.write('\t<rect width="100%" height="100%" fill="white" />\n')
        for line in drawing:
            x_ordinates = line[0]
            y_ordinates = line[1]
            if len(x_ordinates) != len(y_ordinates):
                raise ValueError("Unequal number of x and y coordinates")

            for point_index, x_ord in enumerate(x_ordinates):
                if point_index == 0:
                    f.write('\t<path d = "M {:d} {:d}'.format(x_ord, y_ordinates[point_index]))
                else:
                    f.write(' L {:d} {:d}'.format(x_ord, y_ordinates[point_index]))
            f.write('" stroke="black" fill="transparent"/>\n')

        f.write('</svg>')


