import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.07)

def RNG10():
    num = randint(1-100);
    if (num < 11):
        RNG10 = False;
    else:
        RNG10 = True;
    return RNG10;

def RNG20():
    num = randint(1-100);
    if (num < 21):
        RNG20 = False;
    else:
        RNG20 = True;
    return RNG20;

def RNG30():
    num = randint(1-100);
    if (num < 31):
        RNG30 = False;
    else:
        RNG30 = True;
    return RNG30;

def RNG40():
    num = randint(1-100);
    if (num < 41):
        RNG40 = False;
    else:
        RNG40 = True;
    return RNG40;

def RNG50():
    num = randint(1-100);
    if (num < 51):
        RNG50 = False;
    else:
        RNG50 = True;
    return RNG50;

def RNG60():
    num = randint(1-100);
    if (num < 61):
        RNG60 = False;
    else:
        RNG60 = True;
    return RNG60;

def RNG70():
    num = randint(1-100);
    if (num < 71):
        RNG70 = False;
    else:
        RNG70 = True;
    return RNG70;

def RNG80():
    num = randint(1-100);
    if (num < 31):
        RNG80 = False;
    else:
        RNG80 = True;
    return RNG80;

def RNG90():
    num = randint(1-100);
    if (num < 91):
        RNG90 = False;
    else:
        RNG90 = True;
    return RNG90;


delay_print ('Gah! You awake, in the middle of a forest. As your vision starts to sharpen, you slowly begin to take in the details of your surroudings anxiously. You find that its around dawn, and that your hunting crew... is no longer there! In panic you scramble to your feet and walk around the camp, looking for any signs of where they could possible be, but none are to be found. You check how warm the fireplace is, how warm is it?');
print ('a) hot');
print ('b) warm');
print ('c) cold');
fireChoice  = input('');
if fireChoice == 'hot':
    firstChoice = 1;
if fireChoice  == 'warm':
    firstChoice = 2;
if fireChoice  == 'cold':
    firstChoice = 3;
    
delay_print ('Now you,');
playerName = input('');
delay_print ('the');
print ('a) archer');
print ('b) mage');
print ('c) warrior');
print ('d) theif');

classChoice = input('');

if classChoice == 'a':
    charClass = 1;
    charAttack = 90;    
    charArmor = 55;
    charSpeed = 55;
    charAbilities = ['Long Shot', 'Head Shot'];

elif classChoice == 'b':
    charClass = 2;
    charAttack = 150;
    charArmor = 20;
    charSpeed = 30;
    charAbilties = ['Fireball', "Dragon's Breathe"];

elif classChoice == 'c':
    charClass = 3;
    charAttack = 70;
    charArmor = 120;
    charSpeed = 10;
    charAbilities = ['Bash', 'Charge'];

elif classChoice == 'd':
    charClass = 4;
    charAttack = 100;
    charArmor = 0;
    charSpeed = 100;
    charAbilities = ['Backstab', 'Quicken'];

#delay_print ('Here are your stats');
#print ('Attack =', str(charAttack));
#print ('Armor = ', str(charArmor));
#print ('Speed = ', str(charSpeed));
#print ('Abilities = ', charAbilities)

delay_print ('of the Ednosie Village must find your crew!');

if firstChoice == 1:
    delay_print('Ah! Its hot the touch... they cant have gotten to far now have they. You are looking for 3 people. Brom, Carac, and Thea. Brom is rough, stoic, combat trained from years in the royal army. Carac is your mage, pissy at times but reliable when stuck in a rut, you can expect an on point Dragons Breath to take your foes out. Thea...is the type of person you would describe as a hardass. Determined to prove her worth to become your apprentice as you are well known for your, classChoice, skills. she followed you and the group out into the wild until Brom found her sneaking around camp one night.');
