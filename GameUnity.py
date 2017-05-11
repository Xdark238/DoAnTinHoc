class Gameunity:
        board = [[0]*11]*9; 
	playerActing = 1;

        def Restart():
            board =[[0]*11]*9; 
        def getIndex(x, y):
			if (board[y][x] > 20):
				return board[y][x] - 20;
			else:
				return board[y][x] - 10;
	def isThingThere(indexX, indexY):
		if (board[indexY][indexX] != 0):
				return True;
	def getSide(board, iX, iY):
				return (int)(board[iY][iX] / 10);
	def isCheckSameSide( iX,  iY,  jX,  jY):
			return ( getSide(board, iX, iY) == getSide(board, jX, jY));
	def isCheckWayToStrike( iX, iY,  increaseX,  increaseY,  steps):
			kt = 0;
			
			for i in range(1,steps):
				if (isThingThere( iX + i * increaseX + increaseX, iY + i * increaseY + increaseY )):
                                        kt = kt + 1;
			if (kt == 0):
				return True;
			else:
				return False;
	def setValideMoveElementArray( iX, iY, increaseX,increaseY,steps, board):
			 ps = [{0,0}];
                         if (board[iY + steps * increaseY][iX + steps * increaseX] == 1):
                                if (isThingThere( iX + steps * increaseX + increaseX,iY + steps * increaseY + increaseY)== False):
                                        board[iY + steps * increaseY + increaseY][iX + steps * increaseX + increaseX] =1;
					board[iY, iX]=0;
					ps[0][0] = iY + steps * increaseY + increaseY;
					ps[1][0] = iX + steps * increaseX + increaseX;
					return ps;
        def setValidMoveLogicAdd(iX, iY, increaseX, increaseY, board):
			ps = [{0,0}];
			if (isThingThere(iX + increaseX, iY + increaseY)==True and isCheckSameSide(iX + increaseX, iY + increaseY, iX, iY)==True):
				t = getIndex(iX + increaseX, iY + increaseY);
				k = getIndex(iX, iY);
				l = (t + k) % 10;
                        if (k > 0 and l > 0 and (isThingThere(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY)==True)and (isCheckSameSide(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY, iX, iY)== False)and(isCheckWayToStrike(iX, iY, increaseX, increaseY, l)==True)):
					board[iY + increaseY + l * increaseY][iX + increaseX + l * increaseX] = 1;
					board[iY][iX] = 0;
					ps[0][0] = iY + increaseY + l * increaseY;
					ps[1][0] = iX + increaseX + l * increaseX;
					return ps;
	def setValidMoveLogicMinus(iX, iY, increaseX, increaseY, board):
			ps = [{0,0}];
			if (isThingThere(iX + increaseX, iY + increaseY) and isCheckSameSide(iX + increaseX, iY + increaseY, iX, iY)):
				 k = getIndex(iX, iY);
				 t = getIndex(iX + increaseX, iY + increaseY);
				 l = k - t;
				 if (l > 0):
					if (isThingThere(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY)and (isCheckSameSide(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY, iX, iY)==False)and(isCheckWayToStrike(iX, iY, increaseX, increaseY, l))):
						board[iY + increaseY + l * increaseY][iX + increaseX + l * increaseX] = 1;
						board[iY][iX] = 0;
						ps[0, 0] = iY + increaseY + l * increaseY;
						ps[1, 0] = iX + increaseX + l * increaseX;
						return ps;
   
	def setMovablePositionLogicDivide(iX, iY, increaseX, increaseY, board):
			ps = [{0,0}];
			if(isThingThere(iX + increaseX, iY + increaseY) and isCheckSameSide(iX + increaseX, iY + increaseY, iX, iY)):
				k = getIndex(iX, iY);
				t = getIndex(iX + increaseX, iY + increaseY);
				if ((k > t) and (t > 0)):
					l = k / t;
					if (isThingThere(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY)and (isCheckSameSide(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY, iX, iY)==False)and(isCheckWayToStrike(iX, iY, increaseX, increaseY, l))):
						board[iY + increaseY + l * increaseY][iX + increaseX + l * increaseX] = 1;
						board[iY][iX] = 0;
						ps[0, 0] = iY + increaseY + l * increaseY;
						ps[1, 0] = iX + increaseX + l * increaseX;
						return ps;
	def setValidMoveLogicMultiply(iX, iY, increaseX, increaseY, board):
			ps = [{0,0}];
			if (isThingThere(iX + increaseX, iY + increaseY) and isCheckSameSide(iX + increaseX, iY + increaseY, iX, iY)):
				k = getIndex(iX, iY);
				t = getIndex(iX + increaseX, iY + increaseY);
				l = (k * t) % 10;
				if (l > 0 and isThingThere(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY)and (isCheckSameSide(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY, iX, iY)==False)and(isCheckWayToStrike(iX, iY, increaseX, increaseY, l))):
                                        board[iY + increaseY + l * increaseY, iX + increaseX + l * increaseX] = 1;
                                        board[iY, iX] = 0;
                                        ps[0, 0] = iY + increaseY + l * increaseY;
                                        ps[1, 0] = iX + increaseX + l * increaseX;
                                        return ps;

	def setValidMoveLogicDivide(iX, iY, increaseX, increaseY, board):
			ps = [{0,0}];
			if (isThingThere(iX + increaseX, iY + increaseY) and isCheckSameSide(iX + increaseX, iY + increaseY, iX, iY)):
				k = getIndex(iX, iY);
				t = getIndex(iX + increaseX, iY + increaseY);
                                if ((k > t) and (t > 0)):
                                        l = k / t;
                                        if (isThingThere(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY)and (False== isCheckSameSide(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY, iX, iY))and (isCheckWayToStrike(iX, iY, increaseX, increaseY, l))):
                                            board[iY + increaseY + l * increaseY, iX + increaseX + l * increaseX] = 1;
                                            board[iY, iX] = 0;
                                            ps[0, 0] = iY + increaseY + l * increaseY;
                                            ps[1, 0] = iX + increaseX + l * increaseX;	
                                        return ps;
                    

	def setValidMoveLogicModulus(iX, iY, increaseX, increaseY, board):
			ps = [{0,0}];
			if (isThingThere(iX + increaseX, iY + increaseY) and isCheckSameSide(iX + increaseX, iY + increaseY, iX, iY)):
				k = getIndex(iX, iY);
				t = getIndex(iX + increaseX, iY + increaseY);
                                if ((k > t) and (t > 0)):
                                        l = k % t;
                                        if (l > 0 and isThingThere(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY)and(False==isCheckSameSide(iX + increaseX + l * increaseX, iY + increaseY + l * increaseY, iX, iY))and (isCheckWayToStrike(iX, iY, increaseX, increaseY, l))):
                                                board[iY + increaseY + l * increaseY, iX + increaseX + l * increaseX] = 1;
                                                board[iY, iX] = 0;
                                                ps[0, 0] = iY + increaseY + l * increaseY;
                                                ps[1, 0] = iX + increaseX + l * increaseX;
                                                return ps;
   
	def GetValidPositionForAChess( x, y, board):
			newboard = [[0]*11]*9;
			if (getIndex(x, y) != 0 and getIndex(x, y) != 10 and getIndex(x, y) != 20):
                                chessIndex = getIndex(x, y);
            #Check if the other player is currently in turn
                                iDirections = [[1, -1 ], [ 1, 0 ], [1, 1] , [ 0, -1 ], [0, 1 ], [-1, -1 ], [-1, 0 ], [-1, 1 ] ];

                                for  i in range(0,chessIndex):
                                        for iDir in range(0,8):
                                                newboard[setValideMoveElementArray(x, y, iDirections[iDir][0], iDirections[iDir][1], i, board)[0][0]][ setValideMoveElementArray(x, y, iDirections[iDir][0], iDirections[iDir][1], i, board)[0][1]] = 1;
                                                newboard[setValidMoveLogicAdd(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicAdd(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                newboard[setValidMoveLogicMinus(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicMinus(x, y, iDirections[iDir][0], iDirections[iDir][1],board)[0][1]] =1;
                                                newboard[setValidMoveLogicMultiply(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicMultiply(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                newboard[setValidMoveLogicDivide(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicDivide(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                newboard[setValidMoveLogicModulus(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicModulus(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                return  newboard;
	def  GetValidPositionForAChhessToStrike(x, y, board):
			newboard = [[0]*11]*9;
			if (getIndex(x, y) != 0 and getIndex(x, y) != 10 and getIndex(x, y) != 20):
                                chessIndex = getIndex(x, y);
                                                #Check if the other player is currently in turn
                                iDirections = [[1, -1 ], [ 1, 0 ], [1, 1] , [ 0, -1 ], [0, 1 ], [-1, -1 ], [-1, 0 ], [-1, 1 ] ];
                                for  i in range(0,chessIndex):
                                                for iDir in range(0,8):
                                                        newboard[setValidMoveLogicAdd(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicAdd(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                        newboard[setValidMoveLogicMinus(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicMinus(x, y, iDirections[iDir][0], iDirections[iDir][1],board)[0][1]] =1;
                                                        newboard[setValidMoveLogicMultiply(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicMultiply(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                        newboard[setValidMoveLogicDivide(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicDivide(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                        newboard[setValidMoveLogicModulus(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][0]][setValidMoveLogicModulus(x, y, iDirections[iDir][0], iDirections[iDir][1], board)[0][1]] = 1; 
                                                        return  newboard;

	def  GetNewValidBoards(board, currentPlayer):
		newBoards = [][100];
		for y in range(0,board.length()) :
				for x in range(0, board.length()):
					if (board[y, x] != 0):
						if (getSide( board, x, y) == currentPlayer):
							newBoards.append(CopyBoardsMoveChess(board, x, y));
                                                        return newBoards;
        def  CopyBoardMoveChess( board, oldX,oldY, newX, newY):
                        clonedBoard = [][100];
                        clonedBoard=copy.deepcopy(board);
                        index = board[oldY][oldX];
                        clonedBoard[oldY][oldX] = 0;
                        clonedBoard[newY][newX] = 1;
                        return clonedBoard;
	def GetWinner():
                if (board[7][4] != 20):
                    return 1;
                elif (board[1][4] != 10):
                    return 2;
                else:
			return 0;
        

        def GetWinner(board):
                if (board[7][4] != 20):
                    return 1;
                elif (board[1, 4] != 10):
                    return 2;
                else:
			return 0;
        def IsTerminal(state):
                return GetWinner(state) != 0;
        

 
    




    
