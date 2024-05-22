class Game:
    
    all = []
    
    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            return "Unable to change title"
        if isinstance(title, str) and len(title) > 0:
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        results = self.results() # utilize results()
        players = set() # initialize set for uniqueness
        for result in results:
            players.add(result.player) # add result.player to set
        unique_players = [player for player in players] # turn set back to a list
        return unique_players

    def average_score(self, player):
        results = self.results()
        total_score = 0
        total_games = []
        for results in results:
            total_score += results.score
            total_games.append(results.game)
        return total_score / len(total_games)

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        results = self.results()
        games_played = set()
        for result in results:
            games_played.add(result.game)
        unique_list = [game for game in games_played]
        return unique_list

    def played_game(self, game):
        games_played = self.games_played()
        if game in games_played:
            return True
        else:
            return False

    def num_times_played(self, game):
        games_played = [results.game for results in self.results()]
        counter = 0
        for games in games_played:
            if games == game:
                counter += 1
        return counter


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, "score"):
            return "Unable to change title"
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score


game = Game("Skribbl.io")
game_2 = Game("Scattegories")
game_3 = Game("Codenames")

player_1 = Player("Nick")
player_2 = Player("Saaammm")
Result(player_1, game, 5000)
Result(player_2, game_2, 19)
Result(player_1, game_3, 10)
