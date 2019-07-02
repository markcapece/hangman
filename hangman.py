from hangman.game import Game


def hangman():
    print('Welcome to Hangman')
    game = Game()

    while True:
        game.display_gamestate()
        user_guess = input('Please guess a letter.\n>')
        game.guess_letter(user_guess)

        if game.won:
            print('\nYou Win! The word is {}\n'.format(game.correct_answer))
            playagain()
            break
        elif game.lost:
            print('\nYou Lose! The word is {}\n.'.format(game.correct_answer))
            playagain()
            break


def playagain():
    resp = input('Would you like to play again or view the scoreboard? [Y/N/S]\n>')
    while True:
        if resp.upper() == 'Y':
            hangman()
            break
        elif resp.upper() == 'N':
            print('\nThanks for playing!\n')
            break
        elif resp.upper() == 'S':
            with open('hangman/scores.txt', 'r') as fp:
                score_list = fp.read()
            print(score_list)
            break
        else:
            print('Invalid input. [Y/N/S]')


if __name__ == '__main__':
    hangman()
