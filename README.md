## Resumo

Bateu vontade de fazer um rice no meu computador e então me veio a ideia de usar wallpapers com caracteres (unicode/ASCII), por fim deu nesse código caseiro. 

Ele foi dividido em 3 partes, sendo elas:

 * **Busca.py**
    * **busca_caminho** = Retorna o caminho da imagem se ela estiver nos diretórios *~/Downloads*, *~/Documentos* e *~/Imagens*;
    * **busca_fonte** = Retorna o caminho da fonte que preferir ao procurar no diretório */usr/share/fonts/*;
* **Gerador.py**
    * **gera_txt** =  Cria um arquivo.txt contendo os caracteres utilizados na ordem em que foram implementados e além disso salva este documento na mesma pasta onde se encontra a imagem original;
    * **geta_bitmap** = Cria um arquivo.jpeg sendo ele o produto final da imagem já transformada em ASCII e também armazena no mesmo caminho da imagem original;
* **Conversor.py**
    * **img_ascii** = Função final onde mescla todas as anteriores.

## Exemplos

### Imagem Padrão

```
python -c "import Conversor; Conversor.img_ascii('Nome do arquivo', 'Nome da fonte', size = (largura, altura))"
```

![Imagem Original](/imgs/kurono.jpeg)

![Imagem Padrão(preto e branco)](/imgs/kuronoASCII.jpeg)

### Escolha de Cores

```
python -c "import Conversor; Conversor.img_ascii('nome do arquivo', 'nome da fonte', size = (largura, altura), background_color = 'black', letter_color = "purple")"
```

![Imagem Original](/imgs/'Who the hell do you think i am?.png')

![Imagem Colorida](/imgs/'Who the hell do you think i am?ASCII.jpeg')
