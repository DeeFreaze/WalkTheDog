from django.urls import path
from django.views.generic import TemplateView
#
# from walkthedog.users.views import (
#     user_detail_view,
# )

app_name = "dashboard"
urlpatterns = [
    path("", TemplateView.as_view(template_name="dashboard/main.html"), name="home"),
    path("client_order/", TemplateView.as_view(template_name='dashboard/client_order.html'), name="client_order"),
    path("filter_orders/", TemplateView.as_view(template_name="dashboard/filter_orders.html"), name="filter_orders"),
    path("list_orders/", TemplateView.as_view(template_name="dashboard/list_orders.html"), name="list_orders"),
    path("review_order/", TemplateView.as_view(template_name="dashboard/review_order.html"), name="review_order"),
    path("about_us/", TemplateView.as_view(template_name="dashboard/about_us.html"), name="about_us"),
    path("services/", TemplateView.as_view(template_name="dashboard/services.html"), name="services"),
    path("my_profile/", TemplateView.as_view(template_name="dashboard/my_profile.html"), name="my_profile"),
]
