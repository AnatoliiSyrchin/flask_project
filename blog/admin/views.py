from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for

from blog.models import db, Tag, Article, User

class CustomView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_staff
    
    def inaccessible_callback(self):
        return redirect(url_for("auth_app.login"))
    
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for('auth_app.login'))
        return super(MyAdminIndexView, self).index()

class TagView(CustomView):
    column_searchable_list = ("name",)
    column_filters = ("name",)
    can_export = True
    export_types = ["csv", "xlsx"]
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_set_page_size = True

class ArticleView(CustomView):
    can_edit = False
    can_delete = False
    can_view_details = True
    can_export = True

class UserView(CustomView):
    column_exclude_list = ("_password",)
    column_searchable_list = ("first_name", "last_name", "username", "is_staff", "email")
    column_filters = ("first_name", "last_name", "username", "is_staff", "email")
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_create = False
    can_edit = True
    can_delete = False


admin_app = Admin(name='blog admin', index_view=MyAdminIndexView(), template_mode='bootstrap4')

admin_app.add_view(TagView(Tag, db.session))
admin_app.add_view(ArticleView(Article, db.session))
admin_app.add_view(UserView(User, db.session))