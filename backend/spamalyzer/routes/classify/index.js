'use strict';

const dotenv = require('dotenv');

dotenv.config();

module.exports = async function (fastify, opts) {
  fastify.post('/', async (request, reply) => {
    const { emailText } = request.body;

    if (!emailText) {
      return reply.code(400).send({ error: 'emailText is required' });
    }

    const pythonServiceUrl = process.env.PYTHON_SERVICE_URL; 

    console.log('[INFO] Using Python service URL:', pythonServiceUrl);

    try {
      const resp = await fetch(pythonServiceUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ emailText })
      });

      if (!resp.ok) {
        const errBody = await resp.text();
        console.error('[Python Service Error]', resp.status, errBody);
        return reply.code(resp.status).send({
          error: 'Python service error',
          details: errBody
        });
      }

      const data = await resp.json();
      return reply.send({
        message: `Wynik klasyfikacji: ${data.prediction}`
      });

    } catch (err) {
      console.error('[HTTP Error]', err.message);
      return reply.code(500).send({
        error: 'Internal Server Error',
        details: err.message
      });
    }
  });
};
