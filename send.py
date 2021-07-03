from etext import send_sms_via_email
import getQuote

class Person:
    def __init__(self, number, prov):
        self.number = number
        self.prov = prov

t = Person("321-208-6947", "Metro PCS")
mo = Person("321-288-4704", "Sprint")
balmer = Person("321-848-1625", "Verizon")

people = [t, mo, balmer]

obj = getQuote.Quote("quotes.txt")
message = obj.text + obj.author

stmp_server = "stmp.gmail.com"
stmp_port = 465

sender_credentials = ("goodquotessender@gmail.com", "awpfprbtwsmyyxqt")

for person in people:
    send_sms_via_email(
    person.number, message, person.prov, sender_credentials)

print("Done and Dunner")
