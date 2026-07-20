import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// dev proxy: /api → 后端 8000（C1+C2+C3 已跑通）
// build 产物 dist/ 由后端 main.py 静态托管（SPA 兜底）。
export default defineConfig({
  plugins: [vue()],
  server: { proxy: { '/api': 'http://localhost:8000' } },
  build: { outDir: 'dist' },
})
