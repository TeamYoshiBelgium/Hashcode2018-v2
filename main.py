from importer import *
import sys

def main():
    print("Google Hashcode 2018")
    print("")

    f = sys.argv[1]
    
    C = importFile(f, True)
    f = f.split("/")
    f = f[-1]
    f = f.split(".in")
    f = f[0]
    print(f)
    C.findSolution()
    C.printOutput("output/" + f)

    return 0
    
main()