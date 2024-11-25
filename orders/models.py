from django.db import models

# Модель для заказов
class Order(models.Model):
    name = models.CharField(max_length=255)  # Название заказа
    description = models.TextField()  # Описание заказа
    status = models.CharField(max_length=50)  # Статус заказа
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return self.name

# Модель для техкарт
class TechCard(models.Model):
    name = models.CharField(max_length=255)  # Название техкарты
    raw_materials = models.TextField()  # Список сырья
    steps = models.TextField()  # Этапы производства

    def __str__(self):
        return self.name

# Модель для складских объектов
class InventoryItem(models.Model):
    ITEM_TYPES = [
        ('raw', 'Сырье'),
        ('semi', 'Полуфабрикат'),
        ('finished', 'Готовая продукция'),
        ('consumable', 'Расходник'),
    ]
    name = models.CharField(max_length=255)  # Название объекта
    type = models.CharField(max_length=50, choices=ITEM_TYPES)  # Тип объекта
    quantity = models.IntegerField()  # Количество

    def __str__(self):
        return self.name
