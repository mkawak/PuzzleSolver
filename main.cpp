#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <unordered_set>
#include "node.h"
#include "Astar.h"

using namespace std;

vector<vector<int>> defaultPuzzle = {{1, 2, 3},
                                     {4, 8, 0},
                                     {7, 6, 5}};

vector<vector<int>> goalPuzzle =    {{1, 2, 3},
                                     {4, 5, 6},
                                     {7, 8, 0}};

void printPuzzle(const vector<vector<int>> &puzzle) {
    for (const auto &row : puzzle) {
        for (const auto &val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

bool isPuzzleValid(const vector<vector<int>> &puzzle) {
    unordered_set<int> numbers;
    for (const auto &row : puzzle) {
        for (const auto &val : row) {
            if (val >= 0 && val <= 8) {
                if (numbers.find(val) == numbers.end()) {
                    numbers.insert(val);
                } else {
                    return false; // Duplicate found
                }
            } else {
                return false; // Invalid number
            }
        }
    }
    return true;
}

vector<vector<int>> getPuzzleFromInput() {
    vector<vector<int>> puzzle(3, vector<int>(3));
    bool zeroEntered = false;
    cout << "Enter your puzzle, use a zero to represent the blank." << endl;
    while (true) {
        for (int i = 0; i < 3; ++i) {
            cout << "Enter the " << (i + 1) << " row, use space or tabs between numbers." << endl;
            string input;
            getline(cin, input);
            stringstream ss(input);
            for (int j = 0; j < 3; ++j) {
                int value;
                ss >> value;
                if (value == 0) {
                    if (!zeroEntered) {
                        zeroEntered = true;
                    } else {
                        cout << "Only 1 blank (zero) is allowed. Please try again." << endl;
                        --i; // Repeat the current row input
                        break;
                    }
                }
                puzzle[i][j] = value;
            }
        }
        if (isPuzzleValid(puzzle)) {
            break;
        } else {
            cout << "Invalid puzzle, please make sure numbers 0 to 8 are entered with no duplicates. Try again." << endl;
        }
    }
    return puzzle;
}

int main() {
    int choice;
    cout << "Welcome to XXX (change this to your student ID) 8 puzzle solver. Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle." << endl;
    cin >> choice;
    cin.ignore();
    vector<vector<int>> puzzle;
    if (choice == 1) {
        puzzle = defaultPuzzle;
    } else if (choice == 2) {
        puzzle = getPuzzleFromInput();
    } else {
        cout << "Invalid choice." << endl;
        return 1;
    }

    printPuzzle(puzzle);

    cout << "Enter your choice of algorithm:" << endl;
    cout << "1- Uniform Cost Search" << endl;
    cout << "2- A* with the Misplaced Tile heuristic." << endl;
    cout << "3- A* with the Euclidean distance heuristic." << endl;
    int algorithmChoice;
    cin >> algorithmChoice;

    switch(algorithmChoice) {
        case 1:
            cout << "Uniform Cost Search" << endl;
            break;
        case 2:
            cout << "A* with the Misplaced Tile heuristic." << endl;
            //AStar(puzzle);
            break;
        case 3:
            cout << "A* with the Euclidean distance heuristic." << endl;
            break;
        default:
            cout << "Whats up with you? " << endl;
    }
    return 0;
}