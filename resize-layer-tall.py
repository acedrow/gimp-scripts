#!/usr/bin/env python

from gimpfu import *

def resize_layer_tall(img, layer) :
    width = 660
    height = 1050

    try:
      pdb.gimp_message('scaling layer tall')
      pdb.gimp_layer_scale(layer, width, height, TRUE)


    except Exception as err:
        gimp.message("Unexpected error: " + str(err))
    
register(
    "python-fu-resize-layer-tall",
    "Resize Layer",
    "Resizes a layer to a fixed size",
    "",
    "",
    "",
    "<Image>/Image/Card Macros/Resize Layer (Tall)",
    "RGB, RGB*",
    [],
    [],
    resize_layer_tall)

main()