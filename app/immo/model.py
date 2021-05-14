from pydantic.main import BaseModel


class City(BaseModel):
    nom: str
    code: str
    codeDepartement: str
    codeRegion: str
