# docker-open-street-map-practice

## Requirements

- docker
- osm.pbf file (Downloading Kanto Japan data is introduced later.)

## Setup

```sh
docker compose up
```

You can see map on http://localhost:8000 after loading map data.

## Put kanto of Japan to DB

```sh
cd [this repo]
wget -P ./postgis https://download.geofabrik.de/asia/japan/kanto-latest.osm.pbf
```

```sh
docker compose exec postgis bash
```
```sh
osm2pgsql \
  -d $POSTGRES_DB \
  -P 5432 \
  -U $POSTGRES_USER \
  --create \
  --slim \
  --multi-geometry \
  --cache 2000 \
  ./kanto-latest.osm.pbf
```

## References

- [OpenStreetMapデータから地図を作成する](https://qiita.com/studio_haneya/items/255c876893f6f1f5214c)
- [OSMデータをPostGISにインポートしてQGISで可視化する](https://qiita.com/hiyuzawa/items/ba1b9de36bf911145c1c)
- [Rendering a map with Mapnik and PostGIS](https://help.openstreetmap.org/questions/24833/rendering-a-map-with-mapnik-and-postgis/)
