from datetime import datetime
from flask import make_response, abort


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


PEOPLE = {
    "Farrell": {"fname": "Doug", "lname": "Farrell", "timestamp": get_timestamp()},
    "Brockman": {"fname": "Kent", "lname": "Brockman", "timestamp": get_timestamp()},
    "Easter": {"fname": "Bunny", "lname": "Easter", "timestamp": get_timestamp()},
}


def read():
    """
    GET /api/people 
    :return:
    """
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]


def create(person):
    """
    creates a person in people dict based on passed in person data
    PUT /api/people
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {"lname": lname, "fname": fname, "timestamp": get_timestamp()}

        return make_response(f"{lname} successfully created", 201)
    else:
        abort(f"Person with {lname} already exists")


def read_one(lname):
    """
    Read a person by lname
    GET /api/people/{lname}
    """
    if lname in PEOPLE:
        return PEOPLE.get(lname)
    else:
        abort(404, f"Person with last name {lname} not found")
    return {}


def update(lname, person):
    """
    Update person with lname with new first/last name
    PUT /api/people/{lname}
    """
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(
            404, f"Person with last name {lname} not found"
        )
