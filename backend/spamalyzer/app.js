'use strict';

const path = require('node:path');
const AutoLoad = require('@fastify/autoload');

module.exports = async function (fastify, opts) {
  try {

    fastify.addHook('onRequest', async (request, reply) => {
      console.log(`[REQUEST] ${request.method} ${request.url}`);
      console.log(`[HEADERS]`, request.headers);
      if (request.body) {
        console.log(`[BODY]`, request.body);
      }
    });

    fastify.addHook('onResponse', async (request, reply) => {
      console.log(`[RESPONSE] ${reply.statusCode} ${request.method} ${request.url}`);
    });

    fastify.setErrorHandler((error, request, reply) => {
      console.error(`[ERROR HANDLER]`, error.message, error.stack);
      reply.status(500).send({ error: true, message: error.message });
    });

    fastify.register(require('@fastify/cors'), { origin: '*' });
    fastify.register(require('@fastify/helmet'), { contentSecurityPolicy: false });

    fastify.register(AutoLoad, { dir: path.join(__dirname, 'plugins'), options: Object.assign({}, opts) });
    fastify.register(AutoLoad, { dir: path.join(__dirname, 'routes'), options: Object.assign({}, opts) });

    fastify.ready(err => {
      if (err) {
        console.error('[Critical Error] Server startup failed:', err);
        process.exit(1);
      }
      console.log('[INFO] Server is ready at http://localhost:6050');
    });
  } catch (err) {
    console.error('[Critical Error] Exception during server setup:', err);
    process.exit(1);
  }
};
