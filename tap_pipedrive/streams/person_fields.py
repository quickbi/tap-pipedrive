import singer
from tap_pipedrive.stream import PipedriveStream


class PersonFieldsStream(PipedriveStream):
    endpoint = 'personFields'
    schema = 'person_fields'
    # state_field = None
    key_properties = ['id']
