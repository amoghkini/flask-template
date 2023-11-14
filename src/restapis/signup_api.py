from flask import render_template, g, redirect, url_for, request
from flask.views import MethodView


class SignUpAPI(MethodView):

    def get(self):
        if g.user:
            return redirect(url_for('index_api'))
        return render_template('signup.html', form_data=request.form, errors={})
    
    def post(self):
        if g.user:
            return redirect(url_for('dashboard_api'))
        
         # Get the form data from the request
        first_name = request.form.get('firstName')
        
        errors = {}
        if len(first_name) < 5:
            errors['firstName'] = f'First name should be at least 5 characters long \n Please provide the valid data'

            # Assuming there's an error with confirmPassword validation
            # errors['confirmPassword'] = "Password and confirm password should be same"

        # If there are errors, render the template with error messages
        if errors:
            return render_template('signup.html', form_data=request.form, errors=errors)
        
        # If no errors, proceed with form submission logic
        # ... (your form submission logic here)
        print("Going to login page")
        return redirect(url_for('login_api'))  # Redirect to a success page
        
