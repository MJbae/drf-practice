from django.contrib import admin
from .models import Dog, Owner, Customer, Transaction, OtherTransaction, Currency, OtherCurrency

admin.site.register(Dog)
admin.site.register(Owner)
admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(OtherCurrency)
admin.site.register(Transaction)
admin.site.register(OtherTransaction)
