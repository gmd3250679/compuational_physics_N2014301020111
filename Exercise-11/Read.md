# The eleventh assignment of computational physics: The movement of Hyperion

### Name :郭明达
### Number：2014301020111
### Date：4.Dec.2016

## 1.Abstract

Three-body system is famous for its complexity and an analytical solution is known not to exist. This is where numerical solutions can show
its values in scientific significance. It is known that te motion of asteriods located near the Kirkwood gaps is believed to be chaotic.And
there is various chaotic motion of planet which will be a fairly difficult stimulation.However,there is one case of chaos in our solar system 
that is accessible to a fairly simple stimulation,that is the Hyperion.In this passage,we are going to investigate the properities of the 
movement of Hyperion.And the behavior of two slightly different intial conditions.

### Problem 4.19

Study the behavior of our model for Hyperion for differnt initial conditions. Estimate the Lyapunov expoenent from calculations of
<img src="http://latex.codecogs.com/gif.latex?\Delta\theta" alt="" title="" />, such as those shown in Figure 4.19. Exmaine how this expoent varies as a function of the ccentricity of the orbit.

### Problem 4.20

Our results for the divergence of the two trajectories <img src="http://latex.codecogs.com/gif.latex?\theta_{1}^{}" alt="" title="" /> and <img src="http://latex.codecogs.com/gif.latex?\theta_{2}^{}" alt="" title="" />  in the chaotic regime, shown on the right in Figure 4.19,are complicated by the way we dealt with the angle <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" /> . In Figure 4.19 we followed the practice employed in Chapter3 and restricted <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />  to the range <img src="http://latex.codecogs.com/gif.latex?-\pi" alt="" title="" /> to <img src="http://latex.codecogs.com/gif.latex?+\pi" alt="" title="" /> , since angles outside this range are equivalent to angles within it. However, when during the course of a calculation the angle passes out of this range and is then "reset" (by adding or substracting <img src="http://latex.codecogs.com/gif.latex?2\pi" alt="" title="" /> ), this shows up in the results for <img src="http://latex.codecogs.com/gif.latex?\Delta\theta" alt="" title="" /> as a discontinuous (and distracting) jump. Repeat the calculation of <img src="http://latex.codecogs.com/gif.latex?\Delta\theta" alt="" title="" /> as in Figure 4.19, but do not restrict the value of <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />. This should remove the large (<img src="http://latex.codecogs.com/gif.latex?\Delta\theta~2\pi" alt="" title="" />) jumps in <img src="http://latex.codecogs.com/gif.latex?\Delta\theta" alt="" title="" /> in Figure 4.19, but the smaller and more frequent dips will remain. What is the origin of these dips?

## 2.Background

Hyperion, also known as Saturn VII, is a moon of Saturn discovered by William Cranch Bond, George Phillips Bond and William Lassell in 1848. It is distinguished by its irregular shape, its chaotic rotation, and its unexplained sponge-like appearance. It was the first non-round moon to be discovered. 
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-00.jpg)
The Voyager 2 images and subsequent ground-based photometry indicated that Hyperion's rotation is chaotic, that is, its axis of rotation wobbles so much that its orientation in space is unpredictable. Its Lyapunov time is around 30 days. Hyperion, together with Pluto's moons Nix and Hydra,is among only a few moons in the Solar System known to rotate chaotically, although it is expected to be common in binary asteroids. It is also the only regular planetary natural satellite in the Solar System known not to be tidally locked.---Wikipedia 
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-01.png)
The formulation of the synchronized spin is not discussed here,it's clearly illustrated in the text book on page 123.Additionally,it turns out that all of the moons in the solar system except one exhibit such synchronism.The exception is Hyperion.
To simulate the motion of Hyperion we will first make few simplifying assumptions.Our goal will not be to perform a relastic simulations.Rather,our objective is simply to show that the motion of such an irregularly shaped moon can be chaotic.With that goal in mind we consider the model with two bodies. We can write the gravity from Jupiter to Earth in horizon as
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-02.png)
Considering the fixed position of the Sun, we obtain the horizontal acceleration of Earth
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-03.png)
We have used an essential equation in this formate
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-04.png)
As for Hyperion, we have the relation of angular acceleration and angle
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-05.png)
This equation is the crucial part of our problems

## 3.Body contents

### 3.1 Different time steps

First of all,We shall see the most general situation with the circular orbit.We plot <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" /> versus time.With dt=0.0001 .However there is some disorder that should not exsist in this oribit orbit.So here we take this as a consequence of dt.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-06.png)
In the area closed by RED-LINE,we see obviously diorder of the plot.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-07.png)
We take dt to seperately be 0.0001,0.00001
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-08.png)
Now let us investigate situations with different dt,here we set dt to seperately be 0.001,0.0005,0.0001,0.00001.It is evident that the disorder disappear with the increment of precision.With dt=0.0001,we barely see any disorder or chaos in the plot!
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-09.png)
### 3.2 Single initial condition

Here it is an amplifying plot of dt=0.0001,as the precision is extremely high,the program take much longer time to process.In the later discussion,we shall use less precision with dt=0.001 without the interference of general results.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-10.png)
Let us take a better look at the behavior of <img src="http://latex.codecogs.com/gif.latex?\omega" alt="" title="" /> versus time!Tumbling of Hyperion calculated assuming a circular orbit.It is eviedtly the <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" /> as well as <img src="http://latex.codecogs.com/gif.latex?\omega" alt="" title="" /> is periodic and not chaotic.The vertical jumps of the plot are due to the resetting of the angle from <img src="http://latex.codecogs.com/gif.latex?-\pi" alt="" title="" /> to <img src="http://latex.codecogs.com/gif.latex?+\pi" alt="" title="" />.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-11.png)
Additionally,we also draw the Phase Plot,which means plot with <img src="http://latex.codecogs.com/gif.latex?\omega" alt="" title="" /> versue <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" />.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-12.png)
### 3.3 Slightly varied inition condition

Here we consider the divergence of two nearby trajecotries of the tumbling motion of Hyperion.We plot the differnece between two calculated results of <img src="http://latex.codecogs.com/gif.latex?\theta" alt="" title="" /> with <img src="http://latex.codecogs.com/gif.latex?\Delta\theta=0.01" alt="" title="" />.Noting that it being a circular orbit,we are not able to observe the chaotic in the plot.However,we found some strange points that interfered with periodic.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-13.png)
Now we also displays different situations with slightly different <img src="http://latex.codecogs.com/gif.latex?\Delta\theta" alt="" title="" />=0.5 and 1.0.There is no obious chaos in both of them.
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-14.png)
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-11/Figure/Ex11-15.png)

## 4. Acknowledgement

### [Zhang Zitong](https://www.zybuluo.com/zy-0815/note/586758)
### [Tan Shan](http://www.jianshu.com/p/df50d3dd4523)
### [Prof.Cai](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357)
