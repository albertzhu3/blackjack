from random import shuffle
from IPython.display import clear_output

class Deck:
    def __init__(self, decklist):
        self.decklist = decklist
    #def __str__
            

class Card:
    def __init__(self, name, value, what):
        self.name = name
        self.value = value
        self.what = what
    def __str__(self):
        return(f'{self.name} of {self.what}')
       
def DeckCreator():
    decklist = []
    def sectioncreator(str):
        x=1
        while x<= 13:
            if x<=9:
                decklist.append(Card(f'{x+1}', x+1, str))
            if x==10:
                decklist.append(Card('Jack', 10, str))
            if x==11:
                decklist.append(Card('Queen', 10, str))
            if x==12:
                decklist.append(Card('King', 10, str))
            if x==13:
                decklist.append(Card('Ace', 11, str)) 
            x+=1   
    y = 1
    while y<= 4:
        if y==1:
            sectioncreator('Spades')
        if y==2:
            sectioncreator('Hearts')
        if y==3:
            sectioncreator('Clovers')
        if y==4:
            sectioncreator('Diamonds')
        y+=1
    return decklist

def dealcard(deck):
    dealtcard = deck.decklist.pop(0)
    return dealtcard

def shuffledeck(deck):
    return(shuffle(deck.decklist))



class Bankroll:
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return self.balance
    def deposit(self,amt):
        self.balance += amt
    def withdraw(self,amt):
            if amt>self.balance:
                print('Funds Unavailable!')
            else:
                self.balance = self.balance - amt
'''
ace cases:
start with ace in your hand, counts as an 11 --> hit = value becomes over 21, so ace now counts as a 1, now its permanently a 1
draw the ace from a hit, total value w ace as 11 is over 21 = the ace permanently is a 1 
ace's default value is 11, if the hand.value exceeds 21, then the ace's value becomes 1 and can no longer change
'''


class Hand:
    def __init__(self, handlist):
        self.handlist = handlist
    def __str__(self):
        str = ''
        for card in self.handlist:
            str += f'{card.name} of {card.what}\n'
        return str
    def addcard(self, deck):
        self.handlist.append(dealcard(deck))
    def checkval(self):
        val = 0
        for card in self.handlist:
            val += card.value
        return val
    def checkaces(self):
        for card in self.handlist:
            if (card.name == 'Ace') and (self.checkval > 21):
                card.value = 1
    def checkbust(self):
        sum = 0
        for card in self.handlist:
            sum += card.value
        if sum > 21:
            return True
        else:
            return False

def rungame():
    playerbank = Bankroll(500)
    dealerbank = Bankroll(500)
    deck = Deck(DeckCreator())
    shuffledeck(deck)
    while (playerbank.balance != 0) and (dealerbank.balance != 0):
        playerwager = 0
        dealerwager = 0
        while True:
            playerwager = int(input(f'Your Bankroll Value: ${playerbank.balance}\nDealer Bankroll Value: ${dealerbank.balance}\nHow much would you like to wager? '))
            if playerwager > playerbank.balance:
                print("Not enough money in Bankroll. Please provide another wager.")
                continue
            else:
                if dealerbank.balance < playerwager:
                    dealerwager = dealerbank.balance
                    break
                else:
                    dealerwager = playerwager
                    break
        playerhand = Hand([])
        dealerhand = Hand([])
        playerhand.addcard(deck)
        playerhand.addcard(deck)
        dealerhand.addcard(deck)
        dealerhand.addcard(deck)
        while True:
            clear_output()
            print('    ')
            print(f"Your wager: ${playerwager} Dealer's wager: ${dealerwager}\n\nYour hand:\n{playerhand}\nDealer's hand:\nXXXXX\n{str(dealerhand.handlist[1])}")
            hs = input('\nHit or stay? Enter h to hit, s to stay. ')
            if hs.lower() == 'h':
                playerhand.addcard(deck)
                print(str(playerhand.handlist[-1]))
                playerhand.checkaces()
                #print(f"Your wager: ${playerwager} Dealer's wager: ${dealerwager}\nYour hand:\n{playerhand}\nDealer's hand:\nXXXXX\n{str(dealerhand.handlist[1])}")
                if (playerhand.checkbust()):
                    print('    ')
                    print('Value over 21, you have busted!\nYou lose the round.')
                    print('    ')
                    dealerbank.deposit(playerwager)
                    playerbank.withdraw(playerwager)
                    break
                else:
                    continue
            if hs.lower() == 's':
                print('    ')
                while (dealerhand.checkbust() == False) and (dealerhand.checkval() < playerhand.checkval()):
                    dealerhand.addcard(deck)
                    dealerhand.checkaces()
                    print(f"Dealer's hit:\n{str(dealerhand.handlist[-1])}")
                    if (dealerhand.checkbust()):
                        print('    ')
                        print(f"Dealer's hand:\n{dealerhand}")
                        print("Dealer has busted. You win the round!")
                        print('    ')
                        playerbank.deposit(dealerwager)
                        dealerbank.withdraw(dealerwager)
                        break
                    if dealerhand.checkval() > playerhand.checkval():
                        print('    ')
                        print(f"Dealer's hand:\n{dealerhand}\nYour total value: {playerhand.checkval()}\nDealer's total value: {dealerhand.checkval()}\nDealer wins the round.")
                        print('    ')
                        dealerbank.deposit(playerwager)
                        playerbank.withdraw(playerwager)
                        break
            break
    if playerbank.balance == 0:
        yee = str(input("Your bankroll has been depleted, Dealer wins.\n\nWould you like to play again? Enter Yes or No. "))
        if yee.lower() == 'yes':
            print('    ')
            rungame()
            
        else:
            return
    if dealerbank.balance == 0:
        nah = str(input("Dealer's bankroll has been depleted, You win.\n\nWould you like to play again? Enter Yes or No. "))
        if nah.lower() == 'yes':
            print('    ')
            rungame()
            
        else:
            return
        

while True:
    try:
        yn = str(input('Welcome to BlackJack!\nAre you ready to play? Enter Yes or No. '))
    except:
        print('Please enter Yes or No.')
        continue
    else:
        if yn.lower() == 'yes': 
            clear_output()
            print('    ')
            rungame()
            break
        if yn.lower() == 'no':
            print('Okay, then.')
            break 









'''
d = Deck(DeckCreator())
shuffledeck(d)
n = Hand([])
n.addcard(d)
n.addcard(d)
print(n)
print([str(item) for item in d.decklist])

human vs computer
player has a bankroll, starting with $$ amount of money
game:
player places a bet
deck is shuffled
player gets 2 random cards face up
dealer gets 2 random cards, one face up and one face down
player goes first, 2 options: hit or stay
hit: player gets one more random card from deck, adding to his current amt of cards
stay: player ends his turn, moving to the dealers turn
'''
#n = Deck(DeckCreator())
#print(n.decklist[4])
#n = DeckCreator()
#print([str(item) for item in n])



