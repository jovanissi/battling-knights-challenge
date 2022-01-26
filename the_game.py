import directions

init_board_dict = {
    "red": [[0, 0], "LIVE", None, 1, 1],
    "blue": [[7, 0], "LIVE", None, 1, 1],
    "green": [[7, 7], "LIVE", None, 1, 1],
    "yellow": [[0, 7], "LIVE", None, 1, 1],
    "magic_staff": [[5, 2], False],
    "helmet": [[5, 5], False],
    "dagger": [[2, 5], False],
    "axe": [[2, 2], False]
}


def update_board(moves=None):

    if not moves or len(moves) < 1:  # If no moves found in instruction file
        return init_board_dict

    else:
        current_b_dict = init_board_dict
        for move in moves:  # Update the current board dictionary based on moves
            update_dict(current_b_dict, move)

    return current_b_dict


def update_dict(current_dict, move):
    knights_pos = {
        "red": current_dict["red"][0],
        "blue": current_dict["blue"][0],
        "green": current_dict["green"][0],
        "yellow": current_dict["yellow"][0],
    }

    items_pos = {
        "magic_staff": current_dict["magic_staff"][0],
        "helmet": current_dict["helmet"][0],
        "dagger": current_dict["dagger"][0],
        "axe": current_dict["axe"][0]
    }

    # Assigning appropriate names to knights
    if move[0] == "R":
        k_name = "red"
    elif move[0] == "B":
        k_name = "blue"
    elif move[0] == "G":
        k_name = "green"
    elif move[0] == "Y":
        k_name = "yellow"
    else:
        return None

    #  Initialize the moving (attacking) knight dictionary
    k_dict = {
        "knight": k_name,
        "position": current_dict[k_name][0],
        "status": current_dict[k_name][1],
        "item": current_dict[k_name][2],
        "attack": current_dict[k_name][3],
        "defence": current_dict[k_name][4]
    }

    if k_dict["status"] == "LIVE":  # Check if the moving knight is not dead
        if move[1] == 'S':
            new_pos = directions.move_down(k_dict["position"][0], k_dict["position"][1])
        elif move[1] == 'N':
            new_pos = directions.move_up(k_dict["position"][0], k_dict["position"][1])
        elif move[1] == 'E':
            new_pos = directions.move_right(k_dict["position"][0], k_dict["position"][1])
        elif move[1] == 'W':
            new_pos = directions.move_left(k_dict["position"][0], k_dict["position"][1])
        else:
            return None

        moving_the_knight(
            current_dict=current_dict,
            k_dict=k_dict,
            new_pos=new_pos,
            knights_pos=knights_pos,
            items_pos=items_pos
        )
    else:
        pass


def moving_the_knight(current_dict, k_dict, new_pos, knights_pos, items_pos):
    if 0 <= new_pos[0] <= 7 and 0 <= new_pos[1] <= 7:  # When the position is valid
        k_dict["position"] = new_pos  # Update the knights position

        item = ""
        if new_pos in items_pos.values():  # If position has item

            nbr_items_on_pos = list(items_pos.values()).count(new_pos)  # Get the number of items on position

            if nbr_items_on_pos == 1:
                key_list = list(items_pos.keys())
                val_list = list(items_pos.values())
                new_pos_index = val_list.index(new_pos)
                item = key_list[new_pos_index]

            else:  # When the position has more than one item
                items_on_pos = []
                for key in list(items_pos.keys()):
                    if items_pos[key] == new_pos:
                        items_on_pos.append(key)

                if "axe" in items_on_pos:
                    item = "axe"
                elif "magic_staff" in items_on_pos:
                    item = "magic_staff"
                elif "dagger" in items_on_pos:
                    item = "dagger"
                elif "helmet" in items_on_pos:
                    item = "helmet"

            if not k_dict["item"]:
                k_dict["item"] = item
                if item == "magic_staff":
                    k_dict["attack"] = k_dict["attack"] + 1
                    k_dict["defence"] = k_dict["defence"] + 1
                elif item == "helmet":
                    k_dict["defence"] = k_dict["defence"] + 1
                elif item == "dagger":
                    k_dict["attack"] = k_dict["attack"] + 1
                elif item == "axe":
                    k_dict["attack"] = k_dict["attack"] + 2

                current_dict[item][1] = True

        if new_pos in knights_pos.values():  # If position has knight
            key_list = list(knights_pos.keys())
            val_list = list(knights_pos.values())
            new_pos_index = val_list.index(new_pos)
            d_knight = key_list[new_pos_index]

            #  Initializing the defending knight dictionary
            d_knight_dict = {
                "knight": d_knight,
                "position": current_dict[d_knight][0],
                "status": current_dict[d_knight][1],
                "item": current_dict[d_knight][2],
                "attack": current_dict[d_knight][3],
                "defence": current_dict[d_knight][4]
            }

            if d_knight_dict["status"] == "LIVE":  # Check if the found knight is not dead
                att_val = k_dict["attack"] + 0.5
                def_val = d_knight_dict["defence"]

                if att_val > def_val:  # If the attacking knight wins
                    d_knight_dict["status"] = "DEAD"
                    d_knight_dict["attack"] = 0
                    d_knight_dict["defence"] = 0

                    if d_knight_dict["item"]:
                        current_dict[d_knight_dict["item"]] = [d_knight_dict["position"], False]

                    current_dict[d_knight_dict["knight"]] = [d_knight_dict["position"], d_knight_dict["status"], None, 0, 0]

                else:  # If the defending knight wins

                    if k_dict["item"]:
                        current_dict[k_dict["item"]] = [k_dict["position"], False]

                    k_dict["status"] = "DEAD"
                    k_dict["attack"] = 0
                    k_dict["defence"] = 0
                    k_dict["item"] = None

        current_dict[k_dict["knight"]] = [
            k_dict["position"],
            k_dict["status"],
            k_dict["item"],
            k_dict["attack"],
            k_dict["defence"]
        ]

    else:  # When knight is drowned
        if k_dict["item"] is not None:  # If knight had item, update the position of that item
            item = k_dict["item"]
            current_dict[item] = [k_dict["position"], False]

        # Update current dict and remove the knight from the game
        current_dict[k_dict["knight"]] = [None, "DROWNED", None, 0, 0]
        knights_pos[k_dict["knight"]] = None
