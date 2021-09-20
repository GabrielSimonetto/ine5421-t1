# ine5421-t1

## Entregas

- [x] Conversão de Expressão Regular para Autômato Finito Determinístico (livro do
Aho).
- [x] União de Autômatos via Epsilon-transição
- [x] Determinização de Autômatos
- [ ] Construção da TS (incluir palavras reservadas e outras informações pertinentes)</br>
    R: TS nao foi feita

- [ ] A interface de projeto deve permitir a inclusão de expressões regulares para todos
os padrões de tokens;</br>
    R: TS nao foi feita

- [x] Para cada ER deve ser gerado o AFD corresponde

- [x] Os AFD devem ser unidos

- [ ] O AFND resultante deve ser determinizado gerando a tabela de análise léxica</br>
    R: TS nao foi feita

- [ ] A interface de execução deve permitir a entrada de um texto fonte</br>
    R: TS nao foi feita

- [ ] O texto fonte será analisado e deve gerar um arquivo de saída com todos os tokes</br>
encontrados.
    R: TS nao foi feita

## Instalação

### Instalando o Poetry

Usamos o poetry no trabalho para gerar um pacote importavel para o modulo de testes

```
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
echo 'export PATH=$PATH:$HOME/.poetry/bin' >> ~/.bashrc
source ~/.bashrc
```

## Instalando as dependencias do projeto.

```
make install
```

Caso encontre a mensagem `ModuleNotFoundError: No module named 'distutils.util'`, no Ubuntu, é necessário fazer um passo adicional descrito [nesse link](https://askubuntu.com/questions/1239829/modulenotfounderror-no-module-named-distutils-util)


```
sudo apt-get install python3-distutils
sudo apt-get install python3-apt
```

## Rodando o projeto.

```
make tests
```

## Rodar os testes

Os testes por padrão recebem uma flag que permitem os prints internos da funções, de modo a mostrar as operações internas.

```
make tests
```
