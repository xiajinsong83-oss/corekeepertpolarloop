/* ============================================================
   Core Keeper Hub — 工具共享辅助脚本 (tools.js)
   零外部依赖原生 JS · 全局命名空间 CK
   供全部 12 个交互工具调用（esc / toast / copy / sortTable 等）
   ============================================================ */
(function(global){
  'use strict';
  var CK = {};

  /* HTML 转义：任何外部数据渲染进 innerHTML 前必须过 esc() */
  function esc(s){
    return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){
      return { '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[c];
    });
  }

  /* 简易防抖 */
  function debounce(fn, ms){
    var t;
    return function(){
      var args = arguments, ctx = this;
      clearTimeout(t);
      t = setTimeout(function(){ fn.apply(ctx, args); }, ms || 150);
    };
  }

  /* 解析百分比/数值字符串："37%" → 37；"Common" → NaN */
  function pct(v){
    return parseFloat(String(v == null ? '' : v).replace(/[^0-9.\-]/g, ''));
  }

  /* 轻量 toast 提示（复用 .tool-toast 样式） */
  var toastTimer = null;
  function toast(msg){
    var el = document.querySelector('.tool-toast');
    if(!el){
      el = document.createElement('div');
      el.className = 'tool-toast';
      document.body.appendChild(el);
    }
    el.textContent = msg;
    // 触发重排后再加 show，保证过渡动画生效
    void el.offsetWidth;
    el.classList.add('show');
    if(toastTimer){ clearTimeout(toastTimer); }
    toastTimer = setTimeout(function(){ el.classList.remove('show'); }, 2200);
  }

  /* 复制文本到剪贴板（含降级方案），成功时按钮反馈 + toast */
  function copy(text, btn){
    var done = function(ok){
      if(btn && btn.classList){
        var old = btn.textContent;
        btn.disabled = true;
        btn.textContent = ok ? '✓ Copied' : 'Copy';
        setTimeout(function(){ btn.disabled = false; btn.textContent = old; }, 1400);
      }
      toast(ok ? 'Copied to clipboard' : 'Copy failed');
    };
    if(navigator.clipboard && navigator.clipboard.writeText){
      navigator.clipboard.writeText(text).then(function(){ done(true); }, function(){ legacyCopy(text, done); });
    } else {
      legacyCopy(text, done);
    }
  }
  function legacyCopy(text, done){
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch(e){ ok = false; }
    document.body.removeChild(ta);
    done(ok);
  }

  /* 表格排序：col 从 0 起；dir 为 'asc'|'desc'，省略则自动切换。
     数字感知：单元格首段含数字按数值比较，否则按字符串比较。
     调用后自动更新 th 上的 asc/desc 标记类。 */
  function sortTable(table, col, dir){
    if(!table || !table.tBodies || !table.tBodies[0]) return;
    var tbody = table.tBodies[0];
    var rows = Array.prototype.slice.call(tbody.rows);
    var ths = table.querySelectorAll('th');
    var current = ths[col] ? (ths[col].classList.contains('asc') ? 'asc' : ths[col].classList.contains('desc') ? 'desc' : null) : null;
    var ndir = dir || (current === 'asc' ? 'desc' : 'asc');

    for(var i = 0; i < ths.length; i++){
      ths[i].classList.remove('asc', 'desc');
    }
    if(ths[col]){ ths[col].classList.add(ndir); }

    function cellVal(r){
      var c = r.cells[col];
      var txt = c ? (c.textContent || '').replace(/\s+/g, ' ').trim() : '';
      var m = txt.match(/-?\d+(\.\d+)?/);
      return m ? { n: parseFloat(m[0]), s: txt } : { n: null, s: txt };
    }
    rows.sort(function(a, b){
      var va = cellVal(a), vb = cellVal(b);
      var r;
      if(va.n !== null && vb.n !== null){ r = va.n - vb.n; }
      else { r = va.s.localeCompare(vb.s); }
      return ndir === 'asc' ? r : -r;
    });
    for(var j = 0; j < rows.length; j++){ tbody.appendChild(rows[j]); }
    return ndir;
  }

  /* 唯一 id 生成（多实例短代码防冲突） */
  function uid(prefix){
    return (prefix || 'ck') + '-' + Math.random().toString(36).slice(2, 9);
  }

  /* 便捷查询 */
  function qs(sel, root){ return (root || document).querySelector(sel); }
  function qsa(sel, root){
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  /* 状态栏条带取色：按数值/百分比区间给条形图配色（始终带基类 tool-bar__fill，保证 height:100%） */
  function barColor(v, max){
    var r = max ? (v / max) : (v > 1 ? 1 : v);
    if(r >= 0.66) return 'tool-bar__fill';
    if(r >= 0.33) return 'tool-bar__fill tool-bar__fill--gold';
    return 'tool-bar__fill tool-bar__fill--blue';
  }

  /* 从元素 dataset 建键值对（可选） */
  function dataset(el){ return el ? (el.dataset || {}) : {}; }

  CK.esc = esc;
  CK.debounce = debounce;
  CK.pct = pct;
  CK.toast = toast;
  CK.copy = copy;
  CK.sortTable = sortTable;
  CK.uid = uid;
  CK.qs = qs;
  CK.qsa = qsa;
  CK.barColor = barColor;
  CK.dataset = dataset;

  global.CK = CK;
})(window);
