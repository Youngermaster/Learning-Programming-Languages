% Clase 4 de abril de 2019

a = 2
b = 6
U = rand(10000, 1)      % Uniforme entre cero y uno.
X = a + (b - a)*U
hist(X)
mean(X)
var(X)

p = mean((X <= 3))
mu = 20
u = rand(10000, 1)
x = -mu * log(u)
hist(x)
mean(x)
var(x)

p=mean(x <= 25)

mu = 3.5
sig = 0.2
z = randn(100 ,1)
x = mu + sig * z
hist(x)
mean(x)
var(x)
p = mean(2 <= x & x <= 3.7)     % Calcular experimental p(2 <= x <= 3.7)
normcdf(3.7, 3.5, 0.2)      % Calcular teorica