from django.db import models
from utils.models import BaseModel
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="main_category")

    ads_count = models.IntegerField(default=0)


class SubCategory(BaseModel):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="subcategory"
    )
    attributes = models.ManyToManyField("attribute.Attribute", blank=True)

    ads_count = models.IntegerField(default=0)


# class AdsImage(BaseModel):
#     ads = models.ForeignKey("ads.Ads", on_delete=models.CASCADE, related_name="images")


class Ads(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ads_images")
    price = models.IntegerField(default=0)
    content = models.TextField()

    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category"
    )
    district = models.ForeignKey("common.District", on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_top = models.BooleanField(default=False)

    # EXTRA FIELDS
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_address_text(self):
        return f"{self.district.region.title}, {self.district.title}"


class AdsAttributeValue(BaseModel):
    value = models.CharField(max_length=255, null=True, blank=True)

    ads = models.ForeignKey(
        Ads, on_delete=models.CASCADE, related_name="attribute_values"
    )
    attribute = models.ForeignKey("attribute.Attribute", on_delete=models.CASCADE)


class AdsAttributeValueOption(BaseModel):
    ads_attribute_value = models.ForeignKey(
        AdsAttributeValue, on_delete=models.CASCADE, related_name="value_options"
    )
    option = models.ForeignKey("attribute.AttributeOption", on_delete=models.CASCADE)
