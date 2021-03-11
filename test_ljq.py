import ijq
import json


def test_main():
    text = """ We can parse
    {"key": ["value1"  , "value2"  , ["value3"]]  } and [{}, {"k": "v"}, []]
    separately."""
    assert [*ijq.main(text)] == [
        " We can parse",
        "{\n"
        "    \u001b[94m\"key\"\u001b[39;49;00m: [\n"
        "        \u001b[33m\"value1\"\u001b[39;49;00m,\n"
        "        \u001b[33m\"value2\"\u001b[39;49;00m,\n"
        "        [\n"
        "            \u001b[33m\"value3\"\u001b[39;49;00m\n"
        "        ]\n"
        "    ]\n"
        "}\n",
        "and",
        "[\n"
        "    {},\n"
        "    {\n"
        "        \u001b[94m\"k\"\u001b[39;49;00m: \u001b[33m\"v\"\u001b[39;49;00m\n"
        "    },\n"
        "    []\n"
        "]\n",
        "separately."
    ]


if __name__ == '__main__':
    test_main()
