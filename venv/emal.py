

from django.core.exceptions import ValidationError
from django.core.validators import validate_email
# import pyDNS
try:
    validate_email('example@example.com',check_mx=True)
except ValidationError as e:
    print ("oops! wrong email")
else:
    print ("hooray! email is valid")

