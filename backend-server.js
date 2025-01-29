const express = require('express');
const app = express();
const port = 3000;

// Middleware para permitir o recebimento de dados em JSON
app.use(express.json());

// Rota de exemplo para receber alertas
app.post('/alert', (req, res) => {
  const alertData = req.body;
  console.log('Alerta recebido:', alertData);
  res.status(200).send('Alerta recebido');
});

// Inicia o servidor
app.listen(port, () => {
  console.log(`Servidor backend rodando na porta ${port}`);
});
