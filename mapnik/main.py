from fastapi import FastAPI, Query
from fastapi.responses import Response
import mapnik
import time

app = FastAPI()

@app.get("/map")
def render_map(z: int = Query(10), x: int = Query(1000), y: int = Query(1000)):
    # m = mapnik.Map(256, 256)
    time_start = time.time()
    px_width = 600
    px_height = 400
    m = mapnik.Map(px_width, px_height)
    mapnik.load_map(m, "style.xml")  # Mapnik XMLファイルを用意しておく

    m.background = mapnik.Color('ghostwhite')
    # m.zoom_all()
    # area = mapnik.Box2d(-180.0, -90.0, 180.0, 90.0)
    # area = mapnik.Box2d(0, 0, 180.0, 90.0)
    # area = mapnik.Envelope(139.18430749155274, 36.06460782132949, 139.4172157248683, 36.25925904331936)
    area = mapnik.Box2d(139.4172157248683, 36.06460782132949, 139.18430749155274, 36.25925904331936)
    # area = mapnik.Box2d(36.06460782132949, 139.18430749155274, 36.25925904331936, 139.4172157248683)
    # area = mapnik.Box2d(35.82868723332095, 138.6976890886359, 36.348001206983106, 139.83213235475225)
    # area = mapnik.Box2d(138, 35, 140, 37)
    bbox=(area)
    m.zoom_to_box(bbox)

    time_finish_loading = time.time()
    print("time of loading %.3lf seconds" % (time_finish_loading - time_start))
    im = mapnik.Image(px_width, px_height)
    mapnik.render(m, im)
    time_end = time.time()
    print("time of rendering %.3lf seconds" % (time_end - time_finish_loading))

    im.save('file.png','png32:z=1')
    png = im.tostring("png")

    return Response(content=png, media_type="image/png")
