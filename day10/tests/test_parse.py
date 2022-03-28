from day10.score import find_middle_score_of_incomplete_lines, score_completed_line, score_corrupted_lines
import pytest
from day10.parse import fill_incomplete_line, parse
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

def test_score_completed_line():
    lines = {
        '}}]])})]': 288957,
        ')}>]})': 5566,
        '}}>}>))))': 1480781,
        ']]}}]}]}>': 995444,
        '])}>': 294
    }
    for line in lines:
        score = score_completed_line(line)
        assert score == lines[line]

def test_find_middle_score_of_incomplete_lines():
    lines = [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '(((({<>}<{<{<>}{[]{[]{}',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]
    assert 288957 == find_middle_score_of_incomplete_lines(lines)
