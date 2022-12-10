# OdioIVocali Telegram BOT

Bot Telegram che riceve i messaggi vocali e li trascrive, sfruttando [OpenAI Whisper](https://github.com/openai/whisper).

## Utilizzo

Chiedere a @BotFather un token per un nuovo bot e salvare il token ottenuto in `.env`. Installare le dipendenze con

```cmd
pip install -r requirements.txt
```

Da linea di comando lanciare il bot con

```cmd
python main.py
```

Mandare un vocale al bot o aggiungerlo in una chat di gruppo. In questo caso al bot andrà dato ruolo di amministratore in modo che abbia accesso ai messaggi.

## TODO

- [ ] Testare docker
- [ ] Configurare webhook invece che polling
  
## Note installazione

Per riuscire a caricare file audio in Windows con Whisper serve installare `ffmpeg` sia con:

```cmd
pip install ffmpeg
```

che seguendo questa [guida](https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/).
