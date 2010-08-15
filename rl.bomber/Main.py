from Manager import Manager
from Settings import *

def main():
	mgr = Manager(iters=ITERATIONS,maxturns=MAX_TURNS)
	mgr.run()

if __name__ == "__main__":
    main()