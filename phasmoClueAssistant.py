from simpleMenu import simpleMenu, pause
from ghost import Ghost
from printableTable import printableTable

Evidence =	{
	1: "Emf",
	2: "Fingerprint",
	3: "Freezing Temp",
	4: "GhostOrb",
	5: "SpiritBox",
	6: "Writing"
}

def EvidenceList( i, j, k):
	return [ Evidence[i], Evidence[j], Evidence[k] ]

sMenu = simpleMenu( 'Phasmophobia' )

possibleEvidence = []
eliminated = []
ghostList = []

Spirit = 		Ghost('Spirit', 		EvidenceList( 5, 2, 6), 'Smudge sticks longer')
Wraith =		Ghost('Wraith', 		EvidenceList( 2, 3, 5), 'Toxic to Salt, floating, phasing')
Phantom = 		Ghost('Phantom', 		EvidenceList( 1, 4, 3), 'Looking drops sanity, Photo disappearance')
Poltergeist = 	Ghost('Poltergeist', 	EvidenceList( 5, 2, 4), 'Loves Throwing stuff')
Banshee = 		Ghost('Banshee', 		EvidenceList( 1, 2, 3), 'One person at a time, fears Crucifix')
Jinn = 			Ghost('Jinn', 			EvidenceList( 5, 4, 1), 'Fast,power must be off')
Mare = 			Ghost('Mare', 			EvidenceList( 5, 4, 3), 'weak to light')
Revenant = 		Ghost('Revenant', 		EvidenceList( 1, 2, 6), 'fast while haunting, slow while you hide')
Shade = 		Ghost('Shade', 			EvidenceList( 1, 4, 6), 'shy with multiple ppl')
Demon = 		Ghost('Demon', 			EvidenceList( 5, 6, 3), 'agressive, ouija wont drain sanity')
Yurei = 		Ghost('Yurei', 			EvidenceList( 4, 6, 3), 'stronger sanity drain, smuding makes it stick')
Oni = 			Ghost('Oni', 			EvidenceList( 1, 5, 6), 'Be more active')

ghostList = [ 	Spirit,
				Wraith,
				Phantom,
				Poltergeist,
				Banshee,
				Jinn,
				Mare,
				Revenant,
				Shade,
				Demon,
				Yurei,
				Oni]

