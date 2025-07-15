# Simple models for reference, not used directly with Pydantic
class Message:
    def __init__(self, message_id, channel_name, message_text):
        self.message_id = message_id
        self.channel_name = channel_name
        self.message_text = message_text

class Detection:
    def __init__(self, message_id, detected_object_class, confidence_score):
        self.message_id = message_id
        self.detected_object_class = detected_object_class
        self.confidence_score = confidence_score
