# ine5421-t1

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
make run
```

## Rodar os testes

Os testes por padrão recebem uma flag que permitem os prints internos da funções, de modo a mostrar as operações internas.

```
make tests
```
