from flask import render_template, request, redirect, url_for
from reader import app

from .models import Role
from .forms import RoleForm

@app.route('/role', methods=['GET', 'POST'])
def role():
    form = RoleForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
        }
        obj = Role.query.filter_by(name=form.name.data).first()
        if obj is None:
            obj = Role(**data)
            obj.save()
            return redirect('/role')
    roles = Role.query.order_by(Role.id).all()
    return render_template('role/role.html', form=form, roles=roles)