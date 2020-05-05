#! /usr/bin/python3

import ndjson
def _write_header(f, out_size, key_id):
    """ 
    Writes the svg header to file f 

    :params f: the file to write to
    :params out_size: the size of the svg image to write
    :params key_id: the key_id taken from the ndjson file
    """
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
    f.write('<!--Created with ndjsontosvg (https:https://github.com/thompson318/ndjsontosvg) \n')
    f.write('\tfrom the simplified Google quickdraw data set. key_id = {:s}-->\n'.format(key_id))
    f.write('<svg width="{:d}" height="{:d}"\n'.format(out_size, out_size))
    f.write('\txmlns="http://www.w3.org/2000/svg">\n')
    f.write('\txmlns:ndjsontosvg="https://github.com/thompson318/ndjsontosvg"\n')
    f.write('\txmlns:quickdraw="https://quickdraw.withgoogle.com/data"\n')
    f.write('\txmlns:scikit-surgery="https://doi.org/10.1007/s11548-020-02180-5">\n\n')


def _draw_line(fileout, line, colour, scale):
    """
    Writes a line of colour to fileout
    """
    x_ordinates = line[0]
    y_ordinates = line[1]
    if len(x_ordinates) != len(y_ordinates):
        raise ValueError("Unequal number of x and y coordinates")

    for point_index, x_ord in enumerate(x_ordinates):
        if point_index == 0:
            fileout.write('\t<path d = "M {:.2f} {:.2f}'.format(x_ord * scale, y_ordinates[point_index] * scale))
        else:
            fileout.write(' L {:.2f} {:.2f}'.format(x_ord * scale, y_ordinates[point_index] * scale))
    fileout.write('" stroke="{:s}" fill="transparent"/>\n'.format(colour))



def ndjsontosvns(filein, input_size, out_size , 
                 line_colour='black', background_colour='white', 
                 check_if_identified = True):
    scale = out_size / input_size
    data = None
    with open('cat_200.ndjson') as f:
        data = ndjson.load(f)

    for index, item in enumerate(data):
        if check_if_identified:    
            if 'recognized' not in item:
                raise KeyError("Item has no recognized key")
            if not item.get('recognized'):
                continue    

        if 'drawing' not in item:
            raise KeyError("Item has no drawing data")
        
        if 'key_id' not in item:
            raise KeyError("Item has no key_id data")
        
        outfilename = 'cat_{:04d}.svg'.format(index)

        with open(outfilename, 'w') as f:
            drawing = item.get('drawing')
            _write_header(f, out_size, item.get('key_id'))
            f.write('\t<rect width="100%" height="100%" fill="{:s}" />\n'.format(background_colour))
            for line in drawing:
                _draw_line(f, line, line_colour, scale)
            f.write('</svg>')

if __name__ == '__main__':
    in_size = 256  #this is from the simplified data set
    out_size = 600 #this is what we want it to be, it's easier to set it in the image, as phaser doesn't scale svg well
    line_colour = "black"
    background_colour = "white"
    ndjsontosvns('cat_200.ndjson', in_size, out_size, line_colour, background_colour)
