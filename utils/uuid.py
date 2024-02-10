import base64
import uuid


# get a UUID
def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return str(r_uuid).replace('=', '')
