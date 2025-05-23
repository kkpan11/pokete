# DO NOT EDIT!
# This code was auto generated by the `protoc-gen-pokete-resources-python` plugin,
# part of the pokete project, by <lxgr@protonmail.com>
from typing import TypedDict


class ItemDict(TypedDict):
    pretty_name: str
    desc: str
    price: int | None
    fn: str | None


class Item:
    def __init__(
        self,
        pretty_name: str,
        desc: str,
        price: int | None,
        fn: str | None
    ):
        self.pretty_name: str = pretty_name
        self.desc: str = desc
        self.price: int | None = price
        self.fn: str | None = fn

    @classmethod
    def from_dict(cls, _d: ItemDict | None) -> "Item | None":
        if _d is None:
            return None
        return cls(
            pretty_name=_d["pretty_name"],
            desc=_d["desc"],
            price=_d.get("price", None),
            fn=_d.get("fn", None),
        )

    @staticmethod
    def validate(_d: ItemDict) -> bool:
        return all([
            "pretty_name" in _d and type(_d["pretty_name"]) is str,
            "desc" in _d and type(_d["desc"]) is str,
            type(_d.get("price", None)) is int or _d.get("price", None) is None,
            type(_d.get("fn", None)) is str or _d.get("fn", None) is None,
        ])

    def to_dict(self) -> ItemDict:
        ret: ItemDict = {}
        
        ret["pretty_name"] = self.pretty_name
        ret["desc"] = self.desc
        if self.price is not None:
            ret["price"] = self.price
        if self.fn is not None:
            ret["fn"] = self.fn

        return ret
