f1 = open("leet_message.txt", "r")
msg = f1.read()
f2 = open("translation.txt", "w")
leetMap = {
	"4": "A",
	"8": "B",
	"C": "C",
	"D": "D",
	"3": "3",
	"F": "F",
	"G": "G",
	"H": "H",
	"I": "I",
	"J": "J",
	"K": "K",
	"1": "L",
	"M": "M",
	"N": "N",
	"0": "O",
	"P": "P",
	"Q": "Q",
	"R": "R",
	"5": "S",
	"7": "T",
	"U": "U",
	"V": "V",
	"W": "W",
	"X": "X",
	"Y": "Y",
	"Z": "Z",
	"@": "a",
	"b": "b",
	"c": "c",
	"d": "d",
	"3": "e",
	"f": "f",
	"g": "g",
	"h": "h",
	"i": "i",
	"j": "j",
	"k": "k",
	"1": "l",
	"m": "m",
	"n": "n",
	"0": "o",
	"p": "p",
	"q": "q",
	"r": "r",
	"5": "s",
	"7": "t",
	"u": "u",
	"v": "v",
	"w": "w",
	"x": "x",
	"y": "y",
	"z": "z",
	"!": "!",
	",": ",",
	":": ":",
	"-": "-",
	"_": "_",
	"'": "'",
	".": ".",
}

def main():
	for line in msg:
		for char in line:
			if char in leetMap:
				f2.write(leetMap.get(char))
			elif char == " ":
				f2.write(" ")
			elif char == "\n":
				f2.write("\n")
main()