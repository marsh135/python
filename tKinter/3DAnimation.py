# Copyright (c) 2019 Christian Calderon
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter
from random import random, randint
from math import atan2, sin, cos, pi, sqrt


def direction(v):
    """Computes the unit vector that points in the same direction as v."""
    a, b, c = v
    s = sqrt(a*a + b*b + c*c)
    return [a/s, b/s, c/s]


def rot_z(vs, theta):
    """Rotates a list of vectors around the z axis by radians theta."""
    s = sin(theta)
    c = cos(theta)

    for v in vs:
        x, y, z = v
        v[0] = x*c - y*s
        v[1] = x*s + y*c


def rot_y(vs, theta):
    """Rotates a list of vectors around the y axis by radians theta."""
    s = sin(theta)
    c = cos(theta)

    for v in vs:
        x, y, z = v
        v[0] = x*c - s*z
        v[2] = x*s + z*c


def sub(vs, u):
    """Subtracts u from every vector in the list vs."""
    a, b, c = u

    for v in vs:
        v[0] -= a
        v[1] -= b
        v[2] -= c


def add(vs, u):
    """Adds u to every vector in the list vs."""
    a, b, c = u

    for v in vs:
        v[0] += a
        v[1] += b
        v[2] += c


def rotate_axis(vs, theta, d_axis, p_axis):
    """Rotates a list of vectors around an arbitrary axis.

    vs is the list of vectors, theta is the radians of the rotation,
    d_axis is the direction of the axis, and p_axis is a point on the axis.
    """
    a, b, c = d_axis
    z_theta = -atan2(b, a)
    y_theta = -atan2(a*cos(z_theta) - b*sin(z_theta), c)

    sub(vs, p_axis)
    rot_z(vs, z_theta)
    rot_y(vs, y_theta)
    
    rot_z(vs, theta)
    
    rot_y(vs, -y_theta)
    rot_z(vs, -z_theta)
    add(vs, p_axis)


def random_sphere_points(radius, center, count):
    """Creates a list of points randomly distributed on a sphere.
    
    The sphere has the given radius and center.
    """
    a, b, c = center
    
    result = []
    for i in range(count):
        u = random()*2 - 1
        theta = random()*2*pi
        term = sqrt(1 - u*u)
        x = cos(theta)*term
        y = sin(theta)*term
        z = u
        result.append([radius*x + a, radius*y + b, radius*z + c])
    return result


def demo(
        WIDTH = 1000,      # pixel width of the canvas
        HEIGHT = 1000,     # pixel height
        RADIUS = 150,      # pixel radius of the sphere
        SPR = 4,           # seconds per revolution about the axis
        FPS = 60,          # target framerate
        POINT_COUNT = 1000 # number of random surface points
):
    """A demo of 3d animation using a Tkinter Canvas."""
    TITLE = 'Demo: Random Points on a Rotating Sphere'
    HW = WIDTH//2
    HH = HEIGHT//2
    TICK = 1000//FPS
    ANGLE_STEP = 2*pi/SPR/FPS

    master = tkinter.Tk()
    center_width = master.winfo_screenwidth()//2
    center_height = master.winfo_screenheight()//2
    master.geometry(
        '{}x{}+{}+{}'.format(
            WIDTH,
            HEIGHT,
            center_width - HW,
            center_height - HH
        )
    )
    master.title("Demo: Random Points on a Rotating Sphere")
    
    canvas = tkinter.Canvas(
        master,
        width=WIDTH,
        height=HEIGHT,
        background='black',
        highlightthickness='0'
    )
    canvas.pack()

    center = [randint(-HH + RADIUS, HH - RADIUS),
              randint(-HW + RADIUS, HW - RADIUS),
              randint(-HH + RADIUS, HH - RADIUS)]
    points = random_sphere_points(RADIUS, center, POINT_COUNT)
    d = direction([0.0, random(), random()])
    p = [0.0, 0.0, 0.0]

    def update():
        canvas.delete('all')
        rotate_axis(points, ANGLE_STEP, d, p)

        for p_i in points:
            x, y, z = p_i
            canvas.create_oval(HW + y - 2, HH - z - 2,
                               HW + y + 2, HH - z + 2,
                               fill='white')
        master.after(TICK, update)

    master.after(0, update)
    master.mainloop()


if __name__ == '__main__':
    demo()
