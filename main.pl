:- use_module(library(clpfd)).

% parse_puzzle(+Puzzle, -Vars, -Operators)
parse_puzzle(Puzzle, Vars, Operators) :-
    Puzzle = [V, Op|Rest],
    Vars = [V|Vars1],
    Operators = [Op|Operators1],
    parse_puzzle(Rest, Vars1, Operators1).
parse_puzzle(Puzzle, Vars, Operators) :-
    Puzzle = [V],
    Vars = [V],
    Operators = [].

% solve(+Puzzle, -Solution)
% ?- solve([[S,E,N,D],'+',[M,O,R,E],'#=',[M,O,N,E,Y]]).
% ?- solve([[O,N,E],'+',[O,N,E],'+',[O,N,E],'#=',[T,W,O]]).
solve(Puzzle) :-
    parse_puzzle(Puzzle, Vars, Operators).
