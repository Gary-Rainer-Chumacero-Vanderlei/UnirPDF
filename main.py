import PyPDF2
import os

# Criar um objeto PdfMerger
merger = PyPDF2.PdfMerger()

# Listar os arquivos na pasta "literatura"
lista_arquivos = os.listdir("literatura")
lista_arquivos.sort()  # Ordenar os arquivos

# Adicionar apenas arquivos PDF à fusão
for arquivo in lista_arquivos:
    if arquivo.endswith(".pdf"):  # Verificar se é um arquivo PDF
        caminho_arquivo = f"literatura/{arquivo}"  # Corrigir o caminho
        merger.append(caminho_arquivo)  # Adicionar o arquivo ao merger

# Escrever o arquivo final
merger.write("Literatura.pdf")
merger.close()

print("Todos os PDFs foram combinados com sucesso em Literatura.pdf!")
