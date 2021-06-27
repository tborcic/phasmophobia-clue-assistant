class Ghost:
	def __init__(self, name, EvidenceList, description=""):
		self.name = name
		self.Evidence = EvidenceList
		self.desc = description	
	def evidence_present(self, Evidence):
		if Evidence in self.Evidence:
			return True
		else:
			return False
	def desc_get(self):
		return self.desc
	def evidence_len(self):
		output = 0
		for i in self.Evidence:
			output += len(i)
		return output