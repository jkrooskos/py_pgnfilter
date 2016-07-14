"""Tests for pgn_filter."""

from pgn_filter import color_match


def test_color_match_white_first():
    """It should return True because this is a game where white moves first."""
    white_first_game = [
        '[Event "White to move & win"]',
        '[Site "?"]',
        '[Date "1998.??.??"]',
        '[Round "?"]',
        '[White "1001 Winning Chess Sacrifices"]',
        '[Black "and Combinations"]',
        '[Result "*"]',
        '[Annotator "Magne,Alf"]',
        '[SetUp "1"]',
        '[FEN "3qk2r/1pp1nppp/1p6/r7/8/5Q2/PP3PPP/R1B1R1K1 w k - 0 1"]',
        '[PlyCount "5"]',
        '[EventDate "1998.??.??"]',

        '[1. Bg5 Rxg5 2. Rad1 Qa8]',
        '[3. Qe3 *]'
    ]

    assert True is color_match(white_first_game, 'w')
    assert False is not color_match(white_first_game, 'w')


def test_color_match_black_first():
    """It should return True because this is a game where black moves first."""
    black_first_game = [
        '[Event "White to move & win"]',
        '[Site "?"]',
        '[Date "1998.??.??"]',
        '[Round "?"]',
        '[White "1001 Winning Chess Sacrifices"]',
        '[Black "and Combinations"]',
        '[Result "*"]',
        '[Annotator "Magne,Alf"]',
        '[SetUp "1"]',
        '[FEN "3qk2r/1pp1nppp/1p6/r7/8/5Q2/PP3PPP/R1B1R1K1 b k - 0 1"]',
        '[PlyCount "5"]',
        '[EventDate "1998.??.??"]',

        '[1. Bg5 Rxg5 2. Rad1 Qa8]',
        '[3. Qe3 *]'
    ]

    assert True is color_match(black_first_game, 'b')
    assert False is not color_match(black_first_game, 'b')
