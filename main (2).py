'''Implement a class called player that represents a cricket player The player class should have a 
method called play() which prints "the player is playing cricket. derive two classes batsman and 
Bowler,from the player class override the play() method in each derived class to print "the batsman 
is batting"and"the bowler is bowling", respectively.write a program to create object of both the
batsman and bowler classes and call the play() method for each object.'''


#define the base class player 
class player:
  def Play(self):
     print("The player is playing cricket.")

#define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")
    
#Define the derived class bowler classes 
class Bowler(player):
  def play(self):
    print("the bowler is bowling.")

#create object of batsman and bowler classes
batsman=Batsman()
bowler=Bowler()

#call the play()method for each object
batsman.play()
bowler.play()