import json

from models.places import PlaceModel
from typing import Optional


class PlacesService:
    """
    Сервис для работы с данными о любимых местах.
    """

    @staticmethod
    def create_place(place: dict) -> PlaceModel:
        return PlaceModel(
            id=place.get("id"),
            latitude=place.get("latitude"),
            longitude=place.get("longitude"),
            description=place.get("description"),
            country=place.get("country"),
            city=place.get("city"),
            locality=place.get("locality"),
            created_at=place.get("created_at"),
            updated_at=place.get("updated_at"),
        )

    def get_places(self) -> list[PlaceModel]:
        """
        Получение списка любимых мест.

        :return:
        """

        result = []
        with open("fixtures/places.json", encoding="utf-8") as file:
            if data := json.load(file):
                result = [
                    self.create_place(place)
                    for place in data.get("data", [])
                ]

        return result

    def get_place(self, id: int) -> Optional[PlaceModel]:
        """
        Получение списка любимых мест.

        :return:
        """

        result = None
        with open("fixtures/places.json", encoding="utf-8") as file:
            if data := json.load(file):
                places = data.get("data", [])
                result = [
                    self.create_place(place)
                    for place in places if place["id"] == id
                ]
                return result[0] if len(result) > 0 else None

        return result
