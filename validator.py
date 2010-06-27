import re

class Validator:

    def __init__(self, doc_id):
        self.doc_id = doc_id
        self.stripChars()

    def stripChars(self):
        regex = '[^A-Z0-9]'
        self.clean_doc_id = re.sub(regex,'',self.doc_id)

    def _Spain_get_letter(self, number):
        NIF='TRWAGMYFPDXBNJZSQVHLCKE'
        return NIF[number%23]

    def Spain_NIF(self):
        regex = '^(\d{8})([TRWAGMYFPDXBNJZSQVHLCKE]{1})$'
        match = re.match(regex, self.clean_doc_id)
        if None == match:
            return False
        else:
            letter = self._Spain_get_letter(int(match.group(1)))
            if letter != match.group(2):
                return False
            else:
                return True

    def Spain_NIE(self):
        regex = '^([XYZ]{1})(\d{7})([TRWAGMYFPDXBNJZSQVHLCKE]{1})$'
        match = re.match(regex, self.clean_doc_id)
        if None == match:
            return False
        else:
            letter = self._Spain_get_letter(int(match.group(2)))
            if letter != match.group(3):
                return False
            else:
                return True
