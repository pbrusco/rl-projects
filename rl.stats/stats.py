import os, fnmatch

MAX_GAMES = 10000
PERCENTAGE_OF_LOST_GAMES = 0.15
WIN_STATUS = 3

class GameData():
	def __init__(self, splitteddata):
		self.elapsed, self.turns, self.status, self.movementActionsCount, self.dropActionsCount, self.explodeActionsCount, self.noResultActionsCount = [float(data) for data in splitteddata]

def calculateConvergence(games):
	statuses = [g.status for g in games]
	win = statuses.count(WIN_STATUS) 
	lose = len(statuses) - win
	haswon = False
	
	for i,status in enumerate(statuses):
		if haswon and float(win) * PERCENTAGE_OF_LOST_GAMES > float(lose):
			return i
		elif status == WIN_STATUS:
			haswon = True
			win -= 1
		else:
			lose -= 1
		
	return None
	
		
def printStats(filepath, games):
	totalTime = float(sum([g.elapsed for g in games]))
	totalMovements = float(sum([g.turns for g in games]))
	timePerMovement = totalTime / totalMovements
	convergence = calculateConvergence(games)
	
	print "{0} & {1:.2e} & {2} \\\\".format(filepath, timePerMovement, convergence)

	
def loadData(filepath):
	games = []
	with open(filepath, 'r') as input:
		for line in input:
			games.append(GameData(line.split()))
			if len(games) >= MAX_GAMES: break
			
	return games		
	

def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)
			
def main():
	for filepath in locate('*-result.out', '..'):
		games = loadData(filepath)
		file = os.path.basename(filepath)
		printStats(file, games)

if __name__ == "__main__":
    main()