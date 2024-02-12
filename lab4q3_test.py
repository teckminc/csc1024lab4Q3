import lab4q3
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab4q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip().find(f'10101010101') != -1
    assert captured_stdout.strip().count(f'10101010101') == 5


def test_case2(monkeypatch, capsys):
  with open(f"lab4q3.py") as tf:
    head = [next(tf) for _ in range(16)]
    s = tf.read()
    assert(s.find("while") != -1 )

def test_case3(monkeypatch, capsys):
  with open(f"lab4q3.py") as tf:
    head = [next(tf) for _ in range(16)]
    s = tf.read()
    assert(s.find("10101010101") == -1 )