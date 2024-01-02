

projects = [
    {
        "id": 1,
        "name": "Who is AI",
        "description": "",
        "duration": -1,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 2,
        "name": "livre Inaya",
        "description": "",
        "duration": 50,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 3,
        "name": "visualiser",
        "description": "",
        "duration": -1,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 4,
        "name": "guitar",
        "description": "",
        "duration": -1,
        "weekly_time": 2,
        "time_spend": 0
    },
    {
        "id": 5,
        "name": "lire/mind map",
        "description": "",
        "duration": -1,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 6,
        "name": "yogi",
        "description": "",
        "duration": -1,
        "weekly_time": 4,
        "time_spend": 0
    },
    {
        "id": 7,
        "name": "maison",
        "description": "",
        "duration": -1,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 8,
        "name": "pleg système",
        "description": "",
        "duration": -1,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 9,
        "name": "theâtre miniature",
        "description": "",
        "duration": 25,
        "weekly_time": 0,
        "time_spend": 0
    },
    {
        "id": 10,
        "name": "dessiner",
        "description": "",
        "duration": -1,
        "weekly_time": 5,
        "time_spend": 0
    },

]

def show_total_weekly_time(projects):
    return sum([project['weekly_time'] for project in projects])

def show_total_time_spend(projects):
    return sum([project['time_spend'] for project in projects])

