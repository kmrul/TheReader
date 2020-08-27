from flask import render_template, request, redirect, url_for
from reader import app

from .models import Membership
from .forms import MembershipForm

@app.route('/membership', methods=['GET', 'POST'])
def membership():
    form = MembershipForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "price": form.price.data,
            "post_limit": form.post_limit.data,
        }
        obj = Membership.query.filter_by(name=form.name.data,price=form.price.data, post_limit=form.post_limit.data).first()
        if obj is None:
            obj = Membership(**data)
            obj.save()
            return redirect('/membership')
    memberships = Membership.query.order_by(Membership.id).all()
    print("memberships:", memberships)
    return render_template('membership/membership.html', form=form, memberships=memberships)