from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup 
from telegram.ext import CallbackQueryHandler
from telegram.ext.updater import Updater # Conter a chave da api vinda do botfather
from telegram.update import Update # Isso será invocado toda vez que um bot receber uma atualização
from telegram.ext.callbackcontext import CallbackContext # Não usaremos sua funcionalidade diretamente em nosso código, mas quando adicionarmos o dispatcher, será necessário (e funcionará internamente)
from telegram.ext.commandhandler import CommandHandler #Esta classe Handler é usada para lidar com qualquer comando enviado pelo usuário ao bot, um comando sempre começa com “/” ou seja, “/start”,”/help” etc.
from telegram.ext.messagehandler import MessageHandler #Esta classe Handler é usada para lidar com qualquer mensagem normal enviada pelo usuário ao bot
from telegram.ext.filters import Filters # Isso filtrará texto normal, comandos, imagens, etc. de uma mensagem enviada.
import re

from menus.gerenciamento import entrarEmGerenciamento
from menus.modooperacao import entrarEmModoOperacao
#from core.usuario import verificaEmailCadastrado

updater = Updater("5389773517:AAEzhBQZ5vTExZ7MsA77OzTKhtbdgjoWctM", use_context=True)

#   Processo do BOT
#   1 - Inicializar atravez do comando start
#   2 - Solicitar ao usuario o email cadastrado
#   3 - 

# inicializar o processo do BOT
def start(update: Update, context: CallbackContext):
    f = open("usuarios.txt", "a")
    f.write(str(update.message.chat_id) + '|0|' + '\n')
    f.close()
    update.message.reply_text("Informe abaixo o seu e-mail exatamente como você colocou quando foi realizar a sua inscrição em nosso produto :")
   
# Usuario informou o email
def validarEmail(update: Update, context: CallbackContext):
    if( update.message.text == "teste@teste.com.br"):
        update.message.reply_text("O email informado não foi encontrado em nossa base de dados.")
        update.message.reply_text("Informe abaixo o seu e-mail exatamente como você colocou quando foi realizar a sua inscrição em nosso produto :")
    else:     
        mainbutton = [
            ['🧠 Gerênciamento','⚙️ Modo de Operação'],
            ['🎯 Lista','🚨 Suporte'],
            ['🤖 Operar']
        ]
        keyBoard1 = ReplyKeyboardMarkup(mainbutton , resize_keyboard=True)
        message_reply_text = 'Seja muito bem vindo !'
        update.message.reply_text(message_reply_text, reply_markup= keyBoard1)
        




def recepcionar(update: Update, context: CallbackContext):

    if(update.message.text == 'Voltar'):
        mainbutton = [
            ['🧠 Gerênciamento','⚙️ Modo de Operação'],
            ['🎯 Lista','🚨 Suporte'],
            ['🤖 Operar']
        ]

        keyBoard1 = ReplyKeyboardMarkup(mainbutton , resize_keyboard=True)
        message_reply_text = 'Menu Principal'
        update.message.reply_text(message_reply_text, reply_markup= keyBoard1)

    else:        

        if(update.message.text == '🧠 Gerênciamento'):
            entrarEmGerenciamento(update,context)

        else:
            if(update.message.text == '⚙️ Modo de Operação'):
                entrarEmModoOperacao(update,context)
            else:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", update.message.text):
                    update.message.reply_text("Por favor informe um email válido")
                else:
                    validarEmail(update,context)       





updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, recepcionar))


updater.start_polling()
print('bot iniciado')
