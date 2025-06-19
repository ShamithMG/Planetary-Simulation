import CONSTANTS
import numpy as np

#=================================================================
#Increase memory limit to store all plots for the animation
#PLEASE DECREASE IF LAGGING

from matplotlib import rcParams
rcParams['animation.embed_limit'] = 500 #in mb 
#=================================================================

YEAR    = 3.154e7    # one year in seconds

#create class for all gravitationally interacting objects
class Body:
    """
    Body class:
    Attributes: 
     - name                 :  name (string)
     - current position     :  position (array) [m]
     - current velocity     :  velocity (arraya) [m]
     - mass                 :  mass (float) [kg]
     - previous positions x : x positions in orbit (list)[m]
     - previous positions y : y positions in orbit (list)[m]

     Methods:
      - Calculate Gravitational Attraction to another body
      - Update position
      - Update velocity 
      - Update Trajectory
    """

    G = 6.6743e-11 # gravitational constant [m^3 kg^-1 s^-2]

    def __init__(self,name, position, velocity, mass):
        self.name = name                            
        self.pos = np.array(position,dtype = float) 
        self.vel = np.array(velocity,dtype = float) 
        self.mass = mass                            
        self.orbitx = []                            
        self.orbity = []                           

        
    def Gravititational_Attraction(self, other):
        """
        Calculate the gravitational force between self and another body
        Arguments:
         - other : Another body object
        
        """
        #Use the force function defined in part a to calculate the individual forces
        
        #calculate vector from other object to self
        r_vec = self.pos - other.pos
        r_mag = np.sqrt(r_vec[0]**2 + r_vec[1]**2)

        if r_mag <= 1e+3:
            return np.array(0,0)    #return no force if object gets too close

        r_hat = r_vec/r_mag

        #calculate Force
        Force = -((CONSTANTS.G*self.mass*other.mass)/(r_mag**2))*(r_hat)
        
        return Force


    def update_position(self, dt):
        """
        Updates position of body given its current velocity and step in time
        Arguments:
         - dt : time step
        """
        self.pos += self.vel * dt


    def update_velocity(self, force, dt):
        """
        Updates velocity of body given the resultant force on the body and step in time
        Arguments:
         - dt    : time step
         - force : resultant force on body
        """
        acceleration = force/self.mass
        self.vel += acceleration * dt


    def update_trajectory(self, Bodies, dt):
        """
        Updates the trajectory/position of the orbit
        Arguments:
         - Bodies  : list of all body objects included in animation
         - dt      : time step 
        """
        Force = 0 
        for body in Bodies:
            if self == body:              #Dont calculate force against the same body
                continue
        
            force = self.Gravititational_Attraction(body)
            Force += force
        
            if force[0]+force[1] == (0):    #If force is 0 change velocity to 0
                self.velocity = (0,0)
                Force = 0
                
        #update positions, velocity and add the position to orbit lists
        self.update_position(dt)
        self.update_velocity(Force,dt)
        self.orbitx.append(self.pos[0])
        self.orbity.append(self.pos[1])


    def Get_Max(self):
        """
        Return the max positions in x and y 
        """
        max_x = max(np.abs(self.orbitx))
        max_y = max(np.abs(self.orbity))
        return max_x ,max_y

#Create children classes for Stars and Moons
class Star(Body):
    def __init__(self, name, position, velocity, mass):
        super().__init__(name, position, velocity, mass)

class Moon(Body):
    def __init__(self, name, position, velocity, mass, parent_planet = None):
        super().__init__(name, position, velocity, mass)
        self.parent_planet = parent_planet              #Body the moon orbits 

    def orbit_status(self):
        if self.parent_planet:
            return (f"{self.name} orbits around {self.parent_planet.name}.")
        return (f"{self.name} is not orbiting any planet.")
        

