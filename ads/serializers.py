from rest_framework import serializers
from ads import models
from common.serializers import DistrictSerializer
from attribute.serializers import (
    AttributeOptionSerializer,
    AttributeSerializer,
    FilterAttributeSerializer,
)
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ads.documents import AdsDocument


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "title", "ads_count", "image")


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.SubCategory
        fields = (
            "id",
            "title",
            "category",
            "ads_count",
        )


class FilterSubCategorySerializer(serializers.ModelSerializer):
    attributes = FilterAttributeSerializer(many=True)

    class Meta:
        model = models.SubCategory
        fields = ("id", "title", "ads_count", "attributes")


class FilterCategorySerializer(serializers.ModelSerializer):
    subcategory = FilterSubCategorySerializer(many=True)

    class Meta:
        model = models.Category
        fields = ("id", "title", "ads_count", "image", "subcategory")


class AdsAttributeValueOption(serializers.ModelSerializer):
    option = AttributeOptionSerializer()

    class Meta:
        model = models.AdsAttributeValueOption
        fields = (
            "id",
            "option",
        )


class AdsAttributeValueSerializer(serializers.ModelSerializer):
    value_options = AdsAttributeValueOption(many=True)
    attribute = AttributeSerializer()

    class Meta:
        model = models.AdsAttributeValue
        fields = ("id", "attribute", "value_options", "value")


class AdsSerializer(serializers.ModelSerializer):
    # sub_category = SubCategorySerializer()
    # district = DistrictSerializer()
    attribute_values = AdsAttributeValueSerializer(many=True)

    class Meta:
        model = models.Ads
        fields = (
            "id",
            "title",
            "image",
            "price",
            "is_top",
            # "sub_category",
            "address",
            "attribute_values",
            "created_at",
            "updated_at",
        )


class AdsDocumentSerializer(DocumentSerializer):
    class Meta:
        """Meta options."""

        document = AdsDocument
        fields = "__all__"
