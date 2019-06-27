"""
Utility for SVG manipulation, inspired by the utils from write-rnn-tensorflow to a large extend:
https://github.com/hardmaru/write-rnn-tensorflow
"""

import svgwrite
import matplotlib.pyplot as plt
import subprocess

def initiate(size_x, size_y, filename):
    """Initiate SVG drawing.

    Parameters
    ----------
    size_x : int
        Size along the X axis.
    size_y : int
        Size along the Y axis.
    filename : filesystem filename

    Returns
    -------
    dwg : Drawing object.
    """
    dims = (size_x, size_y)
    dwg = svgwrite.Drawing(filename, size=dims)
    dwg.add(dwg.rect(insert=(0, 0), size=dims,fill='white'))
    return dwg


def add_row_strokes(dwg, abs_x, abs_y, data, svg_scale=10, stroke_width=1):
    """Add a row path to a SVG object.

    Parameters
    ----------
    dwg : Drawing object
        SVG object where the path will be added to.
    abs_x : int
        Absolute X position.
    abs_y : int
        Absolute Y position.
    data : np.ndarray
        List of coordinates of the path and stroke indicator.
    svg_scale : int
        SVG scale factor.

    """
    lift_pen = 1
    p = "M%s,%s " % (abs_x, abs_y)
    command = "m"

    for i in range(len(data)):
        if (lift_pen == 1):
            command = "m"
        elif (command != "l"):
            command = "l"
        else:
            command = ""
        x = float(data[i,0])/svg_scale
        y = float(data[i,1])/svg_scale
        lift_pen = data[i, 2]
        p += command+str(x)+","+str(y)+" "

    the_color = "black"

    dwg.add(dwg.path(p).stroke(the_color,stroke_width).fill("none"))


def convert_to_img(filename_svg, filename_png, density):
    """Convert SVG file to img numpy array.

    Parameters
    ----------
    filename_svg : filesystem filename
        Filename for the SVG file.
    filename_png : filesystem filename
        Filename for the PNG file.
    density : int
        Density used during the imagemagick convert.

    Returns
    -------
    img : np.ndarray
        Matrix of the image.
    """
    convert = subprocess.run(['convert', '-density', str(density), filename_svg, filename_png])
    img = plt.imread(filename_png)
    return img
