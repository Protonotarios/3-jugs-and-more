:- use_module(library(clpfd)).
:- use_rendering(sudoku).

sudoku(Rows) :-
        length(Rows, 9), maplist(same_length(Rows), Rows),
        append(Rows, Vs), Vs ins 1..9,
        maplist(all_distinct, Rows),
        transpose(Rows, Columns),
        maplist(all_distinct, Columns),
        Rows = [As,Bs,Cs,Ds,Es,Fs,Gs,Hs,Is],
        blocks(As, Bs, Cs), blocks(Ds, Es, Fs), blocks(Gs, Hs, Is).

blocks([], [], []).
blocks([N1,N2,N3|Ns1], [N4,N5,N6|Ns2], [N7,N8,N9|Ns3]) :-
        all_distinct([N1,N2,N3,N4,N5,N6,N7,N8,N9]),
        blocks(Ns1, Ns2, Ns3).

problem(1, [[_,_,_,2,_,_,_,6,3],
            [3,_,_,_,_,5,4,_,1],
            [_,_,1,_,_,3,9,8,_],
            [_,_,_,_,_,_,_,9,_],
            [_,_,_,5,3,8,_,_,_],
            [_,3,_,_,_,_,_,_,_],
            [_,2,6,3,_,_,5,_,_],
            [5,_,3,7,_,_,_,_,8],
            [4,7,_,_,_,1,_,_,_]]).

