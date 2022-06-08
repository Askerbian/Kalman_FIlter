# Kalman_FIlter
The filter is ONE dimensional , the code is Object oriented . 
Firstly initialize the filter by creating class object i.e    signal= Kalman_1D(......)
For signal filtering use the following : 
filtered signal = signal.predict(measured signal)

for better understanding of how to choose filter parameters (mesurement uncertainty , process noise and other...) 
I highly recommend to visit Kalmanfilter.net and read the section about one dementional filter . 
