from flask import render_template, request, redirect, url_for
from reader import app

from .models import Categories
from .form import CategoryForm

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    return render_template('posts/posts.html')

@app.route('/category', methods=['GET', 'POST'])
def category():
    form = CategoryForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "slug": form.slug.data,
            "description": form.description.data,
        }
        obj = Categories.query.filter_by(name=form.name.data,slug=form.slug.data, description=form.slug.data).first()
        if obj is None:
            obj = Categories(**data)
            obj.save()
            return redirect('/category')
    categories = Categories.query.order_by(Categories.id).all()
    print("categories:", categories)
    return render_template('category/category.html', form=form, categories=categories)