const express = require('express');
const bodyParser = require('body-parser');
const qr = require('qrcode');
const cors = require('cors');

const app = express();
const port = 3000;

// Configurar middlewares
app.use(cors());
app.use(bodyParser.json());

// Dados simulados (seriam substituídos por um banco de dados em produção)
const products = [
  { id: 1, name: 'Produto A', price: 50.0 },
  { id: 2, name: 'Produto B', price: 30.0 },
  { id: 3, name: 'Produto C', price: 20.0 },
];

// Rota para listar produtos
app.get('/products', (req, res) => {
  res.json(products);
});

// Rota para gerar QR Code Pix
app.post('/generate-pix', async (req, res) => {
  try {
    const { name, cpf, products } = req.body;

    // Calcular o valor total do pedido
    const totalAmount = products.reduce((acc, product) => acc + product.price * product.quantity, 0);

    // Gerar código Pix (Exemplo simples - substitua com integração real)
    const pixPayload = `PIX: Nome=${name}; CPF=${cpf}; Total=${totalAmount.toFixed(2)}`;

    // Gerar QR Code a partir do payload
    const qrCode = await qr.toDataURL(pixPayload);

    // Retornar QR Code e resumo do pedido
    res.json({
      qrCode,
      summary: {
        name,
        cpf,
        products,
        totalAmount,
      },
    });
  } catch (error) {
    res.status(500).json({ error: 'Erro ao gerar QR Code Pix' });
  }
});

// Rota para simular a visualização do pedido pelo administrador
app.get('/orders', (req, res) => {
  // Exemplo: você pode armazenar pedidos em um banco de dados e retornar aqui
  res.json({ message: 'Admin view não implementada ainda.' });
});

// Inicializar o servidor
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
