from django.shortcuts import render
from django.http import HttpResponse

def myview(request):
    # Get the number of visits from the session, defaulting to 0
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits  # Update the session with the new count

    # If the visit count exceeds 4, delete the session key
    if num_visits > 4:
        del request.session['num_visits']

    # Create the response with the current view count
    resp = HttpResponse('view count=' + str(num_visits))

    # Set a cookie with a specific value and max age
    resp.set_cookie('dj4e_cookie', '6e03a392', max_age=1000)

    return resp
