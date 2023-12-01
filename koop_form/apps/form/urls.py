from django.urls import path

from apps.form.views import (
    ProductsView,
    OrderCreateView,
    OrderProductsFormView,
    ProducersView,
    OrderUpdateView,
    OrderDeleteView,
    OrderProducersView,
    OrderUpdateFormView,
    ProducerProductsReportView,
    ProducerBoxReportView,
    UsersReportView,
    ProducerProductsListView,
    ProducerBoxListView,
    ProducersFinanceReportView,
    product_search_view,
    OrderItemFormView, ProducerBoxReportDownloadView,
)


urlpatterns = [
    path("producenci/", ProducersView.as_view(), name="producers"),
    path(
        "producenci/<str:slug>/",
        ProductsView.as_view(),
        name="products",
    ),
    path(
        "raporty/producenci-produkty/",
        ProducerProductsListView.as_view(),
        name="producer-products-list",
    ),
    path(
        "raporty/producenci-produkty/<str:slug>/",
        ProducerProductsReportView.as_view(),
        name="producer-products-report",
    ),
    path(
        "zamowienie/producenci/",
        OrderProducersView.as_view(),
        name="order-producers",
    ),
    path(
        "zamowienie/producenci/<str:slug>/",
        OrderProductsFormView.as_view(),
        name="order-products-form",
    ),
    path("zamowienie/nowe/", OrderCreateView.as_view(), name="order-create"),
    path(
        "zamowienie/edytuj/",
        OrderUpdateFormView.as_view(),
        name="order-update-form",
    ),
    path(
        "zamowienie/szczegoly/edytuj/<int:pk>/",
        OrderUpdateView.as_view(),
        name="order-update",
    ),
    path(
        "zamowienie/szczegoly/usun/<int:pk>/",
        OrderDeleteView.as_view(),
        name="order-delete",
    ),
    path(
        "raporty/producenci-skrzynki/",
        ProducerBoxListView.as_view(),
        name="producer-box-list",
    ),
    path(
        "raporty/producenci-skrzynki/<str:slug>/",
        ProducerBoxReportView.as_view(),
        name="producer-box-report",
    ),
    path(
        "raporty/kooperanci/",
        UsersReportView.as_view(),
        name="users-report",
    ),
    path(
        "raporty/producenci-finanse/",
        ProducersFinanceReportView.as_view(),
        name="producers-finance",
    ),
    path("wyszukiwarka/", product_search_view, name="product-search"),
    path(
        "wyszukiwarka/produkt/<int:pk>",
        OrderItemFormView.as_view(),
        name="order-item-form",
    ),
    path(
        "pobierz/raporty/producenci-skrzynki/<str:slug>/",
        ProducerBoxReportDownloadView.as_view(),
        name="producer-box-report-download",
    ),
]
