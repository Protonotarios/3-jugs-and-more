solution(Path) :- length(Path, _), phrase(path([0-3, 0-7, 10-10]), Path).

path(State) --> { equivalent(State, [3-3, 5-7, 2-10]) }.
path(State0) --> [From-To],
        { move(State0, State), State = [_-From, _-To, _] },
        path(State).

equivalent(State1, State2) :- forall(member(X, State1), member(X, State2)).

move(State, [NewX-From, NewY-To|NewRest]) :-
    select(X-From, State, Rest),
    X \== 0,
    select(Y-To, Rest, NewRest),
    Fillable is To - Y,
    ToFill is min(X, Fillable),
    NewY is Y + ToFill,
    NewX is X - ToFill.
