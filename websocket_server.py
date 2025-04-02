import asyncio
import websockets
import random
import json

async def stock_prices(websocket, path):
    while True:
        stock_data = {
            "AAPL": round(random.uniform(140, 150), 2),
            "GOOGL": round(random.uniform(2700, 2800), 2)
        }
        await websocket.send(json.dumps(stock_data))
        await asyncio.sleep(5)

start_server = websockets.serve(stock_prices, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
