"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from esv_sdk.types import BaseModel
from esv_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Callable, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SearchPassagesRequestTypedDict(TypedDict):
    query: str
    r"""The text to search for"""
    page_size: NotRequired[int]
    r"""Number of results to return per page"""
    page: NotRequired[int]
    r"""Page number to return"""


class SearchPassagesRequest(BaseModel):
    query: Annotated[
        str,
        pydantic.Field(alias="q"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""The text to search for"""

    page_size: Annotated[
        Optional[int],
        pydantic.Field(alias="page-size"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 20
    r"""Number of results to return per page"""

    page: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""Page number to return"""


class VersesTypedDict(TypedDict):
    verse: NotRequired[str]
    r"""Verse reference"""
    text: NotRequired[str]
    r"""Verse text"""


class Verses(BaseModel):
    verse: Optional[str] = None
    r"""Verse reference"""

    text: Optional[str] = None
    r"""Verse text"""


class ResultsTypedDict(TypedDict):
    reference: NotRequired[str]
    r"""The passage reference"""
    content: NotRequired[str]
    r"""The matching passage content"""
    verses: NotRequired[List[VersesTypedDict]]


class Results(BaseModel):
    reference: Optional[str] = None
    r"""The passage reference"""

    content: Optional[str] = None
    r"""The matching passage content"""

    verses: Optional[List[Verses]] = None


class SearchPassagesResponseBodyTypedDict(TypedDict):
    r"""Successful response"""

    page: NotRequired[int]
    r"""Current page number"""
    total_pages: NotRequired[int]
    r"""Total number of pages"""
    total_results: NotRequired[int]
    r"""Total number of results"""
    results: NotRequired[List[ResultsTypedDict]]


class SearchPassagesResponseBody(BaseModel):
    r"""Successful response"""

    page: Optional[int] = None
    r"""Current page number"""

    total_pages: Optional[int] = None
    r"""Total number of pages"""

    total_results: Optional[int] = None
    r"""Total number of results"""

    results: Optional[List[Results]] = None


class SearchPassagesResponseTypedDict(TypedDict):
    result: SearchPassagesResponseBodyTypedDict


class SearchPassagesResponse(BaseModel):
    next: Callable[[], Optional[SearchPassagesResponse]]

    result: SearchPassagesResponseBody
