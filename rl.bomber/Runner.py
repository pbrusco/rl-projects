import shutil
import os

RUN_CONFIGURATIONS = ['SettingsStochastic/StochasticNav.QLearn',
'SettingsStochastic/StochasticExplo.QLearn',
'SettingsStochastic/StochasticNav.Sarsa',
'SettingsStochastic/StochasticExplo.Sarsa',
'SettingsStochastic/StochasticNav.SarsaLambda',
'SettingsStochastic/StochasticExplo.SarsaLambda',
'SettingsStochastic/StochasticNav.Dyna',
'SettingsStochastic/StochasticExplo.Dyna',
]

def main():
	
	for conf in RUN_CONFIGURATIONS:
		filename = "Settings/" + conf + ".py"
		shutil.copyfile(filename, "Settings.py")
		tofile = "Output/" + conf + "-result.out"
		os.system("python Main.py > " + tofile)
		

	shutil.copyfile("Settings/Settings.original.py", "Settings.py")	

if __name__ == "__main__":
    main()