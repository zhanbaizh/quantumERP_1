from rest_framework.test import APITestCase
from rest_framework import status
from .models import TechCard

class TechCardAPITestCase(APITestCase):
    def setUp(self):
        self.tech_card = TechCard.objects.create(
            name="Техкарта 1",
            raw_materials="Сырье A, Сырье B",
            steps="Шаг 1 -> Шаг 2"
        )
        self.list_url = '/api/techcards/'

    def test_list_techcards(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_techcard(self):
        data = {
            "name": "Техкарта 2",
            "raw_materials": "Сырье C, Сырье D",
            "steps": "Шаг 1 -> Шаг 2 -> Шаг 3"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TechCard.objects.count(), 2)

    def test_update_techcard(self):
        data = {
            "name": "Обновленная техкарта",
            "raw_materials": "Сырье E, Сырье F",
            "steps": "Шаг 1 -> Шаг 2 -> Шаг 3 -> Шаг 4"
        }
        response = self.client.put(f'/api/techcards/{self.tech_card.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.tech_card.refresh_from_db()
        self.assertEqual(self.tech_card.name, "Обновленная техкарта")

    def test_delete_techcard(self):
        response = self.client.delete(f'/api/techcards/{self.tech_card.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TechCard.objects.count(), 0)
