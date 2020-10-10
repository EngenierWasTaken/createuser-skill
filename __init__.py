from mycroft import MycroftSkill, intent_file_handler


class Createuser(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('createuser.intent')
    def handle_createuser(self, message):
        self.speak_dialog('createuser')


def create_skill():
    return Createuser()

