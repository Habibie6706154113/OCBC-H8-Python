from flask import make_response, abort
from config import db
from models import Directors, DirectorsSchema, Movies


def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of directors
    :return:        json string of list of directors
    """
    # Create the list of directors from our data
    directors = Directors.query.order_by(db.desc(Directors.id)).limit(50)

    # Serialize the data for the response
    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)
    return data

def create(directors):
    """
    This function creates a new director in the directors structure
    based on the passed in director data
    :param directors:  director to create in directors structure
    :return:        201 on success, 409 on director name or uid exists, 409 gender invalid 
    """
    valid_gender = [0, 1, 2]
    name = directors.get("name")
    uid = directors.get("uid")
    gender = directors.get("gender")

    existing_name = (
        Directors.query.filter(Directors.name == name)
        .one_or_none()
    )

    existing_uid = (
        Directors.query.filter(Directors.uid == uid)
        .one_or_none()
    )

    # Can we insert this director?
    if existing_uid is not None:
        abort(409, f"Directors uid: {uid} exists already")
    
    elif existing_name is not None:
        abort(409, f"Directors name: {name} exists already")

    elif gender not in valid_gender:
        abort(409, f"Please insert gender with val:0  -> i prefer not to say , 1 -> for female, 2 -> for male ")

    # Otherwise, yes, create directors
    else:
        # Create a director instance using the schema and the passed in director
        schema = DirectorsSchema()
        new_directors = schema.load(directors, session=db.session)

        # Add the director to the database
        db.session.add(new_directors)
        db.session.commit()

        # Serialize and return the newly created director in the response
        data = schema.dump(new_directors)

        return data, 201
        
def read_one(director_id):
    """
    This function responds to a request for /api/director/{director_id}
    with one matching director from directors
    :param director_id:   Id of director to find
    :return:            director matching id
    """
    # Build the initial query
    director = (
        Directors.query.filter(Directors.id == director_id)
        .outerjoin(Movies)
        .one_or_none()
    )

    # Did we find a director?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorsSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for Id: {director_id}")

def read_gender_director(gender):
    """
    This function responds to a request for /api/director/{gender}
    with one matching director from directors
    :param gender:   Gender of director to find
    :return:            director matching gender
    """
    valid_gender = [0, 1, 2]

    if gender in valid_gender:
        # Build the initial query
        director = Directors.query.filter(Directors.gender == gender).limit(10)

        # Serialize the data for the response
        director_schema = DirectorsSchema(many=True)
        data = director_schema.dump(director)
        return data

    else:
        abort(409, f"Please insert gender with val:0  -> i prefer not to say , 1 -> for female, 2 -> for male ")

def read_department_director(department):
    """
    This function responds to a request for /api/director/{department}
    with one matching director from directors
    :param department:   Department of director to find
    :return:            director matching department
    """

    # Build the initial query
    directors = Directors.query.filter(Directors.department.like(department)).limit(10)
    empty = []

    # Serialize the data for the response
    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)
    if len(data) != len(empty):
        return data
    else:
        abort(409, f"director not found for Department: {department}")

def update(director_id, directors):
    """
    This function updates an existing director in the directors structure
    :param director_id:   Id of the director to update in the directors structure
    :param directors:      director to update
    :return:            updated director structure
    """
    valid_gender = [0, 1, 2]
    gender = directors.get("gender")

    # Get the director requested from the db into session
    update_director = Directors.query.filter(
        Directors.id == director_id
    ).one_or_none()

    # Did we find an existing director?
    if update_director is None:
        abort(404, f"Director not found for Id: {director_id}")
    
    # wes the gender valid?
    elif gender not in valid_gender:
        abort(409, f"Please insert gender with val:0  -> i prefer not to say , 1 -> for female, 2 -> for male ")

    # Otherwise, yes, we find that director and the gender is valid
    else:

        # turn the passed in director into a db object
        schema = DirectorsSchema()
        update = schema.load(directors, session=db.session)

        # Set the id to the director we want to update
        update.id = update_director.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated director in the response
        data = schema.dump(update_director)

        return data, 200

def delete(director_id):
    """
    This function deletes a director from the directors structure
    :param director_id:   Id of the director to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the director requested
    director = Directors.query.filter(Directors.id == director_id).one_or_none()

    # Did we find a director?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director {director_id} deleted", 200)

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for Id: {director_id}")