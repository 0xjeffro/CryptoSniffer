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
doctl serverless init --language go function-name
```



**Deploy Function**:

```
doctl serverless deploy project-name --remote-build
```



