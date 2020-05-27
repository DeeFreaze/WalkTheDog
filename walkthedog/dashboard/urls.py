from django.urls import path
from django.views.generic import TemplateView

from walkthedog.dashboard.views import ClientOrderView, FilterOrdersView, FilterReviewOrderView

app_name = "dashboard"
urlpatterns = [
    path("", TemplateView.as_view(template_name="dashboard/main.html"), name="home"),
    path("client_order/", ClientOrderView.as_view(), name="client_order"),
    path("filter_orders/", FilterOrdersView.as_view(), name="filter_orders"),
    path("review_order/", FilterReviewOrderView.as_view(), name="review_order"),
    path("about_us/", TemplateView.as_view(template_name="dashboard/about_us.html"), name="about_us"),
    path("services/", TemplateView.as_view(template_name="dashboard/services.html"), name="services"),
    path("my_profile/", TemplateView.as_view(template_name="dashboard/my_profile.html"), name="my_profile"),
    path("mapbox/", TemplateView.as_view(template_name="dashboard/mapbox.html"), name="mapbox"),
]
