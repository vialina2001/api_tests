USER_DATA_SCHEME = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "avatar": {"type": "string"}
    },
    "required": ["id", "email", "first_name", "last_name", "avatar"]
}

CREATED_USER_SCHEME = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "id": {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

LIST_RESOURSE_SCHEME = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "year": {"type": "number"},
        "color": {"type": "string"},
        "pantone_value": {"type": "string"}
    },
    "required": ["id", "name", "year", "color"]
}

REGISTRATION_SCHEME = {
    "type": "object",
    "properties":{
        "id": {"type": "number"},
        "token": {"type": "string"}
    },
    "required": ["id", "token"]
}

USER_UPDATE_SCHEME = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "job": {"type": "string"},
        "updatedAt": {"type": "string"}
    },
}