# CryptoSniffer

This is the source code of Telegram Channel: [CryptoSniffer](https://t.me/CryptoSnifferPro), which is deployed on DigitalOcean Functions Platform. 



## Dictionary Structure

**MessageBot** : a simple message bot, forward the message to the Channel.

**ScheduledFunctions**: some scheduled functions deployed on DigitalOcean Functions, execute periodically and send the message to the MessageBot.



## Deploying

DOC: https://docs.digitalocean.com/products/functions/how-to/create-functions/

**Switch Namespace**:

```bash
doctl serverless connect crypto-sniffer-bot
```



**Initialize a Sample Function (Optional)**: 

```bash
doctl serverless init --language go project-name
```



**Deploy Function**:

```
doctl serverless deploy project-name --remote-build
```



## ScheduledFunctions

### dexscreener chains

parameters

```
{}
```

environment variables:

- mongoURI: mongoDB URI
- msgBotAPI: API link of msgBot
- flareSolverrAPI: API link of [flareSolverr](https://github.com/FlareSolverr/FlareSolverr) , this is a service based on https://hub.docker.com/r/flaresolverr/flaresolverr, aiming to bypass the cloudflare 5 second challenge.

