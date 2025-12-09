# Sistema de Gerenciamento de Transporte Escolar

<p align="center">
  <a href="https://github.com/ViniciusOliver13/Gerenciamento-Transporte-Escolar">
    <img src="https://img.shields.io/badge/projeto-conclu%C3%ADdo-brightgreen?style=for-the-badge&labelColor=434343" alt="Status do Projeto"/>
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  </a>
  <a href="https://www.djangoproject.com/">
    <img src="https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django" alt="Django"/>
  </a>
  <a href="https://getbootstrap.com/">
    <img src="https://img.shields.io/badge/Bootstrap-5.3-563d7c?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  </a>
</p>

---

## 1. Objetivo do sistema

O *Sistema de Transporte Escolar* é uma solução web para apoiar prefeituras e secretarias de educação no gerenciamento da frota escolar municipal.  
O objetivo é centralizar informações de *alunos, **motoristas, **veículos* e *rotas, substituindo planilhas manuais por uma plataforma que integra **Gestores, **Motoristas* e *Alunos* em um mesmo ambiente.

---

## 2. Principais funcionalidades

### Módulo Gestor (Administrativo)
- Dashboard com visão geral das rotas, veículos e alertas.
- Cadastro e gestão de veículos, motoristas e alunos.
- Upload e controle de validade da declaração escolar do aluno.
- Alertas para CNH vencida e cadastros de alunos a renovar.
- Criação de rotas, definição de horários e alocação de alunos.

### Módulo Motorista (Painel Operacional)
- Visualização apenas das rotas atribuídas ao motorista logado.
- Lista de passageiros por rota com situação do aluno:
  - Sem confirmação, confirmou *ida, **volta* ou *ida e volta*.
- Registro de ocorrências (problemas mecânicos, atrasos, aluno ausente etc.).

### Módulo Aluno (Portal do Aluno)
- Confirmação diária de presença na rota:
  - Botões separados para *“Vou na Ida”* e *“Vou na Volta”*.
- Visualização da(s) rota(s) em que está cadastrado, com veículo e horário previsto.

---

## 3. Tecnologias utilizadas

- *Linguagem:* Python 3.10+
- *Framework backend:* Django 5.0
- *Frontend:* HTML5, CSS3, Bootstrap 5.3, Django Templates
- *Banco de dados (desenvolvimento):* SQLite
- *Controle de versão:* Git e GitHub
- *Metodologia de organização:* Kanban

---

## 4. Como executar o projeto

Pré-requisitos:  
- Git instalado  
- Python 3.10+ instalado

### 4.1 Clonar o repositório


git clone https://github.com/ViniciusOliver13/Gerenciamento-Transporte-Escolar.git
cd Gerenciamento-Transporte-Escolar


### 4.2 Criar e ativar o ambiente virtual


# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate


### 4.3 Instalar as dependências


pip install -r requirements.txt


### 4.4 Configurar o banco de dados


python manage.py makemigrations
python manage.py migrate


### 4.5 (Opcional) Criar um superusuário


python manage.py createsuperuser


### 4.6 Executar o servidor


python manage.py runserver


Acesse em: http://127.0.0.1:8000/

---

## 5. Como navegar/testar o protótipo

1. Acesse o painel administrativo em http://127.0.0.1:8000/admin/ com o superusuário criado.  
2. Cadastre:
   - Veículos, motoristas e alunos.
   - Rotas, associando veículo, motorista e alunos.
3. Crie usuários para cada perfil (ou vincule usuários existentes):

| Usuário (exemplo) | Perfil            | Acesso principal                      |
|-------------------|-------------------|---------------------------------------|
| admin           | Gestor            | Gestão completa via /admin e painéis  |
| motorista1      | Motorista         | Painel do motorista, “Minhas Rotas”   |
| aluno1          | Aluno             | Painel do aluno, confirmação ida/volta|

4. Faça login como:
   - *Aluno: acesse o painel do aluno, confirme **ida* e/ou *volta* em uma rota.  
   - *Motorista*: veja no painel do motorista a lista de passageiros e o status de confirmação de cada aluno.  
   - *Gestor*: gerencie cadastros, rotas e acompanhe o funcionamento geral.

## Screenshots

### Tela de Acesso (Login Unificado)
![Tela de Login](screenshots/login_screen.png)
A interface direciona automaticamente cada perfil para seu painel específico

## 6. Integrantes do grupo

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/ViniciusOliver13">
        <img src="https://avatars.githubusercontent.com/u/146228058?v=4" width="100px;" alt="Antonio Vinicius"/><br>
        <sub><b>Antonio Vinicius</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/marceloDev0">
        <img src="https://avatars.githubusercontent.com/u/140117398?v=4" width="100px;" alt="Marcelo Augusto"/><br>
        <sub><b>Marcelo Augusto</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/thyagofab">
        <img src="https://avatars.githubusercontent.com/u/143232809?v=4" width="100px;" alt="Thyago Fabricio"/><br>
        <sub><b>Thyago Fabricio</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/dinarteefilho">
        <img src="https://avatars.githubusercontent.com/u/146675089?v=4" width="100px;" alt="Dinarte Rodrigues"/><br>
        <sub><b>Dinarte Rodrigues</b></sub>
      </a>
    </td>
  </tr>
</table>
