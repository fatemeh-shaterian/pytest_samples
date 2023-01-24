def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_capsys(capsys):
    print('hello')
    #out, err = capsys.readouterr()
    captured = capsys.readouterr()

    assert 'hello\n' == captured.out

    print('world')
    captured = capsys.readouterr()
    assert 'world' in captured.out