from Settings import *
from Manager import Manager

RUN_CONFIGURATIONS = ["conf1", "conf2"]

def main():
	
	for conf in RUN_CONFIGURATIONS:
		filename = "Settings/Settings." + conf + ".py"

		file = open(filename, 'r')
		exec(file.read())
		file.close()
		
		execfile("Maps.py")
		
		mgr = Manager(iters=ITERATIONS,maxturns=MAX_TURNS)
		mgr.run()

if __name__ == "__main__":
    main()