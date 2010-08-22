import shutil
import os

#RUN_CONFIGURATIONS = ["QLearningBombProportionalToExit", "SarsaBombProportionalToExit","SarsaBombReward", "SarsaLambdaNoRewards", "SarsaLambdaBombReward"]
RUN_CONFIGURATIONS = ["DynaBombProportionalToExit"]
#RUN_CONFIGURATIONS = ["RmaxNoRewards", "RMaxNavigationRewards","RMaxBombRewards", "RMaxBombProportionalToExit"]
def main():
	
	for conf in RUN_CONFIGURATIONS:
		filename = "Settings/SettingsDyna/" + conf + ".py"
		shutil.copyfile(filename, "Settings.py")
		tofile = "Output/Dyna/" + conf + "-result.out"
		os.system("python Main.py > " + tofile)
		

	shutil.copyfile("Settings/Settings.original.py", "Settings.py")	

if __name__ == "__main__":
    main()