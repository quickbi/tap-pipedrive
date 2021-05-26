import singer
from tap_pipedrive.stream import PipedriveStream


class OrganizationFieldsStream(PipedriveStream):
    endpoint = 'organizationFields'
    schema = 'organization_fields'
    # state_field = None
    key_properties = ['id']
