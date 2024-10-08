# Generated by Django 4.2.15 on 2024-08-26 22:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_cart_items_alter_cartitem_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="items",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="session_id",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="updated_at",
        ),
        migrations.RemoveField(
            model_name="cartitem",
            name="price",
        ),
        migrations.AddField(
            model_name="cart",
            name="session_key",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name="cartitem",
            name="added_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="cart",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="cart.cart",
            ),
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
