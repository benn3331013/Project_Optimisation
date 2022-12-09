set J;

set I;

param Q {J} integer > 0;

param demands {I} integer > 0;

param alpha integer > 0;

set K := 1 .. alpha;

param a {K} {I};




var centroids {K} {J};

var n {J} integer > 0;

var y {I} {J} binary;




minimize Obj:
	sum {i in I, j in J, k in K} (a[k][i] - centroids[k][j] + 0.0000001)**2;

subject to Constr33 {i in I}:
	sum {j in J} y[i][j] == 1;
	
subject to Constr34 {j in J}:
	sum {i in I} y[i][j] <= n[j];
	
subject to Constr35 {j in J}:
	sum {i in I} a[i] * y[i][j] <= n[j] * centroids[j];
	
subject to Constr36 {j in J}:
	sum {i in I} demands[i] * y[i][j] <= Q[j];