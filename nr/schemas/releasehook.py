from pydantic import BaseModel, Field
from datetime import datetime

class Note(BaseModel):
    title: str
    message: str

class Account(BaseModel):
    _type: Field(str, alias="type")
    _id: Field(str, alias="id")
    name: str

class ReleaseHook(BaseModel):
    provider: str
    project: str
    version: str
    time: datetime
    is_prerelease: bool
    is_updated: bool
    note: Note
    account: Account

    class Config:
        schema_extra = {
            "provider": "github",
            "project": "nodejs/node",
            "version": "v11.5.0",
            "time": "2018-12-30T16:08:51.864468Z",
            "is_prerelease": True,
            "is_updated": True,
            "note": {
                "title": "Release v11.5.0",
                "message": "Release features\u003cbr\u003eBugfixes"
            },
            "account": {
                "type": "user",
                "id": "fwykdar796rkd6s2hwmqvhpsd1",
                "name": "My Account Name"
            }
        }
