from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(view):
    """
    Protect routes from unauthenticated users.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if session.get("user_id") is None:
            flash("Please log in to continue.", "error")
            return redirect(url_for("login"))

        return view(*args, **kwargs)

    return wrapped_view


def guest_required(view):
    """
    Prevent logged-in users from accessing
    Login and Register pages.
    """

    @wraps(view)
    def wrapped_view(*args, **kwargs):

        if session.get("user_id") is not None:
            return redirect(url_for("home"))

        return view(*args, **kwargs)

    return wrapped_view


def current_user():
    """
    Returns the logged-in user's id.
    """

    return session.get("user_id")


def current_username():
    """
    Returns the logged-in username.
    """

    return session.get("username")


def is_logged_in():
    """
    Returns True if a user is authenticated.
    """

    return session.get("user_id") is not None


def logout_user():
    """
    Clears the current session.
    """

    session.clear()