/* Follows the formula for continuous compounding
 * A  = Pe^rt 
 * where: 
 * A = end value 
 * P = principal value 
 * r = rate of return 
 * t = time period 
 * e = euler constant -- C++ std::exp()
 *
 *
 *
 */

#include <iostream> 
#include <cmath>

class CompInterest {

  public:


  void t(double *A, double *P, double *r) { 
	  double t[4];
	  for(int i = 0; i< 4; i++) { 
		  t[i] = std::log(A[i]/P[i]) / r[i]; 
	  }
	  for(int i = 0; i< 4; i++) { 
		  std::cout << std::abs(t[i]) << std::endl; 
	  }
  }

  void r(double *A, double *P, double *t) { 
	  double r[4];
	  for(int i = 0; i< 4; i++) { 
		  r[i] = std::log(A[i]/P[i]) / t[i]; 
	  }
	  for(int i = 0; i < 4; i++) { 
		  std::cout << std::abs(r[i]) << std::endl; 
	  }
	}

  void principal_value(double *A, double *r, double *t){
	  double P[4];
	  for(int i = 0; i< 4; i++) { 
		  double r_t [4]; 
		  r_t[i] = r[i] * t[i]; 
		  P[i] = A[i]/std::exp(r_t[i]); 
	  }
	  for(int i = 0; i<4; i++) { 
		  std::cout << P[i] << std::endl; 
	  }
  }

  void end_value(double *P, double *r, double *t) {
	  double A[4]; 
	  for(int i = 0; i < 4; i++) {
		  double r_t [4];
		  r_t [i] = r[i] * t[i]; 
		  A [i] = P[i] * std::exp(r_t[i]); 
	  }
	  for(int i = 0; i < 4; i++) { 
		  std::cout << A[i] <<std::endl; 
	  } 
 }

}; 

int main() { 

  CompInterest end; 

  double P [] = {13.8, 10.0, 13.22, 12.00}; 
  //double r [] = {0.05, 0.80, 0.23, 0.123}; 
  double t [] = {10, 23, 4, 5};
  double A [] = {22.44, 23, 54, 8.332}; 
  //end.end_value(P, r, t);
  end.r(A, P, t); 

  return 0; 
}
