from pydantic import BaseModel


class NnInput(BaseModel):
    geo_lat: float
    geo_lon: float
    level: int
    levels: int
    rooms: int
    area: float
    object_type: int

    class Config:
        schema_extra = {
            "example": {
                "geo_lat": 55.683807,
                "geo_lon": 37.297405,
                "level": 5,
                "levels": 24,
                "rooms": 2,
                "area": 69.1,
                "object_type": 2
            }
        }