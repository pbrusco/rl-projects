import shutil
import os

#RUN_CONFIGURATIONS = ["QLearningBombProportionalToExit", "SarsaBombProportionalToExit","SarsaBombReward", "SarsaLambdaNoRewards", "SarsaLambdaBombReward"]
#RUN_CONFIGURATIONS = ["SarsaLambdaNoRewards", "SarsaLambdaNavigationRewards","SarsaLambdaBombRewards", "SarsaLambdaBombProportionalToExit", "DynaBombProportionalToExit"]
#RUN_CONFIGURATIONS = ["RmaxNoRewards", "RMaxNavigationRewards","RMaxBombRewards", "RMaxBombProportionalToExit"]
RUN_CONFIGURATIONS = ["StochasticExplo.SarsaLambda", "StochasticNav.SarsaLambda"]

def main():
	
	for conf in RUN_CONFIGURATIONS:
		filename = "Settings/SettingsStochastic/" + conf + ".py"
		#filename = "Settings/SettingsRMax/" + conf + ".py"
		#filename = "Settings/SettingsFaltantes/" + conf + ".py"
		#filename = "Settings/SettingsDyna/" + conf + ".py"
		shutil.copyfile(filename, "Settings.py")
		tofile = "Output/SettingsStochastic/" + conf + "-result.out"
		#tofile = "Output/RMax/" + conf + "-result.out"
		#tofile = "Output/Faltantes/" + conf + "-result.out"
		#tofile = "Output/SarsaLambda/" + conf + "-result.out"
		os.system("python Main.py > " + tofile)
		

	shutil.copyfile("Settings/Settings.original.py", "Settings.py")	

if __name__ == "__main__":
    main()