# The tenth assignment of computational physics: Kepler's law and the precession of the perihelion of Mercury 

### Name :郭明达
### Number：2014301020111
### Date：27.Nov.2016

## 1.Abstract
This article mainly discusses orbits of planets and precession of the perihelion of Mercury by using Euler-Cromer method, and motion equation of planets. In addition, solutions of exercise 4.8,4.9, and 4.10 are included, all done by python and Vpython programs.

### Problem.4.8
Verify Kepler's third law for elliptical orbits. Run the planetary motion program with initial conditions chosen to give orbits that are noncircular. Calculate <img src="http://latex.codecogs.com/gif.latex?T_{}^{2}\diva_{}^{3}" alt="" title="" /> and compare with the values given in Table 4.2

### Problem.4.9
In this section we saw that orbits are unstable for any value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> that is not precisely 2 in (4.12). A related question, which we did not address (until now), is how unstable an orbit might be. That is, how long will it take for an unstable orbit to become obvious. The answer to this question depends on the nature of the orbit. If the intial velocity is chosen so as to make the orbit precisely circular, then the value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> in (4.12) will make absolutely no difference. Of course, in practice it is impossible to construct an orbit that is exactly circular, so the instabilities when <img src="http://latex.codecogs.com/gif.latex?\beta\neq2" alt="" title="" /> will always be apparent given enough time. Even so, orbits that start out as nearly circular will remain almost stable for a longer period than those that are highly elliptical. Investigate this by studying orbits with the same value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> (say, <img src="http://latex.codecogs.com/gif.latex?\beta=2.05" alt="" title="" /> and comparing the behavior with different values of the ellipticity of the orbit. You should find that the orientation of orbits that are more nearly circular will rotate more slowly than those that are highly elliptical.

### Problem 4.10
Calculate the precession of the perihelion of Mercury, following the approach described this section

## 2.Background

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/dgujde6ipnt1s1xf17cp.png.resize.710x399.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%201.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%202.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%203.png)

However, when the kinetic energy of the planet is large enough, its trajectory can be parabola or hyperbola.

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%205.png)

## 3.Solution

### Exercise 4.8 Kepler's third law.
The Kepler's third law is that T^2/a^3 =constant, where T is the period of the planet and a is its major semi-axis. In the solar system, this constant is about 1 (yr^2/AU^3). Here, I imagine three planets in the solar system and plot their trajectories and calculate their periods to verify the Kepler's third law. The initialized parameter is Mp,e,a. For these three imaginary planets, these values are respectively, 7,0.1,3; 60,0.05,13; 200,0.5,25.
Output

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%206.png)

The values of T^2/a^3 are respectively 0.99998, 0.99997, 0.99990. From this, we can say the Kepler's third law is workable, at least in the solar system.

So, let's us move to a different stellar system to investigate whether the constant changes or not. The mass of the new "sun" is 100 times smaller than our sun. And the values of  Mp,e,a are the same as those of the above imaginary planets.

Output

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%207.png)
The values of T^2/a^3 are 9.9955, 9.9700,and 9.9009 respectively. So the constant in the third law is different in different stellar system. 
### Exercise 4.10 Deviation from an inverse-squre dependence
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%208.png)

First, we select some initial conditions of two planet to make one of their trajectory is circular and the other one is ellipse when beta=2

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%209.png)

Then, we change the value of beta to be 2.05,2.2,2.5.

Output

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2010.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2011.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2012.png)

Vpython Animation

When beta=2.2

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2014.gif)

When beta=2.5

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2015.gif)

From these figures, we find that circular orbit when beta=2 is stable even beta changes while ellipse orbits are unstable.
### Exercise 4.10 Precession of Mercury
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2016.png)

Output

When a=0.01

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2017.png)

When a=0.02

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-10/Figure/EX10%2018.png)

The precession phenomenon is more obvious when a is large.

## 4.Conclusion
By programming, we find that Kepler's third law is effective in a stellar system but not workable in two systems. In addition, a precession phenomenon will occur according to general relativity. 

## 5.Acknowledgement

### [Prof Cai](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357)
### [Tan Shan](http://www.jianshu.com/p/cdb6d12bc02d)
### [Shen Yang](https://www.zybuluo.com/whu-sy/note/572123)
