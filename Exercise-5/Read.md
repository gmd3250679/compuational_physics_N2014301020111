# Computational Physics Homework 5
***

#### Student class: 14级彭桓武班
#### Student name: 郭明达
#### Student number: 201430102011
***

# The Fifth Time Homework-Realistic Projectile Motion

## 1.Abstract
In warfare you generally want to hit a particular target (as opposed to having the cannon shells land indicriminately). Of course, good prediction is quite helpful to realize it. Daily life tell us the trajectory of a cannon shell is related to a lot of factors, including the uniform air drag, the isothermal air drag, the adiabatic air drag and so on. Here, we will take some of them into consideration in the following parts. It will considerably important for us to learn and use the same method to solve similar problem in the furture.


In the last homework, we have already used the Euler method to solve questions, but, last time, we just applied it to differential equation of first order. Now, we will apply it to more complicated situations. To be specific, we consider a projectile such as a shell shot by a cannon. If we air resistance, the equations of motion, which are again obtained from Newton's second law, can be written as

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation1.png)

where x and y are the horizontal and vertical coordinates of the projectile, and g is the acceleration due to gravity. But these equation can't be used to python directly, so one can transform them into four first-order differential equations

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation2.png)

Under this condition, to use the Euler method, we write each derivative in finite difference form, which leads to

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/Equation/equation3.png)

 (https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/code/%E5%8A%A0%E5%86%9C%E7%82%AE%E6%97%A0%E9%98%BB.py)

The result is below.

![图片](https://github.com/TanMingjun/compuational_physics_N2014301020106/blob/master/shujubao/Ex_5/figure/figure_1.png)

Of course, just the gravity was considered, and here the gravity velocity are constant. In real war, the above situation is not work, in the following process, I will solve this problem step by step.

## 2.Background


## 4.Conclusion

## 5.Reference
