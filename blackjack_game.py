

#blackjack game
#=============================================================
#account of player and dealer

from  random import randint

class account():
    
    def __init__(self,balance):
        self.balance=balance
        
        
    def bet(self,bet_amount):
        balance=self.balance
        self.bet_amount=bet_amount
        if balance-bet_amount>0:
            self.balance-=self.bet_amount
        else:
            print("NOT SUFFICIENT COINS")
    
    def show_bet_amount(self):
        bet_amount=self.bet_amount
        print(bet_amount)
        
        
    def show_balance(self):
        balance=self.balance
        return self.balance
    
    def won(self,amount_won):
        balance=self.balance
        self.amount_won=amount_won
        self.balance=self.balance+(self.amount_won)

        
    pass

#=============================================================
dealer_turn=0
class players():
    
    
    
    def __init__(self,chance):
        self.chance=chance
        
        
        
    def chance_(self):
        chance=self.chance
        if chance.isalpha()==True:
            if chance=='stand':
                dealer_turn=1
                return dealer_turn
            elif chance=='hit': 
                pass
                
                                    
                    
       
    pass
#=================================================================
class cards():
    
 #   def __init__(self):
  #      pass
        
        
    def cards_value(self):
            i=randint(1,14)
            if    11>i>0:
                pass
            else:
                i=10
            return i      
    def card_type_value(self):
         card_type=0
         j=randint(1,4)
         if j==1:
            card_type='daimond'
         elif  j==2:
            card_type='hearts'
         elif j==3:
            card_type='clubs'
         elif j==4:
            card_type='spades'
         else:
            pass
         return card_type

#===================================================



#game body


print('\t\t\tHELLO AND WELCOME TO BLACK JACK GAME')
print('\t\t\t\t PRESS X TO CONTINUE')
x=input()
if x.isalpha()==True:
    pass
else:
    pass
print('\t\tINSTRUCTIONS')
print('@\tPlace your bet ammount')
print('@\tTwo cards from player side and one card from dealer side is presented')
print('@\tChoose stand for passing the chance to dealer')
print('@\tChoose hit for taking a card')
print('@\tSum of cards does not exeed 21 if excced he will loose')
print('@\tIf card total does not exceed any player total then the one with more total value of cards won')
    
