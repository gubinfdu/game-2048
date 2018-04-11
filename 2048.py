import numpy as np
import random

class game():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.score = 0
        self.randdata = [2, 4]
        self.data = np.zeros((row, col)).astype(int)
        
    def createNum(self):
        '''randomly create 2 or 4 at 0 position'''
        loc = []
        for i in range(self.row):
            for j in range(self.col):
                if self.data[i, j] == 0:
                    loc.append([i, j])
        pos = random.choice(loc)
        self.data[pos[0], pos[1]] = random.choice(self.randdata)
    
    def left(self):
        '''left move, for each row:
        1 find non-zero number
        2 calculate merged result
        3 fill in the new array with the result'''        
        # for each row
        for ind in range(self.row):
            row = self.data[ind]
            # find non-zero number
            l = list(row[row != 0])
            # all zeros
            if len(l) == 0:
                newrow = row
            # one non-zero number
            elif len(l) == 1:
                newrow = np.zeros_like(row)
                newrow[0] = l[0]
            # two or more non-zero numbers
            else:
                # store the result after merging
                res = []
                # for l[i+1]
                l.append(0)
                i = 0
                while i <= len(l) - 2:
                    # two adjacent numbers are equal, modify the two numbers
                    if l[i] == l[i + 1]:
                        l[i] = 2 * l[i]
                        l[i + 1] = 0
                        self.score += l[i]
                    # skip zeros after merging
                    if l[i] == 0:
                        i += 1
                        continue
                    res.append(l[i])
                    i += 1
                # save the result with same length as input row
                newrow = np.zeros_like(row)
                newrow[: len(res)] = res
            if (row == newrow).sum() != self.col:
                self.change = True
            self.data[ind] = newrow

    def right(self):
        '''right move'''
        # for each row, get inverse array, then call left()
        self.data = self.data[:, self.col-1: : -1]
        self.left()
        # change back
        self.data = self.data[:, self.col-1: : -1]
        
    def up(self):
        '''up move'''
        # get transposed data array, then call left()
        self.data = self.data.T
        self.left()
        # change back
        self.data = self.data.T
    
    def down(self):
        '''down move'''
        # first get transposed data array, then get inverse for rows,
        # finally call left()
        self.data = self.data.T
        self.data = self.data[:, self.col-1: : -1]
        self.left()
        # change back
        self.data = self.data[:, self.col-1: : -1]
        self.data = self.data.T
    
    def show(self):
        '''show the status and score'''
        print (self.data)
        print ('score: %d' % self.score)
    
    def getInput(self):
        '''get keyboard input'''
        move = input('Please enter the move (q for quit): ')
        while move not in ['w', 's', 'a', 'd', 'q']:
            move = input('The move should be chosen in wsad, enter again: ')
        return move
    
    def check(self):
        '''check the status: win, lose, continue'''
        # win
        if 32 in self.data:
            return 1
        # lose
        elif (self.data == 0).sum() == 0:
            return 0
        # continue
        else:
            return 2
    
    def main(self):
        '''main process in each step:
        1 create new number
        2 show data, score
        3 get input, move and merge, check change status
        4 check result status, win, lose, continue'''
        while True:
            # create new number
            self.createNum()
            # show data, score
            self.show()
            # initialize change status
            self.change = False
            # get input, move and merge, check change status
            # if the move is invalid, get another move
            while not self.change:
                move = self.getInput()
                if move == 'q':
                    break
                elif move == 'w':
                    self.up()
                elif move == 's':
                    self.down()
                elif move == 'a':
                    self.left()
                elif move == 'd':
                    self.right()
                if not self.change:
                    print ('The move is invalid.')

            if move == 'q':
                break
            
            # check result status, win, lose, continue
            status = self.check()
            if status == 1:
                self.show()
                print ('You win!')
                break
            elif status == 0:
                self.show()
                print ('You lose!')
                break

a = game(4, 4)   
a.main()
