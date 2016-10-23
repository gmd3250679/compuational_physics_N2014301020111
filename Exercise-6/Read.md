
#  The sixth assignment of computational physics : Super Precision Attack
### Name:郭明达
### Number:2014301020111 
### Date:23.Oct.2016

## 1.Abstract
In the last homework, we have already drawn some trajectories of cannon shells. That situation requires known initial(firing) velocity and firing angle, and we just hit a random target. Of corse, it is not impractical in the war. In fact, what we can know is the distance between enemies(targets) and us. So, how can we use the distance and our cannon shells' firing velocity to hit the target. Besides, if the position of the target is told, what should we do to get the target with the smallest velocity. 
![大炮](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/figure/U31P27T1D370853F3DT20060517093426.jpg)
### Question 2.10 
Generalize the program developed for the previous problem so that it can deal with situations in which the target is at a different altitude than the cannon. Consider cases in which the target is higher and lower than the cannon. Also investigate how the minimum firing velocity requried to hit the target varies as the altitude of the target is varied. Consider the wind drag and use the adiabatic approxiation.

## 2.Background and introduction
In the last section, we have already gotten the differential equations of motorial cannon shells. It were given below:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_1.png) (1)

Now, let next add the effect of the wind. We will assume that it is blowing in horizontal (x) direction and has a constant magnitude and direction during flight of cannon shell. In this case the compnonents of the drag force become:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_2.png) (2)

Or we can rewrite the compnonents of the drag force in another form:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_3.png) (3)

So, combine (1)(3), the equations of motion become as:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_4.png) (4)

Though it seems that everything was been done, one forget to conduct a transform:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_5.png) (5)

Thus, equation (4) can be expressed like this:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_6.png) (6)

When it comes to here, it's time for us to write our programs. By the way, don't forget to put this constants into our program:

![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_7.png), 
![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_8.png), 
![tupian](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/equation/equation_9.png), 

## 3.Body content
###Level 1
Introducing the facing-air drag for Pro.2.10
For this programme, we input the firing velocity is 1000km/s,each time gap is 0.01s, the target altitude is 3km, velocity of wind is 30m/s.After that, we scan the different firing angles for each date and get the range of distance showing below
![Facing-air shell](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/figure/figure_hit.png)
As we can easily see in this graph, for this condition, the 55 seems the angle for longest distance. Of course, changing the parameters would give changable angle for distance, here I demonstrate one example 
![Another condition](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/figure/figure_2hit.png)
There is maximum distance for 65 degree.
###Level 2
Further update for precision attack
Considering the error of firing angle,velocity and facing air drag,we presue the more precise attack location
I prefer to introduce the loop calculation to presue more precise result. Here, for example, 5 loop steps for the calculation. The results present the firing velocity, firing angle and the distance from the target in horizon respectly. Obiviously, more loops we require, more precious results we could get in spite of the limitation of computer.
![Loop](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-6/figure/figure_hitup.png)

## 4.Conclusion
There is always updates for programmes with the chase of better results, however, the practical method can satisfy our need in a way.
So, cannon shell trajectories needs more experience rather than innovation
## 5.Acknowledge
###Yang Shen (https://www.zybuluo.com/whu-sy/note/540944)
###Shan Tan (https://github.com/TanMingjun/compuational_physics_N2014301020106/edit/master/shujubao/Ex_6/Ex-6.md)
###Pro.Cai (https://www.evernote.com/shard/s140/sh/26f85380-ee6c-4b4b-b33f-6871804d91ff/fb8cc702cb0e8ed7fafb50b2de4596ca)
