from etext import send_sms_via_email

phone_number = "321-208-6947"
message = "your mom suck me good and hard through my jorts"
provider = "Metro PCS"
stmp_server = "stmp.gmail.com"
stmp_port = 465

sender_credentials = ("goodquotessender@gmail.com", "awpfprbtwsmyyxqt")

send_sms_via_email(
    phone_number, message, provider, sender_credentials)
