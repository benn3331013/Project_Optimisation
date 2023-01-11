#-- Parameters

	set I; 					# the set of individuals

	set J; 					# the set of clusters |I| > |J|


param Q {J} integer > 0; 	# Max capacities of the clusters

param demands {I} integer > 0; # Cost of an individual

param d integer   > 0;  	# Number of dimensions of the problem, in general : 2
	set K := 1 .. alpha; 	# Dimensions of the problem

param a {I} {K}; 			# The coordinates of the individuals




#-- Variables

var x{I}{K} ;  			#-- 1 if the individual i is assigned to the median j, 0 otherwise
var n {J} integer > 0; 	#-- Number of individuals in the cluster j 
var y {I} {J} binary; 	#-- Decision variable : 1 if the individual i is in j, 0 otherwise




minimize Obj :                   # minimize objective function
   sum {I in I, j in J} sqrt( ( sum {k in K} a[i,k] - x[j,k] ) + 0.0000001) * y[i,j];

#-- Constraints

# (33) each individual belongs to one and only one cluster
subject to C33 {i in I}:
	sum {j in J} y[i,j] == 1;
	
# (34) sets the number of individuals in each cluster
subject to C34 {j in J}:
	sum {i in I} y[i,j] <= n[j];

# (35) The geometric centers of the clusters	
subject to C35 {j in J}:
	sum {i in I} a[i] * y[i,j] <= n[j] * x[j];
	
# (36) Assure we do not overload a cluster
subject to C36 {j in J}:
	sum {i in I} demands[i] * y[i,j] <= Q[j];