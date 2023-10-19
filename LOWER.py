


Upper_To_Lower = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 
'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 
'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 
'x', 'Y': 'y', 'Z': 'z'}
    
def getLowercase(text):
    lowercaseText = ''    
    for charachter in text:
        if charachter in Upper_To_Lower:
            lowercaseText += Upper_To_Lower[charachter]
        else:
            lowercaseText += charachter
            
    return lowercaseText        