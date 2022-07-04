import inspect

import dtoo.forJson as jsonParser
from dtoo.forModel import dataclass_wrapper
from typing import List

@dataclass_wrapper
class TwitData_ReferencedTweets:
    type: str = None
    id: str = None

@dataclass_wrapper
class TwitData_PublicMetrics:
    retweet_count: int = None
    reply_count: int = None
    like_count: int = None
    quote_count: int = None

@dataclass_wrapper
class TwitData_Geo:
    place_id: str = None

@dataclass_wrapper
class TwitData:
    source: str = None
    id: str = None
    conversation_id: str = None
    created_at: str = None
    lang: str = None
    geo: TwitData_Geo = None
    author_id: str = None
    reply_settings: str = None
    text: str = None
    public_metrics: TwitData_PublicMetrics = None

@dataclass_wrapper
class Meta:
    newest_id: str = None
    oldest_id: str = None
    result_count: int = None
    next_token: str = None

@dataclass_wrapper
class HttpRespons:
    data: List[TwitData] = None
    meta: Meta = None

json_data = jsonParser.loadJson(r"myJson.json", encoding="UTF-8")
deserializeObj = jsonParser.Deserialization(json_data, HttpRespons)
serializeObj = jsonParser.Serialization(deserializeObj)