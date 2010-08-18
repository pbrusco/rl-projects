import shutil
import os

RUN_CONFIGURATIONS = ["conf1"]

def main():
	
	for conf in RUN_CONFIGURATIONS:
		filename = "Settings/Settings." + conf + ".py"
		shutil.copyfile(filename, "Settings.py")
		tofile = "Output/" + conf + "-result.out"
		os.system("python Main.py > " + tofile)
		

	shutil.copyfile("Settings/Settings.original.py", "Settings.py")	

if __name__ == "__main__":
    main()