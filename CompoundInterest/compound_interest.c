/* Compound Function 
 *
 *A = Pe^rt
 *Compile with: 
 *gcc compound_interest.c -lm 
 *exp() - euler constant
 *log() - natural logarithm -- to calculate r and t 
 *fabs() - absolute value -- double data type
 */

#include <stdio.h> 
#include <math.h>


//Functions A end (final value), P principal, r rate of growth, t time period

void end_value(double *P, double *t, double *r, int len) { 
  double A [len]; 
  double r_t[len]; 

  for(int i = 0; i< len; i++) { 
	  r_t[i] = r[i] * t[i]; 
	  A [i] = P[i] * exp(r_t[i]); 
  }
  for(int i = 0; i< len; i++) { 
	  printf("%f\n", A[i]); 
  }

} 

void principal_value(double *A, double *r, double *t, int len) { 
  double P[len]; 
  double r_t[len]; 

  for(int i = 0; i < len; i++) { 
	  r_t[i] = r[i] * t[i]; 
	  P[i] = A[i]/exp(r_t[i]); 
  }
  for(int i = 0; i < len; i++) { 
	  printf("%f\n", P[i]); 
  }
} 

void r(double *A, double *P, double *t, int len) { 
	double r[len]; 
	
	for(int i = 0; i < len; i++) { 
		r[i] = log(A[i]/P[i]) / t[i]; 
	}
	for (int i = 0; i < len; i++) { 
		printf("%f\n", fabs(r[i])); 
	}

}

void t(double *A, double *P, double *r, int len) { 
	double t[len]; 
	
	for(int i = 0; i < len; i++) { 
		t[i] = log(A[i]/P[i]) / r[i];
	}
	for(int i = 0; i< len; i++) { 
		printf("%f\n", fabs(t[i])); 
	}

}


int main() { 
  //declaring arrays 
  double A [] = {22.75, 23.99, 244.00, 3434.00}; 
  double P [] = {13.8, 334.55, 345.44, 42.00}; 
  //double rate [] = {0.05, 0.03, 0.3, 0.12}; 
  double time_period [] = {10, 22, 4, 5}; 
  
  int len = sizeof(A)/sizeof(A[0]);
  r(A, P, time_period, len); 

  return 0; 
}

