var pjson = require('./package.json');
console.log(`Starting MUSE v${pjson.version}...`);

window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector)
      if (element) element.innerText = text
    }
  
    for (const type of ['chrome', 'node', 'electron']) {
      replaceText(`${type}-version`, process.versions[type])
    }

    replaceText('muse-version', pjson.version);
  })
  
  