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

## 📌 Sobre o Projeto

O **Sistema de Transporte Escolar** é uma solução web desenvolvida para auxiliar prefeituras e secretarias de transporte no gerenciamento logístico da frota escolar municipal.

O sistema resolve o problema da descentralização de informações, substituindo planilhas e controles manuais por uma plataforma unificada que conecta **Gestores**, **Motoristas** e **Alunos**.

---

## Screenshots

### Tela de Acesso (Login Unificado)
![Tela de Login](screenshots/login_screen.png)
*(A interface direciona automaticamente cada perfil para seu painel específico)*

---

## Funcionalidades Principais

O sistema conta com controle de acesso baseado em papéis (RBAC) e redirecionamento inteligente:

### Módulo Gestor (Administrativo)
- **Dashboard:** Visão geral da frota e alertas.
- **Gestão de Frota:** Cadastro de veículos e controle de motoristas.
- **Gestão de Alunos:** Matrícula, upload de declaração escolar (PDF) e controle de validade do cadastro.
- **Alertas Automáticos:** Notificação visual de CNH vencida (Motoristas) e Cadastros a renovar (Alunos).
- **Roteirização:** Criação de rotas, definição de horários e alocação de alunos.

### Módulo Motorista (Operacional - Mobile First)
- **Minhas Rotas:** Visualização apenas das rotas atribuídas ao motorista logado.
- **Lista de passageiros**: lista para cada rota, a situação do aluno. Se confirmou **ida**, **volta** ou **ida e volta**.
- **Ocorrências:** Reporte rápido de problemas mecânicos ou ausências.

### Módulo Aluno (Portal)
- **Agendamento:** Confirmação de presença ("Vou na Ida" / "Vou na Volta") para o dia seguinte.
- **Minha Rota:** Visualização do veículo e horário previsto.

---

## Tecnologias Utilizadas

* **Backend:** Python 3, Django Framework.
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsivo), Django Templates.
* **Banco de Dados:** SQLite (Desenvolvimento)
* **Controle de Versão:** Git & GitHub.
* **Metodologia:** Kanban.

---

## 📦 Como Rodar o Projeto

Pré-requisitos: Ter o **Python** e o **Git** instalados na máquina.

### 1. Clonar o repositório

```bash
git clone https://github.com/ViniciusOliver13/Gerenciamento-Transporte-Escolar.git
```
Entrar na pasta do projeto:
```
cd Gerenciamento-Transporte-Escolar
```

### 2. Criar um ambiente virtual

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar um superusuário (opcional)

```bash
python manage.py createsuperuser
# Siga as instruções para criar login e senha
``` 
### 6. Iniciar o servidor

```bash
python manage.py runserver
```

### Perfis para Teste
Para validar as diferentes visões do sistema, recomenda-se criar os seguintes usuários via Painel Admin (/admin):

| Usuário (Sugestão) | Perfil (Model) | O que ele vê? |
|---|---:|---|
| `admin` | Gestor | Acesso total, CRUDs, Relatórios. |
| `motorista1` | Motorista | Apenas "Minhas Rotas". |
| `aluno1` | Aluno | Painel de confirmação de presença. |


## Estrutura do Projeto
- **transporte-escolar/**: Configurações de redirecionamento de login e mixins de segurança.

- **usuarios/**: Gestão de contas, perfis de Motorista e Gestor.

- **veiculos/**: Cadastro da frota física.
- **educacional/**: Gestão de alunos e documentos.
- **rotas/**: Lógica principal das rotas escolares, incluindo horários e alocação de alunos.

##  Equipe de Desenvolvimento

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