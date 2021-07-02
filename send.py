from etext import send_sms_via_email
import getQuote

phone_number = "321-208-6947"
obj = getQuote.Quote("quotes.txt")
message = obj.message + '\n' + obj.author
provider = "Metro PCS"
stmp_server = "stmp.gmail.com"
stmp_port = 465

sender_credentials = ("goodquotessender@gmail.com", "awpfprbtwsmyyxqt")

send_sms_via_email(
    phone_number, message, provider, sender_credentials)
