# Computational Physics Homework 5
***

#### Student class: 14级彭桓武班
#### Student name: 郭明达
#### Student number: 201430102011
***

# The Fifth Time Homework-Realistic Projectile Motion

## 1.Abstract
In warfare you generally want to hit a particular target (as opposed to having the cannon shells land indicriminately). Of course, good prediction is quite helpful to realize it. Daily life tell us the trajectory of a cannon shell is related to a lot of factors, including the uniform air drag, the isothermal air drag, the adiabatic air drag and so on. Here, we will take some of them into consideration in the following parts. It will considerably important for us to learn and use the same method to solve similar problem in the furture.


In the last homework, we have already used the Euler method to solve questions, but, last time, we just applied it to differential equation of first order. Now, we will apply it to more complicated situations. To be specific, we consider a projectile such as a shell shot by a cannon. If we ignore the air drag we can write the horizonal and vertical fuctions repectively

![公式](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-5/E5%20formula.png)

Under this condition, to use the Euler method, we write each derivative in finite difference form, which leads to

![方程](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-5/equation1.png)

The result is below.

![图片](https://github.com/gmd3250679/compuational_physics_N2014301020111/blob/master/Exercise-5/figure_1.png)

Of course, just the gravity was considered, and here the gravity velocity are constant. In real war, the above situation is not work, in the following process, I will solve this problem step by step.

## Acknowledge
[tan shan](https://github.com/TanMingjun/compuational_physics_N2014301020106)
Pro.cai
