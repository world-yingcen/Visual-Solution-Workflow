(() => {
  'use strict';

  const snippets = document.querySelectorAll('main pre > code');
  if (!snippets.length) return;

  const status = document.createElement('p');
  status.className = 'sr-only';
  status.setAttribute('role', 'status');
  document.body.append(status);

  // 直接開啟本機 HTML 或剪貼簿 API 不可用時，沿用瀏覽器的複製能力。
  const fallbackCopy = text => {
    const focus = document.activeElement;
    const selection = window.getSelection();
    const ranges = selection
      ? Array.from({ length: selection.rangeCount }, (_, i) => selection.getRangeAt(i).cloneRange())
      : [];
    const buffer = document.createElement('textarea');
    buffer.className = 'clipboard-buffer';
    buffer.value = text;
    buffer.readOnly = true;
    buffer.tabIndex = -1;
    document.body.append(buffer);

    try {
      buffer.focus({ preventScroll: true });
      buffer.select();
      if (!document.execCommand('copy')) throw new Error('Copy unavailable');
    } finally {
      buffer.remove();
      if (focus instanceof HTMLElement) focus.focus({ preventScroll: true });
      if (selection) {
        selection.removeAllRanges();
        ranges.forEach(range => selection.addRange(range));
      }
    }
  };

  snippets.forEach(code => {
    const pre = code.parentElement;
    if (pre.parentElement.classList.contains('copy-block')) return;

    const block = document.createElement('div');
    block.className = 'copy-block';
    pre.before(block);
    block.append(pre);

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-button';
    button.textContent = '複製';
    button.setAttribute('aria-label', '複製這段指令');
    block.append(button);

    let resetTimer;
    button.addEventListener('click', async () => {
      clearTimeout(resetTimer);
      status.textContent = '';
      button.disabled = true;
      const text = code.textContent.trim();

      try {
        if (navigator.clipboard?.writeText) {
          try {
            await navigator.clipboard.writeText(text);
          } catch {
            fallbackCopy(text);
          }
        } else {
          fallbackCopy(text);
        }
        button.textContent = '已複製';
        status.textContent = '指令已複製到剪貼簿。';
      } catch {
        button.textContent = '請手動複製';
        status.textContent = '無法自動複製，請選取指令後手動複製。';
      } finally {
        button.disabled = false;
        resetTimer = setTimeout(() => { button.textContent = '複製'; }, 2000);
      }
    });
  });
})();
