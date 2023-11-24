from fastapi import FastAPI

from bingo_simulator.bingo_card.bingo_card import BingoCard
from bingo_simulator.bingo_game import BingoGame

app = FastAPI()


@app.get("/")
async def check_board(
    card: BingoCard, pattern: list[tuple[int, int]], drawn_values: list[int]
):
    game = BingoGame(bingo_card=card, bingo_pattern=pattern, drawn_values=drawn_values)
    if game.check_winner():
        return {"result": True}
    return {"result": False}