card_deck=cards()#52 cardsdeck
start=0
card_total_player1=0
card_total_dealer=0
cardvalue=0
cardstype=0
i=0
j=0
game_time=0
newcard_p=0
newcard_d=0
new=0
newcard_type_p=0
newcard_type_d=0
while game_time<10:
    if new==0:
        player1=account(1000)
        dealer=account(1000)
        print("ENTER YOUR BET")

        bettamount=input()
            
        bettamount=int(bettamount)
            
        player1.bet(int(bettamount))
        dealer.bet(int(bettamount))
            
        newcard_p=card_deck.cards_value()
        newcard_d=card_deck.cards_value()
        card_total_dealer=card_total_dealer+newcard_d
        card_total_player1=card_total_player1+newcard_p
        newcard_type_d=card_deck.card_type_value()
        newcard_type_p=card_deck.card_type_value()
        new=new+1
    
    if new==1:
        print('ENTER TO CONTINUE')
        new=new+1
    else:
        print('CHOOSE STAND OR HIT')
    if dealer_turn!=1:
            choice=input()
            player1_=players(choice)
            dealer_turn=player1_.chance_()
    if dealer_turn==1:
        while card_total_dealer<21:
              
              cardvalue=0
              for i in range(1,6):
                  print('\n')
    
    
              cardvalue=card_deck.cards_value()
              cardstype=card_deck.card_type_value()
              card_total_dealer=card_total_dealer+cardvalue
             
              new=''
              if new.isalpha()==True:
                  pass
              else:
                  pass
              print('===============================================')
              for i in range(1,10):
                  if i==2:
                      print('!   PLAYER1                      DEALER       !')
                      print('!           {0}                {0}            !'.format(bettamount))
                      print('!                    {0}                      !'.format(int(bettamount)*2)) 
                      print('!  {0}      {1}            {2}   {3}        !'.format(newcard_p,newcard_type_p,cardvalue,cardstype))
                      print('!       {}                    {}              !'.format(card_total_player1,card_total_dealer))
                  else:
                      print('!                                             !')
              print('===============================================')
              print('card1:{}'.format(cardvalue))
              print(cardstype)
              print(card_total_dealer)
              print('PRESS ENTER TO CONTINUE')
              new=input()
              if card_total_dealer>=card_total_player1:
                  break
              else:
                  pass
              
    else:
        
        cardvalue=card_deck.cards_value()
        cardstype=card_deck.card_type_value()
        print(cardvalue)
        print(cardstype)
        card_total_player1=card_total_player1+cardvalue
        print(card_total_player1)
        for i in range(1,6):
            print('\n')
    
    
                
    
   
    print('===============================================')
    for i in range(1,10):
        if i==2:
            print('!   PLAYER1                      DEALER       !')
            print('!           {0}                {0}           !'.format(bettamount))
            print('!                    {0}                     !'.format(bettamount*2))
            print('!  {0}    {1}                {2}      {3} !'.format(newcard_p,newcard_type_p,newcard_d,newcard_type_d))
            print('!  {}    {}                               !'.format(cardvalue,cardstype))
            print('!    {}                                      !'.format(card_total_player1))
        else:
            print('!                                            !')
    print('===============================================')
                
        
    if card_total_dealer==card_total_player1:
        print('GAME TIE')
        if input()=='yes':
            start=0
            card_total_player1=0
            card_total_dealer=0
            i=0
            j=0
            new=0
            cardvalue=0
            cardstype=0
            dealer_turn=0
            game_time=game_time+1
        else:
            break
                    
        
    
    elif card_total_player1==21:
        player1.won(bettamount*2)   
        print('PLAYER1 WON          BALANCE:{}'.format(player1.show_balance()))
        if input()=='yes':
            start=0
            card_total_player1=0
            card_total_dealer=0
            i=0
            j=0
            new=0
            cardvalue=0
            cardstype=0
            dealer_turn=0
            game_time=game_time+1
        else:
            break
                    
            
    if card_total_dealer==21:
        dealer.won(int(bettamount)*2)
        print('DEALER WON      BALANCE :{}'.format(dealer.show_balance()))
        print('WANT TO PLAY AGAIN')
        if input()=='yes':
            start=0
            card_total_player1=0
            card_total_dealer=0
            i=0
            j=0
            new=0
            
            cardvalue=0
            cardstype=0
            dealer_turn=0
            game_time=game_time+1
        else:
            break
    elif card_total_dealer>21:
        player1.won(int(bettamount*2))
        print('PLAYER1 WON  BALANCE:{}'.format(player1.show_balance()))
        print('WANT TO PLAY AGAIN')
        if input()=='yes':
            start=0
            card_total_player1=0
            card_total_dealer=0
            i=0
            j=0
            new=0
            dealer_turn=0
            
            cardvalue=0
            cardstype=0
            game_time=game_time+1
        else:
            break
    elif card_total_player1>21:
        dealer.won(int(bettamount*2))
        print('DEALER WON BALANCE:{}'.format(dealer.show_balance()))
        print('WANT TO PLAY AGAIN')
        if input()=='yes':
            start=0
            card_total_player1=0
            card_total_dealer=0
            i=0
            j=0
            new=0
            dealer_turn=0
            cardvalue=0
            cardstype=0
            game_time=game_time+1 
        else:
            break
    else:
        pass
                
    
if player1.show_balance()>dealer.show_balance():
    print('PLAYER1 HAS MORE MONEY:{0} SO WON\n DEALER MONEY:{1}'.format(player1.show_balance(),dealer.show_balance()))
else:
    print('DEALER HAS MORE MONEY:{0} HENCE WON\n PLAYER MONEY:{1}'.format(dealer.show_balance(),player1.show_balance()))                
                
    
                
    
    
    
    
    
    



