# Mn2 Bi4 Te8
# Mn Mn Bi2 Bi2 Te4 Te4
initalCombination = ["Mn", "Mn", "Bi", "Bi", "Te", "Te"]
ASites = ["Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Mo", "Nb", "Tc", "Ru", "Rh", "Re"]
BSites = ["Sn", "Sb", "Pb", "Bi"]
XSites = ["S", "Se", "Te"]

combinations = []
elementNum = []
for i in range(len(ASites)):
	firstElement = ASites[i]
	for j in range(len(ASites)):
		if (i >= j):
			secondElement = ASites[j]
			for k in range(len(BSites)):
				thirdElement = BSites[k]
				for l in range(len(BSites)):
					if (k >= l):
						fourthElement = BSites[l]
						for m in range(len(XSites)):
							fifthElement = XSites[m]
							for o in range(len(XSites)):
								if (m >= o):
									sixthElement = XSites[o]
									combinations.append([firstElement, secondElement, thirdElement,
														fourthElement, fifthElement, sixthElement])
									elementNum.append([1, 1, 2, 2, 4, 4])

print(len(elementNum))
tempIdx = 0
for entry in combinations:
	elementNumEntry = elementNum[tempIdx]

	for idx in range(5):
		if (entry[idx] == entry[idx+1]):
			entry[idx+1] = " "
			elementNumEntry[idx] += elementNumEntry[idx+1]
			elementNumEntry[idx+1] = 0

	for k in range(6):
		for idx in range(5):
			if (entry[idx] == " "):
				entry[idx] = entry[idx+1]
				entry[idx+1] = " "
				elementNumEntry[idx] = elementNumEntry[idx+1]
				elementNumEntry[idx+1] = 0

	elementNum[tempIdx] = elementNumEntry
	tempIdx += 1

for idx in range(100):
	print("Elements: ", combinations[idx], " Quantities: ", elementNum[idx])

print("Done Generation...saving....")
for idx in range(len(combinations)):
	if(combinations[idx][0] == initalCombination[0]):
		if(combinations[idx][1] == "Bi"):
			if(combinations[idx][2] == "Te"):
				print("Found MnBi2Te4")
				print(combinations[idx])
				print(elementNum[idx])

def go_fast(combinations, elementNum):
	for idx in range(len(combinations)):
		elements = ""
		for entry in range(len(combinations[idx])):
			elements += combinations[idx][entry] + " "
		numbers = ""
		for entry in range(len(elementNum[idx])):
			if(elementNum[idx][entry] != 0):
				numbers += str(elementNum[idx][entry]) + " "
		elementWithoutSpaces = elements.replace(" ", "")
		directory = "./EndPOSCARs/CONTCAR_mono_" + elementWithoutSpaces
		f = open(directory, "w+")
		f.write("MnBi2Te4 family\n")
		f.write("   1.00000000000000\n")
		f.write("     8.7650431443767047   -0.0005399029840135   -0.0002448848942337\n")
		f.write("    -2.1916738836961653    3.7946514128751252    0.0007424981544355\n")
		f.write("     0.0070287791392392    0.0124711294102474   40.0129482350765855\n")
		f.write(elements+"\n")
		f.write(numbers+"\n")
		f.write("Direct\n")
		f.write("  0.3333332823320356  0.3333328298824974  0.3333332722325493\n")
		f.write("  0.8333333674139776  0.3333331165432443  0.3333333934235932\n")
		f.write("  0.0000223243934183  0.9999368181655564  0.4269753168727731\n")
		f.write("  0.5000223290071062  0.9999366406062024  0.4269753511710188\n")
		f.write("  0.1666443464177227  0.6667300472086830  0.2396913669576135\n")
		f.write("  0.6666442674989261  0.6667299474708771  0.2396913237775453\n")
		f.write("  0.3332956032977298  0.3333910367802608  0.4704450692447294\n")
		f.write("  0.8332956264593446  0.3333910504325873  0.4704450750121638\n")
		f.write("  0.3333710319699740  0.3332758705559914  0.1962215920354875\n")
		f.write("  0.8333711107035396  0.3332759865777827  0.1962215887702038\n")
		f.write("  0.0000507531443909  0.0001286758053019  0.2937616366195669\n")
		f.write("  0.5000508546181424  0.0001287539079278  0.2937616314221337\n")
		f.write("  0.1666159866367555  0.6665380101898929  0.3729050252581044\n")
		f.write("  0.6666158497552283  0.6665379997497312  0.3729050139388994\n")
		f.close()
		if(idx % 1000 == 0):
			print("Progress: ", idx/len(combinations)*100, "%")

#go_fast(combinations, elementNum)
