from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from mainapp import models as mainapp_models

# Отключение базовой функции действия над объектами 'delete_selected'
# т.к. она напрямую удаляет объект из БД, навсегда.
# Ниже меняем её на ручную "Mark deleted".
admin.site.disable_action("delete_selected")


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title", "preambule", "body"]
    list_display = ["title", "preambule", "created", "updated", "deleted"]
    ordering = ["-updated"]
    list_per_page = 10
    list_filter = [
        ("created", DateRangeFilter),
        ("updated", DateTimeRangeFilter),
        "deleted",
    ]
    actions = ["mark_deleted"]
    list_editable = ["deleted"]
    # save_on_top = True

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "num", "title", "deleted"]
    ordering = ["-course__name", "-num"]
    list_per_page = 15
    list_filter = ["course", "created", "deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(deleted=True)

    mark_deleted.short_description = _("Mark deleted")


admin.site.site_title = "Админ-панель сайта"
admin.site.site_header = "Админ-панель сайта"
