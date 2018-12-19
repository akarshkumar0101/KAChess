import java.util.ArrayList;

public class Chessboard {
	// FIXME things like checkmate, stalemate, and promotion
	
	/**
	 * positive is white
	 * negative is black
	 * 
	 * 1 -- pawn
	 * 2 -- rook
	 * 3 -- knight
	 * 4 -- bishop
	 * 5 -- queen
	 * 6 -- king
	 * 0 -- empty square
	 * 
	 * {{-2, -3, -4, -5, -6, -4, -3, -2}
	 * 	{-1, -1, -1, -1, -1, -1, -1, -1}
	 * 	{ 0,  0,  0,  0,  0,  0,  0,  0}
	 * 	{ 0,  0,  0,  0,  0,  0,  0,  0}
	 * 	{ 0,  0,  0,  0,  0,  0,  0,  0}
	 * 	{ 0,  0,  0,  0,  0,  0,  0,  0}
	 * 	{ 1,  1,  1,  1,  1,  1,  1,  1}
	 *  { 2,  3,  4,  5,  6,  4,  3,  2}
	 */
	
	int[][] board;
	int[] canEnPassant; //{row, col, resetNextTurn} if no row/col, set to -1. reset on 1, don't on 0
	boolean whiteToMove;
	boolean[] canCastle; // {whiteKingside, whiteQueenside, blackKingside, blackQueenside}
	
	// constructors //////////////////////////////////
	
	public Chessboard() {
		setUpBoard();
	}
	public Chessboard(boolean a) {
		setUpBoard();
		whiteToMove = a;
	}
	public Chessboard(int[][] b, boolean a) {
		setUpBoard();
		board = b;
		whiteToMove = a;
	}
	
	// public methods //////////////////////////////////
	
