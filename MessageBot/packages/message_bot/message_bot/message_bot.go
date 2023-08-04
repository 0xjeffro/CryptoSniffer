package main

import (
	tgbotapi "github.com/go-telegram-bot-api/telegram-bot-api/v5"
	"os"
)

var bot *tgbotapi.BotAPI

func Main(args map[string]interface{}) map[string]interface{} {
	token := func() string {
		if os.Getenv("BOT_TOKEN") == "" {
			panic("BOT_TOKEN is not set")
		} else {
			return os.Getenv("BOT_TOKEN")
		}
	}()
	bot, err := tgbotapi.NewBotAPI(token)
	if err != nil {
		panic(err)
	}

	message, _ := args["message"].(string)
	var channelID int64 = -1001855610228

	// send message to channel
	msg := tgbotapi.NewMessage(channelID, message)
	_, err = bot.Send(msg)

	rsp := make(map[string]interface{})
	rsp["body"] = err
	return rsp
}

// comment out this function if you want to run this function locally
//func main() {
//	Main(map[string]interface{}{"message": "Hello, World!"})
//}
