import shutil
import os

RUN_CONFIGURATIONS = ["pabloQlearning", "pabloSarsa","pabloSarsaLambda"]

def main():
	
	for conf in RUN_CONFIGURATIONS:
		filename = "Settings/" + conf + ".py"
		shutil.copyfile(filename, "Settings.py")
		tofile = "Output/PabloTests/" + conf + "-result.out"
		os.system("python Main.py > " + tofile)
		

	shutil.copyfile("Settings/Settings.original.py", "Settings.py")	

if __name__ == "__main__":
    main()