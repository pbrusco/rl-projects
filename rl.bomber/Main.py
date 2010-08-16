from Settings import *
from Manager import Manager

def main():
	mgr = Manager(iters=ITERATIONS,maxturns=MAX_TURNS)
	mgr.run()

if __name__ == "__main__":
    main()