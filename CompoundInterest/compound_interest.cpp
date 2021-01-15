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
 *This program uses vectors and pass-by reference.
 *If there are any errors or fixes, please let me know. 
 */

#include <iostream> 
#include <cmath>
#include <vector>

class CompInterest {

  public:


  void t(std::vector<double> &A, std::vector<double> &P, std::vector<double> &r) { 
	  std::vector<double> t;
	  for(int i = 0; i< 4; i++) { 
		  t.push_back(std::log(A[i]/P[i]) / r[i]); 
	  }
	  for(int i = 0; i< 4; i++) { 
		  std::cout << std::abs(t[i]) << std::endl; 
	  }
  }

  void r(std::vector<double> &A,std::vector<double> &P,std::vector<double> &t) { 
	  std::vector<double> r;
	  for(int i = 0; i< 4; i++) { 
		  r.push_back(std::log(A[i]/P[i]) / t[i]); 
	  }
	  for(int i = 0; i < 4; i++) { 
		  std::cout << std::abs(r[i]) << std::endl; 
	  }
	}

  void principal_value(std::vector<double> &A, std::vector<double> &r, std::vector<double> &t){
	  std::vector<double> P;
	  std::vector<double> r_t;
	  for(int i = 0; i< 4; i++) { 		  
		  r_t.push_back(r[i] * t[i]); 
		  P.push_back(A[i]/std::exp(r_t[i])); 
	  }
	  for(int i = 0; i<4; i++) { 
		  std::cout << P[i] << std::endl; 
	  }
  }

  void end_value(std::vector<double> &P, std::vector<double> &r, std::vector<double> &t) {
	  std::vector<double> A; 
	  std::vector<double> r_t;
	  for(int i = 0; i < 4; i++) {	
		  r_t.push_back(r[i] * t[i]); 
		  A.push_back(P[i] * std::exp(r_t[i])); 
	  }
	  for(int i = 0; i < 4; i++) { 
		  std::cout << A[i] <<std::endl; 
	  } 
 }

}; 

int main() { 

  CompInterest end; 

  std::vector<double> A = {22.75, 10.0, 13.22, 12.00}; 
  std::vector<double> r= {0.05, 0.80, 0.23, 0.123}; 
  std::vector<double> t = {10, 23, 4, 5};
  //std::vector<double> P = {13.8, 23, 54, 8.332};
  
  end.principal_value(A,r,t); 

  //Working Properly 
  //end.t(A,P,r);
  //end.r(A, P, t);
  //end.end_value(P,r,t);
  //end.principal_value(A,r,t); 


  return 0; 
}
