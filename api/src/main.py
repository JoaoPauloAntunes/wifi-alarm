import os
from typing import Callable
from fastapi import FastAPI, Request, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from starlette.exceptions import ExceptionMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from dotenv import load_dotenv

import utils


load_dotenv(".env")
if utils.load_bool_env("USE_VLC"):
    import vlc
elif utils.load_bool_env("USE_MPV_MODULE"):
    import mpv


class LoggerRouteHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def route_handler(request: Request) -> Response:
            # Add fastapi context to logs
            ctx = {
                "path": request.url.path,
                "route": self.path,
                "method": request.method,
            }
            # utils.logger.append_keys(fastapi=ctx)
            utils.logger.info("Received request")

            return await original_route_handler(request)

        return route_handler
    
app = FastAPI(
    title="API",
    description="The Software API",
    version="0.1.0",
    # openapi_tags=tags_metadata,
)

app.router.route_class = LoggerRouteHandler
app.add_middleware(ExceptionMiddleware, handlers=app.exception_handlers)

allow_origins = [
    "http://localhost:3333"
]
app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_origins = allow_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print("http_exception_handler:", {
        "detail": exc.detail,
        "status_code": exc.status_code,
    })
    return JSONResponse(exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        error["message"] = error.pop("msg")

    res = utils.ResponseDataList(
        "Request validation error, verify if request follows the expected format",
        exc.errors(),
    ).__dict__
    content = jsonable_encoder(res)

    return JSONResponse(content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/")
def read_root(request: Request):
    res = {
        "Success": f"{app.title}: {os.environ.get('STAGE', 'local')}",
    }
    return res


@app.post("/alarm", status_code=status.HTTP_204_NO_CONTENT)
def play_alarm():
    alarm_file_path = "./src/assets/ring_sound.mp3"
    if utils.load_bool_env("USE_VLC"):
        vlc.MediaPlayer(alarm_file_path).play()
    elif utils.load_bool_env("USE_MPV_MODULE"):
        player = mpv.MPV(ytdl=True)
        player.play(alarm_file_path)
        player.wait_for_playback()
    else:
        os.system(f"mpv {alarm_file_path}")
