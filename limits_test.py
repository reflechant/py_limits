from limits import maximum, minimum

objects = (
    0,
    1 << 30,
    "",
    "abcdefg",
    [],
    [1, 2, 3, 4, 5],
    (),
    (1, 2, 3, 4, 5),
    {},
    dict(zip((1, 2, 3, 4, 5), "abcdef")),
    set,
    {1, 2, 3, 4},
    # etc.
)


def test_max():
    for o in objects:
        assert maximum > o
        assert maximum >= o

def test_min():
    for o in objects:
        assert minimum < o
        assert minimum <= o
