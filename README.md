# ine5421-t1

Nossa entrega numero 1 nao possui uma CLI, e demonstra os algoritmos que foram criados atraves da bateria de testes.

## Entregas

- [x] Conversão de Expressão Regular para Autômato Finito Determinístico (livro do
Aho).
- [x] União de Autômatos via Epsilon-transição
- [x] Determinização de Autômatos
- [ ] Construção da TS (incluir palavras reservadas e outras informações pertinentes)
    R: TS nao foi feita

- [ ] A interface de projeto deve permitir a inclusão de expressões regulares para todos
os padrões de tokens;
    R: TS nao foi feita

- [x] Para cada ER deve ser gerado o AFD corresponde

- [x] Os AFD devem ser unidos

- [ ] O AFND resultante deve ser determinizado gerando a tabela de análise léxica
    R: TS nao foi feita

- [ ] A interface de execução deve permitir a entrada de um texto fonte
    R: TS nao foi feita

- [ ] O texto fonte será analisado e deve gerar um arquivo de saída com todos os tokes
encontrados.
    R: TS nao foi feita

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
