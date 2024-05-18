from django.contrib import admin
from django.utils.html import format_html


from . import User,Profile,Hobby,Hotel,Establishment,Comment,BaseHotelModel,Owner

# Регистрация моделей
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Hobby)
admin.site.register(Hotel)
admin.site.register(Establishment)
admin.site.register(Comment)
admin.site.register(BaseHotelModel)
admin.site.register(Owner)


# Классы ModelAdmin
class UsersAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name', 'hobby']
    list_display = ('username', 'age',)  # Добавьте сюда все поля типа int
    list_editable = ('age',)  # Укажите поля, которые должны быть редактируемыми


admin.site.register(User, UsersAdmin)


# Классы InlineModelAdmin
class RelatedModel1:
    pass


class RelatedModel1Inline(admin.TabularInline):
    model = RelatedModel1



class RelatedModel2:
    pass


class RelatedModel2Inline(admin.TabularInline):
    model = RelatedModel2


class RelatedModel3:
    pass


class RelatedModel3Inline(admin.TabularInline):
    model = RelatedModel3


class RelatedModel4:
    pass


class RelatedModel4Inline(admin.TabularInline):
    model = RelatedModel4


class RelatedModel5:
    pass


class RelatedModel5Inline(admin.TabularInline):
    model = RelatedModel5


class ParentModelAdmin(admin.ModelAdmin):
    inlines = [RelatedModel1Inline, RelatedModel2Inline, RelatedModel3Inline,
               RelatedModel4Inline, RelatedModel5Inline]


class ParentModel:

    pass


admin.site.register(ParentModel, ParentModelAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_text_strikethrough',)

    def comment_text_strikethrough(self, obj):
        if obj.user.is_deleted:
            return format_html('<span style="text-decoration: line-through;">{}</span>', obj.comment_text)
        else:
            return obj.comment_text

    comment_text_strikethrough.short_description = 'Комментарий'


@admin.register(ParentModelAdmin)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('highlighted_field',)

    def highlighted_field(self, obj):
        return format_html('<span style="color: red;">{}</span>', obj.your_field)

    highlighted_field.short_description = 'Ваше поле'

    actions = ['highlight_selected_objects']

    def highlight_selected_objects(self, request, queryset):
        # Здесь можно добавить логику для изменения объекта, если это необходимо
        pass

    highlight_selected_objects.short_description = 'Подчеркнуть красным выбранные объекты'
