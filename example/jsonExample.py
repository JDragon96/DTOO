import dtoo.forJson as jsonParser
from dtoo.forModel import DataClassWrapper
from typing import List

@DataClassWrapper
class TwitData_ReferencedTweets:
    type: str = None
    id: str = None

@DataClassWrapper
class TwitData_PublicMetrics:
    retweet_count: int = None
    reply_count: int = None
    like_count: int = None
    quote_count: int = None

@DataClassWrapper
class TwitData_Geo:
    place_id: str = None

@DataClassWrapper
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
    # referenced_tweets: List[TwitData_ReferencedTweets]= None

@DataClassWrapper
class Meta:
    newest_id: str = None
    oldest_id: str = None
    result_count: int = None
    next_token: str = None

@DataClassWrapper
class HttpRespons:
    data: List[TwitData] = None
    meta: Meta = None


json_data = jsonParser.loadJson(r"/dtoo\data\myJson.json", encoding="UTF-8")
response_parsing = HttpRespons()
jsonParser.Serialization(json_data, response_parsing)

print(response_parsing.meta.oldest_id)
print(response_parsing.data[0].text)