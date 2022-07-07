import osutools
import json

OSU_LOCATION = "D:\\osu! ranked"

osu = osutools.osuclient.OsuClientV1("token")
osu.set_osu_folder(OSU_LOCATION)

beatmap_ids = [beatmap.beatmap_id for beatmap in osu.osu_db.map_list()]

with open("beatmap_list.json", "w+") as f:
    json.dump({"beatmaps": beatmap_ids}, f)