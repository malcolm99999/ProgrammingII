"""
Activity 1

You're going to create a program to gather medical history. Below, you'll find a list of things you need to gather from
the user. As they enter the information, you should be adding their responses to the patient_record dictionary. When
they're done, print out the dictionary to them to give them a summary of their responses.

An example of the start of your dictionary might end up looking like this:

{
    'first name': 'Joe',
    'last name': 'Smith',
    ...
}
"""


""" 
info_to_gather = ['first name', 'last name', 'age', 'height', 'weight', 'allergies', 'symptoms']

patient_record = {}

for info in info_to_gather:
    answer = input("Whats your " + info + ": ")
    patient_record[info] = answer
print("Your results are as follows")
print(patient_record)
# your code here
"""

"""
Activity 2

Below there is a dictionary called word_lengths. Your task is to programatically loop through the dictionary and update 
the value of each key value pair to be the length of the word. For example, for rainbow, you'd replace the 0 with 7. 
Then, loop through the dictionary again and print out the words that have a length of 6.
"""
"""
word_lengths = {'rainbow': 0, 'telephone': 0, 'coffee': 0, 'python': 0, 'gargantuan': 0, 'telekinesis': 0, 'lemon': 0, 'sunglasses': 0, 'blanket': 0, 'fireplace': 0, 'cloth': 0, 'velvet': 0, 'magenta': 0, 'lazy': 0, 'mountain': 0, 'headband': 0}

# your code here

for info in word_lengths:
    letter_amnt = len(info)
    word_lengths[info] = letter_amnt
print(word_lengths)
for info in word_lengths:
    if len(info) == 6:
        print(info)
"""
"""
Activity 3

Below is a secret message and a dictionary that contains the key to decoding it! Your job is to loop through each letter
in the message and replace it with it's corresponding letter in the letter_map_dict. You'll know you've solved it when
your code runs without errors and the message makes sense :) Make sure to store the decoded message in a new variable.
"""



message = """abhxqdpxw ds abqqbt qchu xlwe. 
bvjwdfdq ds abqqbt qchu dojwdfdq.
sdojwb ds abqqbt qchu fzojwbv.
fzojwbv ds abqqbt qchu fzojwdfhqbk.
pwhq ds abqqbt qchu ubsqbk.
sjhtsb ds abqqbt qchu kbusb.
tbhkhadwdqe fzxuqs.
sjbfdhw fhsbs htbu'q sjbfdhw buzxlc qz atbhm qcb txwbs.
hwqczxlc jthfqdfhwdqe abhqs jxtdqe.
bttzts sczxwk ubnbt jhss sdwbuqwe.
xuwbss bvjwdfdqwe sdwbufbk.
du qcb phfb zp hoadlxdqe, tbpxsb qcb qbojqhqdzu qz lxbss.
qcbtb sczxwk ab zub-- huk jtbpbthawe zuwe zub --zandzxs ihe qz kz dq.
hwqczxlc qchq ihe ohe uzq ab zandzxs hq pdtsq xuwbss ezx'tb kxqfc.
uzi ds abqqbt qchu ubnbt.
hwqczxlc ubnbt ds zpqbu abqqbt qchu tdlcq uzi.
dp qcb dojwbobuqhqdzu ds chtk qz bvjwhdu, dq's h ahk dkbh.
dp qcb dojwbobuqhqdzu ds bhse qz bvjwhdu, dq ohe ab h lzzk dkbh.
uhobsjhfbs htb zub czumdul ltbhq dkbh -- wbq's kz oztb zp qczsb!
—qdo jbqbts"""

letter_map_dict = {
    'a': 'b',
    'b': 'e',
    'c': 'h',
    'd': 'i',
    'e': 'y',
    'f': 'c',
    'g': 'q',
    'h': 'a',
    'i': 'w',
    'j': 'p',
    'k': 'd',
    'l': 'g',
    'm': 'k',
    'n': 'v',
    'o': 'm',
    'p': 'f',
    'q': 't',
    'r': 'z',
    's': 's',
    't': 'r',
    'u': 'n',
    'v': 'x',
    'w': 'l',
    'x': 'u',
    'y': 'j',
    'z': 'o'}
#for info in letter_map_dict:
""" 
for letter in message:
    letter_map_dict.get()
    new_message = new_message 
"""
def decoder(letter_map_dict):
    for letter in message:
        letter_map_dict.get(letter)
        letter_map_dict(message) + decoded_message

decoded_message = ""

# your code here


"""
Activity 4

It's time to make a letter distribution of your translated message! Your job is to loop through the message and count
how many of each letter, symbol, etc. in the message appears in the message. You can find the basic steps to follow below:

1. loop through your translated message
2. if the current letter you're looking at is not already in the character_frequency_dict, add it to the dictionary as 
   the key, and set its value to 1
3. if the current letter you're looking at is already in the character_frequency_dict, increment it's key by 1
4. print out the distribution when you're done. It should look something like this:

{
    '\n': 19,
    ' ': 120,
    '!': 1,
    "'": 4,
    ',': 3,
    '-': 6,
    '.': 18,
    'a': 53,
    'b': 20,
    ...
}
"""

character_frequency_dict = {

}

# your code here
