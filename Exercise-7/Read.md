# The seventh assignment of computational physics :Oscillatory Motion and Chaos

Name :郭明达
Number

## 1.Abstract

Oscillatory phenomena can be found in many areas of physics, including the motion of electrons in atoms, the behavior of currents and 
voltages in electronic circuits, and planetary orbits. But the simplist one may be the motion of pendulums. Through analying this simple 
example, we will have a better understanding of oscillatory motion and chaos. Chaos theory is the field of study in mathematics that 
studies the behavior of dynamical systems that are highly sensitive to initial conditions. Small differences in initial conditions 
yield widely diverging outcomes for such dynamical sysytems, rendering long-term prediction impossible in general. In this homework, 
I will mainly talk about effects of initial conditions to chaos and some points about strange attractors.
![double pendulum]()

## 2.Background

###Pro.3.12
In constructing the Poincare section in Figure 3.9 we plotted points only at times that were in phaes with the drive force; that is at time
<img src="http://latex.codecogs.com/gif.latex?t$\approx$2n\pi\div\Omega_{D}" alt="" title="" />,where n is an integer. At these value of t the driving force passes through zero. However, we could just as easily have chosen to make the plot at times corresponding to a maximum of the drive force, or at times 
<img src="http://latex.codecogs.com/gif.latex?\pi\div4" alt="" title="" /> out-of-phase with the force, etc. Construct the Poincare sections for these cases and compare them with Figure 3.9

###Pro.3.13
Write a program to calculate and compare the behavior of two, nearly identical pendulums. Use it to calculate the divergence of two nearby trajectories in the chaotic regime, as in Figure 3.7, and make a qualitative estimate of the corresponding Lyapunov exponent form the slope of a plot of <img src="http://latex.codecogs.com/gif.latex?log(\Delta\theta)" alt="" title="" /> as a function of t

###Pro.3.14
Repeat the previous problem, but give the two pendulums slightly different damping factors. How does the value of the Lyapunov exponent compare with that found in Figure 3.7

###Introduce
Before our this class, we have already learned some basic knowledge about the single pendulum, without damping and driving force, 
and when tilt angle is very small, the motion function of the pendulum can be written as <img src="http://latex.codecogs.com/gif.latex?" alt="" title="" />

