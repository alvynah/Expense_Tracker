# Generated by Django 3.2.12 on 2022-03-07 08:31

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseTracker', '0004_auto_20220307_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='quantity',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='KSH ', max_digits=14),
        ),
        migrations.AlterField(
            model_name='expense',
            name='quantity_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('KSH', 'Kenyan Shilling'), ('USD', 'US Dollar')], default='KSH ', editable=False, max_length=3),
        ),
    ]