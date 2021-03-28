# Roguelike-game
Roguelike console game created in three person group in Python with usage of OOP paradigm during Codecool bootcamp.

All below and its behaviour developed as objects with specific methods.

main features: 
  > Player can move with WSAD keys across the board and its parts which are rooms.
  > Gates mechanics which allow player to go through them into another rooms only if correct key is collected.
  > collectable items: 
    > Key (which allow player to unlock gate connected with this specific key)
    > Food (which increase player health)
    > Mana potion (which increase players mana points)
    > Bow (which allow to use ranged attacks - if player have any arrows)
    > Magic stick (which allow to use magic attacks - if player have enough mana points)
  > Three types of enemies - melee Bandit, ranged Archer Bandit, magic Magician Bandit - each of them prioritizes its main type of attack; and Boss in the final room which can be defeated after killing it 5 times
  > Every type of enemy drops connected items e.g. archer can drop bow and arrows or magician can drop magic stick and mana potions.
  > Turn-based fights system with UI and ASCII animations. Each of opponents can use three types of attacks: 
    > melee (great chances for hit - relatively low dmg)
    > ranged (low chances for hit - relatively great dmg, uses arrows)
    > magic (no chances for misss - relatively great dmg, uses mana points)
  > enemies and items are ran
  > Each Player or Enemy object have its own statistcs such as Attack, Defense, Health and Mana points, which have impact on fight performacne
  
Probably to improve/implement in future:
  > Creating some of randomized generation of board
  > Create more types of weapons and items
  > Create more types of enemies 
  > Improve UI especially in fighting 
