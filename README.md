# Package tracker
This is a bot for tracking your packages in Russian Post.
To run it locally from docker, run commands:<br />
1. `docker build -t tracker .`
2. `docker run --env-file variables.env tracker`<br />
variables.env should contain env variables with login and password from Russian Post API, and token from telegram @BotFather.