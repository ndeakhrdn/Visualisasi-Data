from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person
from .models import Fakulti


@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Fakulti)
class FakultiAdmin(ImportExportModelAdmin):
    pass



