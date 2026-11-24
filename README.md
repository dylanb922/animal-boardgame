# Animal Board Game

An abstract animal-themed boardgame where two players, Amethyst and Tangerine, take turns and compete to capture each other's cuttlefish piece. The game ends when a cuttlefish piece is captured.

## Game Details & Rules

* The **distance** is the number of squares a piece can move in its given direction.
* The **locomotion** is either sliding or jumping. A sliding piece can move any (nonzero) number of squares up to its distance in a straight line, but is blocked if a piece is in the way. A jumping piece must move its full number of squares in a straight line, but it cannot be blocked. It technically doesn't matter if a piece with distance 1 is sliding or jumping.
* The **direction** a piece moves is either orthogonal or diagonal (orthogonal just means vertical or horizontal). However, any diagonal-moving piece can also move 1 square orthogonally **instead of** its normal move and any orthogonal-moving piece can also move 1 square diagonally **instead of** its normal move. It technically doesn't matter if a piece with distance 1 is orthogonal or diagonal.
    * For example, an **orthogonal jumping** piece with a distance of **2** could either move 2 squares orthogonally or 1 square diagonally, but could not move 1 square orthogonally.
* If a piece moves to a square that contains an enemy piece, it captures that piece by replacing it on the square and removing the captured piece from the board.
* A piece cannot move to a square that contains a friendly piece.

### Game Pieces

| Name | Direction | Distance | Locomotion |
|---|---|---|---|
| okapi | orthogonal | 4 | sliding |
| wombat | orthogonal | 1 | jumping |
| kinkajou | diagonal | 3 | jumping |
| cuttlefish | diagonal | 2 | sliding |

### Starting Positions 

Tangerine player starts in Row 1, Amethyst player starts in Row 7. Piece order shown below:

| okapi | wombat | kinkajou | cuttlefish |  kinkajou | wombat | okapi |
|---|---|---|---|---|---|---|

## Requirements

* Python 3.8+

## Usage

* Import the included file to your project.
* Create an object of the AnimalGame class.
* Use any of the supplied methods to make moves/check the game status.

### Example

```python
game = AnimalGame()
move_result = game.make_move('c2', 'c4')
state = game.get_game_state()
```

## Acknowledgements

Skeleton code, pieces of the README, and project design provided by Oregon State University's Intro to Computer Science II (CS 162) class.
