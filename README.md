# ine5421-t1

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