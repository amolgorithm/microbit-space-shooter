# Copyright (C) 2023 Amolgorithm (Amol S.).


#global variables
index2 = 0
bullet_speed = 0
index = 0
my_score = 0
list_of_enemies: List[game.LedSprite] = []
bullet: game.LedSprite = None
sprite: game.LedSprite = None
sprite = game.create_sprite(2, 3)
bullet = game.create_sprite(2, 3)
list_of_enemies = [game.create_sprite(randint(0, 4), 0)]
enemy_speed = 1

basic.pause(2000) #Wait 2 seconds before starting game


#Function that checks collision between enemies and the bottom
def enemy_ground_collision():
    global my_score, index
    
    while index <= len(list_of_enemies) - 1:
        if 4 == list_of_enemies[index].get(LedSpriteProperty.Y):
            list_of_enemies[index].delete()
            list_of_enemies.remove_at(index)
            my_score += -1
        index += 1
        
#Shifting x coordinate of sprite and bullet by 1 to the left when Button A is pressed
def on_button_pressed_a():
    sprite.change(LedSpriteProperty.X, -1)
    bullet.change(LedSpriteProperty.X, -1)
    
input.on_button_pressed(Button.A, on_button_pressed_a)


#Checks collision between bullet and boundaries (ceiling).
def check_bullet_boundaries():
    global bullet_speed
    
    if bullet.get(LedSpriteProperty.Y) <= 0:
        bullet_speed = 0
        bullet.set(LedSpriteProperty.Y, 3)
        

#Checks if game is over by checking collision between enemy and sprite    
def game_over_check():
	global my_score, list_of_enemies, sprite
	
    for value in list_of_enemies:
        if sprite.get(LedSpriteProperty.X) == value.get(LedSpriteProperty.X) and sprite.get(LedSpriteProperty.Y) == value.get(LedSpriteProperty.Y):
            game.set_score(my_score)
            basic.show_number(my_score)
            game.game_over()
            

#Ejects bullet when both buttons A and B are pressed simultaneouslys
def on_button_pressed_ab():
    global bullet_speed
    
    bullet_speed = 1
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.slide),
        SoundExpressionPlayMode.UNTIL_DONE)
        
input.on_button_pressed(Button.AB, on_button_pressed_ab)


#Shifting x coordinate of sprite and bullet by 1 to the right when Button A is pressed
def on_button_pressed_b():
    sprite.change(LedSpriteProperty.X, 1)
    bullet.change(LedSpriteProperty.X, 1)
    
input.on_button_pressed(Button.B, on_button_pressed_b)


#Checks collision between bullet and any enemy. If there is collision, score is incremented.
def bullet_collision():
    global my_score, index2
    while index2 <= len(list_of_enemies) - 1:
        if bullet.get(LedSpriteProperty.X) == list_of_enemies[index2].get(LedSpriteProperty.X) and bullet.get(LedSpriteProperty.Y) == list_of_enemies[index2].get(LedSpriteProperty.Y):
            list_of_enemies[index2].delete()
            list_of_enemies.remove_at(index2)
            my_score += 1
        index2 += 1


#Moves the enemies down every second
def move_enemies():
    for value2 in list_of_enemies:
        value2.change(LedSpriteProperty.Y, enemy_speed)
        
loops.every_interval(1000, move_enemies)


#Spawns new enemies every 2.5 seconds
def spawn_enemies():
    list_of_enemies.append(game.create_sprite(randint(0, 4), -1))
    
loops.every_interval(2500, spawn_enemies)


#forever loop
def on_forever():
    game_over_check()
    bullet_collision()
    enemy_ground_collision()
    if bullet.get(LedSpriteProperty.Y) > 0:
        bullet.change(LedSpriteProperty.Y, 0 - bullet_speed)
    basic.pause(100)
    check_bullet_boundaries()
    
basic.forever(on_forever)


#Music to play in the background
def on_in_background():
    music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
        
control.in_background(on_in_background)


### --------- END --------- ###
