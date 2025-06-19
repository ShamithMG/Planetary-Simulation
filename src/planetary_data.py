import body_physics as BP

#Positions of each body:
p_merc = [0, 69.6e+9]
p_ven = [-107.8e+9, 0]
pos1 = [1.597e+11,0]
p_mars = [0,-245e+9]
pos3 = [-777e+9, 0]
p_sat = [0 , 1.44e+12]
p_ura = [2.9e+12, 0]
p_nep = [0, -4.5e+12]

pos_star = [0,0]


#velocity of each body:
v_merc = [ -47.4e+3, 0]
v_ven = [0,-35e+3]
vel1 = [0,2.89e+4]
v_mars = [24e+3, 0]
vel3 = [0, -13.1e+3]
v_sat = [- 9.67e+3, 0]
v_ura = [0, 6.81e+3]
v_nep = [5.45e+3, 0]

vel_star = [0,0]


#Masses of each body:
m_merc = 0.33e+24
m_ven = 4.9e+24
mass1 = 6e+24
m_mars = 6.4e+23
mass3 = 1.9e+27
m_sat = 568e+24
m_ura = 8.9e+25
m_nep = 1e+26

Mass_Star = 2e+30

#Create objects for each body:
Mercury = BP.Body("Mercury",p_merc,v_merc,m_merc)
Venus = BP.Body("Venus", p_ven, v_ven, m_ven)
Earth = BP.Body("Earth",pos1, vel1, mass1)
Mars = BP.Body("Mars",p_mars,v_mars,m_mars)
Jupiter = BP.Body("Jupiter", pos3, vel3, mass3)
Saturn = BP.Body("Saturn", p_sat, v_sat, m_sat)
Uranus = BP.Body("Uranus", p_ura, v_ura, m_ura)
Neptune = BP.Body("Neptune", p_nep, v_nep, m_nep)

Star    = BP.Body("Sun",pos_star, vel_star, Mass_Star)