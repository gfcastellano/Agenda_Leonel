# Aplicativo criado usando a biblioteca Kivy para python. ( EM PROCESSO DE DESENVOLVIMENTO )

## Uso/Aplicações:
✅| Visualizar, adicionar e editar lista de contatos comerciais

✅| Visualizar distribuição de contatos comerciais em um mapa da cidade

✅| Realizar buscas avançadas por caracteristicas especificas de clientes
- Adicionar lembretes

✅| Adicionar eventos de contato/visitas comercial (agenda)
- Gerenciar estoques de produtos
- Emitir relatórios e métricas de eficiencia de contatos comerciais (melhor dia e horario para contato, sugestão de produtos, etc) 
- Adicionar eventos automaticamente na agenda, criar assistete pessoal (Automatização de eventos, ligar, fazer visita, acompanhamento de venda)

## Código:
Funcionalidade serão escritas em linguagem .py e design será escrito em "linguagem" .kv
## Objetivo:
Auxiliar profissionais que trabalham com vendas diretas a gerenciarem sua lista de clientes, otimizando sua rotina de visitas.

## Contará com: 
    - facil visualização de dados dos clientes;
    - mecanismo de busca por caracteristicas de clientes, como: região, porte, serviços, etc...
    - visualização de clientes cadastrados proximos da sua localização atual
    - acompanhamento do estágio de uma venda (Contato inicial, apresentação do produto, oferecimento de amostra, proposta comercial, fechamento de pedido)
    - manejamento de estoque de produtos (alerta de estoque baixo e estoque critico)
    - métricas para produtos (rendimento, custo para cliente, etc)
    - métricas para clientes (quando compra, qual a quantia mais apropriada, qual a sazonalidade)
    - histórico das visitas para cada cliente (dados da visita, cometários, contato, o que foi conversado)


# Primeiros passos para instalar em seu celular Android

Primeiro é necessário uma máquina com sistema operacional Linux®.

Caso você não possua podendo ser uma máquina virtual instalada em seu PC Windows®.

Também é preciso habilitar o modo desenvolvedor de seu Android®.

Nela você deverá executar no terminal:

    sudo apt-get install git
    git clone https://github.com/kivy/buildozer.git
    sudo apt-get install python3.6
    sudo apt-get install python3-setuptools
    
    cd buildozer
    sudo python3 setup.py install
    cd ..
    
    git clone https://github.com/gfcastellano/Agenda_Leonel.git
    sudo apt install -y git zip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev
    pip3 install --user --upgrade cython virtualenv
    sudo apt-get install cython
    sudo apt install libssl-dev
    
    cd Agenda_Leonel
    
    #Caso queira pode testar diferentes branchs
    #git checkout <nome_do_branch>
    
    
    buildozer android debug deploy run logcat
    
    
    
