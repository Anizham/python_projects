import phonenumbers
from phonenumbers import geocoder
ph_no = phonenumbers.parse("+91**********")
print(geocoder.description_for_number(ph_no,'en'))
