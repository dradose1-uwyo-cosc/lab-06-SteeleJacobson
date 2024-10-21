#Steele Jacobson
# UWYO COSC 1010
# Submission Date:10/20/24
# Lab 06
# Lab Section: 12
# Sources, people worked with, help given to: 
# your
# comments
# here


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(len(random_string)) # Print out the size for reference 

# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary
# Output each letter and its corresponding occurrence in alphabetical order
# Output which letter occurred the most 
# Output which letter occurred the least 
# Output what the percentage of the string each character is, again in alphabetical

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 


#Load all the elements into a dictionary
#Will need to first declare a dictionary 

a1 = random_string.count('a')
b1 = random_string.count('b')
c1 = random_string.count('c')
d1 = random_string.count('d')
e1 = random_string.count('e')
f1 = random_string.count('f')
g1 = random_string.count('g')
h1 = random_string.count('h')
i1 = random_string.count('i')
j1 = random_string.count('j')
k1 = random_string.count('k')
l1 = random_string.count('l')
m1 = random_string.count('m')
n1 = random_string.count('n')
o1 = random_string.count('o')
p1 = random_string.count('p')
q1 = random_string.count('q')
r1 = random_string.count('r')
s1 = random_string.count('s')
t1 = random_string.count('t')
u1 = random_string.count('u')
v1 = random_string.count('v')
w1 = random_string.count('w')
x1 = random_string.count('x')
y1 = random_string.count('y')
z1 = random_string.count('z')





numbers = {
  "a": a1, 
  "b": b1, 
  "c": c1,
  "d": d1, 
  "e": e1, 
  "f": f1,
  "g": g1, 
  "h": h1, 
  "i": i1,
  "j": j1, 
  "k": k1, 
  "l": l1,
  "m": m1, 
  "n": n1, 
  "o": o1,
  "p": p1, 
  "q": q1, 
  "r": r1,
  "s": s1, 
  "t": t1, 
  "u": u1,
  "v": v1, 
  "w": w1, 
  "x": x1,
  "y": y1, 
  "z": z1, 
}


# Output: each letter and its corresponding occurrence in alphabetical order
print(numbers)

print("*"*75)
# Output which letter occurred the most 

#number = []
#
#for numb in numbers:
#    numbers[numb]
#    number.append(numbers)



numbe = []

for number in numbers:
    numb = numbers[number]
    numbe.append(numb)

#nummax = max(zip(numbers.values(), numbers.keys()))[1]
#nummin = min(zip(numbers.values(), numbers.keys()))[1]

nummax = max(numbers.values())
nummin = min(numbers.values())

nummax2 = (list(numbers.keys()))[list(numbers.values()).index(nummax)]
nummin2 = (list(numbers.keys()))[list(numbers.values()).index(nummin)]

most_occurred = nummax2
least_occurred = nummin2

print(f"The letter that occurred the most is {most_occurred}")
print("*"*75)
# Output which letter occurred the least 
print(f"The letter that occurred the least is {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical

numbers2 = {
  "a": (a1/2500)*100 , 
  "b": (b1/2500)*100, 
  "c": (c1/2500)*100,
  "d": (d1/2500)*100, 
  "e": (e1/2500)*100, 
  "f": (f1/2500)*100,
  "g": (g1/2500)*100, 
  "h": (h1/2500)*100, 
  "i": (i1/2500)*100,
  "j": (j1/2500)*100, 
  "k": (k1/2500)*100, 
  "l": (l1/2500)*100,
  "m": (m1/2500)*100, 
  "n": (n1/2500)*100, 
  "o": (o1/2500)*100,
  "p": (p1/2500)*100, 
  "q": (q1/2500)*100, 
  "r": (r1/2500)*100,
  "s": (s1/2500)*100, 
  "t": (t1/2500)*100, 
  "u": (u1/2500)*100,
  "v": (v1/2500)*100, 
  "w": (w1/2500)*100, 
  "x": (x1/2500)*100,
  "y": (y1/2500)*100, 
  "z": (z1/2500)*100, 
}

print(numbers2)
# initializing string

 
