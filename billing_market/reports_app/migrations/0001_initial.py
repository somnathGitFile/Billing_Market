# Generated by Django 4.0.5 on 2022-06-21 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyExpensesReport',
            fields=[
                ('daily_expenses_id', models.IntegerField(primary_key=True, serialize=False)),
                ('daily_expenses_total_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyPurchaseReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_purchase_orders', models.CharField(max_length=50)),
                ('daily_purchase_product_quantity', models.FloatField()),
                ('daily_purchase_product_total_price', models.FloatField()),
                ('daily_purchase_total_suppliers', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DailySaleReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_sale_product_quantity', models.IntegerField()),
                ('daily_sale_product_total_price', models.FloatField()),
                ('daily_sale_total_customers', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('expense_id', models.IntegerField(primary_key=True, serialize=False)),
                ('expense_use_for', models.CharField(max_length=50)),
                ('expense_amount', models.FloatField()),
                ('expense_datetime', models.DateTimeField()),
                ('dailyexpensesreport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reports_app.dailyexpensesreport')),
            ],
        ),
    ]
