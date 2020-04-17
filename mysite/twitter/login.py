from django.contrib.auth import authenticate

user = authenticate(username= enteredUsername, password= enteredPassword)
if user is not None:
    # A backend authenticated the credentials
    HttpResponseRedirect('/twitter/')

else:
    # No backend authenticated the credentials
    HttpResponseRedirect('')
