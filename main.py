from the_game import update_board
import json

moves = []
knights_names = ['R', 'B', 'G', 'Y']
allowed_moves = ['S', 'N', 'E', 'W']


def getting_moves():
    with open('moves.txt', 'r') as f:  # Reading the input file
        lines = f.readlines()

        if len(lines) < 3:  # Verify if the input file is valid
            print("Invalid input file! Please try another one")
            return None

        if lines[0] == 'GAME-START\n' and lines[len(lines)-1] == 'GAME-END\n':  # Verify if the input file is valid
            for i in range(1, len(lines)-1):
                move = lines[i].strip("\n").split(":")
                if len(move) == 2:
                    if move[0] in knights_names and move[1] in allowed_moves:
                        moves.append(move)
        else:
            print("Invalid input file! Please try another one")
            return None

        f.close()


getting_moves()

# Generating the output file
with open("final_state.json", "w") as output_file:
    json.dump(update_board(moves), output_file)
    output_file.close()
