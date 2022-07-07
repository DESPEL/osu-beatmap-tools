import osutools

data = None
def update():
    global data
    OSU_LOCATION = "D:\\osu! ranked"
    osu = osutools.osuclient.OsuClientV1("token")
    osu.set_osu_folder(OSU_LOCATION)
    beatmap_ids = [beatmap.mapset_id for beatmap in osu.osu_db.map_list()]
    data = {"beatmaps": beatmap_ids}


update()
from fastapi import FastAPI
app = FastAPI()

@app.get("/beatmaps")
def beatmaps():
  return data

@app.get("/refresh")
def beatmaps():
    update()
    print("refreshing beatmaps")
    return "beatmaps updated"