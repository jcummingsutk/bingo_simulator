import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from bingo_simulator.bingo_card.bingo_card import BingoCard
from bingo_simulator.bingo_game import BingoGame

app = FastAPI()
handler = Mangum(app)


@app.get("/")
async def test():
    return {"test": "data_new_updating_with_ci"}


@app.post("/check_game")
async def check_game(
    card: BingoCard, pattern: list[tuple[int, int]], drawn_values: list[int]
):
    game = BingoGame(bingo_card=card, bingo_pattern=pattern, drawn_values=drawn_values)
    if game.check_winner():
        return {"game_won": True}
    return {"game_won": False}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
