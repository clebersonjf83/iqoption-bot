from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup
from telegram.ext.updater import Updater # Conter a chave da api vinda do botfather
from telegram.update import Update # Isso será invocado toda vez que um bot receber uma atualização
from telegram.ext.callbackcontext import CallbackContext # Não usaremos sua funcionalidade diretamente em nosso código, mas quando adicionarmos o dispatcher, será necessário (e funcionará internamente)
from telegram.ext.commandhandler import CommandHandler #Esta classe Handler é usada para lidar com qualquer comando enviado pelo usuário ao bot, um comando sempre começa com “/” ou seja, “/start”,”/help” etc.
from telegram.ext.messagehandler import MessageHandler #Esta classe Handler é usada para lidar com qualquer mensagem normal enviada pelo usuário ao bot
from telegram.ext.filters import Filters # Isso filtrará texto normal, comandos, imagens, etc. de uma mensagem enviada.
from iq import verificarSaldo

def entrarEmGerenciamento(update: Update, context: CallbackContext):
   
    banca = verificarSaldo()
    delay = 2
    stop_win = 0
    stop_loss = 0

    

    mainbutton = [
        ['💰 Banca : R$' + str(banca) ,'⏱️ Delay : ' + str(delay)],
        ['📈 Stop Win : R$ ' + str(stop_win),'📉 Stop Loss : R$ ' + str(stop_loss)],
        ['Voltar']
    ]
    
    
    keyBoard1 = ReplyKeyboardMarkup(mainbutton , resize_keyboard=True)
    message_reply_text = 'Painel de gerênciamento'
    update.message.reply_text(message_reply_text, reply_markup= keyBoard1)


  

