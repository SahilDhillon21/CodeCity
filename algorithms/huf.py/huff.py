original_text = '''a


b'''
# modtext = original_text.replace(" ","").replace("\n","").replace("\r","")
# print(modtext)
freq = [0]*127
letterset = []
for i in range(0,127):
    letterset.append(chr(i))
print(letterset)
for c in original_text:
    freq[ord(c)-ord('\x00')] += 1

print(freq)

i=0
while(i<len(freq)):
    if freq[i]==0:
        freq.pop(i)
        letterset.pop(i)
    else:
        i += 1

# print(freq)
# print(letterset)

final_freq = []
final_letterset = []

while(len(freq)>0):
    maxFreq = max(freq)
    maxIndex = freq.index(maxFreq)

    final_freq.append(maxFreq)
    final_letterset.append(letterset[maxIndex])

    freq.pop(maxIndex)
    letterset.pop(maxIndex)

# print(final_freq)
print("final letterset = ",final_letterset)

total = sum(final_freq)
prefix=""
encodings=[]



for i in range(0,len(final_freq)-2):
    total = total - final_freq[i]
    if total<final_freq[i]:
        encodings.append(prefix+"1")
        prefix += "0"
    else:
        encodings.append(prefix+"0")
        prefix += "1"

encodings.append(prefix+"1")
encodings.append(prefix+"0")

print("encodings = ",encodings)

encodingDictionary = {}
decodingDictionary = {}

for i in range(0,len(final_freq)):
    encodingDictionary[final_letterset[i]] = encodings[i]
    decodingDictionary[encodings[i]] = final_letterset[i]

print(encodingDictionary)
print(decodingDictionary)

decodingDictionary = {}
# for i in range (0,len(final_freq)):
#     decodingDictionary[]

compressedText = ""

for c in original_text:
    if c.isspace():
        compressedText += c
    else:
        compressedText += encodingDictionary.get(c)

print(compressedText)



print(ord('a')-ord(' '))


