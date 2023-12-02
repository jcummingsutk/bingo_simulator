import numpy as np
import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from bingo_simulator.bingo_card.bingo_card import BingoCard
from bingo_simulator.bingo_card.bingo_card_generator import generate_bingo_card
from bingo_simulator.bingo_game import BingoGame
from bingo_simulator.random_number_generator import SampleWithoutReplacement

app = FastAPI()
handler = Mangum(app)


@app.get("/test")
async def test():
    return {"test": "data_new_updating_with_ci"}


@app.get("/bingo_card")
async def get_bingo_card(
    min_card_value: int, max_card_value: int, num_rows: int, num_cols: int
):
    possible_card_values = list(np.arange(min_card_value, max_card_value + 1))
    card_values_generator = SampleWithoutReplacement(possible_card_values)
    bingo_card = generate_bingo_card(
        nrows=num_rows,
        ncols=num_cols,
        random_number_generator=card_values_generator,
    )

    return bingo_card


@app.post("/check_game")
async def check_game(
    card: BingoCard, pattern: list[tuple[int, int]], drawn_values: list[int]
):
    game = BingoGame(bingo_card=card, bingo_pattern=pattern, drawn_values=drawn_values)
    if game.check_winner():
        return {"game_won": True}
    return {"game_won": False}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
