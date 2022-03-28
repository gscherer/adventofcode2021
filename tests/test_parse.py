import pytest
from main import parse, score_lines, CorruptedException

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
