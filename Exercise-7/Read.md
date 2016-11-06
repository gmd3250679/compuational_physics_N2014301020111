# The seventh assignment of computational physics :Oscillatory Motion and Chaos

### Name :郭明达
### Number：2014301020111
### Date：30.Oct.2016

## 1.Abstract

Oscillatory phenomena can be found in many areas of physics, including the motion of electrons in atoms, the behavior of currents and 
voltages in electronic circuits, and planetary orbits. But the simplist one may be the motion of pendulums. Through analying this simple 
example, we will have a better understanding of oscillatory motion and chaos. Chaos theory is the field of study in mathematics that 
studies the behavior of dynamical systems that are highly sensitive to initial conditions. Small differences in initial conditions 
yield widely diverging outcomes for such dynamical sysytems, rendering long-term prediction impossible in general. In this homework, 
I will mainly talk about effects of initial conditions to chaos and some points about strange attractors.
![double pendulum](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/Double-compound-pendulum.gif)

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
and when tilt angle is very small, the motion function of the pendulum can be written as 
![1](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/Ex7-01.png)
Obviously, the pendulum will do a periodic motion.
If we add damping to our pendulum, the motion function will become
![2](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/Ex7-02.png)
And it will give us some interesting results. But, we can easily tell that our pendulum will stop eventually.
However, everything will totally different when there is a driving force that put on the pendulum. Maybe you will get this equation
![3](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/Ex7-03.png)
But it is not right, because, in some cases, the tilt angle will be large, so we'd better write it as
![4](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/Ex7-04.png)
Use the Euler-Cromer method, we can get the equation that is helpful for us to write program. By the way, in this homework, all programs are based on the Euler-Cromer method.

## 3.Body context

###-Pro.3.12
We have talked what is chaos and we have already known that the trajectory of chaos is hard to predict. But it is not all right. In fact, if we plot <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" /> as a function of t, and plot tthe angular velocity <img src="http://latex.codecogs.com/gif.latex?\omega" alt="" title="" /> as a function of <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />(Plot in phase space.). Strange things will appear.
![1](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/7%20figure%209.png)
Just look at this picture, first, the trajectory is not perfect, but, eventually, we will can two ellipses. And our results exactly accord with the reality that every angle is corresponding to two angular velocity. This is because that the pendulum will be stable eventually.
![2](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/7%20figure%2010.png)
Well, first, it's beautiful! Maybe it is complicated, but if we take a second look, not only it is fantastic, but also are there some regularity.
###-Pro.3.13
As what I said, in abstact, that the system, in chaos, is quite sensitive to initial conditions. There I give an another figure for comparison. As for the program, you can set a log function or adjust your coordinate axis after plotting. Here I choose the latter.
<img src="http://latex.codecogs.com/gif.latex?q=0.l=g=9.8\Omega_{D}=2/3dt=0.04\theta_{}{1}=0.1,\theta_{}{2}=1.001\omega(0)=0F_{}{D}=0.5" alt="" title="" />
The initial values of \theta for two pendulums differed by 0.001 rad.
![figure 1](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/E7figure01.png)
<img src="http://latex.codecogs.com/gif.latex?q=0.5l=g=9.8\Omega_{D}=2/3dt=0.04\theta_{}{1}=0.1,\theta_{}{2}=1.001\omega(0)=0F_{}{D}=1.5" alt="" title="" />
![figure 2](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/E7%20figure_2.png)
####The first picture shows that, in non-chaotic field, the effects of initial condition is really small, with the time goes on, the difference of these two pendulums will become smaller.
####The second picture implys that there exsit a lot of distinctions between these two pendulum, especially when time is large. The values of \theta for the two pendulums differed by some values that is smaller than 2\pi.
####In fact, if we obseve these pictures carefully, it is not hard to draw a conclusion that log(\Delta \theta) will decrease or increase with time in some laws.
####As given by textbook, there exists the parameter that is known as a Lyapunov exponent.
These two figure 's corresponding Lyapunov is about -0.30 and 024.

###Pro.3.14 Changing the damping factor
We have already told about the effects of a initial condition, but now if we add another initial condition to it, will the value of the Lyapunov exponent change?
Just like question 3.13, what we should do is to change the damping factors. The following figures,
<img src="http://latex.codecogs.com/gif.latex?q_{}{1}=0.6q_{}{2}=0.601g=9.8\Omega_{D}=2/3dt=0.04\theta_{}{1}=0.1,\theta_{}{2}=1.00\omega(0)=0F_{}{D}=0.5" alt="" title="" />
![figure 3](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/E7figure03.png)
<img src="http://latex.codecogs.com/gif.latex?q_{}{1}=0.6q_{}{2}=0.601g=9.8\Omega_{D}=2/3dt=0.04\theta_{}{1}=0.1,\theta_{}{2}=1.00\omega(0)=0F_{}{D}=1.2" alt="" title="" />
![figure 4](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-7/E7figure04.png)
####Obviouly, when F_D=0.5, if we change q, we will find the Lyapunov exponent will be zero.
####However, when F_D=1.2, that is, the system is in the chaostic regime, if we change q, just shown in figure, the Lyapunov exponent will be larger, it's about 0.23, this is because that thier initial conditions is much more different, and the system is easier to be chaostic.

##4.Conculsion
####In non-chaotic regime, the effects of initial condition is really small, with the time goes on, the difference of these two pendulums will become smaller.
####There exsit a lot of distinctions between these two pendulum, especially when time is large. The values of<img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />  for the two pendulums differed by some values that is smaller than <img src="http://latex.codecogs.com/gif.latex?2\div\pi" alt="" title="" />.
####Obviouly, when <img src="http://latex.codecogs.com/gif.latex?F_{}{D}=0.5" alt="" title="" /> , if we change q, we will find the Lyapunov exponent will be zero.
####However, when<img src="http://latex.codecogs.com/gif.latex?F_{}{D}=1.2" alt="" title="" /> , that is, the system is in the chaostic regime, if we change q, just shown in figure, the Lyapunov exponent will be larger, it's about 0.1, this is because that thier initial conditions is much more different, and the system is easier to be chaostic.
####When we choose the points when <img src="http://latex.codecogs.com/gif.latex?\omega_{}{Dt}=2n\div\pi" alt="" title="" />  , we are surprised that this points consistitute a fractal strcture. And this surface of points is known as a strange attractor. We can draw the same conclusion in other phase too.

##5. Acknowledge
###Shan Tan [](http://www.jianshu.com/p/e5960d756664)
###Kang yu [](http://www.jianshu.com/p/045c5b8c91fb)
###Professor.Cai 




