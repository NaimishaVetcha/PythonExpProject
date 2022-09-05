from collections import OrderedDict
from .atomic_id_counter import AtomicIdCounter
import datetime

class Attendee:
    """
    The NBRMeetingDetail data-object is an object meant to house and ingest and convert the Webex API's root response.
    
    The object will make sure to create objects and keep references for nested information.
    """


    def __init__(self, init_dict: dict, parent_id: int, atomic_id: AtomicIdCounter):
        super().__init__()
        if isinstance(init_dict, dict):
            self.init_dict = init_dict
            self.atomic_id = atomic_id
            self.pk_id = atomic_id.get_id('attendee')
            self.meeting_id = parent_id
            self.meeting_key = init_dict.get('history:meetingKey', None)
            self.meeting_uuid = init_dict.get('history:meetingUUID', None)
            self.conf_name = init_dict.get('history:confName', None)
            self.ip_address = init_dict.get('history:ipAddress', None)
            self.client_agent = init_dict.get('history:clientAgent', None)
            self.phone_number = init_dict.get('history:phoneNumber', None)
            self.country = init_dict.get('history:country', None)
            self.name = init_dict.get('history:name', None)
            self.email = init_dict.get('history:email', None)

            if init_dict.get('history:joinTime', None) is not None:
                self.join_time = datetime.datetime.strptime(init_dict.get('history:joinTime', None), '%m/%d/%Y %H:%M:%S')
            else:
                self.join_time = None
                
            if init_dict.get('history:leaveTime', None) is not None:
                self.leave_time = datetime.datetime.strptime(init_dict.get('history:leaveTime', None), '%m/%d/%Y %H:%M:%S')
            else:
                self.leave_time = None
            self.duration = init_dict.get('history:duration', None)
            self.participant_type = init_dict.get('history:participantType', None)
            self.voip_duration = init_dict.get('history:voipDuration', None)
            self.conf_id = init_dict.get('history:confID', None)
            self.external_participant = init_dict.get('history:external_participant', None)
            self.session_key = init_dict.get('history:sessionKey', None)
            self.attendee_name = init_dict.get('history:attendeeName', None)
            self.attendee_email = init_dict.get('history:attendeeEmail', None)
            if init_dict.get('history:startTime', None) is not None:
                self.start_time = datetime.datetime.strptime(init_dict.get('history:startTime', None), '%m/%d/%Y %H:%M:%S')
            else:
                self.start_time = None

            if init_dict.get('history:endTime', None) is not None:
                self.end_time = datetime.datetime.strptime(init_dict.get('history:endTime', None), '%m/%d/%Y %H:%M:%S')
            else:
                self.end_time = None

            self.registered = init_dict.get('history:registered', None)
            self.invited = init_dict.get('history:invited', None)


    # Getters and Setters


    def get_row(self) -> OrderedDict:
        """Summary: Export the data object and it's children to csvs.
    
        Parameters: path: String that is the absolute path to the output csv.
        
        Returns: N/A
        """            
        row = OrderedDict()
        row['pk_id'] = self.pk_id
        row['meeting_id'] = self.meeting_id
        row['meeting_key'] = self.meeting_key
        row['meeting_uuid'] = self.meeting_uuid
        row['conf_name'] = self.conf_name
        row['ip_address'] = self.ip_address
        row['client_agent'] = self.client_agent
        row['phone_number'] = self.phone_number
        row['country'] = self.country
        row['name'] = self.name
        row['email'] = self.email
        row['join_time'] = self.join_time
        row['leave_time'] = self.leave_time
        row['duration'] = self.duration
        row['participant_type'] = self.participant_type
        row['voip_duration'] = self.voip_duration
        row['conf_id'] = self.conf_id
        row['external_participant'] = self.external_participant
        row['session_key'] = self.session_key
        row['attendee_name'] = self.attendee_name
        row['attendee_email'] = self.attendee_email
        row['start_time'] = self.start_time
        row['end_time'] = self.end_time
        row['registered'] = self.registered
        row['invited'] = self.invited
        return row
