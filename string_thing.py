class StringThing:
    """Find some things about a string"""
    def __init__(self, start=""):
        self.value = str(start)

    def length(self):
        return len(self.value)

    def substring_count(self, substring):
        return self.value.count(substring)

    def substring_count_lower(self, substring):
        return self.value.lower().count(substring.lower())

    def find_first(self, substring):
        return self.value.find(substring)

    def find_first_lower(self, substring):
        return self.value.lower().find(substring.lower())

    def find_all(self, substring):
        return [i for i in range(len(self.value))
                if self.value.startswith(substring, i)]

    def find_all_lower(self, substring):
        return [i for i in range(len(self.value))
                if self.value.lower().startswith(substring.lower(), i)]


def counterstring(target_length=2, marker="*"):
    """
    Create and return a counterstring
    A counterstring is a string that counts its own length
    e.g. "2*4*6*8*11*14*" - the number before each * gives the length of
    the string at the *
    """
    marker = marker[:1]
    # Minimal starting counterstring
    counting_number = 2
    counter_str = str(counting_number) + marker
    while len(counter_str) < target_length:
        cn_len = len(str(counting_number))
        # Increase the counting number to next marker position
        counting_number = len(counter_str) + cn_len + 1
        # Allow for additional char when counting number gains a digit
        counting_number += len(str(counting_number)) > cn_len
        # Extend the counterstring
        counter_str = counter_str + str(counting_number) + marker
    # Trim as final addition can exceed target
    counter_str = counter_str[:target_length]
    return counter_str
