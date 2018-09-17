def session(request):

    if request.user.is_authenticated:
        return True
    return False