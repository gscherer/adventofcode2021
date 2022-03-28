import pytest
from day10.parse import parse, score_lines
from day10.errors import CorruptedException

def test_corrupted():
    corrupted = [
        '{([(<{}[<>[]}>{[]{[(<()>',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{'
    ]
    for line in corrupted:
        with pytest.raises(CorruptedException):
            parse(line)


def test_score():
    lines = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]
    score = score_lines(lines)
    assert score == 26397
