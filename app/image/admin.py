from django.contrib import admin
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from index import admin as index_admin


from .models import Image, HotImage, ImageTag, TagImage, ImageScore, UserRateing, ImageCategory, CategoryImage
from index import admin as index_admin


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    # def show_tags(self, obj):
    #     return ' '.join([tag.name for tag in obj.tags.all()])
    # tags= Tag.objects.filter(image_id=obj.id)

    # show_tags.short_description = '显示所有标签'

    list_display = ['id', 'name', 'url', 'width', 'height', 'type']
    list_display_links = ['id', 'name', 'url', 'width', 'height', 'type']

    search_fields = ['name', 'width', 'height', 'type']

    list_filder = ['width', 'height', 'type']
    ordering = ['id']

    actions = [index_admin.export_as_json]

    list_per_page = 10


@admin.register(HotImage)
class HotImageAdmin(admin.ModelAdmin):
    def get_image_name(self, obj):
        return obj.image.name

    get_image_name.short_description = '图片名'

    def get_image_url_thumb(self, obj):
        return obj.image.url_thumb

    get_image_url_thumb.short_description = '图片链接'

    list_display = ['id', 'index', 'get_image_name', 'get_image_url_thumb', 'date_add']
    list_display_links = ['id', 'index', 'get_image_name', 'get_image_url_thumb', 'date_add']

    search_fields = ['image.name', 'width', 'height', 'type']

    ordering = ['index']

    actions = [index_admin.export_as_json]


@admin.register(ImageTag)
class ImageTagAdmin(admin.ModelAdmin):
    class CountFilter(admin.SimpleListFilter):
        title = '标签数量'
        parameter_name = 'count'

        def lookups(self, request, model_admin):
            return (
                ('0', '小于 100'),
                ('1', '大于 100'),
            )

        def queryset(self, request, queryset):
            if self.value() == '0':
                return queryset.filter(count__lte='100')
            if self.value() == '1':
                return queryset.filter(count__gte='100')

    list_display = ('id', 'name', 'count')
    list_display_links = ('id', 'name', 'count')

    list_filter = (CountFilter,)

    search_fields = ['id', 'name']
    list_per_page = 10

    ordering = ['id']

    empty_value_display = '- null -'

    actions = [index_admin.export_as_json]


@admin.register(TagImage)
class TagImageAdmin(admin.ModelAdmin):

    def show_tag(self, obj):
        return ','.join([item.get_tag_name() for item in obj.tags.all()])

    show_tag.short_description = '分类名'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户'

    list_display = ['id', 'show_tag', 'show_image', 'show_user', 'date_add']
    list_display_links = ['id', 'show_tag', 'show_image', 'show_user', 'date_add']

    # list_filter = ['tag__count', 'date_add']
    list_filter = ['date_add']

    filter_horizontal = ['tags']

    search_fields = ['tag__name', 'date_add']

    ordering = ['id']
    list_per_page = 10

    actions = [index_admin.export_as_json]

    empyt_value_dispaly = '- null -'


@admin.register(ImageScore)
class ImageSourceAdmin(admin.ModelAdmin):
    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ('id', 'show_image', 'average_stars', 'date_update')
    list_display_links = ('id', 'show_image', 'average_stars', 'date_update')

    list_filter = ['date_update', 'average_stars']

    search_fields = ['image__name', 'average_stars']
    list_per_page = 10

    ordering = ['id']

    empty_value_display = '- null -'

    actions = [index_admin.export_as_json]


@admin.register(UserRateing)
class UserRatingAdmin(admin.ModelAdmin):

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    list_display = ['id', 'show_user', 'show_image', 'date_evaluation']
    list_display_links = ['id', 'show_user', 'show_image', 'date_evaluation']

    # list_filter = ['tag__count', 'date_add']
    list_filter = ['start', 'date_evaluation']

    search_fields = ['user__name', 'image__name', 'image__url', 'date_evaluation']

    ordering = ['id']
    list_per_page = 10

    actions = [index_admin.export_as_json]

    empyt_value_dispaly = '- null -'


@admin.register(ImageCategory)
class ImageCategoryAdmin(admin.ModelAdmin):
    # def upper_case_name(obj):
    #     return obj.name.upper()
    # upper_case_name.short_description = 'Upper Name'
    # list_display = (upper_case_name,)

    class CountFilter(admin.SimpleListFilter):
        title = '图片数量'
        parameter_name = 'count'

        def lookups(self, request, model_admin):
            return (
                ('0', '小于 300'),
                ('1', '大于 300'),
            )

        def queryset(self, request, queryset):
            if self.value() == '0':
                return queryset.filter(count__lte='300')
            if self.value() == '1':
                return queryset.filter(count__gte='300')

    list_display = ('id', 'name', 'count')
    list_display_links = ('id', 'name', 'count')

    list_filter = (CountFilter,)
    show_full_result_count = True

    search_fields = ['id', 'name', 'count']
    list_per_page = 10

    # 进入实际链接查看
    # def view_on_site(self, obj):
    #     url = reverse('person-detail', kwargs={'slug': obj.slug})
    #     return 'https://example.com' + url
    # view_on_site = True

    ordering = ['id']

    actions = ['make_published', index_admin.export_as_json]

    empty_value_display = '- empty value display -'

    def make_published(self, request, queryset):
        rows_updated = queryset.update(count='100')
        if rows_updated == 1:
            message_bit = "1 个分类"
        else:
            message_bit = "%s 个分类" % rows_updated
        self.message_user(request, "%s 成功更新." % message_bit)

    make_published.short_description = '设置图片数量为 100'

    # 重定向测试
    def export_selected_objects(self, request, queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        ct = ContentType.objects.get_for_model(queryset.model)
        return HttpResponseRedirect("/export/?ct=%s&ids=%s" % (ct.pk, ",".join(selected)))

    # 禁用默认的删除选项
    # admin.site.disable_action('delete_selected')


# 旧式的添加方法
# admin.site.register(Category, CategoryAdmin)

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):

    def show_category(self, obj):
        return obj.category.get_category_name()

    show_category.short_description = '分类名'

    def show_image(self, obj):
        return obj.image.get_image_url()

    show_image.short_description = '图片链接'

    def show_user(self, obj):
        return obj.user.get_user_username()

    show_user.short_description = '用户'

    list_display = ['id', 'show_category', 'show_image', 'show_user', 'date_add']
    list_display_links = ['id', 'show_category', 'show_image', 'show_user', 'date_add']

    list_filter = ['category__name', 'date_add']

    search_fields = ['category__name', 'date_add']

    ordering = ['id']
    list_per_page = 10

    actions = [index_admin.export_as_json]

    empyt_value_dispaly = '- null -'
