Spam call blocker for fritzbox user in Germany

This is snap of the nice spam caller blocker that is part
of https://github.com/bufemc/a1fbox.git

Setup is still a bit complicated.

Make sure your Fritzbox has 3 Phonebooks, the first is your
regular one. The second and third are the "spam" blocker 
books. Also make sure that you allow call monitoring, dial
`#96*5*` to enable it.

```
snap set a1fbox-spamblock username="username"
snap set a1fbox-spamblock password="password"
```

