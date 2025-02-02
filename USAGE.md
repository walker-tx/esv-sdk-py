<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from esv_sdk import Esv
import os

with Esv(
    api_key=os.getenv("ESV_API_KEY", ""),
) as esv:

    res = esv.passages.get_html(query="John 1:1")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from esv_sdk import Esv
import os

async def main():
    async with Esv(
        api_key=os.getenv("ESV_API_KEY", ""),
    ) as esv:

        res = await esv.passages.get_html_async(query="John 1:1")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->