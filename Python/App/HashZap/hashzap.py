
# importando o flat
import flet as ft

# criando a tela principal
def main(page):
    #criando elemento
    titulo = ft.Text('HashZap')
    titulo_janela = ft.Text('Bem vindo ao Hashzap')
    
    # Criando a coluna do chat
    chat = ft.Column()
     
    def enviar_mensagem_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        page.update()
    page.pubsub.subscribe(enviar_mensagem_tunel)
      
# funcao de mensagem    
    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_usuario.value
        mensagem = f'{nome_usuario} : {texto_mensagem}'
        page.pubsub.send_all(mensagem)
        campo_mensagem.value = ''
        page.update()
                
    campo_mensagem = ft.TextField(label='Digite sua mensagem', on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

# funcao entrar no chat    
    def entrar_chat(evento):
        page.remove(titulo)
        page.remove(botao_iniciar)
        janela.open = False
        #adicionar elementos ao entrar no chat
        page.add(chat)
        page.add(linha_mensagem)
        mensagem = f'{campo_usuario.value}: Entrou no chat!'
        page.pubsub.send_all(mensagem)
        page.update()    
           
    campo_usuario = ft.TextField(label='Escreva seu nome no chat', on_submit=entrar_chat)            
    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)
    janela = ft.AlertDialog(
        title= titulo_janela, 
        content=campo_usuario, 
        actions=[botao_entrar])   
       
    def iniciar_chat(evento):
        page.dialog = janela
        janela.open = True
        page.update()
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=iniciar_chat)
    
    #adicionar elemento a pagina
    page.add(titulo)
    page.add(botao_iniciar)

    
# saida da tela principal    
ft.app(main, view = ft.WEB_BROWSER) 
