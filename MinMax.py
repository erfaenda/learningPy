import random

guess_number = random.randint(0, 200)

player_guess = [11,23,44,32,12,76]
if max(player_guess) > guess_number:
    print('Лооооохх пиддрррр %s ' % guess_number)
else:
    print('Грриитиингзз май френд %s ' % guess_number)