
class CriarArquivo():

    def criaArquivoDeTeste(self, path:str):
        arquivo_criado = open (mode='w')
        arquivo_criado.write("arquivo de teste criado pela classe CriarArquivo")
        arquivo_criado.close()
