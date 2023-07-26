import ijq


def test_main():
    text = """ We can parse
    {"key": ["value1"  , "value2"  , ["value3"]]  } and [{}, {"k": "v"}, []]
    separately."""
    assert [*ijq.ijq(text)] == [
        ' We can parse',
        '{\x1b[37m\x1b[39;49;00m\n\x1b[37m    \x1b[39;49;00m\x1b[94m"key"\x1b[39;49;00m:\x1b[37m \x1b[39;49;00m[\x1b[37m\x1b[39;49;00m\n\x1b[37m        \x1b[39;49;00m\x1b[33m"value1"\x1b[39;49;00m,\x1b[37m\x1b[39;49;00m\n\x1b[37m        \x1b[39;49;00m\x1b[33m"value2"\x1b[39;49;00m,\x1b[37m\x1b[39;49;00m\n\x1b[37m        \x1b[39;49;00m[\x1b[37m\x1b[39;49;00m\n\x1b[37m            \x1b[39;49;00m\x1b[33m"value3"\x1b[39;49;00m\x1b[37m\x1b[39;49;00m\n\x1b[37m        \x1b[39;49;00m]\x1b[37m\x1b[39;49;00m\n\x1b[37m    \x1b[39;49;00m]\x1b[37m\x1b[39;49;00m\n}\x1b[37m\x1b[39;49;00m\n',
        'and',
        '[\x1b[37m\x1b[39;49;00m\n\x1b[37m    \x1b[39;49;00m{},\x1b[37m\x1b[39;49;00m\n\x1b[37m    \x1b[39;49;00m{\x1b[37m\x1b[39;49;00m\n\x1b[37m        \x1b[39;49;00m\x1b[94m"k"\x1b[39;49;00m:\x1b[37m \x1b[39;49;00m\x1b[33m"v"\x1b[39;49;00m\x1b[37m\x1b[39;49;00m\n\x1b[37m    \x1b[39;49;00m},\x1b[37m\x1b[39;49;00m\n\x1b[37m    \x1b[39;49;00m[]\x1b[37m\x1b[39;49;00m\n]\x1b[37m\x1b[39;49;00m\n',
        'separately.'
    ]
    assert [*ijq.ijq(text, no_color=True)] == [
        ' We can parse',
        '{\n    "key": [\n        "value1",\n        "value2",\n        [\n            "value3"\n        ]\n    ]\n}',
        'and', '[\n    {},\n    {\n        "k": "v"\n    },\n    []\n]',
        'separately.',
    ]


if __name__ == '__main__':
    test_main()
