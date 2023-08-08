import bpy

# Sierpinski's triangle 2D fractal
# x1, x2, x3 are the points on the triangle where the cube mesh is placed
# l is the length of the overall triangle
# d is the depth of recursion --- NOTE: higher number = more expensive
def tri( x1, x2, x3, l, d=5 ):
    # stop recursion when d reaches 0
    if d == 0:
        return
    else:
        # recursion call at bottom left point of triangle
        tri( x1, x2, x3, l/2, d-1 )
        bpy.ops.mesh.primitive_cube_add( location=(x1+l, x2, x3), size=0.75 )
        
        # recursion call at top middle point of triangle
        tri( x1+l, x2, x3, l/2, d-1 )
        bpy.ops.mesh.primitive_cube_add( location=(x1+(l/2), x2+l, x3), size=0.75 )
        
        # recursion call at bottom right point of triangle
        tri( x1+(l/2), x2+l, x3, l/2, d-1 )
        
# I put d=5 recursions here.
# you can set higher depending on how fast your PC is.
# would not recommend going above 6
tri( 0, 0, 0, 50, 5 )

# place a cube at the origin,
bpy.ops.mesh.primitive_cube_add( location=( 0, 0, 0 ), size=0.75 )