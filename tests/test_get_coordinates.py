import pytest
import responses

from functions.get_coordinates import get_coordinates, Coordinates


@responses.activate
def test_get_coordinates_city():
    valid_json_answer = [
        {
            "place_id": 211282847,
            "licence": "Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright",
            "osm_type": "way",
            "osm_id": 113246147,
            "lat": "51.198559",
            "lon": "49.72654",
            "class": "place",
            "type": "town",
            "place_rank": 18,
            "importance": 0.3259285856241072,
            "addresstype": "town",
            "name": "Озинки",
            "display_name": "Озинки, Озинское городское поселение, Озинский район, Саратовская область, Приволжский федеральный округ, Россия",
            "boundingbox": [
                "51.1841321",
                "51.2116463",
                "49.6960640",
                "49.7602973"
            ]
        }
    ]
    responses.add(method=responses.GET, url="https://nominatim.openstreetmap.org/search?q=Ozinki&format=json&limit=1",
                  json=valid_json_answer, status=200)

    assert get_coordinates("Ozinki") == Coordinates(latitude=51.198559, longitude=49.72654)


def test_get_empty_value():
    with pytest.raises(ValueError):
        get_coordinates("")
