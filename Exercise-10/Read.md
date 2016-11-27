# The tenth assignment of computational physics: Kepler's law and the precession of the perihelion of Mercury 

### Name :郭明达
### Number：2014301020111
### Date：27.Nov.2016

## 1.Abstract
This article mainly discusses orbits of planets and precession of the perihelion of Mercury by using Euler-Cromer method, and motion equation of planets. In addition, solutions of exercise 4.8,4.9, and 4.10 are included, all done by python and Vpython programs.

### Pro.4.8
Verify Kepler's third law for elliptical orbits. Run the planetary motion program with initial conditions chosen to give orbits that are noncircular. Calculate <img src="http://latex.codecogs.com/gif.latex?T_{}^{2}\diva_{}^{3}" alt="" title="" /> and compare with the values given in Table 4.2

### Pro.4.9
In this section we saw that orbits are unstable for any value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> that is not precisely 2 in (4.12). A related question, which we did not address (until now), is how unstable an orbit might be. That is, how long will it take for an unstable orbit to become obvious. The answer to this question depends on the nature of the orbit. If the intial velocity is chosen so as to make the orbit precisely circular, then the value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> in (4.12) will make absolutely no difference. Of course, in practice it is impossible to construct an orbit that is exactly circular, so the instabilities when <img src="http://latex.codecogs.com/gif.latex?\beta\neq2" alt="" title="" /> will always be apparent given enough time. Even so, orbits that start out as nearly circular will remain almost stable for a longer period than those that are highly elliptical. Investigate this by studying orbits with the same value of <img src="http://latex.codecogs.com/gif.latex?\beta" alt="" title="" /> (say, <img src="http://latex.codecogs.com/gif.latex?\beta=2.05" alt="" title="" /> and comparing the behavior with different values of the ellipticity of the orbit. You should find that the orientation of orbits that are more nearly circular will rotate more slowly than those that are highly elliptical.

### Pro 4.10
Calculate the precession of the perihelion of Mercury, following the approach described this section

## 2.Background

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/dgujde6ipnt1s1xf17cp.png.resize.710x399.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/2016-11-24_212715.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/2016-11-24_212731.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/figure_1.png)

Animation by Vpython

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/Orbits%208%20planets.gif)

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/Orbits%20solar%20system.py)

However, when the kinetic energy of the planet is large enough, its trajectory can be parabola or hyperbola.

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/p.png)
##Solution
###Exercise 4.8 Kepler's third law.
The Kepler's third law is that T^2/a^3 =constant, where T is the period of the planet and a is its major semi-axis. In the solar system, this constant is about 1 (yr^2/AU^3). Here, I imagine three planets in the solar system and plot their trajectories and calculate their periods to verify the Kepler's third law. The initialized parameter is Mp,e,a. For these three imaginary planets, these values are respectively, 7,0.1,3; 60,0.05,13; 200,0.5,25.

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/4.81.py)

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/Imaginary%20orbits.png)

The values of T^2/a^3 are respectively 0.99998, 0.99997, 0.99990. From this, we can say the Kepler's third law is workable, at least in the solar system.

So, let's us move to a different stellar system to investigate whether the constant changes or not. The mass of the new "sun" is 100 times smaller than our sun. And the values of  Mp,e,a are the same as those of the above imaginary planets.

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/Imaginary%20orbits%20of%20a%20different%20system.png)

The values of T^2/a^3 are 9.9955, 9.9700,and 9.9009 respectively. So the constant in the third law is different in different stellar system. 
###Exercise 4.10 Deviation from an inverse-squre dependence
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/2016-11-24_231900.png)

First, we select some initial conditions of two planet to make one of their trajectory is circular and the other one is ellipse when beta=2

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/4.9.py)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.png)

Then, we change the value of beta to be 2.05,2.2,2.5.

Output

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.05.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.2.png)

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.5.png)

Vpython Animation

When beta=2.05

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.05n.gif)

When beta=2.2

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.2.gif)

When beta=2.5

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/beta%3D2.5n.gif)

From these figures, we find that circular orbit when beta=2 is stable even beta changes while ellipse orbits are unstable.
###Exercise 4.10 Precession of Mercury
![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/2016-11-25_103847.png)

[Here is the code](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/4.10.py)

Output

When a=0.01

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/Simulation%20of%20the%20precession%20of%20Mercury%20a%3D0.01.png)

When a=0.02

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/Simulation%20of%20the%20precession%20of%20Mercury%20a%3D0.02.png)

[Vpython Animation](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/precession.py)

When a=0.01

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/%E6%B0%B4%E6%98%9F%E8%BF%91%E6%97%A5%E7%82%B9%E8%BF%9B%E5%8A%A8.gif)

When a=0.02

![](https://github.com/earthhero2016/compuational_physics_N2014301020108/blob/master/Ex-10/%E6%B0%B4%E6%98%9F%E8%BF%91%E6%97%A5%E7%82%B9%E8%BF%9B%E5%8A%A8a%3D0.02.gif)

The precession phenomenon is more obvious when a is large.
##Conclusion
By programming, we find that Kepler's third law is effective in a stellar system but not workable in two systems. In addition, a precession phenomenon will occur according to general relativity. 
