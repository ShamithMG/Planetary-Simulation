import CONSTANTS
import rendering_orbit as RD
import planetary_data as planet
import body_physics as BP

import matplotlib.pyplot as plt

#------------------ DEFINE CUSTOM BODY 
test_body = BP.Body("test", [0 , -1.44e+12] , [ 9.67e+3, 0] , planet.m_sat)

# or edit premade body 
planet.Saturn.mass *= 50


def main():

    planets = [ planet.Star, planet.Saturn, test_body]
    RD.DrawOrbit( planets, CONSTANTS.dt, 180*CONSTANTS.YEAR)

    anima = RD.create_animation(planets, CONSTANTS.dt, fps = 120, speedup=(18*CONSTANTS.YEAR))

    plt.show()
    #HTML(anima.to_jshtml()) # --> if using jupyter notebook.


main()