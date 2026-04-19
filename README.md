# Chatbot IA com Frontend

## Estrutura do Projeto

```
Projeto_IA_Chatbot/
├── backend/
│   ├── main.py          # API FastAPI
│   └── requirements.txt # Dependências Python
└── frontend/
    ├── src/
    │   ├── App.jsx      # Componente React
    │   ├── main.jsx     # Entry point
    │   └── index.css    # Estilos
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Como Executar

### 1. Backend (FastAPI)

```powershell
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

O backend estará em: `http://localhost:8000`

### 2. Frontend (React)

```powershell
cd frontend
npm install
npm run dev
```

O frontend estará em: `http://localhost:5173`

## Uso

1. Inicie o backend primeiro
2. Inicie o frontend
3. Acesse `http://localhost:5173` no navegador
4. Digite suas mensagens no chat!