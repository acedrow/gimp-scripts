#!/usr/bin/env python

from gimpfu import *

#copies and pastes a layer, moves the new layer a distance to the right equal to it's width
def copy_paste_translate(img, layer) :

    try:
      pdb.gimp_message('copy paste translate')
      width = pdb.gimp_drawable_width(layer)
      pdb.gimp_edit_copy(layer)
      pdb.gimp_edit_paste(layer, FALSE)
      currentLayer = img.layers[0]
      pdb.gimp_layer_translate(currentLayer, width, 0)


    except Exception as err:
        gimp.message("Unexpected error: " + str(err))
    
register(
    "python-fu-copy-paste-translate",
    "Resize Layer",
    "Resizes a layer to a fixed size",
    "",
    "",
    "",
    "<Image>/Image/Card Macros/Copy Paste Translate",
    "RGB, RGB*",
    [],
    [],
    copy_paste_translate)

main()