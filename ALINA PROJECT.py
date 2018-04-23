#Arlina- Valentina, Karla
#alex thorne mansion

from gamelib import*
game = Game(800,600,"Alex Thornes Mansion") 
bk  = Image("creepy room.jpg",game)
bk.resizeTo(800,600)
game.setBackground(bk)
hh  = Image("hh.jpg",game)
hh.resizeTo(800,600)
ghost = Image("ghost.jpg",game)
ghost.resizeBy(-80)
ghost.setSpeed(4,60)
treasure = Image("treasure.png",game)
treasure.resizeBy(-45)
treasure.setSpeed(4,60)
key = Image("key image.png",game)
key.resizeBy(-55)
f = Font(white,20,"Arial")

#title screen
hh.draw()
game.drawText("Alex Thornes Mansion",100,150,f)
game.drawText("press space for story",400,500,f)
game.update()
game.wait(K_SPACE)

bk.draw()
game.drawText("The ghost are stuck in the mansion and want to be free from the house. They have to catch all trasure to leave. However when you catch keys you lose points. If your score is less than 10 you lose.",90,4)
game.drawText("press space to start",400,500,f)
game.update()
game.wait(K_SPACE)

#level 1
while not game.over:
    game.processInput()
    bk.draw()
    ghost.draw()
    key.draw()
    treasure.draw()
    ghost.move(True)
    treasure.move(True)
              
    if keys.Pressed[K_UP]:
        hero.y -= 4
    if keys.Pressed[K_DOWN]:
        hero.y += 4
    if keys.Pressed[K_RIGHT]:
        hero.x += 4
    if keys.Pressed[K_LEFT]:
        hero.x -= 4


    if ghost.collidedWith(treasure):
       game.score+=1
       
    if ghost.collidedWith(key):
       ghost.resizeBy(-1)
        
    if game.score>=10:
        game.drawText("You Win!",100,5)
        game.over = True

    game.displayScore()
    game.update(60)

game.quit()




