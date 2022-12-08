#-- Parameters
   param d integer   > 0;  # Number of dimensions of the problem, in general : 2
# K : the dimensions of the problem
set K := 1 .. d;

   param n integer   > 0;  # the number of individuals
# I : the set of individuals
set I := 1 .. n; 

   param a{I,K}      >= 0; # The coordinates of the individuals
   param q{I}              # The demands of the individual i     

   param p integer   > 0;  # the number of clusters
# J : the set of clusters |I| > |J|
set J := 1 .. p; 
   param Q{J}        > 0;  # Max capacities







#-- Variables 
   var x{I}{K} ;  #-- 1 if the individual i is assigned to the median j, 0 otherwise
   var n{J}>0 integer >= 0;  #-- Number of individuals in the cluster j 
   var y{I}{J} binary;  #-- Decision variable : 1 if the individual i is in j, 0 otherwise



minimize Obj :                   # minimize objective function
   sum {I in I, j in J} sqrt( ( sum {k in K} a[i,k] - x[j,k] ) ) * y[i,j];


#-- Constraints 

# (33) each individual belongs to one and only one cluster
subject to c33{i in I} : 
	sum{j in J} y[i,j] = 1;

# (34) sets the number of individuals in each cluster
subject to c34{j in J} : 
	sum{i in I} y[i,j] <= n[j]; # is actually an equality

# (35) The geometric centers of the clusters
subject to c35{j in J} : 
	sum{i in I} a[i] * y[i,j] <= n[j] * x[j]; # is actually an equality

# (36) Assure we do not overload a cluster
subject to c36{j in J} : 
	sum{i in I} q[i] * y[i,j] <= Q[j];