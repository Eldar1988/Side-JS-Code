from django.contrib import admin
from .models import ServiceCategory, Order, Client, Payment, Task, Key


admin.site.register(ServiceCategory)


class PaymentsInline(admin.TabularInline):
    model = Payment
    extra = 0


class TasksInline(admin.TabularInline):
    model = Task
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'client', 'total_cost', 'balance', 'date')
    search_fields = ('title', 'client__phone', 'client_name')
    list_filter = ('service', 'date', 'update')

    inlines = [TasksInline, PaymentsInline]


class OrderInline(admin.TabularInline):
    model = Order
    show_change_link = ('title',)
    readonly_fields = ('title',)
    fields = ('title', 'date')


class KeysInline(admin.TabularInline):
    model = Key
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('date', 'update')
    inlines = [OrderInline, KeysInline]
