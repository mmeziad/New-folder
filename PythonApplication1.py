import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.10)

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


delay_print ('You wake up, lost from your crew. Your name is..');

print ('As a kid your father was a..');
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

delay_print ('Here are your stats');
print ('Attack =', str(charAttack));
print ('Armor = ', str(charArmor));
print ('Speed = ', str(charSpeed));
print ('Abilities = ', charAbilities)
