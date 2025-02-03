from django.contrib import admin
from faqs.models import Language, FAQ  
# Register your models here.



admin.site.site_header = 'Django FAQ Translate'  

class FAQAdmin(admin.ModelAdmin):
    # Method to return the language names as a comma-separated string
    def get_languages(self, obj):
        return ", ".join([language.name for language in obj.languages.all()])
    get_languages.short_description = 'Languages'  
    
    # Add the custom method to the list_display
    list_display = ['question', 'get_languages']

    # Optionally, filter by languages in the sidebar
    list_filter = ['languages']


admin.site.register(Language)
admin.site.register(FAQ, FAQAdmin)

