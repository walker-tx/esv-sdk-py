# Passages

## Overview

### Available Operations

* [get_html](#get_html) - Get Bible passage HTML
* [search](#search) - Search Bible passages
* [get_audio](#get_audio) - Get Bible passage audio
* [get_text](#get_text) - Get Bible passage text

## get_html

Returns Bible passage text with HTML formatting

Esv.org API Docs for `/v3/passages/html`
<https://api.esv.org/docs/passage-html/>

### Example Usage: ChapterRange

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="ChapterRange" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="Genesis 1-3", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```
### Example Usage: CompactNotation

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="CompactNotation" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="jn11.35", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```
### Example Usage: DigitalRange

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="DigitalRange" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="01001001-01011032", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```
### Example Usage: MultiReference

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="MultiReference" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="John1.1;Genesis1.1", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```
### Example Usage: NumericalEncoding

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="NumericalEncoding" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="43011035", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```
### Example Usage: StandardReference

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="StandardReference" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="John 1:1", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```
### Example Usage: StructuredDigital

<!-- UsageSnippet language="python" operationID="getPassageHtml" method="get" path="/passage/html/" example="StructuredDigital" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="19001001-19001006,19003001-19003008", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Bible passage reference (e.g., "John 3:16" or "43011016")           |                                                                     |
| `include_passage_references`                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include passage references before passages                          | true                                                                |
| `include_verse_numbers`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include verse numbers                                               | true                                                                |
| `include_first_verse_numbers`                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include the verse number for the first verse of a chapter           | true                                                                |
| `include_footnotes`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include callouts to footnotes in the text.                          | true                                                                |
| `include_footnote_body`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include footnote body content                                       | true                                                                |
| `include_headings`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include passage headings                                            | true                                                                |
| `include_short_copyright`                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include a short copyright notice                                    | false                                                               |
| `include_copyright`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include the full copyright notice                                   | false                                                               |
| `include_passage_horizontal_lines`                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include horizontal lines between passages                           | false                                                               |
| `include_heading_horizontal_lines`                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include horizontal lines under headings                             | false                                                               |
| `horizontal_line_length`                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Length of horizontal lines                                          | 55                                                                  |
| `include_selahs`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include "Selah" in passage text                                     | true                                                                |
| `include_css_link`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include a link to the ESV API CSS file                              |                                                                     |
| `inline_styles`                                                     | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include inline styles on HTML elements                              |                                                                     |
| `wrapping_div`                                                      | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Wrap the HTML output in a div with class="esv"                      |                                                                     |
| `div_classes`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Classes to add to the wrapping div                                  |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PassageResponse](../../models/passageresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400, 401         | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## search

Returns search results for Bible passages based on the provided query

Esv.org API Docs for `/v3/passage/search`
<https://api.esv.org/docs/passage-search/>

### Example Usage

<!-- UsageSnippet language="python" operationID="searchPassages" method="get" path="/passage/search/" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.search(query="<value>", page_size=20, page=1)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The text to search for                                              |
| `page_size`                                                         | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of results to return per page                                |
| `page`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Page number to return                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SearchPassagesResponse](../../models/searchpassagesresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400, 401         | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_audio

Returns audio file for Bible passages based on the provided query

Esv.org API Docs for `/v3/passage/audio`
<https://api.esv.org/docs/passage-audio/>

### Example Usage: ChapterRange

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="ChapterRange" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="Genesis 1-3")

    # Handle response
    print(res)

```
### Example Usage: CompactNotation

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="CompactNotation" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="jn11.35")

    # Handle response
    print(res)

```
### Example Usage: DigitalRange

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="DigitalRange" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="01001001-01011032")

    # Handle response
    print(res)

```
### Example Usage: MultiReference

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="MultiReference" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="John1.1;Genesis1.1")

    # Handle response
    print(res)

```
### Example Usage: NumericalEncoding

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="NumericalEncoding" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="43011035")

    # Handle response
    print(res)

```
### Example Usage: StandardReference

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="StandardReference" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="John 1:1")

    # Handle response
    print(res)

```
### Example Usage: StructuredDigital

<!-- UsageSnippet language="python" operationID="getPassageAudio" method="get" path="/passage/audio/" example="StructuredDigital" -->
```python
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_audio(query="19001001-19001006,19003001-19003008")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Bible passage reference (e.g., "John 3:16" or "43011016")           |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[httpx.Response](../../models/.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400, 401         | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |

## get_text

Returns Bible passage text based on the provided query parameters

Esv.org API Docs for `/v3/passages/text`
<https://api.esv.org/docs/passage-text/>

### Example Usage: ChapterRange

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="ChapterRange" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="Genesis 1-3", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```
### Example Usage: CompactNotation

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="CompactNotation" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="jn11.35", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```
### Example Usage: DigitalRange

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="DigitalRange" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="01001001-01011032", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```
### Example Usage: MultiReference

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="MultiReference" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="John1.1;Genesis1.1", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```
### Example Usage: NumericalEncoding

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="NumericalEncoding" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="43011035", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```
### Example Usage: StandardReference

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="StandardReference" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="John 1:1", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```
### Example Usage: StructuredDigital

<!-- UsageSnippet language="python" operationID="getPassageText" method="get" path="/passage/text/" example="StructuredDigital" -->
```python
import esv_sdk
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_text(query="19001001-19001006,19003001-19003008", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, indent_using=esv_sdk.IndentUsing.SPACE, indent_paragraphs=2, indent_poetry=2, indent_poetry_lines=4, indent_declares=40, indent_psalm_doxology=30, line_length=0)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query`                                                             | *str*                                                               | :heavy_check_mark:                                                  | Bible passage reference (e.g., "John 3:16" or "43011016")           |                                                                     |
| `include_passage_references`                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include passage references before passages                          | true                                                                |
| `include_verse_numbers`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include verse numbers                                               | true                                                                |
| `include_first_verse_numbers`                                       | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include the verse number for the first verse of a chapter           | true                                                                |
| `include_footnotes`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include callouts to footnotes in the text.                          | true                                                                |
| `include_footnote_body`                                             | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include footnote body content                                       | true                                                                |
| `include_headings`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include passage headings                                            | true                                                                |
| `include_short_copyright`                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include a short copyright notice                                    | false                                                               |
| `include_copyright`                                                 | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include the full copyright notice                                   | false                                                               |
| `include_passage_horizontal_lines`                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include horizontal lines between passages                           | false                                                               |
| `include_heading_horizontal_lines`                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include horizontal lines under headings                             | false                                                               |
| `horizontal_line_length`                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Length of horizontal lines                                          | 55                                                                  |
| `include_selahs`                                                    | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Include "Selah" in passage text                                     | true                                                                |
| `indent_using`                                                      | [Optional[models.IndentUsing]](../../models/indentusing.md)         | :heavy_minus_sign:                                                  | Character to use for indentation                                    |                                                                     |
| `indent_paragraphs`                                                 | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of indentation characters for paragraphs                     |                                                                     |
| `indent_poetry`                                                     | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of indentation characters for poetry                         |                                                                     |
| `indent_poetry_lines`                                               | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of indentation characters for poetry lines                   |                                                                     |
| `indent_declares`                                                   | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of indentation characters for declares                       |                                                                     |
| `indent_psalm_doxology`                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Number of indentation characters for Psalm doxology                 |                                                                     |
| `line_length`                                                       | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Maximum line length                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.PassageResponse](../../models/passageresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| models.Error     | 400, 401         | application/json |
| models.APIError  | 4XX, 5XX         | \*/\*            |