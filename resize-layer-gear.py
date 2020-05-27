#!/usr/bin/env python

from gimpfu import *

def resize_layer_gear(img, layer) :
    #Assumes resizing for gear cards, 50.8mm x 50.8mm 4x5 grid in a 3300x2550 (letter) file = 600x600 px
    width = 600
    height = 600

    try:
      pdb.gimp_message('scaling layer gear')
      pdb.gimp_layer_scale(layer, width, height, TRUE)


    except Exception as err:
        gimp.message("Unexpected error: " + str(err))
    
register(
    "python-fu-resize-layer-gear",
    "Resize Layer",
    "Resizes a layer to a fixed size",
    "",
    "",
    "",
    "<Image>/Image/Card Macros/Resize Layer (Gear)",
    "RGB, RGB*",
    [],
    [],
    resize_layer_gear)

main()