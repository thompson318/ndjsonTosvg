#! /usr/bin/python3

import ndjson
import random
import os
import ntpath

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



def ndjsontosvg(filein, outsize , numberofsamples,
                 linecolour='black', backgroundcolour='white', 
                 outdir = "./",
                 checkifidentified = True, randomsort = True,
                 inputsize = 256):
    
    print("filein =  " + filein)
    print("outsize =  " + str(outsize))
    print("ns =  " + str(numberofsamples))
    print("outdir =  " + outdir)
    if numberofsamples > 10000:
       raise ValueError("Maximum number_of_samples is 10000")
    
    fileoutprefix=os.path.splitext(ntpath.basename(filein))[0]
    print("fileoutprefix =  " + fileoutprefix)
    scale = outsize / inputsize
    data = None
    with open(filein) as f:
        data = ndjson.load(f)

    if randomsort:
        random.shuffle(data);
    samples = 0;
    
    for item in data:
        if checkifidentified:    
            if 'recognized' not in item:
                raise KeyError("Item has no recognized key")
            if not item.get('recognized'):
                continue    

        if 'drawing' not in item:
            raise KeyError("Item has no drawing data")
        
        if 'key_id' not in item:
            raise KeyError("Item has no key_id data")
        
        outfilename = os.path.join(outdir, fileoutprefix +  '_{:04d}.svg'.format(samples))

        with open(outfilename, 'w') as f:
            drawing = item.get('drawing')
            _write_header(f, outsize, item.get('key_id'))
            f.write('\t<rect width="100%" height="100%" fill="{:s}" />\n'.format(backgroundcolour))
            for line in drawing:
                _draw_line(f, line, linecolour, scale)
            f.write('</svg>')
        
        samples += 1
        if samples >= numberofsamples:
            break


if __name__ == '__main__':
    insize = 256  #this is from the simplified data set
    outsize = 600 #this is what we want it to be, it's easier to set it in the image, as phaser doesn't scale svg well
    linecolour = "black"
    backgroundcolour = "white"
    numberofsamples = 100
    outdir = "white_on_black/"
    ndjsontosvns('hot air balloon.ndjson', outsize, numberofsamples, linecolour, backgroundcolour,
                    outdir )
