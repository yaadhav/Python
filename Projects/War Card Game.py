from random import shuffle
suits=( 'Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks=( 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={ 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank+" of "+self.suit
    
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

    def __init__(self,name):
        self.name=name
        self.allcards=[]

    def add_cards(self,newcards):
        if type(newcards)==list:
            self.allcards.extend(newcards)
        else:
            self.allcards.append(newcards)
        
    def remove_one(self):
        return self.allcards.pop(0)

    def __str__(self):
        return f'{self.name} has {len(self.allcards)} cards.'

    
if __name__=='__main__':
    player1=Player("Reddy")
    player2=Player("Sitha")

    current_deck=Deck()
    shuffle(current_deck.allcards)

    player1.add_cards(current_deck.allcards[0:52:2])
    player2.add_cards(current_deck.allcards[1:52:2])

    game_on=True
    rounds=0
    while game_on:

        rounds+=1

        if len(player1.allcards)==0:
            print(f"Congratulations! Player2 HAS WON THE MATCH")
            game_on=False
            break
    
        elif len(player2.allcards)==0:
            print(f"Congratulations! PLayer1 HAS WON THE MATCH")
            game_on=False
            break

        card1=player1.remove_one()
        card2=player2.remove_one()

        if card1.value>card2.value:
            print(f"Player1 Has Won The Round {rounds}")
            player1.add_cards([card1,card2])

        elif card1.value<card2.value:
            print(f"Player2 Has Won The Round {rounds}")
            player2.add_cards([card2,card1])
        
        else:
            print("WAR")

            while card1.value==card2.value:

                if len(player1.allcards)<5:
                    print(f"Congratulations! Player2 HAS WON THE MATCH")
                    game_on=False
                    break

                elif len(player2.allcards)<5:
                    print(f"Congratulations! PLayer1 HAS WON THE MATCH")
                    game_on=False
                    break

                for num in range(5):
                    card1=player1.remove_one()
                    card2=player2.remove_one()