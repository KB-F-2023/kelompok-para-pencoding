#include <iostream>
#include <math.h>

#define N 8
using namespace std;

//function that configures the array to provide starting-point

void configureRandomly(int board[][N], int* state){
    srand(time(0));
    
    //looping for column indices
	for (int i=0; i<N; i++){
		state[i] = rand()%N; //random row
		board[state[i]][i] = 1; //queen position
	}
}

//function for printing the board
void printBoard(int board[][N]){
	for(int i=0; i<N; i++){
        cout << " ";
		for (int j=0; j<N; j++) {
			cout<<board[i][j] << " ";
		}
		cout<<"\n";
	}
}

//function for printing the array 'state'
void printState(int* state){
	for (int i=0; i<N; i++) {
		cout << " " << state[i] << " ";
	}
	cout << endl;
}

//boolean function that compares 2 arrays (state1 & state2)
bool compareStates(int* state1, int* state2){
	for (int i=0; i<N; i++){
		if (state1[i] != state2[i]) {
			return false;
		}
	}
	return true;
}

//function for filling the board with the values of 'value'
void fill(int board[][N], int value){
	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			board[i][j] = value;
		}
	}
}

//fuction for calculating the value of the state
int calculateObjective(int board[][N], int* state){
	int attacking = 0; //0 queen attacking each other
	int row, col;

	/*every column i, the queen is placed at
	row state[i]*/
	for(int i=0; i<N; i++){
		row = state[i], col = i - 1;
		
		//to left
		while(col>=0 && board[row][col] != 1) {
			col--;
		}
		
		if (col>=0 && board[row][col] == 1) {
			attacking++;
		}

		//to right
		row = state[i], col = i + 1;
		while (col<N && board[row][col] != 1) {
			col++;
		}
		
		if (col<N && board[row][col]==1) {
		    attacking++;
		}

		row = state[i] - 1,
		col = i - 1;
		
		//diagonally left up
		while (col>=0 && row>=0 && board[row][col]!=1) {
			col--;
			row--;
		}
		
		if (col>=0 && row>=0 && board[row][col]==1) {
			attacking++;
		}

		row = state[i] + 1, col = i + 1;
		
		//diagonally right down
		while (col<N && row<N && board[row][col]!=1) {
			col++;
			row++;
		}
		
		if(col<N && row<N && board[row][col]==1) {
			attacking++;
		}

		row = state[i] + 1, col = i - 1;
		
		//diagonally left down
		while(col>=0 && row<N && board[row][col]!=1){
			col--;
			row++;
		}
		
		if(col>=0 && row<N && board[row][col]==1){
			attacking++;
		}

		row = state[i] - 1, 
		col = i + 1;
		
		//diagonally right up
		while(col<N && row>=0 && board[row][col]!= 1){
			col++;
			row--;
		}
		
		if(col<N && row>=0 && board[row][col]==1){
			attacking++;
		}
	}
	return (int)(attacking / 2);
}

//generates board configuration
void generateBoard(int board[][N], int* state){
	fill(board, 0);
	for(int i=0; i<N; i++){
		board[state[i]][i] = 1;
	}
}

//do a copy from state2 to state1
void copyState(int* state1, int* state2){
	for(int i=0; i<N; i++){
		state1[i] = state2[i];
	}
}

/*gets the neighbour of the current state*/
void getNeighbour(int board[][N], int* state){
	int opBoard[N][N];
	int opState[N];

	copyState(opState, state);
	generateBoard(opBoard, opState);

	//initializing the optiamal object value
	int opObjective = calculateObjective(opBoard,opState); //function calling

	int NeighbourBoard[N][N];
	int NeighbourState[N];

	copyState(NeighbourState, state);
	generateBoard(NeighbourBoard, NeighbourState);

	//looping through all possible neighbours
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			//condition for skipping current state
			if (j!=state[i]){
				NeighbourState[i] = j;
				NeighbourBoard[NeighbourState[i]][i] = 1;
				NeighbourBoard[state[i]][i] = 0;

				int temp = calculateObjective(NeighbourBoard,NeighbourState);

				if(temp <= opObjective){
				    opObjective = temp;
					copyState(opState, NeighbourState);
					generateBoard(opBoard, opState);
				}

				NeighbourBoard[NeighbourState[i]][i] = 0;
				NeighbourState[i] = state[i];
				NeighbourBoard[state[i]][i] = 1;
			}
		}
	}

	//copying the optimal board
	copyState(state, opState);
	fill(board, 0);
	generateBoard(board, state);
}


void hillClimbing(int board[][N], int* state){
	/*Declaring and initializing the neighbour board and state with
    the current board and the state as the starting point*/
	int neighbourBoard[N][N] = {};
	int neighbourState[N];

	copyState(neighbourState, state);
	generateBoard(neighbourBoard, neighbourState);

	do{
		/*Copying the neighbour board and state to the current board and
        state, since a neighbour becomes current after the jump.*/
	    copyState(state, neighbourState);
		generateBoard(board, state);

		//Getting the optimal neighbour
		getNeighbour(neighbourBoard, neighbourState);

		if(compareStates(state, neighbourState)){
			printBoard(board);
			break;
		}else if(calculateObjective(board,state) == calculateObjective(neighbourBoard, neighbourState)){
			neighbourState[rand() % N] = rand() % N;
			generateBoard(neighbourBoard, neighbourState);
		}
	} while (true);
}

int main(){
	int state[N] = {};
	int board[N][N] = {};

	//function calling
	configureRandomly(board, state);
	hillClimbing(board, state);

	return 0;
}