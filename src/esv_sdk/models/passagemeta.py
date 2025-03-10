"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from esv_sdk.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PassageMetaTypedDict(TypedDict):
    canonical: NotRequired[str]
    chapter_start: NotRequired[List[int]]
    chapter_end: NotRequired[List[int]]
    prev_verse: NotRequired[int]
    next_verse: NotRequired[int]
    prev_chapter: NotRequired[List[int]]
    next_chapter: NotRequired[List[int]]


class PassageMeta(BaseModel):
    canonical: Optional[str] = None

    chapter_start: Optional[List[int]] = None

    chapter_end: Optional[List[int]] = None

    prev_verse: Optional[int] = None

    next_verse: Optional[int] = None

    prev_chapter: Optional[List[int]] = None

    next_chapter: Optional[List[int]] = None
