# TelegramBot

docker service create --name dl-bot --mount-add type=bind,src=$PWD,dst=/app saikou/dl-bot