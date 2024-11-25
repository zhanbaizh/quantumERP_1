from rest_framework.test import APITestCase
from rest_framework import status
from .models import Order

class OrderAPITestCase(APITestCase):
    # Указываем фикстуры для предварительного заполнения базы данных
    fixtures = ['orders/fixtures/orders.json']

    # Тест получения списка заказов
    def test_list_orders(self):
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Проверяем, что загрузилось 2 объекта из фикстуры

    # Тест создания нового заказа
    def test_create_order(self):
        data = {
            "name": "Новый заказ",
            "description": "Описание нового заказа",
            "status": "новый"
        }
        response = self.client.post('/api/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 3)  # Проверяем, что заказов стало 3

    # Тест обновления заказа
    def test_update_order(self):
        data = {
            "name": "Обновленный заказ",
            "description": "Обновленное описание",
            "status": "завершен"
        }
        response = self.client.put('/api/orders/1/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        order = Order.objects.get(pk=1)
        self.assertEqual(order.name, "Обновленный заказ")  # Проверяем, что имя обновилось
        self.assertEqual(order.status, "завершен")  # Проверяем, что статус обновился

    # Тест удаления заказа
    def test_delete_order(self):
        response = self.client.delete('/api/orders/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 1)  # Проверяем, что остался только 1 заказ

    # Тест на проверку ошибок при создании
    def test_create_order_invalid_data(self):
        data = {"name": ""}  # Пустое имя заказа
        response = self.client.post('/api/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)  # Проверяем, что ошибка связана с полем name

    # Тест на фильтрацию заказов по статусу
    def test_filter_orders(self):
        response = self.client.get('/api/orders/', {"status": "новый"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Проверяем, что нашелся только 1 заказ с таким статусом

    # Тест на поиск заказов по имени
    def test_search_orders(self):
        response = self.client.get('/api/orders/', {"search": "Тестовый заказ 1"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
