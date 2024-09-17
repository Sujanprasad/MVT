from django.urls import path
from .views import *


urlpatterns = [
    
    path('', main,name='main'),

    path('members/', members, name='members'),
    path('members/details/<int:id>', details, name='details'),
    
    path('emp_list/',Employee_names, name='emp_list'),
    path('emp_list/emp_details/id=<int:id>', Employee_details, name='emp_details'),
    
    path('contacts/',contact),

    path('form/',form,name='form'),
    path('form/add_record/',addrecord,name="addrecord"),

    path('calc/',calculator_view, name='calculator'),
    
    path('members_form/',Members_view),
    path('contacts/contact/', contact_view, name='contact'),
    path('success/', success_view, name='success'),

    path('value/', index, name='index'),

    path('register/',register,name='register'),
    path('login/',login_r,name='login'),
    path('dashboard/',dashboard,name="dashboard"),

    path('name/',Names,name='names'),
    path('name/del/<int:id>',delete),
    path('name/edit/<int:id>/', edit, name='edit'),
    path('mail/', send_email_view, name='mail'),
    path('email/',mail),

    path('otp/', login_view, name='login'),
    path('verify/', verify_otp_view, name='verify_otp'),

    path('register_email/',register_email,name='register_email'),
    path('login_email/', login_email,name='login_email'),

    path('login_view/',login__view,name='adminlogin'),
    path('dash_board/', dash_board,name='dash_board'),

    path('product_register/',   Product_register,name='product_register'),
    path('product_login/',   Product_login,name='product_login'),
    path('verify_product/',    verify_otp_product, name='verify_otp_product'),
    path('product_admin/', product_admin,name='product_admin'),
    path('product_admin/delete_product/<int:id>', delete_product,name="delete_product"),
    path('product_admin/edit_product/<int:id>', edit_product,name="edit_product"),
    path('product_user/', product_user,name='product_user'),
    path('product_user/buy/<int:id>', buy,name='buy'),

    path('login_product/', product_login_without_panel,name='without_panel'),
    path('verify_product_/',  verify_otp_, name='verify_otp_'),

    path('Quiz_Questions/', Quiz_Q,name="Quiz_Questions"),
    path('Quiz_Questions/delete_Questions/<int:id>', delete_Question),
    path('Student_name/', Student_name,name='Student_name'),
    path('Student_name/Quiz',Quiz_page,name='Quiz'),
    path('Student_name/Quiz_timer',Quiz_Timer,name='Quiz_timer'),

    
    

]