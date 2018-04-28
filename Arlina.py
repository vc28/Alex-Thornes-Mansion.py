#Arlina- Valentina, Karla
#alex thorne mansion
from gamelib import*
game = Game(800,600,"Alex Thornes mansion!")
bk  = Image("creepyroom2.jpg",game)
bk.resizeTo(800,600)
game.setBackground(bk)
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
game.update(60)
game.wait(K_SPACE)
game.over=True
while game.over:
    bk.draw()
    game.drawText("The ghost are stuck in the mansion and want to ",50,90,f)
    game.drawText("ne free They have to catch all trasure to leave ",50,140,f)
    game.drawText("However when you catch keys you lose points.",50,190,f)
    game.drawText("If your score is less than 10 you lose.",25,240,f)
    game.drawText("press space to start",25,375,f)
    game.update(60)
    game.processInput()
    if keys.Pressed[K_SPACE]:
        game.over=True
#level 1
while game.over:
    game.processInput()
    game.update(60)
    bk.draw()
    key.draw()
    treasure.draw()
    ghost.draw()
    ghost.move(True)
    treasure.move(True)
          	
	
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

    if keys.Pressed[K_UP]:
        ghost.y -= 4
    if keys.Pressed[K_DOWN]:
        ghost.y += 4
    if keys.Pressed[K_RIGHT]:
        ghost.x += 4
    if keys.Pressed[K_LEFT]:
        ghost.x -= 4
    game.displayScore()
	
    game.over=True
game.quit()
