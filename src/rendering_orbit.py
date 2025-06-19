import matplotlib.pyplot as plt
from matplotlib import animation



def DrawOrbit(Bodies,dt,t_max):
    """
    Calculate Orbit, using Euler's method.
    
    Arguments:
      - Bodies: list of all the body objects wanted in the animation
      - dt     : time step 
      - t_max  : total time for animation
    """

    t = 0. 

    #keep adding points to the trajectory until Stopping Condition met
    while t < t_max:
      for body in Bodies:

        #Iterate through every body in the list and update its position and velocity
        #for current time
        body.update_trajectory(Bodies, dt)

      t += dt


def animate_with_trail(i, Bodies, Line2D, Line2DTrail):
    """
    Update display for bodies, with trail.
    
    Arguments:
        i            :  frame number (from 0 at time = 0)
        Bodies       :  List of all Body objects in animation
        Line2D       :  List of Line2D objects used to plot bodies
        Line2DTrail  :  List of Line2D objects used to plot body trails

    Result: updates coordinates in Line2D objects provided as arguments
    "bodies" and "trails".
    """

    j = 0
    for body in Bodies:

        x, y = body.orbitx[i], body.orbity[i]
        
        Line2D[j][0].set_data([x],[y])                                  # Body gets coordinates of current position
        Line2DTrail[j][0].set_data(body.orbitx[:i+1],body.orbity[:i+1]) # Trail has all points up to the current one

        j += 1


def create_animation(Bodies, dt, fps, speedup):
    """
    Create an animation of an object with given bodies.
    
    Arguments:
        Bodies  : list of body objects in animation
        dt      : time step in simulation [s]
        fps     : number of frames per second for animation
        speedup : ratio of simulated time to screen time
    """
    # Find range of coordinates to include full trajectory
    x_max = 0
    y_max = 0
    for body in Bodies:
        x, y = body.Get_Max()
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y

    r_max = 1.05 * max(x_max, y_max)
    
    # Create and configure figure and axes
    plt.ioff()
    fig, axes = plt.subplots()
    axes.set_xlim(-r_max,r_max)
    axes.set_ylim(-r_max,r_max)
    axes.set_aspect('equal')
    axes.set_title('Trajectory of planet')
    axes.set_xlabel('x [m]')
    axes.set_ylabel('y [m]')

    # Create list of Line2D objects to represent bodies and trails
    Line2D = []
    Line2DTrail = []
    for i in range(len(Bodies)):

        L2D =axes.plot([],[],'o')
        Line2D.append(L2D)
        Line2DTrail.append(axes.plot([],[],'-', color = L2D[0].get_color()))

    # Get arrays of coordinates to display (subset of provided data)
    frame_interval = 1/fps                  # time between frames [s]
    skip = round(frame_interval*speedup/dt) # number of calculated points per frame
    if skip==0:
        raise Exception("Speedup factor too low.")
    
    for body in Bodies:
        body.orbitx = body.orbitx[::skip]  # take every Nth value (N = skip)
        body.orbity = body.orbity[::skip]

    n_frames = len(Bodies[0].orbitx)       #every orbit list are the same length

    # Create and return animation object
    ani = animation.FuncAnimation(fig,animate_with_trail, frames=n_frames, interval=frame_interval*1000,
                                  fargs=[Bodies, Line2D, Line2DTrail])
    return ani