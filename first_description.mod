param d integer   > 0;  # Number of dimensions of the problem, in general : 2
param n integer   > 0;  # the number of individuals
param a{n}{d}     >= 0; # The coordinates of the individuals
param p integer   > 0;  # the number of clusters
param Q{p}        > 0;  # Max capacities

# K : the dimensions of the problem
set K := 1 .. d;

# I : the set of individuals
set I := 1 .. n; 

# J : the set of cluster centers |I| > |J|
set J := 1 .. p; 




#-- Variables 
var x{I}{K} ;  #-- 1 if the individual i is assigned to the median j, 0 otherwise
var n{J}>0 integer >= 0;  #-- Number of individuals in the cluster j 
var y{I}{J} binary;  #-- Decision variable : 1 if the individual i is in j, 0 otherwise



minimize Obj :                   # minimize objective function
   sum {I in I, j in J} sqrt( ( sum {k in K} a{i}{k} - x{j}{k} ) ) * y[i,j];
