import bpy
import random
import math

# list of positions
positions = [
    [4, 6, 3],
    [6, 6, 3],
    [3, 3, 3],
    [3, 2, 3],
    [7, 3, 3],
    [7, 2, 3],
    [4, 1, 3],
    [5, 1, 3],
    [6, 1, 3]
]

def createCubeWithMat( x, y, z, scale=1 ):
    # blender API call to create cube
    bpy.ops.mesh.primitive_cube_add( location=( x, y, z ), size=scale )
    
    # get that cube and assign it a new material
    cube = bpy.context.active_object
    cube.data.materials.append( bpy.data.materials.new( name='Material' ) )
    
    # return this cube
    return cube

# create cubes at positions and store them in a list for referencing later
cubes = [ createCubeWithMat( x, y, z ) for x, y, z in positions ]

# THIS LOOP VERSION CREATES A KEYFRAME AT EVERY FRAME BETWEEN 0-100
frames = 100
for frame in range( frames + 1 ):
    for cube in cubes:
        
        # generate a random rotation value in x, y, z axis
        rx = random.uniform( 0, math.radians( 30 ) )
        ry = random.uniform( 0, math.radians( 30 ) )
        rz = random.uniform( 0, math.radians( 30 ) )
        
        # apply that rotation the the cube
        cube.rotation_euler = ( rx, ry, rz )
        
        # add keyframe into the timeline for rotation change
        cube.keyframe_insert( data_path='rotation_euler', frame=frame )
        
        # get the cube's material ( a bit hacky maybe? )
        mat = cube.data.materials[0]
        
        # set material's color to random value between red-green gradient
        mat.diffuse_color = ( 
            random.uniform( 0.0, 1.0 ), # R
            random.uniform( 0.0, 1.0 ), # G
            0.0, # B
            1.0 # A
        )
        
        # add keyframe into the timeline for material color change
        mat.keyframe_insert( data_path='diffuse_color', frame=frame )

## THIS LOOP VERSION CREATES A KEYFRAME AT 0 AND 100 ONLY
#for cube in cubes:
#    
#    # add keyframe at 0 for rotation
#    cube.keyframe_insert( data_path='rotation_euler', frame=0 )
#    
#    # generate a random rotation value in x, y, z axis
#    rx = random.uniform( 0, math.radians( 25 ) )
#    ry = random.uniform( 0, math.radians( 25 ) )
#    rz = random.uniform( 0, math.radians( 25 ) )
#    
#    # apply that rotation the the cube
#    cube.rotation_euler = ( rx, ry, rz )
#    
#    # add keyframe into the timeline for rotation change
#    cube.keyframe_insert( data_path='rotation_euler', frame=100 )
#    
#    # get the cube's material ( a bit hacky maybe? )
#    mat = cube.data.materials[0]
#    
#    # add keyframe at 0 for material color
#    mat.keyframe_insert( data_path='diffuse_color', frame=0 )
#    
#    # set material's color to random value between red-green gradient
#    mat.diffuse_color = ( 
#        random.uniform( 0.0, 1.0 ), # R
#        random.uniform( 0.0, 1.0 ), # G
#        0.0, # B
#        1.0 # A
#    )
#    
#    # add keyframe into the timeline for material color change
#    mat.keyframe_insert( data_path='diffuse_color', frame=100 )