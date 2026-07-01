;(async () => {
  let items = [];
  for (let a of document.querySelectorAll('a[href*="final_documents2"]')) {
    let title = a.textContent.trim();
    let url = a.href;
    if (items.some(x => x.url === url)) continue;
    let idx = items.push({ title, url, files: [] });
    console.log('Checking: ' + title);
    try {
      let r = await fetch(url);
      let html = await r.text();
      let d = document.createElement('html');
      d.innerHTML = html;
      for (let l of d.querySelectorAll('a[href*="deliverable_documents"]')) {
        if (!items[idx - 1].files.some(f => f === l.href)) {
          items[idx - 1].files.push(l.href);
        }
      }
    } catch (e) {
      items[idx - 1].error = e.message;
    }
  }
  window._results = items;
  console.log('Done — ' + items.length + ' activities checked');
  console.log(JSON.stringify(items, null, 2));
})();