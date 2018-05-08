#Arlina- Valentina, Karla
#alex thorne mansion

from gamelib import*
game = Game(800,600,"Alex Thornes mansion!")
bk=Image("creepyroom.jpg",game)
bk.resizeTo(800,600)
hh  = Image("hh.jpg",game)
hh.resizeTo(800,600)
ghost = Image("ghost.png",game,use_alpha=False)
ghost.resizeBy(-80)
ghost.setSpeed(4,60)
treasure = Image("treasure.png",game,use_alpha=False)
treasure.resizeBy(-45)
treasure.setSpeed(4,60)
key = Image("key image.png",game,use_alpha=False)
key.resizeBy(-55)
gameover = Image("gameover.png",game)
f = Font(white,40,white,"Arial")

#title screen
hh.draw()
game.drawText("Alex Thornes Mansion",300,150,f)
game.drawText("press space for story",400,500,f)
game.drawText("The ghost are stuck in the mansion and want to ",25,240,f)
game.drawText("ne free They have to catch all trasure to leave ",25,280,f)
game.drawText("However when you catch keys you lose points.",25,310,f)
game.drawText("If your score is less than 10 you lose.",20,350,f)
game.drawText("press space to start",20,475,f)
game.update(60)
game.processInput()
game.wait(K_SPACE)
if keys.Pressed[K_SPACE]:
        game.over=True

#level 1
while game.over:
    
    game.processInput()
    game.update(60)
    bk.draw()
    key.draw()
    treasure.draw()#dolist variables for the tresure and the keys.
    ghost.draw()
    ghost.move(True)
    treasure.move(True)
    
              
    if keys.Pressed[K_UP]:
        ghost.y -= 4
    if keys.Pressed[K_DOWN]:
        ghost.y += 4
    if keys.Pressed[K_RIGHT]:
       ghost .x += 4
    if keys.Pressed[K_LEFT]:
        ghost.x -= 4


    if ghost.collidedWith(treasure):
       game.score+=1
       
    if ghost.collidedWith(key):
       ghost.resizeBy(-1)
        
    if game.score>=10:
        game.drawText("You Win!",100,5)
        game.over = True

    if ghost.health<0 :
        game.over = True
        gameover.draw()

    game.drawText("Health: " + str(ghost.health),ghost.x-30,ghost.y+40)
        
    game.displayScore()

    
    game.over=True

game.quit()




