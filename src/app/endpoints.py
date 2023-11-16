from flask import Flask


from restapis import (
    about_us_api,
    charnge_password, 
    contact_us_api, 
    index_api, 
    login_api, 
    profile_api,
    profile_pic_api, 
    signup_api, 
    tab_page_api
)

def register_endpoints(app: Flask) -> None:

    app.add_url_rule("/", view_func=index_api.IndexAPI.as_view("index_api"))
    app.add_url_rule("/about", view_func=about_us_api.AboutUsAPI.as_view("about_us_api"))
    app.add_url_rule("/change_password", view_func=charnge_password.ChangePasswordAPI.as_view("change_password_api"))
    app.add_url_rule("/contact", view_func=contact_us_api.ContactUsAPI.as_view("contact_us_api"))
    app.add_url_rule("/login", view_func=login_api.LogInAPI.as_view("login_api"))
    app.add_url_rule("/profile", view_func=profile_api.ProfileAPI.as_view("profile_api"))
    app.add_url_rule("/profile_picture", view_func=profile_pic_api.ProfilePicAPI.as_view("profile_pic_api"))
    app.add_url_rule("/signup", view_func=signup_api.SignUpAPI.as_view("signup_api"))
    app.add_url_rule("/tab_page", view_func=tab_page_api.TabPageAPI.as_view("tab_page_api"))
