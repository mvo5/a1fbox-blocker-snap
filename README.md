# Spam call blocker for fritzbox user in Germany

This is snap of the nice spam caller blocker that is part
of https://github.com/bufemc/a1fbox.git

## Setup

Setup is still a bit complicated.

Make sure your Fritzbox has 3 Phonebooks, the first is your
regular one. The second and third are the "spam" blocker 
books. Also make sure that you allow call monitoring, dial
`#96*5*` to enable it.

```
snap set a1fbox-spamblock username="username"
snap set a1fbox-spamblock password="password"
# optional, fritz.box is the default
snap set a1fbox-spamblock ip-address="192.168.178.1"
snap set a1fbox-spamblock telegram-bot-secret="botNumber:token"
snap set a1fbox-spamblock telegram-bot-chat-id="numberic-chat-id"
```

## Telegram bot

Talk to "botfarther" on https://t.me/botfather and run:
```
/newbot
name-of-the-bot
UserNameOfTheBot
```
this will give you a botNumber:secret that you can configure
above.

The telegram-chat-id is the numberic id of the user/group that the
messages should go to. Talk to e.g. @getidsbot to get it, it's
unfortunately a bit annoying.
