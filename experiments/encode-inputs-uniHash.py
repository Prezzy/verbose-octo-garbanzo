from protocol.InputEncoder import encodeInput

#This function takes input files with circuit inputs for 
#different sized input feilds and encodes the inputs to run
#with randomized circuits. Encoding here means to take a
#circuit input and replace it with three secret shares. 
#note that this means 1 input in the original input file corresponds
#to three inputs in the encoded file. For our experiments the input files
#contain random values.

def main():
    fields = [127, 107, 89]

    for field in fields:
        inputsFile = open("inputs/inputs-{}".format(field), "r")
        inputLines = inputsFile.readlines()
        inputsFile.close()

        encodedInputs = encodeInput(inputLines,(2**field)-1,(field-1)//8)
        #not sure why middle value 1 possible mistake, but not breaking
        encodedInputsFile = open("inputs/encoded-inputs-{}".format(field), "w")
        encodedInputsFile.write(encodedInputs)
        encodedInputsFile.close()

main()
