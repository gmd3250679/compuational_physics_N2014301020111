# The twelfth assignment of computational physics: The numerical results of electromagnetic field

### Name :郭明达
### Number：2014301020111
### Date：11.Dec.2016

## 1.Abstract

This article mainly discusses the electric potentials and fields and solves Laplace's equantion by using Jacobi, Gauss-Seidel, and SOR methods. Plus, the solutions of Exercise 5.1, 5.3, 5.5, and 5.6 are included.

## 2.Background
![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-00.jpg)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-01.png)

## 3.Solution

### 1.Exercise 5.1 Prism
There is an infinitely long, hollow prism, with metallic walls and a square cross-section. Inside this prism is a metal bar, also with a square cross-section. The inner conductor is held at V=1 and the walls of the prism at V=0. We using Jacobi method to plot its Voltage distribution, equipotential lines and electric field.

Output

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-02.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-03.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-04.png)

Delta V is 0.4 since there are 400 grid elements.

### 2.Exercise 5.3 Capacitor

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-05.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-06.jpg)

Again, we use the Jacobi method to solve the capacitor problem.

Output

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-07.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-08.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-09.png)

### 3.Exercise 5.5

Now, we use Gauss-Seidel method and SOR method to solve the capacitor problem and investigate the convergence velocity of three different methods. The number of iterations of Jacobi method is 2890 when Delta V is 0.4. Modifying the above code, we obtain that the number if iterations is 2735 and 2062 for Gauss-Seidel method and SOR method respectively. Thus, the SOR method can highly raise the convergence velocity.

### 4.Exercise 5.6 Lighting rod

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-10.jpg)

The rod is very long and narrow with a high voltage, with one end near a conducting plane. Imagining that the rod is in the x-y plane, we investigate the voltage distribution, equipotential lines and electric field.

Output

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-11.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-12.png)

![](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-12/Figure/Ex12-13.png)

## 4.Conclusion

Instead of Solving the Laplace's equation directly, we use relaxtion method, which is checked to be workable by our programming. There are three different methods, Jacobi, Gauss-Seidel, and SOR method. The SOR method is most effective.

## 5.Referece

### [Zhang Zitong](https://www.zybuluo.com/zy-0815/note/586758)
### [Tan Shan](http://www.jianshu.com/p/df50d3dd4523)
### [Prof.Cai](https://www.evernote.com/shard/s140/sh/0724815b-79a9-4357-9e85-416c33cb1b69/e2b0667446e6f7d74181969ed0c7c357)
