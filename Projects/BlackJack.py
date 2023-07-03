from random import shuffle
suits=( 'Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks=( 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={ 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank+" of "+self.suit
    
    def display(self,hide):
        display=self.value
        suit=self.suit[0]

        if self.rank in ['Jack', 'Queen', 'King', 'Ace']:
            display=self.rank[0]

        if hide:
            display='X'
            suit='X'

        print('    -----------')
        print(f'    | {display}       |')
        print('    |         |')
        print(f'    |    {suit}    |')
        print('    |         |')
        print(f'    |       {display} |')
        print('    -----------')
        
class Deck:

    def __init__(self):
        self.allcards=[]

        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.allcards.append(created_card)

    def shuffle(self):
        shuffle(self.allcards)
    
    def deal_one(self):
        return self.allcards.pop()
    
class Player:

    balance=0

    def __init__(self,name,deposit):
        self.name=name
        Player.balance=deposit

    def win_bet(self,bet):
        Player.balance+=bet
        
    def lose_bet(self,bet):
        Player.balance-=bet

class Hand(Card):

    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
        self.aces_values=[]
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=card.value
        
        if card.rank=='Ace':
            self.aces+=1
            self.aces_values.append(11)

    def adjust_to_ace(self):

        if self.aces>0:
            print(f"\nThere are {self.aces} Ace(s), Choose the Value of each Ace")

            for ace in range(self.aces):

                while True:
                    try:
                        ace_choice=int(input(f"Ace {ace+1} : "))
                    except:
                        print("\nWhoops! Thats Not a Number\n")
                    else:
                        if ace_choice==1 and self.aces_values[ace]==11:
                            self.value-=10
                            self.aces_values[ace]=1
                        elif ace_choice==11 and self.aces_values[ace]==1:
                            self.value+=10
                            self.aces_values[ace]=11
                        if ace_choice in [1,11]:
                            break
                        else:
                            print("\nEnter Only [1,11] !\n")

def take_bet(player):

    while True:
        try:
            player.bet=int(input('Place Your Bet : '))
        except:
            print('\nWhoops! Thats not a Number. Try Again\n')
        else:
            if 0<player.bet<=player.balance:
                break
            elif player.bet>player.balance :
                print(f'\nInsufficent Funds! Place a Bet less than {player.balance}\n')
            elif player.bet<1 :
                print(f'\nInvalid Funds! Place a Bet more than 0\n')

def take_hit(deck,hand):
    drawn_card=deck.deal_one()
    hand.add_card(drawn_card)

def hit_or_stand(deck,hand):

    while True:
        try:
            choice=int(input("\nWhat Do You Want To Do\n1.HIT  2.STAND\nEnter Your Choice : "))
        except:
            print("\nWhoops! Thats not a Number\n")
        else:
            if choice in [1,2]:
                break
            else:
                print("\nEnter Only [1,2]\n")

    if choice==1:
        take_hit(deck,hand)

    return choice

def show_dealer(dealer,cond):
    
    print(f"Dealer Total Value:X")
    card=dealer.cards[0]
    card.display(cond)
    for card in dealer.cards[1:]:
        card.display(False)

def show_player(player):
    
    print(f"Your Cards Total Value:{player.value}")
    for card in player.cards:
        card.display(False)

def player_busts(player,result):

    if player.value>21:
        show_player(player_hand)
        show_dealer(dealer_hand,False)
        print('\n\nGame Over! You got Busted!')
        result.lose_bet(result.bet)
        return False
    else:
        return True

def player_wins(player,dealer,result):
    if dealer.value<player.value:
        print('\n\nCongrats! You Won the Match!')
        result.win_bet(result.bet)

def dealer_busts(dealer,result):

    if dealer.value>21:
        show_player(player_hand)
        show_dealer(dealer_hand,False)
        print('\n\nThe Dealer Busts! You Won the Match!')
        result.win_bet(result.bet)
        return False
    else:
        return True
    
def dealer_wins(player,dealer,result):
    if dealer.value>player.value:
        print('\n\nGame Over! You Lost the Game!')
        result.lose_bet(result.bet)

def push(player,dealer):
    if dealer.value==player.value:
        print('\n\nThe Game Ended in a TIE!')
        
def highest_score(name,player_score):
    with open('Highest_Score.txt') as f:
        data=f.read()

    words=data.split()
    scorecard=[ [words[1],int(words[3])], [words[5],int(words[7])], [words[9],int(words[11])]]                
    
    for ind in range(3):
        if player_score>scorecard[ind][1]:
            temp=scorecard[ind]
            scorecard[ind]=[name,player_score]
            [name,player_score]=temp
        
    print("\n\nLEADER BOARD :")
    j=0
    for i in range(1,12,4):
        words[i]=scorecard[j][0]
        words[i+2]=str(scorecard[j][1])
        j+=1

        out=''
        for word in words[i-1:i+3]:
            out+=word+' '
        print(out)

    data=' '.join(words)
    
    with open('Highest_Score.txt','w') as f:
        f.write(data)
    
if __name__=='__main__':
        
    choice=2
    while choice==2:
        print("\n\n\n      WELCOME TO BLACKJACK")

        name=input("Enter Your First Name : ")
        name=name.upper()
        max_score=0
        player=Player(name,1000)

        choice=1
        while choice==1:
            print(f"\n\nYour High Score : {max_score}")
            print(f"\nCurrent Balance : {player.balance}")
            take_bet(player)

            player_hand=Hand()
            dealer_hand=Hand()

            new_deck=Deck()
            new_deck.shuffle()

            for i in range(2):
                player_hand.add_card(new_deck.deal_one())
                dealer_hand.add_card(new_deck.deal_one())

            input("Press Enter When You are Ready!")
            print('\n'*1000)

            choice=1
            game_over=True
            old=player.balance
            while choice==1 and game_over:
                show_player(player_hand)
                show_dealer(dealer_hand,True)
                player_hand.adjust_to_ace()
                choice=hit_or_stand(new_deck,player_hand)
                game_over=player_busts(player_hand,player)

            while dealer_hand.value<17 and game_over:
                take_hit(new_deck,dealer_hand)
                game_over=dealer_busts(dealer_hand,player)

            if game_over:
                show_player(player_hand)
                show_dealer(dealer_hand,False)
                player_wins(player_hand,dealer_hand,player)
                dealer_wins(player_hand,dealer_hand,player)
                push(player_hand,dealer_hand)

            if player.balance==0:
                print("\nYou Lost All Funds Game Over !\n")
                check=[2,3]
            else:
                print(f"Your Balance After the Match : {player.balance}")
                check=[1,2,3]

            while True:
                try:
                    choice=int(input("\nWhat Do You Like to Do\n1.Continue\n2.Start New Game\n3.Exit\nEnter Your Choice : "))
                except:
                    print('\nWhoops! Thats not a Number!')
                else:
                    if choice in check:
                        break
                    else:
                        print(f'\nEnter Only {check}')

            if player.balance>max_score and player.balance>old:
                max_score=player.balance

            highest_score(player.name,max_score)            

            