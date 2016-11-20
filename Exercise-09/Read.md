# The ninth assignment of computational physics: the Lorentz Model and the Billiard Problem 

### Name :郭明达
### Number：2014301020111
### Date：20.Nov.2016

## 1.Abstract

There are a massive examples about chaos, good understanding of them is very useful for us to predict some normal but interesting in our
daily life.

### Problem 3.30
Investigate the Lyapunov exponent of the stadium billiard for several values of 
<img src="http://latex.codecogs.com/gif.latex?\alpha" alt="" title="" />. 
You can do this qualitatively by examining the 
behavior for only one set of initial conditions for each value of 
<img src="http://latex.codecogs.com/gif.latex?\alpha" alt="" title="" /> you consider, or more quantitatively by averaging over a range of
initial conditions for each value of <img src="http://latex.codecogs.com/gif.latex?\alpha" alt="" title="" />

### Problem 3.31
Study the behavior for other types of tables. One interesting possibility is a square table with a circular interior wall located either
in the center, or slightly off-center. Another possibility is an elliptical table.

## 2.Background and introduction

We have already considered the model of the pendulum. Maybe it is quite easy, yet they exhibit extremely rich behavior. It is thus not surprising that other sightly more complicated systems are also capable of chaotic behavior. When we think of chaotic or unpredictable behavior, an example that naturally comes to mind is the weather. While much of this effort has gone into computer modeling of Earth's atmosphere, much has also been devoted to understanding the weather problem from a more fundamental points of view.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%202.jpg)
To get an appreciation for the different kinds of behavior that can be found, and also the common threads that run through this behavior, we will consider one more chaotic model in this homework. Here we consider the problem of a ball moving without friction on a horizontal table. We imagine that there are walls at the edges of table that reflect the ball perfectly and that there is no frictional force between the ball and the table.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%201.jpg)
We consider the Lorenz model, the Lorenz equations can be written as:
![1](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2001.png)
The main question we will talk about is the billiard problem. Except for the collisions with the walls, the motion of the billiard is quite simple. Between collisions the velocity is constant so we have:
![2](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2002.png)
These equations can be solved using our usual Euler algorithm. The Euler solution gives an exact description of the motion across the table. The most difficult part of the calculation is the treatment of the collisions. We can obtain the following equations:
![3](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2003.png)
Hence, the velocity after reflection from the wall is :
![4](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2004.png)
These equations are the basis of my work in this homework.

## 3.Body context

### (1) Lorenz model
When we plot it with z and t, we cannot find any regularity. Hence, we'd better plot it in phase-space. Here, <img src="http://latex.codecogs.com/gif.latex?\sigma=10" alt="" title="" />, b=8/3, r=25, the step of time is 0.0001.
![5](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2005.png)
Conclusion: When we plot it in phase space, The figure 1. gives some hints of an underlying regularity.
Though we can predict something from the phase-space plot, we would like to have more than hints. Hence, while the time-dependent behavior is unpredictable, we can predict with certainty that the system will be found somewhere on the attractor surface in phase space.
![6](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2006.png)
Conclusion: We see from the figure that even though the behavior is strongly chaotic, there is a very high degree of regularity in the phase-space trajectory.

### (2) Pro.3.20
First, we consider a quite simple model-the motion of a billiard on a square table. The billiard started at point (0.2, 0).
![7](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2007.png)
Conclusion: From figure 3., we can predict this kind of motion easily.
But, when we consider another table, what will change? For example, If the table is circular table, the result will be beautiful and amazing!
![8](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2008.png)
Conclusion: The trajectories are always highly symmetric
By the way, I give its phase-space plot below.
![9](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2009.png)
Conclusion: This motion is quite regular.
However, if we cut the table along the x axis, and pull the two semicircular halves apart (along y), a distance <img src="http://latex.codecogs.com/gif.latex?2\alpha" alt="" title="" /> r, the trajectory will be definitely not symmetric.
![10](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2010.png)
Conclusion: In fact, this figure reminds us of chaotic motion.
Phase-space plots for the trajectories of <img src="http://latex.codecogs.com/gif.latex?\alpha=0,0.001,0.01,0.1" alt="" title="" /> shown in figure 7.
![11](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2011.png)
Conclusion: When <img src="http://latex.codecogs.com/gif.latex?2\alpha=0" alt="" title="" />, it is a nonchaotic system. However, for the <img src="http://latex.codecogs.com/gif.latex?2\alpha" alt="" title="" /> is not equal to 0, it is indeed chaotic.
Now, we have enough knowdgeable to finish the first question-3.30. Here, the initial separation of the billiards was 0.00001.
![12](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2012.png)
![13](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2013.png)
#### 1*As you see in figure 8. and figure 9., when <img src="http://latex.codecogs.com/gif.latex?2\alpha" alt="" title="" /> is larger, the Lyapunov exponent is larger.
#### 2*When <img src="http://latex.codecogs.com/gif.latex?2\alpha=0" alt="" title="" />, we will find that the Lyapunov exponent is zero. When <img src="http://latex.codecogs.com/gif.latex?2\alpha=0.001" alt="" title="" />, the Lyapunov exponent is much small. However, when <img src="http://latex.codecogs.com/gif.latex?2\alpha" alt="" title="" /> become larger, <img src="http://latex.codecogs.com/gif.latex?2\alpha=0.01" alt="" title="" />, the Lyapunov exponent is equal to 0.05, <img src="http://latex.codecogs.com/gif.latex?2\alpha=0.1" alt="" title="" />, the Lyapunov exponent is 0.17.
#### 3*The result told us, when \alpha is larger, the system is more chaotic.

### Pro.3.31
Of course, we can also obtain the trajectory of billiard in elliptical table. I give two figure here, one is situation when the billiard sets out from a focal point, the other is situation when the billiard sets out from the origin.
![14](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2014.png)
![15](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2015.png)
![16](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/E9%2016.png)
Conclusion: For an ellipse, its tracjectory is related to its starting point. For above two situations, we obtain two totally different results. And there is not point of intersection in their phase-space diagram.
Another possibility is given by Vpython, this possibility is a square table with a circular interior wall located in the center.
![17](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-09/Figure/GIF.gif)
Conclusion: In this situation, the trajectory is more complicated, the system is chaotic.

## 4.Acknowledge
### [Prof Cai](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357)
### [Tan Shan](http://www.jianshu.com/p/cdb6d12bc02d)
### [Shen Yang](https://www.zybuluo.com/whu-sy/note/572123)
