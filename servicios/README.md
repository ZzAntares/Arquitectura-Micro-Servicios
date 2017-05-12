# Servicios

En esta carpeta se definen los servicios utilizados en la tarea 2 dentro del Sistema de Procesamiento de Comentarios (SPC). La especificación de los servicios se realizó utilizando blueprint de Apiary.

La documentación esta disponible en el repositorio en la carpeta de `docs` o también puede consultarse en línea a través de Apiary:

- [SV Information API](http://docs.svinformationapi.apiary.io/)
- [SV Tweets API](http://docs.svtweetsapi.apiary.io/)
- [SV Sentiment API](http://docs.svsentimentapi.apiary.io/)


Para una rápida referencia se incluye aquí la especificación de los microservicios, la cual es la siguiente:

## SV Information API (Procesador de Comentarios de IMDb)

FORMAT: 1A

Su función general es proporcionar en un objeto `JSON` información detallada
acerca de una película o una serie en particular haciendo uso del API
proporcionada por IMDb (`https://www.imdb.com/`).

# Group Information
Recursos de **SV Information API**.

## Information [/information{?t}]
### Obtiene información de una película [GET]

+ Parameters
    + t (required, string) ... Es el título de la película a consultar.

+ Request (application/x-www-form-urlencoded)

        t=Stranger+things

+ Response 200 (application/json)

        {
            "Title": "Stranger Things",
            "Year": "2016–",
            "Rated": "TV-14",
            "Released": "15 Jul 2016",
            "Runtime": "55 min",
            "Genre": "Drama, Fantasy, Horror",
            "Director": "N/A",
            "Writer": "Matt Duffer, Ross Duffer",
            "Actors": "Winona Ryder, David Harbour, Finn Wolfhard, Millie Bobby Brown",
            "Plot": "When a young boy disappears, his mother, a police chief, and his friends must confront terrifying forces in order to get him back.",
            "Language": "English",
            "Country": "USA",
            "Awards": "Nominated for 2 Golden Globes. Another 7 wins & 43 nominations.",
            "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzMDAxOTUyMV5BMl5BanBnXkFtZTgwNzAxMzYzOTE@._V1_SX300.jpg",
            "Ratings": [
                {
                    "Source": "Internet Movie Database",
                    "Value": "9.0/10"
                }
            ],
            "Metascore": "N/A",
            "imdbRating": "9.0",
            "imdbVotes": "289,958",
            "imdbID": "tt4574334",
            "Type": "series",
            "totalSeasons": "2",
            "Response": "True"
        }


## SV Tweets API (Procesador de comentarios de Twitter)

FORMAT: 1A

Su función principal es obtener los tweets con respecto a una película para
posteriormente guardar estos tweets en una base de datos Este microservicio
usa la API de twitter a través de la librería de Twython.

# Group Information
Recursos de **SV Tweets API**.

## Information [/api/v1/tweets{?t}&{tipo}]
### Obtiene comentarios a partir de la película especificada [GET]

+ Parameters
    + t (required, string) ... Es el título de la película de la cual se desea saber el sentimiento.
    + tipo (required, string) ... Es el tipo del contenido que se buscará `movie` o `series`.

+ Request (application/x-www-form-urlencoded)

        t=Stranger+things&tipo=movies

+ Response 200 (application/text)

        "Stranger things"


## SV Sentimiento API (Procesador de sentimientos)

FORMAT: 1A

Su función general es proporcionar en un objeto `JSON` información acerca
del sentimiento de los comentarios en twitter sobre una pelicula o una serie
en particular haciendo uso del API proporcionada.

# Group Information
Recursos de **SV Sentimiento API**.

## Information [/api/v1/sentimiento{?t}]
### Obtiene sentimiento a partir de comentarios de la película especificada [GET]

+ Parameters
    + t (required, string) ... Es el título de la película de la cual se desea saber el sentimiento.

+ Request (application/x-www-form-urlencoded)

        t=Stranger+things

+ Response 200 (application/json)

        {
            "sentimiento_pelicula": "positivo",
            "neutral": 9,
            "positivo": 12,
            "negativo": 7
        }
