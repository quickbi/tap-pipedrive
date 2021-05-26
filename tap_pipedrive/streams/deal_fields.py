import singer
from tap_pipedrive.stream import PipedriveStream


class DealFieldsStream(PipedriveStream):
    endpoint = 'dealFields'
    schema = 'deal_fields'
    # state_field = None
    key_properties = ['id']
