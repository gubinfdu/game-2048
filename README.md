This file is prepared to realize the popular game 2048. It contains most functions of this game.

Many parameters could be adjusted easily, such as size (usually 4 * 4), target (usually 2048), random number (usually 2 and 4).

After initialization, a 4 * 4 (or other size) matrix (numpy.array) will be returned.

Orders are chosen from ['w', 's', 'a', 'd', 'q'], refer to up, down, left, right and quit respectively. If the order is out of list, or the order is invalid (the matrix does not change after the move), a message will be generated to ask for another one.

After each move, the status will be checked, "win" or "lose" or "continue". If continue, a new matrix and updated score will be returned.

First define a class called game, all the functions are defined as methods of this class.

createNum(): randomly create 2 or 4 (or other numbers) at blank positions (0).

left(), right(), up(), down(): calculate the new matrix after each move.

show(): show the current matrix and score.

getInput(): get orders, and check if it is invalid.

check(): check the status of the matrix, "win" or "lose" or "continue".

main(): combine all the functions.

The core part is left(), right(), up(), down() functions. Actually these four functions are the same in essence, right() = inverse left(), up() = transpose left(), down() = inverse up(). Therefore only left() is defined, and other three functions are based on left(). The strategy contains three steps. For each row, find non-zero number; calculate the merged result; fill in the new array with the result.
