#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2017-11-17


def input_pawns(num_pawn=0, pawns=None):
    if pawns is None:
        pawns = []

    pawn_num = input("Please enter the number of pawns (0 < n <= 8):")
    if len(pawn_num) == 1:
        if pawn_num in '012345678':
            num_pawn = int(pawn_num)
        else:
            print("The n should be a num between 0 and 8")
    else:
        print("The n should be a num between 0 and 8")

    while num_pawn > 0:
        in_pawn = input(
            "Please enter a(nother) pawn position,an unique coordinate pair\nA letter and A number :")

        if len(in_pawn) == 2:
            if in_pawn[0] in 'abcdefgh':
                if in_pawn[1] in '12345678':
                    if in_pawn not in pawns:
                        pawns.append(in_pawn)
                        num_pawn = num_pawn - 1
                        print("Now the pawns is :", pawns)
                    else:
                        print("The position should be unique,pls check it")
                else:
                    print("The number should be ranged from 1 to 8")
            else:
                print("The letter should be ranged from a to h")
        else:
            print(
                "The pawn position is identified by columns and rows\nFor example, 'a1', 'h8', 'd6'")
    return pawns


def safe_pawns(pawns=None):
    if pawns is None:
        pawns = []
    alpha_table = "abcdefgh"
    safe_count = 0
    for sub in pawns:
        if sub[1] == '1':
            continue
        pos = alpha_table.find(sub[0])
        str_row = str(int(sub[1]) - 1)
        if pos == 0:
            if (alpha_table[1] + str_row) in pawns:
                safe_count += 1
            continue
        if pos == 7:
            if (alpha_table[6] + str_row) in pawns:
                safe_count += 1
            continue
        if (alpha_table[pos - 1] + str_row) in pawns or (alpha_table[pos + 1] + str_row) in pawns:
            safe_count += 1
    return safe_count


# if __name__ == '__main__':
#     print("The number of safe pawn is :", safe_pawns(input_pawns()))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
