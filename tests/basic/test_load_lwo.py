import pytest
import bpy
from lwo_helper import setup_lwo, diff_files, delete_everything

def load_lwo(infile):
    if (2, 80, 0) < bpy.app.version:
        renderers = ['CYCLES']
    elif (2, 79, 0) < bpy.app.version:
        renderers = ['BLENDER_RENDER', 'CYCLES']
    else:
        renderers = ['BLENDER_RENDER']
    
    for render in renderers:
        bpy.context.scene.render.engine = render
        
        outfile0, outfile1 = setup_lwo(infile)
    
        bpy.ops.import_scene.lwo(filepath=infile)
        bpy.ops.wm.save_mainfile(filepath=outfile0)
    
        diff_files(outfile1, outfile0)
    
        delete_everything()

def test_load_lwo_box1():
    infile = "tests/basic/src_lwo/LWO2/box/box1.lwo"
    load_lwo(infile)

def test_load_lwo_box1_uv():
    infile = 'tests/basic/src_lwo/LWO2/box/box1-uv.lwo'
    load_lwo(infile)

def test_load_lwo_box2_uv():
    infile = 'tests/basic/src_lwo/LWO2/box/box2-uv.lwo'
    load_lwo(infile)

def test_load_lwo5_box3_uv_layers():
    infile = 'tests/basic/src_lwo/LWO/box/box3-uv-layers.lwo'
    load_lwo(infile)

def test_load_lwo_box3_uv_layers():
    infile = 'tests/basic/src_lwo/LWO2/box/box3-uv-layers.lwo'
    load_lwo(infile)

def test_load_lwo_box5_ngon():
    infile = 'tests/basic/src_lwo/LWO2/box/box5-ngon.lwo'
    load_lwo(infile)
