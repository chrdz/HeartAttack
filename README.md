# HeartAttack

TD1 :

-Setup of a Git/Github repository

-Reading/Comprehension of the minimal model

-Discretization of the model using the finite differences method with the Euler explicit method

TD2 :

-Implementation and plotting of the minimal model functions without the laplacian

TD3 :

-Discretization of the minimal model taking into consideration of boundary conditions

-Test with the fonction u = cos(k1Pix)cos(k2*Piy) : error not small enough ==> wrong matrix

TD4 :

-Correction of the matrix

-Correction of the second member

-Test with the fonction u = cos(k1ix)cos(k2Piy) : error ok decrease at a O(h^2) rate

TD5 :

-Print colormesh : does not show the expected result (difference of potential does not go back to zero)


TD6 : 

-The previous error was due to the scale of the colormap

-Test with different sets of parameters (first impulse EPI : 0.5, PB : 1)

![alt tag](https://raw.githubusercontent.com/tguegan/HeartAttack/master/euler-epi.gif)

TD7 :

-Sketch of the report

![alt tag](https://raw.githubusercontent.com/tguegan/HeartAttack/master/euler-bande-epi.gif)

-Test with a different impulse : rectangle

-Try new impulse : rectangle + square latter
