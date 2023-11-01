import glfw
import OpenGL.GL
from OpenGL.GL import *
import time

from OpenGL.GL import glBegin, glEnd
from math import *

from OpenGL.raw.GL.VERSION.GL_1_0 import glVertex2f

WIDTH, HEIGHT = 1280, 720

# Define the window variable as a global variable

window = None
t = 0.0
angle = 0.0
speed = 0.15
radius = 0.20
radiusvolcano = 0.18
circle_pos_x = -0.5  # initial x position of the circle
circle_pos_y = 0.0  # initial y position of the circle
circle_radius = 0.1  # radius of the circle
num_segments = 30  # n
cloud_pos_x = -1.5  # initial x position of the cloud
cloud_speed = 0.001
ship_pos_x = -1.0
ship_move_increment = 0.0005


def display():

    global t
    global angle
    global circle_pos_y
    global circle_pos_x
    global cloud_pos_x
    global cloud_speed
    global ship_pos_x
    global window  # Use the global window variable
    glClear(GL_COLOR_BUFFER_BIT)

    # Sun with triangles as sun rays circling around
    glColor3f(0.99, 0.72, 0.07)
    glBegin(GL_TRIANGLES)
    for i in range(24):
        glVertex3f(radius * cos(radians((i * 15 + angle) % 360)) + 0.7,
                   radius * sin(radians((i * 15 + angle) % 360)) + 0.75, 0.0)
        glVertex3f(radius * cos(radians((i * 15 + angle + 120) % 360)) + 0.7,
                   radius * sin(radians((i * 15 + angle + 120) % 360)) + 0.75, 0.0)
        glVertex3f(radius * cos(radians((i * 15 + angle + 240) % 360)) + 0.7,
                   radius * sin(radians((i * 15 + angle + 240) % 360)) + 0.75, 0.0)

    glEnd()
    # update the angle for triangle animation
    angle += speed

    #############################################################
    # Clouds
    # We draw the first circle of the cloud by using a loop to
    # iterate over a set of angles and drawing a line between the points around the circle.
    glColor3f(1.0, 1.0, 1.0)  # white
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * pi * i / num_segments
        x = cloud_pos_x + 0.0 + circle_radius * cos(theta)
        y = 0.6 + circle_radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(0.9, 0.9, 0.9)  # light grey
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * pi * i / num_segments
        x = cloud_pos_x + 0.1 + circle_radius * cos(theta)
        y = 0.6 + circle_radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(0.8, 0.8, 0.8)  # darker grey
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * pi * i / num_segments
        x = cloud_pos_x - 0.03 + circle_radius * cos(theta)
        y = 0.56 + circle_radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)  # white
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * pi * i / num_segments
        x = cloud_pos_x + 0.3 + circle_radius * cos(theta)
        y = 0.2 + circle_radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(0.9, 0.9, 0.9)  # light grey
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * pi * i / num_segments
        x = cloud_pos_x + 0.4 + circle_radius * cos(theta)
        y = 0.2 + circle_radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

    glColor3f(0.8, 0.8, 0.8)  # darker grey
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments):
        theta = 2.0 * pi * i / num_segments
        x = cloud_pos_x + 0.3 + circle_radius * cos(theta)
        y = 0.16 + circle_radius * sin(theta)
        glVertex2f(x, y)
    glEnd()

    cloud_pos_x += cloud_speed
    if cloud_pos_x > 1.5:
        cloud_pos_x = -1.5

    # set the new position of the circle
    circle_pos_x = cloud_pos_x + 0.2
    circle_pos_y = 0.2

    ##############################################


    # Fire from volcano
    glColor3f(0.50, 0.03, 0.03)
    glBegin(GL_TRIANGLES)
    for i in range(24):
        glVertex3f(radiusvolcano * cos(radians((i * 40 + angle) % 360)) - 0.78, radiusvolcano * sin(radians((i * 40 + angle) % 360)) -1,
                   0.0)
        glVertex3f(radiusvolcano * cos(radians((i * 40 + angle + 120) % 360)) - 0.78,
                   radiusvolcano * sin(radians((i * 40 + angle + 120) % 360)) -1, 1)
        glVertex3f(radiusvolcano * cos(radians((i * 40 + angle + 240) % 360)) - 0.78,
                   radiusvolcano * sin(radians((i * 40 + angle + 240) % 360)) + 0.1, 1)

    glEnd()

    # Volcano
    glPushMatrix()
    glTranslatef(-0.3, 0, 0.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.50, 0.50, 0.50)  # Gray
    glVertex2f(-0.86, -0.9)
    glVertex2f(-0.13, -0.9)
    glVertex2f(-0.48, -0.15)
    glEnd()
    glPopMatrix()

    # Small triangle to fill the "fire"
    glPushMatrix()
    glTranslatef(-0.637, -0.1, 0.0)
    glScalef(0.3, 0.3, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.50, 0.03, 0.03)  # Red color
    glVertex2f(-0.86, -0.9)
    glVertex2f(-0.13, -0.9)
    glVertex2f(-0.48, -0.15)
    glEnd()
    glPopMatrix()

    # Docking station for the ship
    glBegin(OpenGL.GL.GL_POLYGON)
    glColor3f(0.72, 0.54, 0.38)  # Wood color
    glVertex2f(1, -0.95)  # Top-left
    glVertex2f(0.7, -0.95)  # Top-right
    glVertex2f(0.7, -0.5)  # Bottom-right
    glVertex2f(1, -0.5)  # Bottom-left
    glEnd()

    # Small extension of a dock
    glBegin(OpenGL.GL.GL_POLYGON)
    glColor3f(0.72, 0.54, 0.38)  # Wood color
    glVertex2f(0.45, -0.5)  # Top-left
    glVertex2f(0.7, -0.5)  # Top-right
    glVertex2f(0.7, -0.55)  # Bottom-right
    glVertex2f(0.45, -0.55) # Bottom-left
    glEnd()

    # Dock barriers
    # In a loop to create 5 barriers next to each other with a 0.10 offset to the right
    for i in range(5):
        x_offset = 0.10 * i
        glPushMatrix()
        glTranslatef(1.4, 0.3, 0.0)
        glBegin(GL_POLYGON)
        glColor3f(0.50, 0.50, 0.50)  # Gray color
        glVertex2f(-0.92 + x_offset, -0.64)  # Top-left
        glVertex2f(-0.9 + x_offset, -0.64)  # Top-right
        glVertex2f(-0.9 + x_offset, -0.8)  # Bottom-right
        glVertex2f(-0.92 + x_offset, -0.8)  # Bottom-left
        glEnd()
        glPopMatrix()

    #SHIP
    glPushMatrix()
    glTranslatef(ship_pos_x, 0.0, 0.0)  # Add translation to ship position
    glRotatef(180, 0.0, 0.0, 1.0)
    glTranslatef(0.2, 1.05, 0.0)
    glScalef(0.5, 0.5, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.95, 0.60, 0.41)  # Fire Color
    glVertex2f(-0.86, -0.9)
    glVertex2f(-0.13, -0.9)
    glVertex2f(-0.48, -0.15)
    glEnd()
    glPopMatrix()

    #PILLAR
    glPushMatrix()
    glTranslatef(ship_pos_x + 0.95, 0.3, 0.0)  # Add ship position to pillar position
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)  # Gray color
    glVertex2f(-0.92, -0.60)  # Top-left
    glVertex2f(-0.9, -0.60)  # Top-right
    glVertex2f(-0.9, -0.9)  # Bottom-right
    glVertex2f(-0.92, -0.9)  # Bottom-left
    glEnd()
    glPopMatrix()

    #SAIL
    glPushMatrix()
    glTranslatef(ship_pos_x + 0.1, -0.4, 0.0)  # Add ship position to sail position
    glScalef(0.15, 0.15, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 1)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glEnd()
    glPopMatrix()

    # If ship reaches the end of the screen, reset its position to the left

    if ship_pos_x < 0.2:
        ship_pos_x += ship_move_increment
    else:
        ship_pos_x -= ship_move_increment






    # WAVES FIRST HALF

    # Included time variable T in calculation for the y value of each vertex.
    # This causes the water wave to oscillate up and down over time

    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.05, 0.36, 0.61)  # set the color to blue
    for i in range(201):
        x = i / -100.0
        y = -0.03 * (25 + 0.3 * sin(10 * x * 2 * pi + t))
        glVertex2f(x, y)
        glVertex2f(x, -10)
    glEnd()
    t += 0.01

    # WAVES SECOND HALF
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(0.05, 0.36, 0.61)  # set the color to blue
    for i in range(201):
        x = i / 100.0
        y = -0.03 * (25 + 0.3 * sin(10 * x * 2 * pi + t))
        glVertex2f(x, y)
        glVertex2f(x, -10)
    glEnd()
    t += 0.01

    # OCEAN
    glBegin(OpenGL.GL.GL_POLYGON)
    glColor3f(0.05, 0.36, 0.61)  # Orange color
    glVertex2f(-1, -0.8)  # Top-left
    glVertex2f(1, -0.8)  # Top-right
    glVertex2f(1, -1)  # Bottom-right
    glVertex2f(-1, -1)  # Bottom-left
    glEnd()

    # Swap buffers
    glfw.swap_buffers(window)


def main():
    global window  # Use the global window variable

    # Initialize GLFW
    if not glfw.init():
        return

    # Create a window and make the context current
    window = glfw.create_window(WIDTH, HEIGHT, "Volcano Wonderland", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)

    # Set the background color
    OpenGL.GL.glClearColor(0.67, 0.84, 0.90, 0.0)

    # Set the display function
    glfw.set_window_size_callback(window, display)

    # Run the event loop
    while not glfw.window_should_close(window):
        # Poll for events
        glfw.poll_events()

        # Render the scene


        display()

    # Terminate GLFW
    glfw.terminate()


if __name__ == '__main__':
    main()
