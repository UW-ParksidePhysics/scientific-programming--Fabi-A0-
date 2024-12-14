from math import pi
m = 0.43 #mass of ball in kg
v_1 = 33.3 #velocity in m/s
v_2 = 2.8 #velocity in m/s
rho = 1.2 #air density in kg/m^3
C = 0.2 #coef of drag
g = 9.8 #acceleration due to gravity in m/s^2
a = 0.11 #radius in m
A = pi * a ** 2 #cross sectional area in m^2
drag_force1 = 0.5*C*rho*A*v_1
drag_force2 = 0.5*C*rho*A*v_2
gravity_force = m*g #force of gravity
ratio_1 = drag_force1/gravity_force
ratio_2 = drag_force2/gravity_force
print("force of drag for hard kick=", drag_force1, "N")
print("force of drag for soft kick=", drag_force2, "N")
print("force of gravity=", gravity_force, "N")
print("hard kick drag over gravity=", ratio_1)
print("soft kick drag over gravity=", ratio_2)
