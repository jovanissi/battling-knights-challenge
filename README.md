# Battling Knights

This projects contains the codes that allow the user to play the Battling Knights game.<br>

## GET STARTED

### Python
> This project was generated with [Python](https://www.python.org/downloads/) version 3.8.

It is advisable to run this project through a python 3 virtual environment

### Create virtualenv
```bash
virtualenv -p python3 venv
```

### Activate the virtualenv
```bash
source venv/bin/activate
```

### Instructions

A  *moves.txt* must be inserted into the project as an instruction file containing how the
knights will move on the board. <br>
The file should be formatted as below:

```bash
GAME-START 
<Knight>:<Direction> 
<Knight>:<Direction> 
<Knight>:<Direction> 
. 
. 
. 
GAME-END 
```

Where **Knight** stands for the knight's name which can be; **R**, **B**, **G** or **Y** for RED, BLUE, GREEN, and YELLOW
knights respectively.<br>
And **Direction** stands for directions; **N**, **S**, **E**, and **W** for North, South, East, and West which stands 
for UP, DOWN, RIGHT, and LEFT directions respectively

**Note**: In this project a sample *moves.txt* file is generated for you. You can edit it anyhow you want.

### Output

The output for the final board will be located in the *final_state.json* that is generated when the project is run.

### Running

To run the project, you go to the project's directory and run the following command

```bash
python main.py
```
