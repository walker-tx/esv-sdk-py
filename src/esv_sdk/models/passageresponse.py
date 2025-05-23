"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .passagemeta import PassageMeta, PassageMetaTypedDict
from esv_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PassageResponseTypedDict(TypedDict):
    query: NotRequired[str]
    r"""The passage reference that was requested"""
    canonical: NotRequired[str]
    r"""The canonical version of the passage reference"""
    parsed: NotRequired[List[List[int]]]
    r"""Array of parsed passage references"""
    passage_meta: NotRequired[List[PassageMetaTypedDict]]
    passages: NotRequired[List[str]]
    r"""Array of formatted passage text"""


class PassageResponse(BaseModel):
    query: Optional[str] = None
    r"""The passage reference that was requested"""

    canonical: Optional[str] = None
    r"""The canonical version of the passage reference"""

    parsed: Optional[List[List[int]]] = None
    r"""Array of parsed passage references"""

    passage_meta: Optional[List[PassageMeta]] = None

    passages: Optional[List[str]] = None
    r"""Array of formatted passage text"""
