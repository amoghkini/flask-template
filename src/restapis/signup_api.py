from flask import render_template, g, redirect, url_for, request, flash
from flask.views import MethodView

from config.config import get_server_config
from exceptions.user_exceptions import InvalidUserDataError, UserNotFoundError
from user.user import User
from user.user_methods import UserMethods

class SignUpAPI(MethodView):

    def get(self):
        if g.user:
            return redirect(url_for('index_api'))
        return render_template('signup.html', form_data=request.form, errors={})
    
    def post(self):
        try:
            if g.user:
                return redirect(url_for('index_api'))
            
            email_id = request.form.get("email")
            user = User(email_id)
            
            # Get the form data from the request
            user.first_name: str = request.form.get('firstName')
            user.last_name: str = request.form.get('lastName')
            user.mobile_no: str = request.form.get("mobileNumber")
            user.password:str = request.form.get('password')
            user.confirm_password: str = request.form.get('confirmPassword')
            user.username: str = UserMethods.generate_username(user.first_name, user.last_name)
            
            # Perform user signup
            UserMethods.sign_up_user(user)

            acct_activation_req = get_server_config().get('accountActivationRequired')
            if acct_activation_req:
                # Activate account
                UserMethods.activate_account(user.email_id)
                flash('The account activation mail has been sent to registerd email address!', 'success')
            else:
                flash('The account created successfully!', 'success')
            return redirect(url_for('login_api'))
        
        except InvalidUserDataError as e:
            flash(str(e), 'danger')
            return render_template('signup.html', form_data=request.form)
        except UserNotFoundError as e:
            flash(str(e), 'danger')
            return render_template('signup.html', form_data=request.form)
        except ValueError as e:
            flash(str(e), 'danger')
            return render_template('signup.html', form_data=request.form)
        except Exception as e:
            flash("Something went wrong while creating the user. Please try after sometime.", 'danger')
            return render_template('signup.html', form_data=request.form)