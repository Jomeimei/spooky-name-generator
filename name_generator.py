import random
import fileinput

def main(parameters = input("Enter number of names and optionally m or f: ")):
    
    #parsing input
    names = file_parser()
    m = names["m"]
    f = names["f"]
    last = names["last"]
    ll = len(last)
    
    parameters = parameters.split()
    length = len(parameters)
    mf = "n"

    if(length > 2 or length == 0):
        return print("Incorrect input")
    elif(length == 2):
        mf = parameters[1]

    if mf == "m":
        sample_list = m
    elif mf == "f":
        sample_list = f
    elif mf == "n":
        sample_list = m + f
    else:
        return print("Incorrect input")

    iterations = int(parameters[0])
    
    while(iterations != 0):
        
        first_name = sample_list[random.randint(0, len(sample_list)-1)]
        last_name = last[random.randint(0, ll - 1)]
        iterations -= 1
        
        print(first_name + " " + last_name)

    return 
    

def file_parser():
    names = {}
    current = ""
    for line in fileinput.input(files = "forgenerator.txt"):

        line = line.strip()

        if line == "m":
            names["m"] = []
            current = "m"
        elif line == "f":
            names["f"] = []
            current = "f"
        elif line == "last":
            names["last"] = []
            current = "last"
        elif line == "":
            continue
        else:
            names[current].append(line)

    m = names["m"]
    f = names["f"]
    last = names["last"]
    
    return names


if __name__ == "__main__":
    main()
