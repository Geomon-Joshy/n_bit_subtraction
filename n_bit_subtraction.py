from qiskit import QuantumCircuit,Aer,assemble
from numpy import array
sim = Aer.get_backend('aer_simulator') # importing the required libraries and simulators.
def conv(a,n): #defining a function which converts a decimal number to a binary number
    """Args:  
        a (int): the number to be converted.
        n (int): the number of bits.
    Returns:
        r(array) An array which returns the binary value of the integer
    """
    r=array([0]*n)
    if a==1:
        r[0]=1
    for i in range(a):
        if a>=1:
              r[i]=a%2
              a=a/2
        i=i+1
    return r
def subc(qc,i): #defining a function which subtract a bit from its next bit a subtracts borrow from upper bits
    qc.cx(i,i+1)
    qc.cx(i+2,i+4)
    qc.ccx(i,i+1,i+2)
    qc.cx(i+2,i+4)
    qc.barrier()
    return qc
n= int(input("Enter number of bits used:")) # the number of bits used (for efficency the number of bits of highest integer number is used)
a= int(input("Enter the first number:"))  # the first number
b= int(input("Enter the second number:")) # the second number
z=0
if a > b: #it is made sure that the bigger number is the second number this is done for more easines
    t = a # if the first number is bigger the two numbers are interchanged
    a = b
    b = t
    z = 1  # a flag is set if the swaping occurs
ar=conv(a,n) # funtion call to convert first number
br=conv(b,n) # funtion call to convert first number
qc = QuantumCircuit((2*n)+1,n) # A quantumcircuit is initialised
q=0
for i in range(n): #  quantum circuit corresponding to the input value is  made
  if ar[i]==1: 
    qc.x(q)
  if br[i]==1:
    qc.x(q+1)
  q +=2
qc.barrier()
i=0
while i < (2*(n-1))-1:
    qc=subc(qc,i) # function call to subtract two consicutive bits
    i +=2
qc.cx(i,i+1) #subtraction of the final two bita
qc.ccx(i,i+1,i+2)
qc.barrier()
i=1
q=0
while i <= 2*(n-1):
    qc.measure(i,q)  # the results are meassured
    q +=1
    i +=2
qobj = assemble(qc) #simulating the circuit 
counts = sim.run(qobj).result().get_counts()
s=list(counts.keys())[0]
s=int(s,2) # the binary number is converted to a decimal
if z == 1: # the decimal is made negative if a swapping had occured that is if the first number was bigger thanthe second number
    s = s*(-1)
print("Answer is :",s) # print result
                                                                                                                                    5,1           Top
