# Gerenciador de Cruzamentos


## Aluno
|Matrícula | Aluno |
| -- | -- |
| 18/0102613  |  Ítalo Fernandes Sales de Serra |

## Sobre 
O trabalho tem com objetivo gerenciar 4 cruzamento por meio de 1 servidor central e 4 distribuídos.

O **servidor central** tem as seguintes responsabilidades:

1. Manter conexão com os servidores distribuídos (TCP/IP);
2. Prover uma interface que mantenham atualizadas as seguintes informações por cruzamento:
    - a. Fluxo de trânsito nas vias principais (Carros/min);
    - b. Velocidade média da via (km/h);
    - c. Número de infrações (Por tipo: avanço de sinal e velocidade acima da permitida);
3. Prover mecanismo na interface para:
    - a. Modo de emergência: liberar o fluxo de trânsito em uma via (os dois cruzamentos com a via principal em verde);
    - b. Modo noturno fazer o sinal amarelo piscar em todos os cruzamento;

Os **servidores distribuídos** tem as seguintes responsabilidades:

1. Controlar os semáforos (temporização) - cruzamento com 4 sinais: os semáforos da via principal tem temporização diferente dos das vias auxiliares conforme e tabela abaixo.
2. Controlar o acionamento dos botões de travessia de pedestres (2 por cruzamento): ao acionar o botão, o sinal em questão deverá cumprir seu tempo mínimo (Ex: permanecer verde pelo tempo mínimo antes de fechar. Caso o tempo mínimo já tenha passado, o sinal irá mudar de estado imediatamente após o botão ser pressionado);
3. Controlar o acionamento dos sensores de passagem de carros nas vias auxiliares. Caso o sinal esteja fechado e um carro pare na via auxiliar, o comportamente será o mesmo que um pedestre pressionar o botões de travessia;
4. Contar a passagem de carros em cada direção e sentido do cruzamento (4 valores sepadados) e enviar esta informação periodicamente (2 segundos) ao servidor central;
5. Monitorar a velocidade da via através dos sensores de velocidade. A velocidade de cada carro deverá ser reportada para o servidor central periodicamente. Veídulos acima da velocidade permitida de 60 Km/h deverão ser reportados ao servidor central e contabilizados separadamente. Além disso, é necessário soar um alarme ao detectar um veículo acima da velocidade permitida;
6. Efetuar o controle de avanço do sinal vermelho tanto através dos sensores de passagem de carros nas vias auxiliares quanto pelos sensores de velocidade na via principal. O número de veículos que avançam o sinal vermelho deverá ser reportado ao servidor central e o alarme deve ser disparado a cada detecção de infração;
7. Cada instância dos servidores distribuídos a ser executada deve automaticamente se configurar para o controle do cruzamento 1 ou 2, seja por passagem de parâmetro de inicialização, arquivo de configuração ou outro mecanismo, ou seja, o programa que controla ambos os cruzamentos deverá ser um só.

**Linguagem**: 
- python (versão 3)<br>

**Bibliotecas**: 
- socket
- RPi.GPIO
- threading
- time <br>

## Uso 
**Para executar o programa é necessário seguir a ordem das informações a seguir**

Siga as instruções a seguir :

1) Clonar o repositório:
```sh 
git clone https://github.com/italofernandes13/Trabalho_1_FSE.git
```

2) Acessar a pasta da aplicação:
```sh
cd Trabalho_1_FSE
```

3) Copie a pasta para a primeira placa rasp inserindo seu user no lugar de <user_>, seu caminho ao inves de <insira/seu/caminho/ate/Trabalho_1_FSE> e o IP ao inves de <000.00.00.00>:
```
scp -P 13508 -r "<insira/seu/caminho/ate/Trabalho_1_FSE>" <user_>@<000.00.00.00>:/home/<user_>
```

4) Copie a pasta para a segunda placa rasp inserindo seu user no lugar de <user_>, seu caminho ao inves de <insira/seu/caminho/ate/Trabalho_1_FSE> e o IP ao inves de <000.00.00.00>:
```
scp -P 13508 -r "<insira/seu/caminho/ate/Trabalho_1_FSE>" <user_>@<000.00.00.00>:/home/<user_>
```

5) Abrir **3 terminais** e em todos acessar via ssh a primeira placa rasp inserindo seu user no lugar de <user_> e o IP ao inves de <000.00.00.00>:
```
ssh <user_>@<000.00.00.00> -p 13508
```

6) Abrir **2 terminais** e em todos acessar via ssh a segunda placa rasp inserindo seu user no lugar de <user_> e o IP ao inves de <000.00.00.00>:
```
ssh <user_>@<000.00.00.00> -p 13508
```

7) Após abrir e acessar via ssh nos **5 terminais**:<br>
    - 7.1. No primeiro terminal abra o servidor central, e inserindo seu IP ao inves de <000.00.00.00>:
    ```
    python3 server.py <000.00.00.00>
    ```

    - 7.2. No segundo terminal abra o servidor distribuído, correspondente ao cruzamento 1, e inserindo seu IP ao inves de <000.00.00.00>:
    ```
    python3 client.py 1 <000.00.00.00>
    ```
    
    - 7.3. No primeiro terminal abra o servidor distribuído, correspondente ao cruzamento 2, e inserindo seu IP ao inves de <000.00.00.00>:
    ```
    python3 client.py 2 <000.00.00.00>
    ```
    
    - 7.4. No primeiro terminal abra o servidor distribuído, correspondente ao cruzamento 3, e inserindo seu IP ao inves de <000.00.00.00>:
    ```
    python3 client.py 3 <000.00.00.00>
    ```
    
    - 7.5. No primeiro terminal abra o servidor distribuído, correspondente ao cruzamento 4, e inserindo seu IP ao inves de <000.00.00.00>:
    ```
    python3 client.py 4 <000.00.00.00>
    ```
8) No primeiro terminal onde está abriu o servidor central:
    - 8.1. Para ligar o modo noturno digite:
    ```
    0
    ```
    - 8.2. Para desligar o modo noturno digite: 
    ```
    1
    ```
    - 8.3. Para ligar o modo emergencia no cruzamento 1 e 2 digite: 
    ```
    2
    ```
    - 8.4. Para desligar o modo emergencia no cruzamento 1 e 2 digite: 
    ```
    3
    ```
    - 8.5. Para ligar o modo emergencia no cruzamento 3 e 4 digite: 
    ```
    4
    ```
    - 8.6. Para desligar o modo emergencia no cruzamento 3 e 4 digite: 
    ```
    5
    ```
9) Para terminar a execução pressione **CONTROL+C** duas vezes em cada terminal

