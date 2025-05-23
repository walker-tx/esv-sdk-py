"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from esv_sdk.types import BaseModel
from esv_sdk.utils import FieldMetadata, QueryParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class IndentUsing(str, Enum):
    r"""Character to use for indentation"""

    SPACE = "space"
    TAB = "tab"


class GetPassageTextRequestTypedDict(TypedDict):
    query: str
    r"""Bible passage reference (e.g., \"John 3:16\" or \"43011016\")"""
    include_passage_references: NotRequired[bool]
    r"""Include passage references before passages"""
    include_verse_numbers: NotRequired[bool]
    r"""Include verse numbers"""
    include_first_verse_numbers: NotRequired[bool]
    r"""Include the verse number for the first verse of a chapter"""
    include_footnotes: NotRequired[bool]
    r"""Include callouts to footnotes in the text."""
    include_footnote_body: NotRequired[bool]
    r"""Include footnote body content"""
    include_headings: NotRequired[bool]
    r"""Include passage headings"""
    include_short_copyright: NotRequired[bool]
    r"""Include a short copyright notice"""
    include_copyright: NotRequired[bool]
    r"""Include the full copyright notice"""
    include_passage_horizontal_lines: NotRequired[bool]
    r"""Include horizontal lines between passages"""
    include_heading_horizontal_lines: NotRequired[bool]
    r"""Include horizontal lines under headings"""
    horizontal_line_length: NotRequired[int]
    r"""Length of horizontal lines"""
    include_selahs: NotRequired[bool]
    r"""Include \"Selah\" in passage text"""
    indent_using: NotRequired[IndentUsing]
    r"""Character to use for indentation"""
    indent_paragraphs: NotRequired[int]
    r"""Number of indentation characters for paragraphs"""
    indent_poetry: NotRequired[int]
    r"""Number of indentation characters for poetry"""
    indent_poetry_lines: NotRequired[int]
    r"""Number of indentation characters for poetry lines"""
    indent_declares: NotRequired[int]
    r"""Number of indentation characters for declares"""
    indent_psalm_doxology: NotRequired[int]
    r"""Number of indentation characters for Psalm doxology"""
    line_length: NotRequired[int]
    r"""Maximum line length"""


class GetPassageTextRequest(BaseModel):
    query: Annotated[
        str,
        pydantic.Field(alias="q"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Bible passage reference (e.g., \"John 3:16\" or \"43011016\")"""

    include_passage_references: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-passage-references"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include passage references before passages"""

    include_verse_numbers: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-verse-numbers"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include verse numbers"""

    include_first_verse_numbers: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-first-verse-numbers"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include the verse number for the first verse of a chapter"""

    include_footnotes: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-footnotes"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include callouts to footnotes in the text."""

    include_footnote_body: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-footnote-body"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include footnote body content"""

    include_headings: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-headings"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include passage headings"""

    include_short_copyright: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-short-copyright"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include a short copyright notice"""

    include_copyright: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-copyright"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include the full copyright notice"""

    include_passage_horizontal_lines: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-passage-horizontal-lines"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include horizontal lines between passages"""

    include_heading_horizontal_lines: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-heading-horizontal-lines"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = False
    r"""Include horizontal lines under headings"""

    horizontal_line_length: Annotated[
        Optional[int],
        pydantic.Field(alias="horizontal-line-length"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 55
    r"""Length of horizontal lines"""

    include_selahs: Annotated[
        Optional[bool],
        pydantic.Field(alias="include-selahs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Include \"Selah\" in passage text"""

    indent_using: Annotated[
        Optional[IndentUsing],
        pydantic.Field(alias="indent-using"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = IndentUsing.SPACE
    r"""Character to use for indentation"""

    indent_paragraphs: Annotated[
        Optional[int],
        pydantic.Field(alias="indent-paragraphs"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 2
    r"""Number of indentation characters for paragraphs"""

    indent_poetry: Annotated[
        Optional[int],
        pydantic.Field(alias="indent-poetry"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 2
    r"""Number of indentation characters for poetry"""

    indent_poetry_lines: Annotated[
        Optional[int],
        pydantic.Field(alias="indent-poetry-lines"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 4
    r"""Number of indentation characters for poetry lines"""

    indent_declares: Annotated[
        Optional[int],
        pydantic.Field(alias="indent-declares"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 40
    r"""Number of indentation characters for declares"""

    indent_psalm_doxology: Annotated[
        Optional[int],
        pydantic.Field(alias="indent-psalm-doxology"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 30
    r"""Number of indentation characters for Psalm doxology"""

    line_length: Annotated[
        Optional[int],
        pydantic.Field(alias="line-length"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Maximum line length"""
