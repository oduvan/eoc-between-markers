"""
TESTS is a dict with all your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['What is >apple<', '>', '<'],
            "answer": 'apple'
        },
        {
            "input": ["<head><title>My new site</title></head>",
                      "<title>", "</title>"],
            "answer": "My new site",
            "explanation": "markers can be longer than one symbol"
        },
        {
            "input": ['No[/b] hi', '[b]', '[/b]'],
            "answer": 'No',
            "explanation": "No beginning marker"
        },
        {
            "input": ['No [b]hi', '[b]', '[/b]'],
            "answer": 'hi',
            "explanation": "No ending marker"
        },
        {
            "input": ['No hi', '[b]', '[/b]'],
            "answer": 'No hi',
            "explanation": "No markers at all"
        },
        {
            "input": ['No <hi>', '>', '<'],
            "answer": '',
            "explanation": "Wrong direction"
        }
    ],
    "Extra": [
        {
            "input": ["Never send a human to do a machine's job.", "Never", "do"],
            "answer": " send a human to "
        },
        {
            "input": ['No <hi> one', '>', '<'],
            "answer": '',
            "explanation": "Wrong direction2"
        }
    ]
}
