from kivy.app import App
from kivy.lang import Builder
from screens import *
from buttons import *
from bannervenda import *
import requests
import os


GUI = Builder.load_file("main.kv")
class myApp(App):
    id_user = 1


    def build(self):
        return GUI


    def on_start(self):
        arquivos = os.listdir("icones/fotos_perfil")
        pagina_foto_perfil = self.root.ids['fotoperfilpage']
        lista_fotos = pagina_foto_perfil.ids['lista_fotos_perfil']
        for foto in arquivos:
            imagem = ImageButton(source=f"icones/fotos_perfil/{foto}", on_release = self.mudar_foto_perfil)
            lista_fotos.add_widget(imagem)

        self.carregar_infos_usuario()



    def carregar_infos_usuario(self):
        link = f"https://aplicativovendashash-9b581-default-rtdb.firebaseio.com/{self.id_user}.json"
        requisicao = requests.get(link)

        # pegando informações do usuário
        dicionario = requisicao.json()

        # preencher foto de perfil
        avatar = dicionario['avatar']
        foto_perfil = self.root.ids["foto_perfil"]
        foto_perfil.source = f"icones/fotos_perfil/{avatar}"

        # preencher lista de vendas
        try:
            vendas = dicionario["vendas"][1:]
            pagina_homepage = self.root.ids['homepage']
            lista_vendas = pagina_homepage.ids['lista_vendas']
            for venda in vendas:
                banner = BannerVenda(cliente=venda['cliente'], foto_cliente=venda['foto_cliente'],
                                     produto=venda['produto'], foto_produto=venda['foto_produto'],
                                     data=venda['data'], preco=venda['preco'], unidade=venda['unidade'],
                                     quantidade=venda['quantidade'])


                lista_vendas.add_widget(banner)
        except:
            pass


    def mudar_tela(self, id_tela):
        manager = self.root.ids["screen_manager"]
        manager.current = id_tela


    def mudar_foto_perfil(self, *args):
        print("Mudar foto Perfil")


myApp().run()