	public int[][] getBoard(){
		Chessboard output =  new Chessboard();
		output.copyBoard(this);
		return output.board;
	}
	public boolean kingInDanger(boolean currentTurn) {
		// if currentTurn is true, returns if the king is in danger for player whose turn it is
		// if currentTurn is false, returns if the king is in danger for player whose turn it is not
		int sign = 0;
		int kingRow = -1;
		int kingCol = -1;
		
		if((currentTurn && whiteToMove) || (!currentTurn && !whiteToMove)) {
			sign = 1;
		}else {
			sign = -1;
		}
		
		// find king
		for(int row = 0; row < 8; row++) {
			for(int col = 0; col < 8; col++) {
				if(board[row][col] == sign * 6) {
					kingRow = row;
					kingCol = col;
				}
			}
		}
		
		if(kingRow == -1 || kingCol == -1) {
			// this should be an exception?
			return false;
		}
		
		// check enemy knights
		for(int row = -2; row <= 2; row++) {
			for(int col = -2; col <= 2; col++) {
				if(!outOfBounds(kingRow + row, kingCol + col) && Math.abs(row*col) == 2) {
					if(board[kingRow + row][kingCol + col] == sign * -3) {
						return true;
					}
				}
			}
		}
		
		//check for danger by enemy king
		for(int row = -1; row <= 1; row++) {
			for(int col = -1; col <= 1; col++) {
				if(!outOfBounds(kingRow + row, kingCol + col)) {
					if(board[kingRow + row][kingCol + col] == sign * -6) {
						return true;
					}
				}
			}
		}
		
		// check up and down
		for(int row = 1; row < 7; row++) {
			if(!outOfBounds(kingRow + row, kingCol)) {
				int tempPiece =  board[kingRow + row][kingCol];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		
		for(int row = 1; row < 7; row++) {
			if(!outOfBounds(kingRow - row, kingCol)) {
				int tempPiece =  board[kingRow - row][kingCol];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		
		// check left and right
		for(int col = 1; col < 7; col++) {
			if(!outOfBounds(kingRow, kingCol + col)) {
				int tempPiece =  board[kingRow][kingCol + col];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		
		for(int col = 1; col < 7; col++) {
			if(!outOfBounds(kingRow, kingCol - col)) {
				int tempPiece =  board[kingRow][kingCol - col];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		
		// check down-right
		for(int i = 1; i < 7; i++) {
			if(!outOfBounds(kingRow + i, kingCol + i)) {
				int tempPiece =  board[kingRow + i][kingCol + i];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		// check up-left
		for(int i = 1; i < 7; i++) {
			if(!outOfBounds(kingRow - i, kingCol - i)) {
				int tempPiece =  board[kingRow - i][kingCol - i];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		// check down-left
		for(int i = 1; i < 7; i++) {
			if(!outOfBounds(kingRow + i, kingCol - i)) {
				int tempPiece =  board[kingRow + i][kingCol - i];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		// check up-right
		for(int i = 1; i < 7; i++) {
			if(!outOfBounds(kingRow - i, kingCol + i)) {
				int tempPiece =  board[kingRow - i][kingCol + i];
				if(tempPiece == sign * -5 || tempPiece == sign * -2) {
					return true;
				}else if(tempPiece * sign > 0) {
					break;
				}
			}else {
				break;
			}
		}
		
		return false; 
	}
	public boolean kingInDanger(Chessboard b, boolean currentTurn) {
		return b.kingInDanger(currentTurn); // returns true if king is in danger on board b for specified turn
	}
	public boolean move(int startRow, int startCol, int endRow, int endCol) {
		
		// if valid move
		if(checkMove(startRow, startCol, endRow, endCol)) {
			movePiece(startRow, startCol, endRow, endCol);
			return true;
		}
		
		return false;
	}
	public String toString() {
		String output = "________________________________________________\n";
		for(int row=0; row<8; row++) {
			output += "|     |     |     |     |     |     |     |     |\n";
			for(int col=0; col<8; col++) {
				if(board[row][col] == 0) {
					output+="|     ";
				}else {
					if(board[row][col] < 0) {
						output += "| ";
					}else {
						output += "|  ";
					}
					output+=board[row][col] + "  ";
				}
			}
			output +="|\n";
			output += "|_____|_____|_____|_____|_____|_____|_____|_____|\n";
		}
		return output;
	}
	public Chessboard clone() {
		Chessboard output = new Chessboard();
		
		output.whiteToMove = this.whiteToMove;
		
		for(int i=0; i < 3; i++) {
			output.canEnPassant[i] = this.canEnPassant[i];
		}
		
		output.copyBoard(this);
		
		return output;
	}
	/**
	 * This function returns a list of all possible moves for the piece at the given square.
	 * Does take turn into account
	 * 
	 * @param row the current row of piece
	 * @param col the current column of piece
	 * @return List of int[] containing the endRow and endCol of each possible move
	 */
	public ArrayList<int[]> getMoves(int row, int col){
		int piece = board[row][col];
		
		switch (piece) {
			case 1:
			case -1:
				return getMovesPawn(row, col);
			case 2:
			case -2:
				return getMovesRook(row, col);
			case 3:
			case -3:
				return getMovesKnight(row, col);
			case 4:
			case -4:
				return getMovesBishop(row, col);
			case 5:
			case -5:
				return getMovesQueen(row, col);
			case 6:
			case -6:
				return getMovesKing(row, col);
			default:
				return new ArrayList<int[]>();
		}
	}
	
	public ArrayList<int[]> getAllMoves(boolean CurrentTurn){
		// TODO implement
		// TODO change get moves method to return array list of int arrays
		// of the form {startRow, startCol, endRow, endCol}
		return new ArrayList<int[]>();
	}
	// private methods //////////////////////////////////
	
	private void castle(String color, String dir) {
		if(color.equals("white")) {
			canCastle[0] = false;
			canCastle[1] = false;
			if(dir.equals("kingside")){
				board[7][7] = 0;
				board[7][5] = 2;
			}else {
				board[7][0] = 0;
				board[7][3] = 2;
			}
		}else {
			canCastle[2] = false;
			canCastle[3] = false;
			if(dir.equals("kingside")){
				board[0][7] = 0;
				board[0][5] = -2;
			}else {
				board[0][0] = 0;
				board[0][3] = -2;
			}
		}
	}
	private void enPassant(int row, int col) {
		board[row][col] = 0;
	}
	private void movePiece(int startRow, int startCol, int endRow, int endCol) { // TODO check movePiece
		
		// reset enPassant if reset flag is set
		if(canEnPassant[2] != 0) {
			canEnPassant = getNewEnPassant();
		}
		
		canEnPassant[2] = 1; // reset next move
		
		int piece = board[startRow][startCol];
		
		if(piece == 6 && endRow == 7 && startRow == 7 && startCol == 4 && endCol == 7 && board[7][7] == 2) {
			castle("white", "kingside");
		}else if(piece == -6 && endRow == 0 && startRow == 0 && startCol == 4 && endCol == 7 && board[0][7] == -2) {
			castle("black", "kingside");
		}else if(piece == 6 && endRow == 7 && startRow == 7 && startCol == 4 && endCol == 2 && board[7][0] == 2) {
			castle("white", "Queenside");
		}else if(piece == -6 && endRow == 0 && startRow == 0 && startCol == 4 && endCol == 2 && board[0][0] == -2) {
			castle("black", "Queenside");
		}else if(piece > 0 && !outOfBounds(endRow + 1, endCol) && isEnemySquare(piece, endRow + 1, endCol) && canEnPassant[0] == endRow + 1 && canEnPassant[1] == endCol) {
			enPassant(endRow + 1, endCol);
		}else if(piece < 0 && !outOfBounds(endRow - 1, endCol) && isEnemySquare(piece, endRow - 1, endCol) && canEnPassant[0] == endRow - 1 && canEnPassant[1] == endCol) {
			enPassant(endRow - 1, endCol);
		}
		
		
		board[startRow][startCol] = 0; // move piece
		board[endRow][endCol] = piece;
		whiteToMove = !whiteToMove;
	}
	private Chessboard movePieceNoCheck(int startRow, int startCol, int endRow, int endCol) {
		Chessboard output = this.clone(); // clone is redundant but for safety
		output.movePiece(startRow, startCol, endRow, endCol);
		return output;
	}
	private boolean checkMove(int startRow, int startCol, int endRow, int endCol) {
		
		int piece = board[startRow][startCol];
		
		// if incorrect turn
		if((piece < 0 && whiteToMove) || (piece > 0 && !whiteToMove)) {
			return false;
		}
		
		// if starting or ending squares are out of bounds
		if(outOfBounds(startRow, startCol) || outOfBounds(endRow, endCol)) {
			return false;
		}
		
		// if starting and ending squares are the same
		if(startRow == endRow && startCol == endCol) {
			return false;
		}
		
		// if ending square is occupied by friendly piece
		if(piece*board[endRow][endCol] > 0) {
			return false;
		}
		
		// if king is in danger after move is completed
		Chessboard turnComplete = this.clone().movePieceNoCheck(startRow, startCol, endRow, endCol); 
		if(kingInDanger(turnComplete, false)) {
			return false;
		}

		switch (piece) {
			case 1:
			case -1:
				return checkMovePawn(startRow, startCol, endRow, endCol);
			case 2:
			case -2:
				return checkMoveRook(startRow, startCol, endRow, endCol);
			case 3:
			case -3:
				return checkMoveKnight(startRow, startCol, endRow, endCol);
			case 4:
			case -4:
				return checkMoveBishop(startRow, startCol, endRow, endCol);
			case 5:
			case -5:
				return checkMoveQueen(startRow, startCol, endRow, endCol);
			case 6:
			case -6:
				return checkMoveKing(startRow, startCol, endRow, endCol);
			default:
				return false;
		}
	}
	private boolean checkMoveBishop(int startRow, int startCol, int endRow, int endCol) {
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
		
		// if not moving diagonally
		if(Math.abs(rowDiff) != Math.abs(colDiff)) {
			return false;
		}
		
		return isEmptyBetween(startRow, startCol, endRow, endCol);
	}
	private boolean checkMoveKing(int startRow, int startCol, int endRow, int endCol) {
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
		int piece = board[startCol][endCol];
		
		if(Math.abs(rowDiff) <= 1 && Math.abs(colDiff) <= 1) {
			if(piece > 0) {
				canCastle[0] = false;
				canCastle[1] = false;
			}else {
				canCastle[2] = false;
				canCastle[3] = false;
			}
			return true;
		}
		
		// castling
		if(!kingInDanger(true) && startCol == 4 && rowDiff == 0) {
			// castling kingside
			if(endCol == 6 && isEmptyBetween(startRow, startCol, endRow, 7) && isSafeBetween(startRow, startCol, endRow, 7)) {
				if(piece > 0 && canCastle[0] && board[7][7] == 2) {
					canCastle[0] = false;
					canCastle[1] = false;
					return true;
				}else if(piece < 0 && canCastle[2] && board[0][7] == -2) {
					canCastle[0] = false;
					canCastle[1] = false;
					return true;
				}
			// castling queenSide
			}else if(endCol == 2 && isEmptyBetween(startRow, startCol, endRow, 0) && isSafeBetween(startRow, startCol, endRow, 0)) {
				if(piece > 0 && canCastle[1] && board[7][0] == 2) {
					canCastle[2] = false;
					canCastle[3] = false;
					return true;
				}else if(piece < 0 && canCastle[3] && board[0][0] == -2) {
					canCastle[2] = false;
					canCastle[3] = false;
					return true;
				}
			}
		}
		
		return false;
	}
	private boolean checkMoveKnight(int startRow, int startCol, int endRow, int endCol) {
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
	
		return Math.abs(rowDiff*colDiff) == 2;
	}
	private boolean checkMovePawn(int startRow, int startCol, int endRow, int endCol) {
		
		int piece = board[startRow][startCol];
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
		
		
		if(colDiff == 0 && isEmptySquare(endRow, endCol)) {
			
			// if moving forward one square
			if(movingForwardOne(piece, rowDiff)) {
				return true;
			}
			
			// moving forward two squares
			if(piece < 0 && startRow == 1 && endRow == 3 && isEmptySquare(2, startCol) && isEmptySquare(3, startCol)) { // black piece
				setEnPassant(endRow, endCol, 0);
				return true;
			}else if(piece > 0 && startRow == 6 && endRow == 4 && isEmptySquare(5, endCol) && isEmptySquare(4, startCol)) {
				setEnPassant(endRow, endCol, 0);
				return true;
			}
			
		}else if(Math.abs(colDiff) == 1 && movingForwardOne(piece, rowDiff)) { // moving diagonally
			
			// if capturing diagonally forward
			if(isEnemySquare(piece, endRow, endCol)) {
				return true;
			}
			
			// enPassanting into an enemy square is not possible
			if(piece > 0 && isEnemySquare(piece, endRow + 1, endCol) && canEnPassant[0] == endRow + 1 && canEnPassant[1] == endCol) {
				enPassant(endRow + 1, endCol);
				return true;
			}else if(piece < 0 && isEnemySquare(piece, endRow - 1, endCol) && canEnPassant[0] == endRow - 1 && canEnPassant[1] == endCol) {
				enPassant(endRow - 1, endCol);
				return true;
			}
		}
		return false;
	}
	private boolean checkMoveQueen(int startRow, int startCol, int endRow, int endCol) {
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
		
		// if not moving diagonally or in a straight line 
		if(Math.abs(rowDiff) != Math.abs(colDiff) && rowDiff * colDiff != 0) {
			return false;
		}
		
		return isEmptyBetween(startRow, startCol, endRow, endCol);
	}
	private boolean checkMoveRook(int startRow, int startCol, int endRow, int endCol) {
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
		
		// if not moving in a straight line
		if(rowDiff * colDiff != 0) {
			return false;
		}
		
		if(isEmptyBetween(startRow, startCol, endRow, endCol)) {
			if(startRow == 7) {
				if(startCol == 0) {
					canCastle[1] = false;
				}else if(startCol == 7) {
					canCastle[0] = false;
				}
			}else if(startRow == 0) {
				if(startCol == 0) {
					canCastle[3] = false;
				}else if(startCol == 7) {
					canCastle[2] = false;
				}
			}
			return true;
		}
		return false;
		
	}
	private ArrayList<int[]> getMovesBishop(int row, int col){
		ArrayList<int[]> output = new ArrayList<int[]>(14);
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(row + i, col + i)) {
				if(checkMove(row, col, row + i, col + i)) {
					int[] temp = new int[2];
					temp[0] = row + i;
					temp[1] = col + i;
					output.add(temp);
				}
			}
		}
		
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(row + i, col - i)) {
				if(checkMove(row, col, row + i, col - i)) {
					int[] temp = new int[2];
					temp[0] = row + i;
					temp[1] = col - i;
					output.add(temp);
				}
			}
		}
		
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(row - i, col + i)) {
				if(checkMove(row, col, row - i, col + i)) {
					int[] temp = new int[2];
					temp[0] = row - i;
					temp[1] = col + i;
					output.add(temp);
				}
			}
		}
		
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(row - i, col - i)) {
				if(checkMove(row, col, row - i, col - i)) {
					int[] temp = new int[2];
					temp[0] = row - i;
					temp[1] = col - i;
					output.add(temp);
				}
			}
		}
		// TODO make bishop get moves more efficient
		return output;
	}
	private ArrayList<int[]> getMovesKing(int kingRow, int kingCol){
		ArrayList<int[]> output = new ArrayList<int[]>(10);
		
		for(int row = -1; row <= 1; row++) {
			for(int col = -1; col <= 1; col++) {
				if(!outOfBounds(kingRow + row, kingCol + col)) {
					if(checkMove(kingRow, kingCol, kingRow + row, kingCol + col)) {
						int[] temp = new int[2];
						temp[0] = kingRow + row;
						temp[1] = kingCol + col;
						output.add(temp);
					}
				}
			}
		}
		
		return output;
	}
	private ArrayList<int[]> getMovesKnight(int knightRow, int knightCol){
		ArrayList<int[]> output = new ArrayList<int[]>(8);
		
		for(int row = -2; row <= 2; row++) {
			for(int col = -2; col <= 2; col++) {
				if(!outOfBounds(knightRow + row, knightCol + col) && Math.abs(row*col) == 2) {
					if(checkMove(knightRow, knightCol, knightRow + row, knightCol + col)) {
						int[] temp = new int[2];
						temp[0] = knightRow + row;
						temp[1] = knightCol + col;
						output.add(temp);
					}
				}
			}
		}
		
		return output;
	}
	private ArrayList<int[]> getMovesPawn(int row, int col){
		ArrayList<int[]> output = new ArrayList<int[]>(4);
		
		if(!outOfBounds(row, col)) {
			if(board[row][col] > 0) {
				if(checkMove(row, col, row -1, col)) {
					int[] temp = new int[2];
					temp[0] = row - 1;
					temp[1] = col;
					output.add(temp);
				}
				if(checkMove(row, col, row -1, col + 1)) {
					int[] temp = new int[2];
					temp[0] = row - 1;
					temp[1] = col + 1;
					output.add(temp);
				}
				if(checkMove(row, col, row -1, col - 1)) {
					int[] temp = new int[2];
					temp[0] = row - 1;
					temp[1] = col - 1;
					output.add(temp);
				}if(checkMove(row, col, row -2, col)) {
					int[] temp = new int[2];
					temp[0] = row - 2;
					temp[1] = col;
					output.add(temp);
				}
			}else {
				if(checkMove(row, col, row + 1, col)) {
					int[] temp = new int[2];
					temp[0] = row + 1;
					temp[1] = col;
					output.add(temp);
				}
				if(checkMove(row, col, row + 1, col + 1)) {
					int[] temp = new int[2];
					temp[0] = row + 1;
					temp[1] = col + 1;
					output.add(temp);
				}
				if(checkMove(row, col, row + 1, col - 1)) {
					int[] temp = new int[2];
					temp[0] = row + 1;
					temp[1] = col - 1;
					output.add(temp);
				}if(checkMove(row, col, row + 2, col)) {
					int[] temp = new int[2];
					temp[0] = row + 2;
					temp[1] = col;
					output.add(temp);
				}
			}
		}
		
		return output;
	}
	private ArrayList<int[]> getMovesQueen(int queenRow, int queenCol){
		ArrayList<int[]> output = new ArrayList<int[]>(14);
		
		for(int row = 0; row < 8; row++) {
			if(checkMove(queenRow, queenCol, row, queenCol)) {
				int[] temp = new int[2];
				temp[0] = row;
				temp[1] = queenCol;
				output.add(temp);
			}
		}
		
		for(int col = 0; col < 8; col++) {
			if(checkMove(queenRow, queenCol, queenRow, col)) {
				int[] temp = new int[2];
				temp[0] = queenRow;
				temp[1] = col;
				output.add(temp);
			}
		}
		
		// TODO make queen moves more efficient
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(queenRow + i, queenCol + i)) {
				if(checkMove(queenRow, queenCol, queenRow + i, queenCol + i)) {
					int[] temp = new int[2];
					temp[0] = queenRow + i;
					temp[1] = queenCol + i;
					output.add(temp);
				}
			}
		}
		
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(queenRow + i, queenCol - i)) {
				if(checkMove(queenRow, queenCol, queenRow + i, queenCol - i)) {
					int[] temp = new int[2];
					temp[0] = queenRow + i;
					temp[1] = queenCol - i;
					output.add(temp);
				}
			}
		}
		
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(queenRow - i, queenCol + i)) {
				if(checkMove(queenRow, queenCol, queenRow - i, queenCol + i)) {
					int[] temp = new int[2];
					temp[0] = queenRow - i;
					temp[1] = queenCol + i;
					output.add(temp);
				}
			}
		}
		
		for(int i=0; i < 8; i++) {
			if(!outOfBounds(queenRow - i, queenCol - i)) {
				if(checkMove(queenRow, queenCol, queenRow - i, queenCol - i)) {
					int[] temp = new int[2];
					temp[0] = queenRow - i;
					temp[1] = queenCol - i;
					output.add(temp);
				}
			}
		}
		
		return output;
	}
	private ArrayList<int[]> getMovesRook(int rookRow, int rookCol){
		ArrayList<int[]> output = new ArrayList<int[]>(14);
		
		for(int row = 0; row < 8; row++) {
			if(checkMove(rookRow, rookCol, row, rookCol)) {
				int[] temp = new int[2];
				temp[0] = row;
				temp[1] = rookCol;
				output.add(temp);
			}
		}
		
		for(int col = 0; col < 8; col++) {
			if(checkMove(rookRow, rookCol, rookRow, col)) {
				int[] temp = new int[2];
				temp[0] = rookRow;
				temp[1] = col;
				output.add(temp);
			}
		}
		
		return output;
	}
	private boolean isEmptySquare(int row, int col) {
		return (board[row][col] == 0);
	}
	private boolean isEmptyBetween(int startRow, int startCol, int endRow, int endCol) { // TODO check isEmptyBetween
		// checks if the squares STRICTLY BETWEEN the starting and ending squares are empty
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;
		
		// if not moving diagonally or vertically or horizontally
		if(Math.abs(rowDiff) != Math.abs(colDiff) && rowDiff * colDiff != 0) {
			return false;
		}
		
		// ensure that startRow <= endRow (problem is symmetric, so this is valid)
		
		if(rowDiff < 0) {
			return isEmptyBetween(endRow, endCol, startRow, startCol);
		}
		
		// actually check if empty between
		if(rowDiff == colDiff) {
			for(int i=1; i < rowDiff; i++) {
				if(!isEmptySquare(startRow + i, startCol + i)) {
					return false;
				}
			}
		}else if(rowDiff == -colDiff) {
			for(int i=1; i < rowDiff; i++) {
				if(!isEmptySquare(startRow + i, startCol - i)) {
					return false;
				}
			}
		}else if(rowDiff ==0){
			for(int col = startCol+1; col < endCol; col++) {
				if(!isEmptySquare(startRow, col)) {
					return false;
				}
			}
		}else if(colDiff == 0) {
			for(int row = startRow+1; row < endRow; row++) {
				if(!isEmptySquare(row, startCol)) {
					return false;
				}
			}
		}
		
		
		return true;
	}
	private boolean isEnemySquare(int piece, int row, int col) {
		return (piece * board[row][col] < 0);
	}
	private boolean isSafeBetween(int startRow, int startCol, int endRow, int endCol) { // TODO check isSafeBetween
		// checks if the squares STRICTLY BETWEEN the starting and ending squares are safe for king to cross
		
		int rowDiff = endRow - startRow;
		int colDiff = endCol - startCol;

		if(Math.abs(rowDiff) != Math.abs(colDiff) && rowDiff * colDiff != 0) {
			return false;
		}
		
		// ensure that startCol <= endCol and startRow <= endRow (problem is symmetric, so this is valid)
		if(colDiff < 0) {
			return isSafeBetween(startRow, endCol, endRow, startCol);
		}
		if(rowDiff < 0) {
			return isSafeBetween(endRow, startCol, startRow, endCol);
		}
		
		Chessboard copy = this.clone();

		// actually check if safe between
		boolean tempTurn = false;
		if(rowDiff == colDiff) {
			for(int i=1; i < rowDiff; i++) {
				copy = copy.movePieceNoCheck(startRow + i - 1, startCol + i - 1, startRow + i, startCol + i);
				
				if(kingInDanger(copy, tempTurn)) {
					return false;
				}
				tempTurn = !tempTurn;
			}
		}else if(rowDiff ==0){
			for(int col = startCol+1; col < endCol; col++) {
				copy = copy.movePieceNoCheck(startRow, col - 1, startRow, col);
				if(kingInDanger(copy, tempTurn)) {
					return false;
				}
				tempTurn = !tempTurn;
			}
		}else if(colDiff == 0) {
			for(int row = startRow+1; row < endRow; row++) {
				copy = copy.movePieceNoCheck(row - 1, startCol, row, startCol);
				if(kingInDanger(copy, tempTurn)) {
					return false;
				}
				tempTurn = !tempTurn;
			}
		}
		
		return true;
	}
	private boolean outOfBounds(int row, int col) {
		// makes sure a is a valid row or column
		return (row < 0 || row > 7 || col < 0 || col > 7);
	}
	private boolean movingForwardOne(int piece, int rowDiff) {
		return (rowDiff * piece < 0 && Math.abs(rowDiff) == 1);
	}
	private void setUpBoard() {
		board = getNewBoard();
		canEnPassant = getNewEnPassant();
		whiteToMove = true;
		canCastle = new boolean[4];
		for(int i=0; i<4; i++) {
			canCastle[i] = true;
		}
	}
	private int[][] getNewBoard() {
		int[][] output = 
			{{-2, -3, -4, -5, -6, -4, -3, -2},
			 {-1, -1, -1, -1, -1, -1, -1, -1},
			 { 0,  0,  0,  0,  0,  0,  0,  0},
			 { 0,  0,  0,  0,  0,  0,  0,  0},
			 { 0,  0,  0,  0,  0,  0,  0,  0},
			 { 0,  0,  0,  0,  0,  0,  0,  0},
			 { 1,  1,  1,  1,  1,  1,  1,  1},
			 { 2,  3,  4,  5,  6,  4,  3,  2}};
		
		return output;
	}
	private void copyBoard(Chessboard from) {
		for(int row=0; row<8; row++) {
			for(int col=0; col<8; col++) {
				this.board[row][col] = from.board[row][col];
			}
		}
	}
	private int[] getNewEnPassant(){
		int[] output = {-1,-1,0};
		return output;
	}
	private void setEnPassant(int row, int col, int reset) {
		canEnPassant[0] = row;
		canEnPassant[1] = col;
		canEnPassant[2] = reset;
	}
}