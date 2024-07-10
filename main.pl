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

generate_constraints(Vars, Operators) :-
    Vars ins 0..9,
    all_distinct(Vars).
    % supported_ops(Operators),
    % last_operator(Operators, #=),
    % generate_expression(Vars, Operators)

% list_to_expr/2 - Convertit une liste de variables en une expression numérique
list_to_expr(List, Expr) :-
    list_to_expr(List, 0, Expr).

% list_to_expr/3 - Prédicat auxiliaire avec accumulateur
list_to_expr([], Acc, Acc).
list_to_expr([H|T], Acc, Expr) :-
    length(T, N),                % Nombre d'éléments restants dans la liste
    Term #= H * 10^N,            % Calculer le terme courant
    NewAcc #= Acc + Term,        % Ajouter le terme à l'accumulateur
    list_to_expr(T, NewAcc, Expr). % Appel récursif pour traiter le reste de la liste

% operator_expr/4 - Convertit un opérateur en une expression Prolog
operator_expr(+, Left, Right, Expr) :- Expr #= Left + Right.
operator_expr(-, Left, Right, Expr) :- Expr #= Left - Right.
operator_expr(*, Left, Right, Expr) :- Expr #= Left * Right.
operator_expr(/, Left, Right, Expr) :- Expr #= Left / Right.
operator_expr(#=, Left, Right, Expr) :- Expr #= Left.

convert_cryptarithm(Operands, Operators, Constraints) :-
    Operands = [Opn1|Ra],
    Operators = [Op|Rb],
    list_to_expr(Opn1, Expr1),
    convert_cryptarithm(Ra, Rb, Constraints1),
    operator_expr(Op, Expr1, Constraints1, Constraints).
convert_cryptarithm([Opn], [], Expr) :-
    list_to_expr(Opn, Expr).

% solve(+Puzzle, -Solution)
% ?- solve([[S,E,N,D],'+',[M,O,R,E],'#=',[M,O,N,E,Y]]).
% ?- solve([[O,N,E],'+',[O,N,E],'+',[O,N,E],'#=',[T,W,O]]).
solve(Puzzle) :-
    parse_puzzle(Puzzle, Operands, Operators),
    generate_vars(Operands, Vars),
    generate_constraints(Vars, Operators),
    convert_cryptarithm(Operands, Operators, Constraints).

% solve([[S,E,N,D],'+',[M,O,R,E],'#=',[M,O,N,E,Y]]),
% M #\= 0, S #\= 0,
% label([S,E,N,D,M,O,R,Y]).
