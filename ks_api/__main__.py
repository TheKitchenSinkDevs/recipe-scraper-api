import string

from fastapi import FastAPI, HTTPException
from recipe_scrapers import scrape_me
from recipe_scrapers._exceptions import WebsiteNotImplementedError
from base64 import b64encode, b64decode
import logging

from .routers import units

app = FastAPI()

app.include_router(units.router)

log = logging.getLogger("RECIPIE_SCRAPER")
log.setLevel(logging.INFO)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/parse/{url}")
async def parse(url: str):
    url = b64decode(url).decode('utf-8')
    log.info(url)
    try:
        scraped = scrape_me(url)
        ingredients = parse_ingredients(scraped.ingredients())
        failed = False
    except AttributeError as err:
        raise HTTPException(status_code=400, detail="Site Not supported")
    except BaseException as err:
        import pdb; pdb.set_trace()
        log.error("Unexpected Exception")
        log.error(err)
        failed = True

    if failed:
        return {"message": "Failed to scrape url"}
    else:
        recipe = {
                "Name": scraped.title(),
                "url": scraped.url,
                "image": scraped.image(),
                "yields": scraped.yields(),
                "ingredients": ingredients,
                "instructions": scraped.instructions().split("\n")
                }
        return {"message": "Site Scraped!",
                "recipe": recipe}

def parse_ingredients(ingredients: "list[str]"):
    output = []
    for line in ingredients:
        words = line.split(" ")
        for idx, word in enumerate(words):
            if word in [digit for digit in string.digits]:
                number = int(word)
                measurement = words[idx + 1]
                if number > 1 and measurement[-1] == 's':
                    measurement = measurement[:-1]
                food = " ".join(words[idx + 2:])
                output.append({
                        "food": food,
                        "quantity": number,
                        "measurement": measurement
                        })
                break

    return output



