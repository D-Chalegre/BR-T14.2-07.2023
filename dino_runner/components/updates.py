class Updates:
    def update_score(self, game):
        game.score+=1
        
    def update_speed(self, game):
        if game.score % 100 == 0:
            game.game_speed += 1