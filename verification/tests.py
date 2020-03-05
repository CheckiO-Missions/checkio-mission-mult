"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1,2,3]],
            "answer": 6,
        },
        {
            "input": [[1]],
            "answer": 1,
        },
        {
            "input": [[10, 10, 10]],
            "answer": 1000,
        },
        {
            "input": [[10, 10, 10, 0]],
            "answer": 0,
        },
        {
            "input": [[1,2,3], 2],
            "answer": 12,
        },
        {
            "input": [[]],
            "answer": 1,
        },
        {
            "input": [[], 2],
            "answer": 2,
        },
    ],
    "Extra": [
        {
            "input": [[4,6,3,7,9,3]],
            "answer": 13608,
        },
        {
            "input": [[4,6,3,7,9,3], 10],
            "answer": 136080,
        },
    ]
}
