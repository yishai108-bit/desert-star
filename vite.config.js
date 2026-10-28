import { defineConfig } from 'vite';
import { resolve } from 'node:path';

// Static multi-page site. Images and og.jpg live in public/ so their URLs never change
// (WhatsApp previews depend on a stable og.jpg URL).
export default defineConfig({
  base: '/desert-star/',
  build: {
    rollupOptions: {
      input: {
        he: resolve(__dirname, 'index.html'),
        en: resolve(__dirname, 'en/index.html'),
        ru: resolve(__dirname, 'ru/index.html'),
      },
    },
  },
});
