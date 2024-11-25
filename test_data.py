from orders.models import Order, TechCard, InventoryItem

# Создаем заказ
order = Order(name="Заказ 1", description="Описание заказа", status="В работе")
order.save()

# Создаем техкарту
tech_card = TechCard(name="Техкарта 1", raw_materials="Материал 1, Материал 2", steps="Шаг 1, Шаг 2")
tech_card.save()

# Создаем складской объект
item = InventoryItem(name="Сырье 1", type="raw", quantity=100)
item.save()

print("Данные созданы успешно!")
