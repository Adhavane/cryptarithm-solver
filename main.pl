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

% Flatten a list of lists and remove duplicates
generate_vars(Ops, Vars) :-
    flatten(Ops, Vars1),
    list_to_set(Vars1, Vars).
% ?- flatten([[1,2],[3,4]], Vars). % Flatten a list of lists
% ?- list_to_set([1,2,3,4,5,5,6], Vars). % Remove duplicates

% solve(+Puzzle, -Solution)
% ?- solve([[S,E,N,D],'+',[M,O,R,E],'#=',[M,O,N,E,Y]]).
% ?- solve([[O,N,E],'+',[O,N,E],'+',[O,N,E],'#=',[T,W,O]]).
solve(Puzzle) :-
    parse_puzzle(Puzzle, Operands, Operators),
    generate_vars(Operands, Vars).
