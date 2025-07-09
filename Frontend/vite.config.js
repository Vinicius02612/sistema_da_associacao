// Plugins
import vue from '@vitejs/plugin-vue'
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

// Utilities
import { defineConfig } from 'vite'
import { fileURLToPath, URL } from 'node:url'

const renderAppHostname = process.env.VITE_RENDER_APP_HOSTNAME || 'sistema-da-associacao-l5ow.onrender.com';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({ 
      template: { transformAssetUrls }
    }),
    // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vite-plugin
    vuetify({
      autoImport: true,
      styles: {
        configFile: 'src/styles/settings.scss',
      },
    }),
  ],
  define: { 'process.env': {} },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
    extensions: [
      '.js',
      '.json',
      '.jsx',
      '.mjs',
      '.ts',
      '.tsx',
      '.vue',
    ],
  },
  server: {
		host: '0.0.0.0',
    port: 3000,
		fs: {
      // Permite o acesso a arquivos fora do diretório raiz do projeto se necessário
      // e inclui o host do Render.
      // O Render pode servir os arquivos de build de forma diferente, mas é bom ter.
      allow: [
        '.', // Permite o diretório atual do projeto
        renderAppHostname // Permite o host do Render
      ],
      cachedir: '.vite_cache' // Adiciona um diretório de cache, boa prática
		},
	}
})
