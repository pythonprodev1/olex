from django.shortcuts import render
from rest_framework import generics
from ads.serializers import AdsSerializer, CategorySerializer, FilterCategorySerializer
from ads.models import Ads, Category, SubCategory
from attribute.models import Attribute

from django.db.models import Prefetch


# Create your views here.
class AdsListView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class MainCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FilterCategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().prefetch_related(
        Prefetch(
            "subcategory",
            queryset=SubCategory.objects.all().prefetch_related(
                Prefetch(
                    "attributes",
                    queryset=Attribute.objects.filter(is_filter=True),
                )
            ),
        )
    )
    serializer_class = FilterCategorySerializer


from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

# Example app models
from ads.documents import AdsDocument
from ads.serializers import AdsDocumentSerializer


class AdsDocumentView(DocumentViewSet):
    """The BookDocument view."""

    document = AdsDocument
    serializer_class = AdsDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        "title",
        "content",
    )
    # Define filtering fields
    filter_fields = {
        "id": {
            "field": "_id",
            "lookups": [
                LOOKUP_FILTER_RANGE,
                LOOKUP_QUERY_IN,
            ],
        },
        "sub_category": "sub_category.id",
        "district": "district.id",
        # "tags": {
        #     "field": "tags",
        #     "lookups": [
        #         LOOKUP_FILTER_TERMS,
        #         LOOKUP_FILTER_PREFIX,
        #         LOOKUP_FILTER_WILDCARD,
        #         LOOKUP_QUERY_IN,
        #         LOOKUP_QUERY_EXCLUDE,
        #     ],
        # },
        # "tags.raw": {
        #     "field": "tags.raw",
        #     "lookups": [
        #         LOOKUP_FILTER_TERMS,
        #         LOOKUP_FILTER_PREFIX,
        #         LOOKUP_FILTER_WILDCARD,
        #         LOOKUP_QUERY_IN,
        #         LOOKUP_QUERY_EXCLUDE,
        #     ],
        # },
    }
    # Define ordering fields
    ordering_fields = {
        "id": "id",
        # "title": "title",
        "price": "price",
        "is_top": "is_top",
    }
    # Specify default ordering
    ordering = (
        "id",
        "title",
    )
