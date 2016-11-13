# The eighth assignment of computational physics: Rouths to chaos and period doubling 

### Name :郭明达
### Number：2014301020111
### Date：13.Nov.2016

## 1.Abstract
We have seen that at low driving forces the damped, nonlinear pendulum exhibits simple oscillatory motion, while at high drive it can be 
chaotic. However, when we consider this question again, the question must come out, that is, exactly how does the transition from simple
to chaotic behavior take place? This is the main problem that we will deal with in the following content. Of course, we also will disscuss 
when the driving force is larger than 1.2, what will happen then?

### Problem 3.18
Calculate Poincare section for the pendulum as it undergoes the period-doubling route to chaos. Plot
<img src="http://latex.codecogs.com/gif.latex?\omega" alt="" title="" /> versus 
<img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />, with one point
plotted for each drive cycle, as in Figure 3.9. Do this for F_D =1.4, 1.44, 1.465, using the other parameters as given in connection with
Figure 3.10. You should find that after removing the points corresponding to the initial transient the attractor in the period-1 regime 
will contain only a single point. Likewise, if the behavior is period n, the attractor will contain n discrete points.

### Problem 3.20
Calculate the bifurcation diagrams for the pendulum in the vicinity of F_D=1.35 to 1.5. Make a magnified plot of the diagram (as compared
to Figure 3.11) and obtain an estimate of the Feigenbaum <img src="http://latex.codecogs.com/gif.latex?\delta" alt="" title="" /> parameter.

## 2.Background

Qualitative and Stability Theory
By work of Liouville, it is well known that most differential equations could not be solved with elementary integal. Then the question of interest becomes whether we can judge the properties of the solution by the equations themselves. The French mathematicist Poincare came up with the qualitative theory and the Russian mathematicist Liapunov established the stability theory separately and contemporarily. ![1](http://latex.codecogs.com/gif.latex?dr\divdt=f(r,t))
The stability of the solution to an equation is defined as:![2](http://latex.codecogs.com/gif.latex?||r_{}{0}-r_{}{1}||<\delta)
for equations and  satisfies the Lipschitz condition, for the initial condition  the solution , for any given , there exist , such that 
Figuratively speaking, the stability means when the initial conditions deviate a little amount, the amount of the variance of the solution is also small.
Liapunov also gived methods to determine whether an equation is stable. The commonly-discussed Liapunov's second method uses a so-called Liapunov funciton , judging the stability by the sign of the derivative .
Phase Plain, Phase Diagram, and Phase Trajectory
Simultaneous differential equations are called a plain autonumous system 
such that the funcitons  satisfy the condition for the unique existence theorem.[2] In our problem the function becomes  and . They are assumed independent also physically  is the time derivative of .
We define the xOy plain (the  plain in our problem) as the phase plain. And the solution to the differential equations  (in our problem  and ) in the plain are called the phase trajectories. The trajectory clusters are called the phase diagram.
Poincare section and Bifurcation Diagram
Once we get the phase trajectories, some interesting and exciting tricks could be used to find more on the properties of chaos.
If we only show the points at the same phase of the driving force, the result is called the Poincare section. Obviously if there is no chaos the Poincare section would be a single point in the phase space. 
However, for chaotic system the Poincare section would show a fractal behavior.
To determine the critical point where the chaotic behavior appears and changes, we observe the angular displacement on the same value of the driving force, which is called bifuraction diagram.

