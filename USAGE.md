<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from esv_sdk import Esv
import os


with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="John 1:1", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from esv_sdk import Esv
import os

async def main():

    async with Esv(
        api_key=os.getenv("ESV_API_KEY", ""),
    ) as esv:

        res = await esv.passages.get_html_async(query="John 1:1", include_passage_references=True, include_verse_numbers=True, include_first_verse_numbers=True, include_footnotes=True, include_footnote_body=True, include_headings=True, include_short_copyright=False, include_copyright=False, include_passage_horizontal_lines=False, include_heading_horizontal_lines=False, horizontal_line_length=55, include_selahs=True, include_css_link=True, inline_styles=False, wrapping_div=True, div_classes="esv")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->