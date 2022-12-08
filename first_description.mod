param n integer > 0; # the number of individuals
param p integer > 0; # the number of clusters

# I : the set of individuals
set I := 1 .. n; 

# J : the set of cluster centers |I| > |J|
set J := 1 .. p; 




#-- Variables 
var x{I}{K} ;  #-- 1 if the individual i is assigned to the median j, 0 otherwise
var n{J}>0 integer > 0;  #-- Number of individuals in the cluster j 
var y{I}{J} >=1;  #-- Decision variable : 1 if the individual i is in j, 0 otherwise



minimize Number:                   # minimize objective function
   sum {I in I, j in J} y[i,j];
