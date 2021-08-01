# ine5421-t1

## TODO

- [ ] Conversão de Expressão Regular para Autômato Finito Determinístico (livro do
Aho).
- [ ] União de Autômatos via Epsilon-transição
- [ ] Determinização de Autômatos
- [ ] Construção da TS (incluir palavras reservadas e outras informações pertinentes)

- [ ] A interface de projeto deve permitir a inclusão de expressões regulares para todos
os padrões de tokens;
- [ ] Para cada ER deve ser gerado o AFD corresponde
- [ ] Os AFD devem ser unidos
- [ ] O AFND resultante deve ser determinizado gerando a tabela de análise léxica
- [ ] A interface de execução deve permitir a entrada de um texto fonte
- [ ] O texto fonte será analisado e deve gerar um arquivo de saída com todos os tokes
encontrados.

## Installation

### Installing Poetry

```
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
echo 'export PATH=$PATH:$HOME/.poetry/bin' >> ~/.bashrc
source ~/.bashrc
```

## Install Dependencies using Poetry

```
make install
```

### Run Tests

```
make tests
```

## Examples Logic

Entradas de exemplo sempre começam com o estado inicial.
Exemplo de regra(regra?): "S: a - A; b - S;"
* S eh o estado em que estamos
* a - A indica que o token a leva ao estado A
* Separamos a proxima transição com ponto e virgula ";"