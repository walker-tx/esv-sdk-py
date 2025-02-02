# PassageResponse


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `query`                                              | *Optional[str]*                                      | :heavy_minus_sign:                                   | The passage reference that was requested             |
| `canonical`                                          | *Optional[str]*                                      | :heavy_minus_sign:                                   | The canonical version of the passage reference       |
| `parsed`                                             | List[List[*int*]]                                    | :heavy_minus_sign:                                   | Array of parsed passage references                   |
| `passage_meta`                                       | List[[models.PassageMeta](../models/passagemeta.md)] | :heavy_minus_sign:                                   | N/A                                                  |
| `passages`                                           | List[*str*]                                          | :heavy_minus_sign:                                   | Array of formatted passage text                      |