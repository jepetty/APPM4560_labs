#include <iostream>
#include <random>

int next_state(int x, double experiment) {
  // require 0 <= x <= 2
  if (x == 0) {
    if (experiment <= .5) {
      return 0;
    }
    else {
      return 1;
    }
  }
  else if (x == 1) {
    if (experiment <= .25) {
      return 0;
    }
    else if (experiment <= .75) {
      return 1;
    }
    return 2;
  }
  else {
    if (experiment <= .5) {
      return 1;
    }
    return 2;
  }
}

int main(int argc, char * argv[]) {
  std::random_device r;
  std::default_random_engine el(r());
  std::uniform_real_distribution<double> u(0, 1);
  std::uniform_int_distribution<int> coin_flip(0, 1);
  
  int max = 100000000;

  int present_flip = coin_flip(el);
  int past_flip = coin_flip(el);

  // the sum of the X_i's for the experiment
  int sigmaX = 0;

  // the sum of the X_i's for the derived Markov chain
  int sigmaX_Markov  = 0;

  int x_Markov;

  // inverse transform simulation
  double experiment = u(el);
  if (experiment <= .25) {
    x_Markov = 0;
  }
  else if (experiment <= .75) {
    x_Markov = 1;
  }
  else {
    x_Markov = 2;
  }
  sigmaX_Markov += x_Markov;
  sigmaX += present_flip + past_flip;

  int magnitudeOrder = 10;
  for (int i = 0; i < max; ++i) {
    past_flip = present_flip;
    present_flip = coin_flip(el);
    sigmaX += present_flip + past_flip;
    
    experiment = u(el);
    x_Markov = next_state(x_Markov, experiment);
    sigmaX_Markov  += x_Markov;
    if ((i + 1) % magnitudeOrder == 0) {
      magnitudeOrder *= 10;
      double eX = ((double) sigmaX) / ((double) max);
      double eX_Markov = ((double) sigmaX_Markov ) / ((double) max);
      std::cout << "E[X] - E[X_Markov], n = " << (i + 1) << ": " <<
	eX - eX_Markov << "\n";
  
    }
  }
  return 0;
}
