# The eighth assignment of computational physics: Rouths to chaos and period doubling 

### Name :郭明达
### Number：2014301020111
### Date：13.Nov.2016

## 1.Abstract
We have seen that at low driving forces the damped, nonlinear pendulum exhibits simple oscillatory motion, while at high drive it can be 
chaotic. However, when we consider this question again, the question must come out, that is, exactly how does the transition from simple
to chaotic behavior take place? This is the main problem that we will deal with in the following content. Of course, we also will disscuss 
when the driving force is larger than 1.2, what will happen then?
[![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-8/figure/pendulum.gif)]
(https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-8/pendulum.py)

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

### Qualitative and Stability Theory
By work of Liouville, it is well known that most differential equations could not be solved with elementary integal. Then the question of interest becomes whether we can judge the properties of the solution by the equations themselves. The French mathematicist Poincare came up with the qualitative theory and the Russian mathematicist Liapunov established the stability theory separately and contemporarily. ![1](http://latex.codecogs.com/gif.latex?dr\divdt=f(r,t))
The stability of the solution to an equation is defined as:![2](http://latex.codecogs.com/gif.latex?||r_{}{0}-r_{}{1}||<theta)
for equations and  satisfies the Lipschitz condition, for the initial condition  the solution , for any given , there exist , such that 
Figuratively speaking, the stability means when the initial conditions deviate a little amount, the amount of the variance of the solution is also small.
Liapunov also gived methods to determine whether an equation is stable. The commonly-discussed Liapunov's second method uses a so-called Liapunov funciton , judging the stability by the sign of the derivative .

### Poincare section and Bifurcation Diagram
Once we get the phase trajectories, some interesting and exciting tricks could be used to find more on the properties of chaos.
If we only show the points at the same phase of the driving force, the result is called the Poincare section. Obviously if there is no chaos the Poincare section would be a single point in the phase space. 
However, for chaotic system the Poincare section would show a fractal behavior.
To determine the critical point where the chaotic behavior appears and changes, we observe the angular displacement on the same value of the driving force, which is called bifuraction diagram.

## 3.Result
### 1. Period Doubling with different values of the drive amplitude.
In the last time, we just gave the results when F_D is smaller than 1.2, now, I'll give results for <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" /> as a fuction of time for our pendulum for several different values of the drive amplitude.
![1](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-8/figure/3413510-1de042eee34adb53.png)
Surprisingly, when F_D=1.2, the system is in chaotic state. When F_D=1.35, the system become well-aligned again, its period is the same as the drive period. When F_D=1.44, its period is the twice as the drive period. When F_D=1.465, its period is the fourth times as the drive period.
Conclusion: If we were to increase the driven amplitude further, the period would double again as the pendulum would switch to a motion that has a period eight times that of the drive. The period-doubling cascade would continue if the drive were increased further.

### 2.Bifurcation diagram
Bifurcation diagram is a quite good method to tell us the transition to chaos. I spend a flood of time on operating the program, it need a long time to calculate. If you find that it seems that my code can't work, don't worried or surprised about, just wait for the results. It is about several minutes to several hours. Of course, it depend on your accuracy.
![2](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-8/figure/9_5.png)
Figure 9.5 Bifurcation Diagram with <img src="http://latex.codecogs.com/gif.latex?\omega_{}{D}=2/3,q=1/2" alt="" title="" />
And we tried several different choices of the frequency of the driving force (in Figure 9.5) and the friction coefficient (in Figure 9.6)
![3](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-8/figure/9_6.png)
Figure 9.5 Bifurcation diagram with
<img src="http://latex.codecogs.com/gif.latex?\omega_{1}{D}=1/2,\omega_{2}{D}=2/3,\omega_{3}{D}=1,\omega_{4}{D}=4/3" alt="" title="" />
![4](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-8/figure/9_7.png)
Figure 9.6 Bifurcation diagram with
<img src="http://latex.codecogs.com/gif.latex?\q=0.4_{1}{},q=0.6_{2}{},q=0.1_{3}{},q=1_{4}{}" alt="" title="" />
The x coordinate is driving force amplitude (unit:<img src="http://latex.codecogs.com/gif.latex?s_{-2}{}" alt="" title="" />), and the y coordinate is angular displacement (unit: radian)
We can see that chaos happen at a relatively large range of the choice of parameters. However, we can not find an analytical expression for the relationship between the number of points of <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />at a certain<img src="http://latex.codecogs.com/gif.latex?F_{}{D}" alt="" title="" />
This is an obvious drawback of numerical simulation discussed by Meerschaert.

## 4.Discussion
###Subtle time step length. 
In order to meet the requirement that we can observe the angular dislplacement in phase with the driving force we adjust the step length of the root-finding program to be an integal division of <img src="http://latex.codecogs.com/gif.latex?\pi" alt="" title="" />
### Reshape of the data with mode <img src="http://latex.codecogs.com/gif.latex?2\pi" alt="" title="" />
### Scatter Diagram

## 5.Reference
### Shan Tan[](http://www.jianshu.com/p/b141af43e303)
### Shixing Wang[](https://www.zybuluo.com/ShixingWang/note/355301)
### Prof.Cai[](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357) 


