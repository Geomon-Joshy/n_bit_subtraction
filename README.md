# n_bit_subtraction
## subtraction of two n_bit numbers using qiskit
This is a qiskit algoritham to subtract a decimal number from another number.
libraries needed :-
  1. python3
  2. qiskit 
  3. qiskit.visualization
Two do subtraction of bits with carry the following code is used.
    - qc.cx(i,i+1)
    - qc.cx(i+2,i+4)
    - qc.ccx(i,i+1,i+2)
    - qc.cx(i+2,i+4)
The number of bit of the biggest number has to be given as input
the total number of bits used **2*n+1**
