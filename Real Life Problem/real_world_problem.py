class mobilePhone:
    def __init__(self):
        self.simCard
        self.battery
        self.housing
        self.processor
        self.memory
        self.display

        self._antenna = "internal"

    def start_phone(self):
        return "Phone Started"

    def make_a_call(self):
        return "Making Phone Call"

    def receiving_a_call(self):
        return "Receiving Phone Call"

    def sate_lite_phone_antenna(self):
        self._antenna = "External"
        return "It is a Satellite Phone"


class smartPhone(mobilePhone):
    def __init__(self):
        mobilePhone.__init__(self)
        self.camera
        self.displayTechonology
        
    def make_a_call(self):
        return "Can make a WhatsApp Call"
