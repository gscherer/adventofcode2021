import pytest
from day10.parse import fill_incomplete_line, parse, score_corrupted_lines
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

def test_score_corrupted_lines():
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
    score = score_corrupted_lines(lines)
    assert score == 26397

def test_fill_incomplete_lines():
    lines = {
        '[({(<(())[]>[[{[]{<()<>>': '}}]])})]',
        '[(()[<>])]({[<{<<[]>>(': ')}>]})',
        '(((({<>}<{<{<>}{[]{[]{}': '}}>}>))))',
        '{<[[]]>}<{[{[{[]{()[[[]': ']]}}]}]}>',
        '<{([{{}}[<[[[<>{}]]]>[]]': '])}>'
    }
    for k in lines:
        filler = fill_incomplete_line(k)
        assert filler == lines[k]