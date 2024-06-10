from django.urls import path
from . import views

urlpatterns = [
    path('gender', views.index_gender),
    path('gender/create', views.create_gender),
    path('gender/store', views.store_gender),
    path('gender/show/<int:gender_id>', views.show_gender),
    path('gender/edit/<int:gender_id>', views.edit_gender),
    path('gender/update/<int:gender_id>', views.update_gender),
    path('gender/delete/<int:gender_id>', views.delete_gender),
    path('gender/destroy/<int:gender_id>', views.destroy_gender),
    path('customers', views.index_customer),
    path('customers/create', views.create_customer),
    path('customers/store', views.store_customer),
    path('customers/show/<int:customer_id>', views.show_customer),
    path('customers/edit/<int:customer_id>', views.edit_customer),
    path('customers/update/<int:customer_id>', views.update_customer),
    path('customers/delete/<int:customer_id>', views.delete_customer),
    path('customers/destroy/<int:customer_id>', views.destroy_customer),
    path("base/",views.base,name="base"),
    path("base/user_login/",views.user_login,name="user_login"),
    path("intro/",views.intro,name="intro"),
]