from .adminStackedInline import ( admin,
    UserAdminStackedInline
)




class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Student', {
            'fields': ['__all__']}
         )
    ]
    inlines = [UserAdminStackedInline]