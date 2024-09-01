# GuitarAccessory
An app that acts as an accessory app to a guitarist
Has a tuner functionality based on Discrete Fourier Transforms
Uses sounddevice's InputStream as a basic input and scikit's data handling functions
funcs.py contains the main functions which are doing pitch detection, using the middle C (approx 260Hz) and finding and assuming guitar strings for the given pitch
main.py contains the code to run the program
soundhandler.py contains the entire code for the sounddevice callback function which processes the inputs into a stream of arrays, then finds the max frequency and then calls the pitch detection functions

Missing functionality:
Front End
