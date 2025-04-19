import asyncio
import websockets

url = "wss://ws.bitstamp.net"

def test_url(url, data=""):
    async def inner():
        async with websockets.connect(url) as websocket:
            await websocket.send(data)
    return asyncio.get_event_loop().run_until_complete(inner())

json_data = {
    "data": [
        {
            "type": "block",
            "id": "1",
            "attributes": {
                "shape": "square",
                "created": "2029-05-22T14:56:29.000Z",
                "updated": "2029-05-22T14:56:28.000Z"
            }
        }
    ]
}

subscripton = {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}

test_url(url, subscripton)