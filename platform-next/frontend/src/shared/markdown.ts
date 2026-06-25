import MarkdownIt from 'markdown-it'
import DOMPurify from 'dompurify'

// 与 DocViewer 同款配置：html/linkify/breaks 全开，输出经 dompurify 净化。
const md = new MarkdownIt({ html: true, linkify: true, breaks: true })

/** 把 markdown 字符串渲染成已净化的 HTML；空输入返回空串。 */
export function renderMarkdown(src: string): string {
  if (!src) return ''
  return DOMPurify.sanitize(md.render(String(src)))
}
