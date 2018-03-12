from chess import Board
import speaker,listener

class Player(object):
    def __init__(self,mode,suggestions):
        self.board = Board.Board()
        self.end_of_game = 0
        self.suggestions = suggestions
        self.mode = int(mode)

        if self.mode == 1:
            self.start_single_player()
        if self.mode == 2:
            self.start_two_player()          

    def get_user_input(self):
        data = ''
        try:
            while len(data) != 2 and not 'exit' in data:
                speaker.speak('Which piece would you like to move?')
                data = listener.listen()
                from_x_pos,from_y_pos = self.board.convert_to_coordinates(data)

            data = ''
            if self.suggestions:
                suggestions = self.board.get_piece((from_x_pos,from_y_pos)).get_moves()
                if len(suggestions) > 0:
                    speaker.speak('Suggested moves: ')
                    for pos in self.board.convert_to_position(suggestions):
                        speaker.speak(str(pos))
                else:
                    return False
                
            while len(data) != 2 and not 'exit' in data:
                speaker.speak('Where would you like to move it?')
                data = listener.listen()
                to_x_pos,to_y_pos= self.board.convert_to_coordinates(data)
            return (from_x_pos,from_y_pos,to_x_pos,to_y_pos)
            
        except AttributeError:
            return False
        
    def start_two_player(self):
        try:
            speaker.speak('What is the name of player playing white pieces: ')
            white_player = listener.listen()
            speaker.speak('What is the name of player playing black pieces: ')
            black_player = listener.listen()

            while self.end_of_game == 0:
                
                if self.board.current_player == 'w':
                    self.board.display_board(white_player)
                else:
                    self.board.display_board(black_player)

                get = True
                while get:
                    try:
                        (from_x_pos,from_y_pos,to_x_pos,to_y_pos) = self.get_user_input()
                        get = False
                    except KeyboardInterrupt:
                        self.end_of_game = 1
                    except:
                        get = True

                piece_to_move = self.board.get_piece((from_x_pos,from_y_pos))
                if piece_to_move is not None and self.board.make_move(piece_to_move,to_x_pos,to_y_pos):
                    if self.board.is_checkmate() or self.board.is_draw:
                        self.end_of_game = 1
                else:
                    speaker.speak('Invalid Move')

            if self.board.is_draw:
                speaker.speak('Game drawn due to stalemate')

            else:
                if self.board.opponent_player == 'w':
                    speaker.speak(white_player+' wins!!!')
                else:
                    speaker.speak(black_player+' wins!!!')

        except KeyboardInterrupt:
            if self.board.opponent_player == 'w':
                speaker.speak(white_player+' wins!!!')
            else:
                speaker.speak(black_player+' wins!!!')

    def start_single_player(self):
        try:
            get_color = True
            while get_color:
                speaker.speak('Which side do you want to play?')
                color_of_player = listener.listen()
                if 'white' in color_of_player:
                    speaker.speak('What is your name?')
                    white_player = listener.listen()
                    get_color = False
                elif 'black' in color_of_player:
                    speaker.speak('Enter the player name: ')
                    black_player = listener.listen()
                    get_color = False

            while self.end_of_game == 0:
                try:
                    if self.board.current_player == 'w':
                        self.board.display_board(white_player)
                    else:
                        self.board.display_board(black_player)
                    get = True
                    while get:
                        try:
                            (from_x_pos,from_y_pos,to_x_pos,to_y_pos) = self.get_user_input()
                            get = False
                        except KeyboardInterrupt:
                            self.end_of_game = 1
                        except:
                            get = True

                    piece_to_move = self.board.get_piece((from_x_pos,from_y_pos))
                    made_move = self.board.make_move(piece_to_move,to_x_pos,to_y_pos)
                    if piece_to_move is not None and made_move:
                        speaker.speak('Moved '+made_move.name+' to '+self.board.convert_to_position([(made_move.x_pos,made_move.y_pos)])[0])
                    else:
                        speaker.speak('Invalid Move')
                except:
                    moved_piece = self.board.choose_best_move()
                    if moved_piece is not None:
                        speaker.speak('Moved '+moved_piece.name+' to '+self.board.convert_to_position([(moved_piece.x_pos,moved_piece.y_pos)])[0])

                if self.board.is_checkmate() or self.board.is_draw:
                    self.end_of_game = 1

            if self.board.is_draw:
                speaker.speak('Game drawn due to stalemate')

            else:
                if self.board.opponent_player == 'w':
                    speaker.speak(white_player+' wins!!!')
                else:
                    speaker.speak(black_player+' wins!!!')

        except KeyboardInterrupt:
            if self.board.opponent_player == 'w':
                speaker.speak(white_player+' wins!!!')
            else:
                speaker.speak(black_player+' wins!!!')
            
def start_play():
    get_choice = True
    while get_choice:
        speaker.speak('Hi!! Would you like to play in Single player mode or two player mode?')
        data = listener.listen()
        if 'single' in data:
            choice = 1
        if 'two' in data:
            choice = 2
        
        speaker.speak('Would you like to get move suggestions?')
        data = listener.listen()

        if choice in [1,2]:
            if 'yes' in data:
                Player(choice,True)
            else:
                Player(choice,False)

            speaker.speak('Would you like to play a new game?')
            data = listener.listen()
            if 'no' in data:
                get_choice = False
        else:
            speaker.speak('Invalid choice')
