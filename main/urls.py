from django.urls import path
from main.views import show_main, create_giggle_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, landing_page, home_page,  add_giggle_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', landing_page, name= 'landing_page'),
    path('home/,',home_page, name='home_page' ),
    path('main/', show_main, name='show_main'),
    path('create_giggle_entry', create_giggle_entry, name='create_giggle_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('main/edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('main/delete/<uuid:id>', delete_product, name='delete_product'),
    path('create-giggle-entry-ajax', add_giggle_entry_ajax, name='add_giggle_entry_ajax'),

]