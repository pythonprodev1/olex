from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from ads.models import Ads, SubCategory
from attribute.models import Attribute
from common.models import District, Region
from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl_drf.compat import KeywordField, StringField


@registry.register_document
class AdsDocument(Document):
    sub_category = fields.ObjectField(
        properties={
            "title": StringField(
                fields={
                    "raw": KeywordField(),
                },
            ),
            "category": fields.ObjectField(
                properties={
                    "title": StringField(
                        fields={
                            "raw": KeywordField(),
                        },
                    ),
                    "ads_count": fields.IntegerField(),
                }
            ),
            "ads_count": fields.IntegerField(),
            "attributes": fields.ListField(
                fields.ObjectField(
                    properties={
                        "title": StringField(
                            fields={
                                "raw": KeywordField(),
                            },
                        ),
                        # "image": StringField(),
                        "type": StringField(),
                        "filter_type": StringField(),
                        "is_required": fields.BooleanField(),
                        "is_filter": fields.BooleanField(),
                        "is_list": fields.BooleanField(),
                        "order": fields.IntegerField(),
                    }
                )
            ),
        }
    )
    attribute_values = fields.ListField(
        fields.ObjectField(
            properties={
                "value": StringField(
                    fields={
                        "raw": KeywordField(),
                    },
                ),
                "attribute": fields.ObjectField(
                    properties={
                        "title": StringField(
                            fields={
                                "raw": KeywordField(),
                            },
                        ),
                        # "image": StringField(),
                        "type": StringField(),
                        "filter_type": StringField(),
                        "is_required": fields.BooleanField(),
                        "is_filter": fields.BooleanField(),
                        "is_list": fields.BooleanField(),
                        "order": fields.IntegerField(),
                    }
                ),
                "value_options": fields.ListField(
                    fields.ObjectField(
                        properties={
                            "option": fields.ObjectField(
                                properties={
                                    "title": StringField(),
                                    "order": fields.IntegerField(),
                                    "attribute": fields.ObjectField(
                                        properties={
                                            "title": StringField(
                                                fields={
                                                    "raw": KeywordField(),
                                                },
                                            ),
                                            # "image": StringField(),
                                            "type": StringField(),
                                            "filter_type": StringField(),
                                            "is_required": fields.BooleanField(),
                                            "is_filter": fields.BooleanField(),
                                            "is_list": fields.BooleanField(),
                                            "order": fields.IntegerField(),
                                        }
                                    ),
                                }
                            )
                        }
                    )
                ),
            }
        )
    )

    district = fields.ObjectField(
        properties={
            "title": StringField(
                fields={
                    "raw": KeywordField(),
                },
            ),
            "region": fields.ObjectField(
                properties={
                    "title": StringField(
                        fields={
                            "raw": KeywordField(),
                        },
                    ),
                }
            ),
        }
    )
    title = StringField(
        fields={
            "raw": KeywordField(),
        },
    )

    content = StringField(
        fields={
            "raw": KeywordField(),
        },
    )

    class Index:
        # Name of the Elasticsearch index
        name = "ads"
        # See Elasticsearch Indices API reference for available settings
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    # def get_instances_from_related(self, related_instance):
    #     if isinstance(related_instance, SubCategory):
    #         print("asddasd")
    #         return related_instance.sub_category

    #     # otherwise it's a Manufacturer or a Category
    #     return related_instance.car_set.all()

    class Django:
        model = Ads  # The model associated with this Document
        fields = [
            "id",
            # "title",
            "image",
            "price",
            # "content",
            "is_top",
            "address",
            # "district",
            # "sub_category",
        ]
        # The fields of the model you want to be indexed in Elasticsearch

        # related_models = [SubCategory, District, Region, Attribute]
        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Configure how the index should be refreshed after an update.
        # See Elasticsearch documentation for supported options:
        # https://www.elastic.co/guide/en/elasticsearch/reference/master/docs-refresh.html
        # This per-Document setting overrides settings.ELASTICSEARCH_DSL_AUTO_REFRESH.
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000
