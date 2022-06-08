from math import fabs

class Kalman_1D:
    def __init__(self,initial_state,initial_uncertainty,measurement_uncertainty,process_noise):
        self.state_estimate=initial_state #Xnn
        self.estimate_uncertainty=initial_uncertainty#Pnn
        self.kalman_gain=0#k
        self.measurement_uncertainty=measurement_uncertainty#R
        self.process_noise=process_noise#q
       

    def predict(self,measurement):
        self.estimate_uncertainty=self.estimate_uncertainty+self.process_noise
        self.kalman_gain=self.estimate_uncertainty/(self.estimate_uncertainty+self.measurement_uncertainty)
        self.state_estimate=self.state_estimate+self.kalman_gain*(measurement-self.state_estimate)
        self.estimate_uncertainty=(1-self.kalman_gain)*self.estimate_uncertainty
        return self.state_estimate



