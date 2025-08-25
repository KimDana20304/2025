<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>꿈 분석 + 심리 테스트 (MBTI 기반)</title>
  <meta name="description" content="MBTI와 원하는 꿈을 입력하면 꿈 해석과 맞춤 심리 테스트를 제공합니다. 결과는 링크로 공유할 수 있습니다." />
  <style>
    :root{
      --bg: #0b1020;         /* deep navy */
      --panel:#121935;       /* panel navy */
      --muted:#93a1be;      /* mute text */
      --text:#eaf0ff;        /* main text */
      --accent:#7aa2ff;     /* blue */
      --accent-2:#b892ff;   /* purple */
      --good:#6ee7a7;
      --warn:#ffd166;
      --bad:#ff6b6b;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Noto Sans KR, Apple SD Gothic Neo, "Malgun Gothic", sans-serif;
      background: radial-gradient(1200px 800px at 20% 0%, rgba(122,162,255,.15), transparent 50%),
                  radial-gradient(900px 600px at 110% 10%, rgba(184,146,255,.15), transparent 50%),
                  var(--bg);
      color:var(--text);
      -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;
    }
    .container{max-width:1000px;margin:0 auto;padding:32px}
    .app-title{font-size:clamp(24px,3vw,36px);font-weight:800;letter-spacing:.3px;display:flex;align-items:center;gap:12px}
    .badge{font-size:12px;padding:4px 10px;border-radius:999px;background:linear-gradient(135deg,var(--accent),var(--accent-2));color:#0b1020;font-weight:700}
    .grid{display:grid;gap:20px}
    @media(min-width:900px){.grid{grid-template-columns:1.1fr .9fr}}
    .card{background:linear-gradient(180deg,rgba(255,255,255,.03),rgba(255,255,255,.01));border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:20px;box-shadow:0 10px 30px rgba(0,0,0,.25), inset 0 1px 1px rgba(255,255,255,.04)}
    .card h2{margin:0 0 12px;font-size:18px;letter-spacing:.2px}
    label{display:block;font-size:13px;color:var(--muted);margin-bottom:6px}
    input[type="text"],textarea,select{
      width:100%; padding:12px 14px; border-radius:12px; border:1px solid rgba(255,255,255,.12);
      background:#0f1530; color:var(--text); outline:none; font-size:14px;
      box-shadow: inset 0 1px 0 rgba(255,255,255,.04);
    }
    textarea{min-height:110px; resize:vertical}
    .row{display:flex; gap:12px}
    .row > *{flex:1}
    .btn{
      display:inline-flex; align-items:center; justify-content:center; gap:10px;
      border:none; border-radius:12px; padding:12px 16px; cursor:pointer; font-weight:700; letter-spacing:.2px;
      color:#0b1020; background:linear-gradient(135deg,var(--accent),var(--accent-2)); box-shadow:0 10px 20px rgba(122,162,255,.25);
    }
    .btn.secondary{background:#1a234a;color:var(--text);border:1px solid rgba(255,255,255,.12);box-shadow:none}
    .btn.ghost{background:transparent;color:var(--text);border:1px dashed rgba(255,255,255,.25)}
    .btn:disabled{opacity:.6;cursor:not-allowed}
    .chips{display:flex;flex-wrap:wrap;gap:8px}
    .chip{font-size:12px;padding:6px 10px;border-radius:999px;background:#18214d;border:1px solid rgba(255,255,255,.1);color:#cfe1ff}
    .muted{color:var(--muted)}
    .mono{font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace}
    .result{line-height:1.7}
    .result h3{margin:18px 0 6px}
    .divider{height:1px;background:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent);margin:16px 0}
    .pill{padding:6px 10px;border-radius:999px;background:#0f1530;border:1px solid rgba(255,255,255,.12);font-size:12px}
    .scale{display:flex;gap:8px}
    .scale button{flex:1;padding:10px 0;border-radius:10px;border:1px solid rgba(255,255,255,.12);background:#0f1530;color:var(--text);cursor:pointer}
    .scale button.active{background:linear-gradient(180deg,rgba(122,162,255,.25),rgba(122,162,255,.05));border-color:rgba(122,162,255,.6)}
    .footer{text-align:center;color:var(--muted);margin-top:18px;font-size:12px}
    .status{font-weight:800}
    .status.good{color:var(--good)}
    .status.warn{color:var(--warn)}
    .status.bad{color:var(--bad)}
    .code{background:#0f1530;border:1px solid rgba(255,255,255,.1);padding:10px;border-radius:10px}
  </style>
</head>
<body>
  <div class="container">
    <div class="app-title">
      🌙 꿈 분석 + 심리 테스트
      <span class="badge">MBTI 기반</span>
    </div>

    <div class="grid" id="app">
      <!-- 입력 패널 -->
      <section class="card">
        <h2>1. 입력</h2>
        <div class="row">
          <div>
            <label for="mbti">MBTI</label>
            <input id="mbti" type="text" placeholder="예: INFP" maxlength="4" />
          </div>
          <div>
            <label for="name">닉네임 (선택)</label>
            <input id="name" type="text" placeholder="공유 카드에 표시" />
          </div>
        </div>

        <label for="dream">원하는 꿈(상상했던 꿈 장면이나 키워드)</label>
        <textarea id="dream" placeholder="예: 무대에서 노래하는 꿈, 시험에 늦는 꿈, 하늘을 나는 꿈..."></textarea>

        <div class="row" style="margin-top:10px">
          <button class="btn" id="analyzeBtn">분석 시작</button>
          <button class="btn secondary" id="clearBtn" title="모든 입력 초기화">초기화</button>
        </div>
      </section>

      <!-- 결과/공유 패널 -->
      <section class="card">
        <h2>2. 결과 & 공유</h2>
        <div id="resultWrap" class="result muted">먼저 왼쪽에서 MBTI와 꿈을 입력하고 분석을 시작하세요.</div>
        <div class="divider"></div>
        <div class="row">
          <button class="btn" id="copyUrlBtn" disabled>공유 URL 복사</button>
          <button class="btn ghost" id="previewBtn" disabled>공유 미리보기</button>
        </div>
        <p class="footer">링크에는 MBTI, 닉네임, 꿈 텍스트, 결과 요약이 포함됩니다.</p>
      </section>
    </div>

    <!-- 심리 테스트 영역 -->
    <section class="card" id="quizCard" style="margin-top:20px; display:none">
      <h2>3. 맞춤 심리 테스트</h2>
      <p class="muted">아래 문항은 입력한 꿈 주제에 맞게 자동 생성됩니다. 각 문항에 대한 동의 정도를 선택하세요.</p>
      <div id="quizWrap"></div>
      <div class="divider"></div>
      <div class="row">
        <button class="btn" id="scoreBtn">심리 점수 계산</button>
        <span class="pill mono" id="quizStatus">5문항 · 5점 척도</span>
      </div>
    </section>

  </div>

  <script>
    // —————— Utilities ——————
    const qs = (s, el=document) => el.querySelector(s);
    const qsa = (s, el=document) => [...el.querySelectorAll(s)];
    const clamp = (n, a, b)=> Math.min(b, Math.max(a, n));

    function toTitle(s){
      return s.toUpperCase().replace(/[^A-Z]/g,"");
    }

    function encodeShare(data){
      const json = JSON.stringify(data);
      const b64 = btoa(unescape(encodeURIComponent(json)));
      return b64;
    }
    function decodeShare(b64){
      try{
        const json = decodeURIComponent(escape(atob(b64)));
        return JSON.parse(json);
      }catch(e){return null}
    }

    function setShareUrl(payload){
      const base = location.origin + location.pathname;
      const b64 = encodeShare(payload);
      const url = base + "?d=" + b64;
      return url;
    }

    // —————— Domain logic ——————
    const THEME_KEYWORDS = [
      {key:"시험", tag:"performance", synonyms:["시험","지각","공부","평가","수능","테스트"]},
      {key:"무대", tag:"stage", synonyms:["무대","공연","댄스","노래","발표"]},
      {key:"추락", tag:"falling", synonyms:["추락","떨어짐","넘어짐","밑으로"]},
      {key:"비행", tag:"flying", synonyms:["나는","비행","하늘","날아","부유"]},
      {key:"이빨", tag:"teeth", synonyms:["이빨","치아","이가 빠짐","충치"]},
      {key:"쫓김", tag:"chase", synonyms:["쫓김","도망","쫓아옴","공포"]},
      {key:"물", tag:"water", synonyms:["물","바다","파도","강","호수","비"]},
      {key:"학교", tag:"school", synonyms:["학교","교실","선생님","친구","급식"]},
      {key:"연애", tag:"love", synonyms:["연애","짝사랑","고백","데이트"]},
      {key:"유명인", tag:"celebrity", synonyms:["아이돌","연예인","유명인","셀럽"]},
      {key:"동물", tag:"animal", synonyms:["강아지","고양이","동물","뱀","거미"]},
      {key:"시험지연", tag:"lateness", synonyms:["지각","늦음","버스 놓침","전철"]},
    ];

    const MBTI_LENSES = {
      I:"내적 성찰 선호", E:"대외 표현 욕구",
      N:"직관·상상 강조", S:"현실·세부 중시",
      T:"논리·분석 성향", F:"감정·관계 중시",
      J:"계획·통제 선호", P:"유연·즉흥 선호"
    };

    function detectTags(text){
      const t = text.toLowerCase();
      const hits = new Set();
      for(const item of THEME_KEYWORDS){
        if(item.synonyms.some(s=> t.includes(s.toLowerCase()))) hits.add(item.tag);
      }
      if(hits.size===0) hits.add("custom");
      return [...hits];
    }

    function analyzeDream(dream, mbti){
      const tags = detectTags(dream);
      const mb = toTitle(mbti);
      const lenses = mb.split("").map(ch=> MBTI_LENSES[ch] || null).filter(Boolean);

      const insights = [];
      const tips = [];

      function add(key, txt, tip){ insights.push({key, txt}); if(tip) tips.push(tip) }

      for(const tag of tags){
        switch(tag){
          case "performance":
            add(tag, "평가 상황에 대한 압박감과 성과 집착이 반영된 테마입니다.", "준비와 휴식의 균형을 잡고, 모의 연습으로 통제감을 높여보세요.");
            break;
          case "stage":
            add(tag, "자기 표현 욕구와 인정 욕구가 강하게 드러납니다.", "작은 무대 경험부터 늘리며 자신감의 근육을 키우세요.");
            break;
          case "falling":
            add(tag, "통제 상실 혹은 실패에 대한 두려움이 시사됩니다.", "현실의 불확실성을 구체적 계획으로 나눠 작게 통제하세요.");
            break;
          case "flying":
            add(tag, "자유·성취·확장 욕구를 상징합니다.", "도전 목록을 만들고 한 단계씩 달성하며 상승감을 현실화하세요.");
            break;
          case "teeth":
            add(tag, "외모·자신감·의사소통에 대한 민감성이 높습니다.", "자기 표현 훈련과 구강 관리 루틴으로 실질적 안정을.");
            break;
          case "chase":
            add(tag, "피하고 싶은 과제나 인물에 대한 회피 정서가 있습니다.", "작은 노출 과제로 회피를 감소시키면 불안이 줄어듭니다.");
            break;
          case "water":
            add(tag, "감정의 파도와 정서 변동성을 반영합니다.", "감정 기록과 수면 위생을 함께 관리하세요.");
            break;
          case "school":
            add(tag, "또래 관계와 성취, 소속감 이슈가 얽혀 있을 수 있습니다.", "관계 경계 설정과 학습 루틴 최적화를 병행하세요.");
            break;
          case "love":
            add(tag, "애착·친밀감 욕구가 활성화된 상태입니다.", "자기 가치 확인 루틴과 건강한 의사소통 연습을 권장.");
            break;
          case "celebrity":
            add(tag, "롤모델 동일시와 이상적 자아에 대한 갈망이 보입니다.", "현실 목표를 아이콘에서 역설계해 체크리스트화 하세요.");
            break;
          case "animal":
            add(tag, "본능·보호욕·두려움 등 기초 정서가 드러납니다.", "동물의 상징과 자신의 현재 스트레스원을 연결해 보세요.");
            break;
          case "lateness":
            add(tag, "시간관리와 책임에 대한 압박이 큽니다.", "수면·알람·버퍼시간 설정으로 예측 가능성을 높이세요.");
            break;
          default:
            add("custom", "개성적 장면의 상징을 바탕으로 개인적 의미가 큽니다.", "핵심 키워드 3개를 뽑아 의미를 적어보세요.");
        }
      }

      // MBTI 조정
      if(mb){
        if(mb.includes("I")) tips.push("혼자 충전 시간을 계획에 넣으면 회복 효율이 올라갑니다.");
        if(mb.includes("E")) tips.push("사람들과의 공유와 피드백이 동기 부여에 도움이 됩니다.");
        if(mb.includes("N")) insights.push({key:"N", txt:"상징과 가능성을 중시하는 경향이 해석을 풍부하게 만듭니다."});
        if(mb.includes("S")) insights.push({key:"S", txt:"구체적 사실과 루틴을 중시해 현실 적용력이 높습니다."});
        if(mb.includes("T")) tips.push("결과와 지표로 진전을 확인하면 안정됩니다.");
        if(mb.includes("F")) tips.push("감정 라벨링(지금 내 감정은 …)을 습관화하세요.");
        if(mb.includes("J")) tips.push("체크리스트·캘린더로 통제감을 확보하세요.");
        if(mb.includes("P")) tips.push("여유 버퍼와 선택지를 남기면 몰입이 좋아집니다.");
      }

      const summary = insights.map(x=>"• "+x.txt).join("\n");
      return {tags, insights, tips:[...new Set(tips)], summary};
    }

    function makeQuiz(tags){
      // 3개 축: 수행불안(PA), 통제감(LOC), 사회표현(SE)
      const base = {
        performance:[
          {t:"중요한 순간에 실수할까 걱정된다.", k:"PA"},
          {t:"준비를 많이 해도 불안이 쉽게 사라지지 않는다.", k:"PA"},
          {t:"일정표를 세우면 마음이 안정된다.", k:"LOC+"},
          {t:"즉흥적인 상황이 더 잘 맞는다.", k:"LOC-"},
          {t:"결과를 사람들과 공유하면 동기부여가 된다.", k:"SE"},
        ],
        stage:[
          {t:"사람들 앞에서 나를 표현하는 게 즐겁다.", k:"SE"},
          {t:"실수하면 오래 기억에 남아 괴롭다.", k:"PA"},
          {t:"리허설을 충분히 하면 마음이 편해진다.", k:"LOC+"},
          {t:"즉흥 무대도 큰 부담이 없다.", k:"LOC-"},
          {t:"칭찬이 나의 추진력을 높인다.", k:"SE"},
        ],
        falling:[
          {t:"통제할 수 없는 상황이 가장 두렵다.", k:"PA"},
          {t:"작은 계획이 있으면 불안이 줄어든다.", k:"LOC+"},
          {t:"실패는 새로운 시도의 일부라고 생각한다.", k:"LOC-"},
          {t:"불안을 숨기기보다 공유하는 편이다.", k:"SE"},
          {t:"예상치 못한 변화는 피하고 싶다.", k:"PA"},
        ],
        flying:[
          {t:"새로운 도전에 설렌다.", k:"LOC-"},
          {t:"자유롭게 계획을 바꾸는 편이다.", k:"LOC-"},
          {t:"목표를 세우면 성취 속도가 빨라진다.", k:"LOC+"},
          {t:"타인의 시선보다 나의 기준이 더 중요하다.", k:"SE-"},
          {t:"실패를 해도 금방 회복한다.", k:"PA-"},
        ],
        custom:[
          {t:"요즘 감정 기복이 있었다.", k:"PA"},
          {t:"작은 루틴만 있어도 마음이 가라앉는다.", k:"LOC+"},
          {t:"즉흥적으로 움직이면 더 잘 된다.", k:"LOC-"},
          {t:"감정과 생각을 주변과 공유한다.", k:"SE"},
          {t:"완벽하지 않아도 일단 시작한다.", k:"PA-"},
        ]
      };
      const pool = tags.map(t=> base[t]).filter(Boolean).flat();
      const fallback = base.custom;
      const picked = (pool.length? pool: fallback).slice(0,5);
      return picked.map((q,i)=> ({ id: i+1, text:q.t, key:q.k }));
    }

    function scoreAnswers(answers){
      // answers: [{key:'PA', val:1..5}, ...]
      const acc = {PA:0, LOCp:0, LOCm:0, SE:0, PAn:0, SEn:0, n:0};
      for(const a of answers){
        if(a.key.startsWith('PA')){
          if(a.key.endsWith('-')) acc.PAn += a.val; else acc.PA += a.val;
        } else if(a.key.startsWith('SE')){
          if(a.key.endsWith('-')) acc.SEn += a.val; else acc.SE += a.val;
        } else if(a.key==='LOC+') acc.LOCp += a.val; else if(a.key==='LOC-') acc.LOCm += a.val;
        acc.n++;
      }
      // Normalize 1..5 -> 0..100 scale
      const norm = v => Math.round((v - 1*acc.n) / (4*acc.n) * 100);
      const posNorm = (v, m) => Math.round((v - 1*m) / (4*m) * 100);
      const mPA = (acc.PA? 1:0) + (acc.PAn?1:0) + (acc.LOCp?0:0); // dummy
      return {
        performance_anxiety: norm(acc.PA),
        control_flex: posNorm(acc.LOCm, Math.max(1, answers.filter(a=>a.key==='LOC-').length)),
        control_plan: posNorm(acc.LOCp, Math.max(1, answers.filter(a=>a.key==='LOC+').length)),
        social_expression: posNorm(acc.SE, Math.max(1, answers.filter(a=>a.key.startsWith('SE') && !a.key.endsWith('-')).length)),
        resilience_hint: posNorm(acc.PAn, Math.max(1, answers.filter(a=>a.key==='PA-').length)),
      };
    }

    function categorizeScore(s){
      const band = (x)=> x>=67? {b:"높음",c:"good"} : x>=34? {b:"중간",c:"warn"}:{b:"낮음",c:"bad"};
      return {
        performance_anxiety: band(100 - s.resilience_hint - s.performance_anxiety/2),
        control_flex: band(s.control_flex),
        control_plan: band(s.control_plan),
        social_expression: band(s.social_expression),
      };
    }

    function buildSummaryText(analysis, scores, bands){
      const lines = [];
      if(analysis.insights.length){ lines.push("꿈 해석 요약", ...analysis.insights.map(x=>"- "+x.txt)); }
      const tipHead = analysis.tips.length? "실천 팁": null;
      const tips = analysis.tips.slice(0,4).map(t=>"- "+t);
      if(tipHead) lines.push(tipHead, ...tips);
      if(scores){
        lines.push("심리 지표", `· 통제 유연성: ${scores.control_flex}% (${bands.control_flex.b})`, `· 계획 기반 통제: ${scores.control_plan}% (${bands.control_plan.b})`, `· 사회적 표현 욕구: ${scores.social_expression}% (${bands.social_expression.b})`);
      }
      return lines.join("\n");
    }

    // —————— UI wiring ——————
    const mbtiEl = qs('#mbti');
    const nameEl = qs('#name');
    const dreamEl = qs('#dream');
    const analyzeBtn = qs('#analyzeBtn');
    const clearBtn = qs('#clearBtn');
    const resultWrap = qs('#resultWrap');
    const copyUrlBtn = qs('#copyUrlBtn');
    const previewBtn = qs('#previewBtn');
    const quizCard = qs('#quizCard');
    const quizWrap = qs('#quizWrap');
    const scoreBtn = qs('#scoreBtn');
    const quizStatus = qs('#quizStatus');

    let current = {
      mbti: '', name:'', dream:'', analysis:null, quiz:null, answers:[], scores:null, bands:null, shareUrl:''
    };

    function renderAnalysis(){
      if(!current.analysis){ return; }
      const {tags, insights, tips} = current.analysis;
      resultWrap.classList.remove('muted');
      resultWrap.innerHTML = `
        <div class="chips" style="margin-bottom:8px">${tags.map(t=>`<span class="chip">#${t}</span>`).join('')}</div>
        <h3>꿈 해석</h3>
        <ul>${insights.map(x=>`<li>${x.txt}</li>`).join('')}</ul>
        <h3>맞춤 팁</h3>
        <ul>${tips.slice(0,5).map(x=>`<li>${x}</li>`).join('')}</ul>
        <div class="divider"></div>
        <div class="pill mono">MBTI: ${current.mbti || '미입력'}</div>
      `;
    }

    function renderQuiz(quiz){
      quizWrap.innerHTML = '';
      quiz.forEach(q=>{
        const row = document.createElement('div');
        row.style.margin = '12px 0';
        row.innerHTML = `
          <div>${q.id}. ${q.text}</div>
          <div class="scale" role="radiogroup" aria-label="${q.text}">
            ${[1,2,3,4,5].map(v=>`<button type="button" data-q="${q.id}" data-val="${v}">${v}</button>`).join('')}
          </div>
        `;
        quizWrap.appendChild(row);
      });
      quizWrap.addEventListener('click', onScaleClick);
      quizStatus.textContent = `${quiz.length}문항 · 5점 척도`;
      quizCard.style.display = 'block';
      current.answers = [];
    }

    function onScaleClick(e){
      const btn = e.target.closest('button[data-q]');
      if(!btn) return;
      const qid = +btn.dataset.q; const val = +btn.dataset.val;
      // toggle state
      const group = btn.parentElement; qsa('button', group).forEach(b=> b.classList.remove('active'));
      btn.classList.add('active');
      // store
      const q = current.quiz.find(x=> x.id===qid);
      const idx = current.answers.findIndex(a=> a.id===qid);
      const rec = { id: qid, key:q.key, val };
      if(idx>-1) current.answers[idx]=rec; else current.answers.push(rec);
    }

    function ensureInputs(){
      const mb = toTitle(mbtiEl.value.trim());
      const dr = dreamEl.value.trim();
      if(!mb || mb.length!==4){ alert('MBTI를 4글자로 입력하세요. 예: INFP'); return null; }
      if(!dr){ alert('원하는 꿈(키워드 또는 장면)을 입력하세요.'); return null; }
      return {mb, dr};
    }

    analyzeBtn.addEventListener('click', ()=>{
      const ok = ensureInputs();
      if(!ok) return;
      current.mbti = ok.mb; current.name = nameEl.value.trim(); current.dream = ok.dr;
      current.analysis = analyzeDream(current.dream, current.mbti);
      current.quiz = makeQuiz(current.analysis.tags);
      renderAnalysis();
      renderQuiz(current.quiz);
      copyUrlBtn.disabled = false; previewBtn.disabled = false;
      // prepare first share url (without scores)
      const payload = {
        v:1, mbti: current.mbti, name: current.name, dream: current.dream,
        analysis: current.analysis.summary, scores:null
      };
      current.shareUrl = setShareUrl(payload);
    });

    scoreBtn.addEventListener('click', ()=>{
      if(!current.quiz){ alert('먼저 분석을 진행하세요.'); return; }
      if(current.answers.length < current.quiz.length){
        const remain = current.quiz.length - current.answers.length;
        alert(`${remain}개 문항이 남았습니다.`); return;
      }
      const scores = scoreAnswers(current.answers);
      const bands = categorizeScore(scores);
      current.scores = scores; current.bands = bands;

      // append scores to result UI
      const scoreHtml = `
        <div class="divider"></div>
        <h3>심리 지표</h3>
        <ul>
          <li>통제 유연성: <span class="status ${bands.control_flex.c}">${scores.control_flex}% (${bands.control_flex.b})</span></li>
          <li>계획 기반 통제: <span class="status ${bands.control_plan.c}">${scores.control_plan}% (${bands.control_plan.b})</span></li>
          <li>사회적 표현 욕구: <span class="status ${bands.social_expression.c}">${scores.social_expression}% (${bands.social_expression.b})</span></li>
        </ul>
      `;
      resultWrap.insertAdjacentHTML('beforeend', scoreHtml);

      // refresh share url with scores
      const textSummary = buildSummaryText(current.analysis, scores, bands);
      const payload = { v:1, mbti: current.mbti, name: current.name, dream: current.dream, analysis: textSummary, scores };
      current.shareUrl = setShareUrl(payload);
    });

    copyUrlBtn.addEventListener('click', async ()=>{
      if(!current.shareUrl){ alert('먼저 분석을 진행하세요.'); return; }
      try{
        await navigator.clipboard.writeText(current.shareUrl);
        copyUrlBtn.textContent = '복사 완료';
        setTimeout(()=> copyUrlBtn.textContent='공유 URL 복사', 1400);
      }catch(e){
        // fallback
        const ta = document.createElement('textarea'); ta.value = current.shareUrl; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove();
        alert('링크가 복사되었습니다.');
      }
    });

    previewBtn.addEventListener('click', ()=>{
      if(!current.shareUrl){ alert('먼저 분석을 진행하세요.'); return; }
      window.open(current.shareUrl, '_blank');
    });

    clearBtn.addEventListener('click', ()=>{
      mbtiEl.value = '';
      nameEl.value = '';
      dreamEl.value = '';
      resultWrap.classList.add('muted');
      resultWrap.textContent = '먼저 왼쪽에서 MBTI와 꿈을 입력하고 분석을 시작하세요.';
      quizWrap.innerHTML=''; quizCard.style.display='none';
      copyUrlBtn.disabled = true; previewBtn.disabled = true;
      current = { mbti:'', name:'', dream:'', analysis:null, quiz:null, answers:[], scores:null, bands:null, shareUrl:'' };
    });

    // —————— Auto load from shared URL ——————
    (function initFromUrl(){
      const b64 = new URLSearchParams(location.search).get('d');
      if(!b64) return;
      const data = decodeShare(b64);
      if(!data) return;
      if(data.mbti) mbtiEl.value = data.mbti;
      if(data.name) nameEl.value = data.name;
      if(data.dream) dreamEl.value = data.dream;

      // render quick readonly summary
      if(data.analysis){
        resultWrap.classList.remove('muted');
        const title = data.name? `${data.name}님의 결과 요약` : '공유 결과 요약';
        resultWrap.innerHTML = `
          <h3>${title}</h3>
          <pre class="code" style="white-space:pre-wrap">${data.analysis}</pre>
        `;
        copyUrlBtn.disabled = false; previewBtn.disabled = false;
        current.shareUrl = location.href;
      }
    })();
  </script>
</body>
</html>
