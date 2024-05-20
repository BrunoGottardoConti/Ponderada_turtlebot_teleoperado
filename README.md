# Ponderada_turtlebot_teleoperado
Atividade ponderada do turtlebot teleoperado

# Controle do TurtleBot3 e Parada de Emergência

## Demonstração em Vídeo

[Assista ao vídeo de demonstração aqui](https://www.youtube.com/watch?v=rrF-uFXSRzU)

## Descrição do Projeto

Este projeto implementa um sistema de controle de robô usando ROS 2, especificamente projetado para o controle do TurtleBot3. Ele inclui um cliente de teleoperação e um serviço de parada de emergência para gerenciar as operações do robô de forma segura.

## Estrutura do Projeto

O projeto está organizado em dois pacotes principais:

- `new_bringup_ws`: Contém os serviços para lidar com a inicialização do robô e a parada de emergência.
- `my_robot_controller`: Contém o cliente de teleoperação para controlar o TurtleBot3.

## Requisitos

- ROS 2 (Humble)
- Python 3.10
- Dependências: `rclpy`, `geometry_msgs`

### Configuração do Workspace

#### No Robô

1. Clone o repositório:

git clone https://github.com/BrunoGottardoConti/Ponderada_turtlebot_teleoperado

2. Navegue até o diretório do repositório e construa o workspace:

cd Ponderada_turtlebot_teleoperado

colcon build

No robô, inicie o serviço de parada de emergência:

ros2 run new_bringup bringup_manager

No seu computador, que deve estar na mesma rede que o robô, execute o cliente de teleoperação:

ros2 run my_robot_controller robot_controller