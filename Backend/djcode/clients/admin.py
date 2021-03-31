from django.contrib import admin
from .models import ServiceCategory, Order, Client, Payment, Task, Key


admin.site.register(ServiceCategory)


class PaymentsInline(admin.StackedInline):
    model = Payment
    extra = 0


class TasksInline(admin.StackedInline):
    model = Task
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'client', 'total_cost', 'balance', 'date')
    search_fields = ('title', 'client__phone', 'client__name')
    list_filter = ('service', 'date', 'update')

    inlines = [TasksInline, PaymentsInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_sum', 'notice', 'date')
    search_fields = ('order__title', 'notice')
    list_filter = ('order', 'date')


class OrderInline(admin.StackedInline):
    model = Order
    classes = ('collapse',)
    extra = 0


class KeysInline(admin.TabularInline):
    model = Key
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date')
    search_fields = ('name', 'phone', 'email')
    list_filter = ('date', 'update')
    inlines = [OrderInline, KeysInline]
