from django.contrib import admin
from .models import GotapTransactions, KnetTransactions, Transactions

class GotapTransactionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(GotapTransactions, GotapTransactionsAdmin)

class KnetTransactionsAdmin(admin.ModelAdmin):
    pass 
admin.site.register(KnetTransactions, KnetTransactionsAdmin)

class TransactionsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Transactions, TransactionsAdmin)


