📄 5. README.md — Estrutura Esperada

ℹ️ O README do grupo deve seguir exatamente esta estrutura, com todas as seções preenchidas. Abaixo, um esboço da estrutura com conteúdo fictício.

# FIAPLab — Sistema de Reserva de Laboratórios

## 📌 Descrição do Problema
O problema proposto foi a difuculdade de antendimento do aluno com o HelpDesk, que atualmente pode gerar coflitos de hórario, fala de organização e perda de tempo para os alunos.

## 🚀 Solução Proposta
A solução proposta é um sistema de agendamento que permita aos alunos visualizarem horários disponíveis, marcar, cancelar ou reagendar atendimentos de foram simplificadad. Para a coordenação, o sistema oferece controle de agenda, permitindo criar horários e acompanhar todos os atendimentos marcados.

## 🛠️ Tecnologias Utilizadas
Python 3.11 
Flask
SqlLite

## ⚙️ Como Executar
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py

## 📂 Estrutura do Projeto
```text
fiaplab/
└── /.cache
|   └── fiaplab.db
|   └── userLogin.json
└── /api
|   └── /Controller/
|       └── horario_controller.py
|       └── login_controller.py
|       └── usuario_controller.py
|   └── /Repositories/
|       └── horario_repository.py
|       └── login_repository.py
|       └── usuario_repository.py
|   └── /Services/
|       └── horario_service.py
|       └── usuario_service.py
|   └── /database/
|       └── Tabelas.py
|   └── nucleo_funcional.py
├── main.py
└── README.md
└── requirements.txt

## 🧩 Funcionalidades Implementadas
- Cadastro de usuários (RF01)
- Login de usuários (RF02)
- Listar horários disponíveis (RF03)
- Agendamento de atendimento (RF04)
- Cancelamento de agendamento (RF05)
- Reagendamento de atendimento (RF06)
- Visualizar agendamentos do usuário (RF07)
- Admin cria horários (RF08)
- Impedir conflitos de horário (RF10)
- Sistema deve responder em < 2 segundos (RNF01)
- Armazenar dados em JSON ou SQLite (RNF03)
- Validar entradas do usuário (RNF04)
- Clean-Code (RNF05)

## 📸 Demonstração
https://www.youtube.com/watch?v=ycl2t34Js5Y

## 👨‍💻 Integrantes do Grupo
- Lucas Santos Rodrigues RM556891 (commits: feat)
- Mayene Gabrielle Aragão Padilha Doria RM558858 (commits: feat)
- Gabriel Lacerda Covello Arimatéa RM556391 (commits: feat)
- Gustavo Andrade de Sousa RM559069 (commits: feat)

## 🔗 Links
- Repositório: github.com/grupo-fiap/fiaplab
- Miro: https://miro.com/app/board/uXjVGqdaLik=/?share_link_id=124295369580
- Vídeo: https://www.youtube.com/watch?v=ycl2t34Js5Y