def updateDescription():
	sMenu.description = '\n'
	possibleGhosts = []
	eliminatedGhosts = []
	neededList = []

	#counts the number of possible evidence in each ghost evidence
	#if all of them are present the gost is added to possibleGhosts
	for ghost in ghostList:
		evidenceLen = 0
		for k in possibleEvidence:
			if ( ghost.evidence_present( k ) ):
				evidenceLen += 1
		if ( evidenceLen == len( possibleEvidence ) ):
			possibleGhosts.append( ghost )
	
	#if ghost contains eliminated evidence it is added to eliminatedGhosts
	for evidence in eliminated:
		for ghost in possibleGhosts:		   
			if ( ghost.evidence_present( evidence ) and ghost not in eliminatedGhosts ):
												#for duplicates
				eliminatedGhosts.append( ghost )

	eliminatedGhostsTable = printableTable()
	eliminatedGhostsTable.style_differentColumns()
	eliminatedGhostsTable.addRow( ['Ghost', 'Evidence', 'Desc'] )

	possibleGhostsTable = printableTable()
	possibleGhostsTable.setTo( eliminatedGhostsTable )

	eliminatedGhostsTable.middleAllign.append( 0 )
	
	#adds ghost to it's proper table
	for ghost in possibleGhosts:
		if ghost in eliminatedGhosts:
			eliminatedGhostsTable.addRow( [ ghost.name, ghost.Evidence, ghost.desc ] )
		else:
			possibleGhostsTable.addRow( [ ghost.name, ghost.Evidence, ghost.desc ] )
		
		#adds evidence need to identify
		for evidence in ghost.Evidence:
			#edicence possible			  				#duplicates					 #evidence not eliminated
			if ( evidence not in possibleEvidence and evidence not in neededList and evidence not in eliminated ):
				neededList.append( evidence )
	
	if( len( possibleGhosts) > 0 ):

		#if present print needed evidance table
		if( len( neededList ) > 0 ):
			newTable = printableTable()
			newTable.drawTitleSeperator = False
			newTable.addRow( neededList )
			sMenu.description += '\n' + newTable.getTableTitleFormat( 'Needed Evidence', allignmMent = 'left' ) + '\n'
			sMenu.description += newTable.getTable()
		
		#if present print possible evidence
		if( len( possibleEvidence ) > 0 ):
			newTable = printableTable()
			newTable.drawTitleSeperator = False
			newTable.addRow( possibleEvidence )
			sMenu.description += '\n' + newTable.getTableTitleFormat( 'Current Evidence', allignmMent='left' ) + '\n'
			sMenu.description += newTable.getTable()
		
		#if present print current eliminated evidence table 
		if( len( eliminated ) > 0 and len( possibleEvidence ) != 3 ):
			newTable = printableTable()
			newTable.drawTitleSeperator = False
			newTable.addRow( eliminated )
			sMenu.description += '\n' + newTable.getTableTitleFormat( 'Eliminated Evidence', allignmMent = 'left') +'\n'
			sMenu.description += newTable.getTable()
		
		#if present print current eliminated ghosts table 
		if ( len( eliminatedGhosts ) > 0 ):
			sMenu.description += '\n' + newTable.getTableTitleFormat( 'Eliminated Ghosts', allignmMent='left') + '\n'
			sMenu.description += eliminatedGhostsTable.getTable()

		#print possible ghosts table
		titleForPossibleTable = 'Possible Ghosts'
		#if there is only one change the title from possible to confirmed
		if( len( possibleGhosts ) == 1 ):
			titleForPossibleTable = 'Confirmed Ghost'
		sMenu.description += '\n' + newTable.getTableTitleFormat( titleForPossibleTable, allignmMent='left') + '\n'
		sMenu.description += possibleGhostsTable.getTable()

	#no ghosts possible remove last evidence
	else:
		possibleEvidence.pop()
		print('Last added evidence not possible')
		pause()

#add item to evidance table if it's not a duplicate and if present in eliminated list remove it
def addToEvidence( i ):
	if( len( possibleEvidence ) < 3):
		print()
		if( Evidence[i] in eliminated ):
			eliminated.remove( Evidence[i] )
		if ( Evidence[i] not in possibleEvidence ):
			possibleEvidence.append( Evidence[i] )
		else:
			print('Already there')
			pause()

#for exiting program
def exiting():
	sMenu.run = False
	sMenu.breaking = True

#menu for eliminating evidance
def eliminateMenu():
	eliminationMenu = simpleMenu( 'To Elimninate' )

	#add evidance to elimination menu
	def addToElimination( toEliminate ):
		if ( toEliminate not in possibleEvidence ):
			eliminated.append( toEliminate )
		eliminationMenu.Back()

	#empty eliminated list
	def resetElimination():
		eliminated.clear()
		eliminationMenu.Back()
	
	#start eliminated menu
	eliminationMenu.reset('')
	eliminationMenu.spacing = [1, len( Evidence ) + 1]
	for i in Evidence:
		eliminationMenu.menu_option_add(	addToElimination,
											Evidence[i],
											args = Evidence[i])
	eliminationMenu.menu_option_add( resetElimination, 'Reset', customKey = 'r')
	eliminationMenu.menu_start()


while (True):

	sMenu.reset( '' )
	sMenu.change_backFunction( 'r', sMenu.Back, 'Reset' )
	possibleEvidence = []
	eliminated = []
	sMenu.defaultFunciton_SetTo(updateDescription)
	for i in Evidence:
		sMenu.menu_option_add(	addToEvidence,
								Evidence[i],
								args = i )
	sMenu.spacing = ['r', str( len( Evidence ) ) ]
	sMenu.menu_option_add( eliminateMenu, 'Eliminate', customKey = 'e')
	sMenu.menu_option_add( exiting, 'Quit' , customKey = 'q')
	sMenu.menu_start()
	
	if( sMenu.breaking ):
		break