from qiskit import QuantumCircuit,Aer,assemble
from numpy import array
sim = Aer.get_backend('aer_simulator') # importing the required libraries and simulators.
def conv(a,n): #defining a function which converts a decimal number to a binary number
    """Args:  
        a (int): the number to be converted.
        n (int): the number of bits.
    Returns:
        r(array) An array which returns the binary value of the integer.
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
def subc(qc,i): #defining a function which subtracts a bit from its consiqutive bit and subtracts borrow from upper bits
    """Args:  
        qc (circuit): the circuit before subtraction.
        i (int): position of qbit.
    Returns:
        qc(circuit) Circuit after subtraction
    """
    qc.cx(i,i+1)
    qc.ccx(i,i+1,i+2)
    c=i+2
    while c <= (2*n)-1:
        qc.x(c)
        qc.barrier
        qc.ccx(c-1,c,c+2)
        qc.barrier()
        qc.x(c)
        c +=2
    qc.barrier()
    return qc
n= int(input("Enter number of bits used:")) # the number of bits used (for efficency the number of bits of highest integer number is used)
a= int(input("Enter the first number:"))  # the first number
b= int(input("Enter the second number:")) # the second number
z=0
if a > b: #it is made sure that the bigger number is the second number this is done for more optimization
    a,b = b,a# if the first number is bigger, then the two numbers are interchanged
    z = 1  # a flag is set if the swaping occurs
ar=conv(a,n) # funtion call to convert first number
br=conv(b,n) # funtion call to convert second number
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
while i < (2*n)-1:
    qc=subc(qc,i) # function call to subtract two consicutive bits
    i +=2
qc.barrier()
i=1
q=0
while i <= 2*n:
    qc.measure(i,q)  # the results are meassured
    q +=1
    i +=2
qobj = assemble(qc) #simulating the circuit 
counts = sim.run(qobj).result().get_counts()
s=list(counts.keys())[0]
s=int(s,2) # the binary number is converted to a decimal
if z == 1: # the decimal is made negative if a swapping had occured that is if the first number was bigger than the second number
    s = s*(-1)
print("Answer is :",s) # print result

                                                                                                                                    5,1           T
