import bpy
import math
import random
import string

# basic parameters for double helix generation
cubeScale = 1
radius = 5
numTurns = 6
numCubes = 200

# values to print to console
numVerts = 0
numMats = 0

def nameGen():
    
    # get random letters and numbers using string lib
    letters = ''.join( random.choice( string.ascii_lowercase ) for i in range( 5 ) )
    numbers = ''.join( random.choice( string.digits ) for i in range( 3 ) )
    
    # f string interpolation return
    return f'{letters}:{numbers}'

def createCube( x, y, z, scale ):
    
    global numVerts, numMats
    
    # call to blender API to generate the cube
    bpy.ops.mesh.primitive_cube_add( location=( x, y, z ), size=scale )
    
    # since adding will also cause it to be the active object, we can get it
    cube = bpy.context.active_object
    
    # call nameGen() to rename this cube
    cube.name = nameGen()
    
    # we can then get its vertices and material to add to the counters
    numVerts += len( cube.data.vertices )
    numMats += len( cube.data.materials )
    
def doubleHelix( numCubes, numTurns, radius, scale ):
    
    for i in range( numCubes ):
        # numTurns will determine how many turns the spiral has
        # angle is in steps according to numCubes
        angle = numTurns * math.pi * i / ( numCubes )
        
        # create spiral on x-y plane with sin and cos functions
        # spiral moves in z-direction respective to scale and numCubes
        x = radius * math.sin( angle )
        y = radius * math.cos( angle )
        z = i * scale
        
        # generate the 2 spirals that are opposite each other on x-y plane
        # this creates the double helix shape
        createCube( x, y, z, scale )
        createCube( -x, -y, z, scale )

doubleHelix( numCubes, numTurns, radius, cubeScale )

# print number of objects, vertices and materials in scene to the console
# NOTE: need to toggle console via: Window > Toggle System Console

print( f'Objects: { len(bpy.context.scene.objects) }, Vertices: { numVerts }, Materials: { numMats }' )