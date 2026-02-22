# 3pt-props
[3pt-scanner-v8 (15).html](https://github.com/user-attachments/files/25471528/3pt-scanner-v8.15.html)
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>3PT Edge Scanner v8.4</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#06080f;color:#e6edf3;font-family:"Segoe UI",system-ui,sans-serif;padding:16px;max-width:740px;margin:0 auto}
h1{font-size:20px;margin-bottom:4px}
.sub{color:#8b949e;font-size:12px;margin-bottom:16px}
.box{background:#0d1117;border:1px solid #21262d;border-radius:12px;padding:16px;margin-bottom:12px}
.row{display:flex;gap:8px;align-items:center;margin-bottom:8px}
label{font-size:11px;color:#8b949e;display:block;margin-bottom:4px}
input,select{height:36px;padding:0 10px;border-radius:8px;border:1px solid #21262d;background:#06080f;color:#e6edf3;font-size:13px;font-family:inherit;width:100%}
textarea{width:100%;padding:10px;border-radius:8px;border:1px solid #21262d;background:#06080f;color:#e6edf3;font-size:12px;font-family:"Consolas",monospace;resize:vertical}
button{font-family:inherit;cursor:pointer}
.btn{height:44px;border-radius:10px;border:none;color:#fff;font-size:14px;font-weight:700;width:100%;cursor:pointer}
.btn-go{background:linear-gradient(135deg,#10b981,#3b82f6)}
.btn-go:disabled{opacity:0.5;cursor:wait}
.btn-sm{height:32px;border-radius:6px;border:1px solid #21262d;background:#161b22;color:#e6edf3;font-size:11px;font-weight:600;padding:0 12px;width:auto}
.btn-sm:hover{border-color:#3b82f6}
.btn-sm.red{border-color:#ef444444;color:#ef4444}
.btn-sm.red:hover{background:#ef444418}
.btn-sm.green{border-color:#10b98144;color:#10b981}
.btn-sm.green:hover{background:#10b98118}
.tabs{display:flex;gap:4px;margin-bottom:12px}
.tab{flex:1;height:38px;border-radius:8px;border:1px solid #21262d;background:#0d1117;color:#8b949e;font-size:11px;font-weight:600}
.tab.active{background:#161b22;color:#e6edf3;border-color:#3b82f6}
.log{background:#0d1117;border:1px solid #21262d;border-radius:8px;padding:12px;margin-top:12px;font-size:11px;color:#8b949e;white-space:pre-wrap;max-height:300px;overflow:auto;line-height:1.7;font-family:"Consolas",monospace}
.card{background:#0d1117;border:1px solid #21262d;border-radius:12px;padding:12px;margin-bottom:8px}
.card.strong{border-color:#10b98155}.card.mod{border-color:#f59e0b44}
.edge-grid{display:grid;grid-template-columns:50px 1fr 1fr;border:1px solid #21262d;border-radius:8px;overflow:hidden;margin-top:8px}
.edge-cell{padding:8px;text-align:center;background:#06080f}
.edge-cell+.edge-cell{border-left:1px solid #21262d}
.green{color:#10b981}.red{color:#ef4444}.amber{color:#f59e0b}.blue{color:#3b82f6}.purple{color:#8b5cf6}
.badge{display:inline-block;padding:3px 8px;border-radius:6px;font-size:10px;font-weight:700}
.badge-strong{background:#10b98118;color:#10b981}.badge-mod{background:#f59e0b14;color:#f59e0b}
.badge-lean{background:#3b82f614;color:#3b82f6}.badge-none{background:#21262d;color:#484f58}
.badge-caution{background:#ef444420;color:#ef4444}
.card.caution{border-color:#ef444444;border-style:dashed}
.msg{padding:10px 14px;border-radius:8px;margin-bottom:10px;font-size:12px;line-height:1.6}
.msg-info{background:#0d1117;border:1px solid #21262d;color:#8b949e}
.msg-ok{background:#10b98112;border:1px solid #10b98133;color:#10b981}
.msg-err{background:#ef444412;border:1px solid #ef444433;color:#ef4444}
.hide{display:none}
.adj-row{display:flex;gap:4px;flex-wrap:wrap;margin-top:6px}
.adj-pill{display:inline-flex;align-items:center;gap:3px;padding:2px 7px;border-radius:10px;font-size:9px;font-weight:600;background:#161b22;border:1px solid #21262d}
.adj-pill.neg{color:#ef4444;border-color:#ef444433}
.adj-pill.pos{color:#10b981;border-color:#10b98133}
.ctx-bar{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:6px}
.ctx-chip{font-size:9px;padding:2px 6px;border-radius:4px;background:#161b22;color:#8b949e;border:1px solid #21262d}
/* Player editor */
.pe-grid{display:grid;grid-template-columns:1fr 50px 45px 50px 45px 42px 40px 36px;gap:4px;font-size:11px;align-items:center}
.pe-grid.hdr{color:#484f58;font-size:9px;font-weight:700;text-transform:uppercase;margin-bottom:4px;padding-bottom:6px;border-bottom:1px solid #21262d}
.pe-grid input{height:28px;font-size:11px;padding:0 6px;text-align:center}
.pe-grid input.name-in{text-align:left}
.pe-row{border-bottom:1px solid #161b22;padding:3px 0}
.pe-count{font-size:12px;color:#8b949e;margin-bottom:8px}
.pe-search{margin-bottom:10px}
.pe-actions{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
</style>
</head>
<body>
<h1>🟢 3PT Edge Scanner <span style="font-size:11px;color:#8b949e;font-weight:400">v8.4</span></h1>
<p class="sub">Sharp-calibrated · 80+ players · Live stats · L10 splits · Teammate effects · Alternate lines · Blowout · Spread · Game total</p>

<div class="box" id="keyBox">
  <label>🔑 ODDS API KEY <span style="color:#484f58">(the-odds-api.com — for scanning props)</span></label>
  <div class="row">
    <input type="password" id="keyInput" placeholder="Paste your Odds API key here" style="flex:1">
    <button class="btn" onclick="saveKey()" style="width:80px;height:36px;background:#3b82f6;font-size:12px">Save</button>
  </div>
  <label style="margin-top:8px">📡 BALLDONTLIE KEY <span style="color:#484f58">(app.balldontlie.io — for live stats refresh)</span></label>
  <div class="row">
    <input type="password" id="bdlKey" placeholder="Paste your balldontlie API key here" style="flex:1">
    <button class="btn" onclick="saveBDL()" style="width:80px;height:36px;background:#8b5cf6;font-size:12px">Save</button>
  </div>
</div>

<div class="tabs">
  <button class="tab active" id="tabScan" onclick="showTab('scan')">🚀 Scan</button>
  <button class="tab" id="tabManual" onclick="showTab('manual')">📋 Manual</button>
  <button class="tab" id="tabPlayers" onclick="showTab('players')">👤 Players</button>
  <button class="tab" id="tabSetup" onclick="showTab('setup')">⚙ Setup</button>
</div>

<!-- SCAN TAB -->
<div id="panelScan">
  <div style="display:flex;gap:8px;align-items:center">
    <button class="btn btn-go" id="scanBtn" onclick="doScan()">🚀 Scan All 3PT Props</button>
    <button class="btn" style="background:#1e2430;border:1px solid #30363d;font-size:13px;padding:8px 14px" onclick="document.getElementById('helpOverlay').style.display='flex'">❓ How to Read</button>
  </div>
  <div id="scanMsg" class="msg hide"></div>
  <div id="injuryPanel" class="hide"></div>
  <div id="scanSummary" class="msg hide"></div>
  <div id="board"></div>
  <div id="logArea" class="hide"><div style="font-size:10px;color:#8b5cf6;font-weight:700;margin-bottom:4px">📋 ACTIVITY LOG</div><div class="log" id="logContent"></div></div>
</div>

<!-- HELP OVERLAY -->
<div id="helpOverlay" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,0.85);z-index:999;justify-content:center;align-items:center;padding:16px;overflow-y:auto" onclick="if(event.target===this)this.style.display='none'">
  <div style="max-width:520px;width:100%;background:#0d1117;border:1px solid #30363d;border-radius:12px;padding:20px;position:relative">
    <button onclick="document.getElementById('helpOverlay').style.display='none'" style="position:absolute;top:10px;right:14px;background:none;border:none;color:#8b949e;font-size:18px;cursor:pointer">✕</button>
    <div style="font-size:16px;font-weight:800;color:#c9d1d9;margin-bottom:16px">📖 How to Read a Card</div>

    <!-- Example card mock -->
    <div style="background:#161b22;border:1px solid #30363d;border-radius:10px;padding:14px;margin-bottom:16px;position:relative">
      <!-- Header -->
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
        <div>
          <span style="font-size:14px;font-weight:700;color:#c9d1d9">Steph Curry</span>
          <span style="font-size:18px;font-weight:800;color:#f59e0b;margin-left:6px">3.5</span>
          <div style="font-size:10px;color:#8b949e">GSW vs Thunder</div>
        </div>
        <div style="text-align:right">
          <span style="padding:2px 8px;border-radius:4px;font-size:10px;font-weight:700;background:#10b98120;color:#10b981">STRONG</span>
          <div style="font-size:10px;color:#484f58;margin-top:2px">λ 3.82 (raw 4.01)</div>
        </div>
      </div>
      <!-- Annotate arrows for header -->
      <div style="display:flex;gap:4px;flex-wrap:wrap;margin-bottom:8px">
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#1e2430;border:1px solid #30363d;color:#8b949e">✈ AWAY</span>
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#1e2430;border:1px solid #30363d;color:#8b949e">📊 -5.5</span>
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#1e2430;border:1px solid #30363d;color:#8b949e">🎯 O/U 224</span>
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#1e2430;border:1px solid #30363d;color:#8b949e">⏱ 33min</span>
      </div>
      <!-- Book rows -->
      <div style="display:grid;grid-template-columns:1fr 80px 80px;gap:0;font-size:9px;color:#484f58;padding:0 4px;margin-bottom:2px"><span>BOOK</span><span style="text-align:center">OVER</span><span style="text-align:center">UNDER</span></div>
      <div style="display:grid;grid-template-columns:1fr 80px 80px;gap:0;padding:4px;border-radius:4px;background:rgba(16,185,129,0.06);align-items:center">
        <span style="font-size:11px;color:#c9d1d9;font-weight:700">FanDuel</span>
        <span style="text-align:center"><span style="font-size:13px;font-weight:700;color:#10b981">-118</span> <span style="font-size:10px;color:#10b981">+6.2%</span></span>
        <span style="text-align:center"><span style="font-size:13px;font-weight:700;color:#c9d1d9">-102</span> <span style="font-size:10px;color:#ef4444">-1.8%</span></span>
      </div>
      <div style="display:grid;grid-template-columns:1fr 80px 80px;gap:0;padding:4px;align-items:center">
        <span style="font-size:11px;color:#c9d1d9">DraftKings</span>
        <span style="text-align:center"><span style="font-size:13px;font-weight:700;color:#c9d1d9">-125</span> <span style="font-size:10px;color:#10b981">+5.1%</span></span>
        <span style="text-align:center"><span style="font-size:13px;font-weight:700;color:#c9d1d9">-105</span> <span style="font-size:10px;color:#ef4444">-0.9%</span></span>
      </div>
      <div style="font-size:9px;color:#484f58;margin-top:4px;text-align:center">fair: over -135 / under +115</div>
      <!-- Adj pills -->
      <div style="display:flex;gap:4px;flex-wrap:wrap;margin-top:6px">
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#ef444418;color:#ef4444">AWAY -0.5%</span>
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#10b98118;color:#10b981">TOTAL 224 +2.1%</span>
        <span style="font-size:9px;padding:2px 6px;border-radius:4px;background:#ef444418;color:#ef4444">MEDIAN -3.0%</span>
      </div>
    </div>

    <!-- Explanations -->
    <div style="font-size:12px;color:#c9d1d9;line-height:1.8">
      <div style="font-weight:700;color:#f59e0b;margin-bottom:6px">① Header</div>
      <div style="margin-bottom:10px;padding-left:10px;border-left:2px solid #30363d;color:#8b949e;font-size:11px">
        <b style="color:#c9d1d9">Player Name</b> + <b style="color:#f59e0b">Line (3.5)</b> = the prop. "Over 3.5 threes made."<br>
        <b style="color:#10b981">Signal badge</b> = model's confidence. <span style="color:#10b981">STRONG</span> (5%+ edge), <span style="color:#3b82f6">MOD</span> (3-5%), <span style="color:#f59e0b">LEAN</span> (1-3%), <span style="color:#484f58">NONE</span>, <span style="color:#ef4444">CAUTION</span>.<br>
        <b style="color:#c9d1d9">λ (lambda)</b> = model's predicted 3PT made. Raw = before adjustments, other = after all 15 variables.
      </div>

      <div style="font-weight:700;color:#f59e0b;margin-bottom:6px">② Context Chips</div>
      <div style="margin-bottom:10px;padding-left:10px;border-left:2px solid #30363d;color:#8b949e;font-size:11px">
        <b style="color:#c9d1d9">Home/Away</b>, <b style="color:#c9d1d9">Spread</b> (negative = favored), <b style="color:#c9d1d9">O/U</b> (game total), <b style="color:#c9d1d9">Minutes</b>, <b style="color:#ef4444">💨 Blowout %</b> (if >15%).
      </div>

      <div style="font-weight:700;color:#f59e0b;margin-bottom:6px">③ Book Odds Table</div>
      <div style="margin-bottom:10px;padding-left:10px;border-left:2px solid #30363d;color:#8b949e;font-size:11px">
        All sportsbooks offering this line, <b style="color:#10b981">best edge on top</b> (highlighted row).<br>
        <b style="color:#c9d1d9">Over/Under odds</b> = what the book is offering (American format).<br>
        <span style="color:#10b981">Green %</span> = <b style="color:#c9d1d9">positive edge</b> — the book is offering better odds than the model's fair price. This is where value lives.<br>
        <span style="color:#ef4444">Red %</span> = <b style="color:#c9d1d9">negative edge</b> — the book's odds are worse than fair. No value on that side.<br>
        <b style="color:#c9d1d9">Fair line</b> = what the model thinks the odds should be. Compare to book odds to see mispricing.
      </div>

      <div style="font-weight:700;color:#f59e0b;margin-bottom:6px">④ Adjustment Pills</div>
      <div style="margin-bottom:10px;padding-left:10px;border-left:2px solid #30363d;color:#8b949e;font-size:11px">
        Each pill shows a variable moving the prediction up or down.<br>
        <span style="color:#10b981">Green = boost</span> (high total, home, hot streak).<br>
        <span style="color:#ef4444">Red = drag</span> (away, cold streak, blowout risk, median regression).<br>
        Teammate injury pills (e.g. "PM OUT -15%") appear when key players are out.
      </div>

      <div style="font-weight:700;color:#f59e0b;margin-bottom:6px">⑤ Quick Decision Guide</div>
      <div style="padding-left:10px;border-left:2px solid #30363d;color:#8b949e;font-size:11px">
        ✅ <b style="color:#10b981">Bet</b>: STRONG signal, green edge on the top book, lambda close to the line.<br>
        🤔 <b style="color:#f59e0b">Consider</b>: MOD signal, check the context — is the edge mostly from one adjustment?<br>
        ⏭ <b style="color:#484f58">Skip</b>: LEAN/NONE signals, or when all edges are red.<br>
        ⚠ <b style="color:#ef4444">Avoid</b>: CAUTION cards — the line is too far from model expectations.
      </div>
    </div>

    <button onclick="document.getElementById('helpOverlay').style.display='none'" style="width:100%;margin-top:16px;padding:10px;background:#10b981;color:#0d1117;border:none;border-radius:8px;font-weight:700;cursor:pointer;font-size:13px">Got it ✓</button>
  </div>
</div>

<!-- MANUAL TAB -->
<div id="panelManual" class="hide">
  <div class="box">
    <label>Paste props — one per line</label>
    <textarea id="manualInput" rows="8" placeholder="Curry 2.5 -115 -105&#10;Mitchell 3.5 +130 -155&#10;Edwards 2.5 +100 -120&#10;SGA 1.5 -130 +110"></textarea>
    <div style="font-size:10px;color:#484f58;margin:6px 0">Format: <span class="amber">PlayerName Line OverOdds UnderOdds</span></div>
    <button class="btn" onclick="parseManual()" style="background:#3b82f6;margin-top:6px">⚡ Analyze Lines</button>
  </div>
</div>

<!-- PLAYERS TAB -->
<div id="panelPlayers" class="hide">
  <div class="box">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
      <div><span style="font-size:14px;font-weight:700">👤 Player Database</span><br>
      <span class="pe-count" id="playerCount"></span></div>
    </div>
    <div class="pe-actions">
      <button class="btn-sm green" onclick="showAddForm()">+ Add Player</button>
      <button class="btn-sm" id="refreshAllBtn" onclick="autoRefreshAll()" style="border-color:#8b5cf644;color:#8b5cf6">📡 Refresh All Stats</button>
      <button class="btn-sm" onclick="testBDL()" style="border-color:#f59e0b44;color:#f59e0b">🔧 Test API</button>
      <button class="btn-sm" onclick="exportPlayers()">📤 Export</button>
      <button class="btn-sm" onclick="importPlayersPrompt()">📥 Import</button>
      <button class="btn-sm red" onclick="resetDefaults()">↺ Reset Defaults</button>
    </div>
    <div id="refreshStatus" class="hide" style="margin-bottom:10px">
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
        <div style="flex:1;height:6px;background:#21262d;border-radius:3px;overflow:hidden"><div id="refreshProgFill" style="height:100%;background:linear-gradient(90deg,#8b5cf6,#3b82f6);border-radius:3px;width:0%;transition:width 0.3s"></div></div>
        <span id="refreshProgPct" style="font-size:10px;color:#8b949e;width:35px;text-align:right">0%</span>
      </div>
      <div id="refreshProgText" style="font-size:10px;color:#8b949e"></div>
    </div>
    <div id="lastRefresh" style="font-size:10px;color:#484f58;margin-bottom:8px"></div>
    <!-- Add form (hidden by default) -->
    <div id="addForm" class="hide" style="margin-bottom:12px">
      <div class="box" style="border-color:#10b98133">
        <div style="font-size:11px;font-weight:700;color:#10b981;margin-bottom:8px">ADD NEW PLAYER</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px">
          <div><label>Full Name</label><input id="addN" placeholder="Trae Young"></div>
          <div><label>Team</label><select id="addT"></select></div>
          <div><label>3PA/Game</label><input id="addA" type="number" step="0.1" placeholder="9.5"></div>
          <div><label>3P%</label><input id="addP" type="number" step="0.1" placeholder="37.5"></div>
          <div><label>Recent 3PA</label><input id="addRA" type="number" step="0.1" placeholder="10.0"></div>
          <div><label>Recent 3P%</label><input id="addRP" type="number" step="0.1" placeholder="38.0"></div>
          <div><label>Minutes/Game</label><input id="addM" type="number" step="0.5" placeholder="34.0"></div>
          <div><label>PF/36 min</label><input id="addPF" type="number" step="0.1" placeholder="2.3"></div>
        </div>
        <div style="display:flex;gap:6px;margin-top:8px">
          <button class="btn-sm green" onclick="addPlayer()">✓ Save</button>
          <button class="btn-sm" onclick="hideAddForm()">Cancel</button>
        </div>
      </div>
    </div>
    <!-- Import form -->
    <div id="importForm" class="hide" style="margin-bottom:12px">
      <div class="box" style="border-color:#3b82f644">
        <div style="font-size:11px;font-weight:700;color:#3b82f6;margin-bottom:8px">IMPORT PLAYERS (JSON)</div>
        <textarea id="importData" rows="4" placeholder='Paste exported JSON here'></textarea>
        <div style="display:flex;gap:6px;margin-top:6px">
          <button class="btn-sm green" onclick="importPlayers()">✓ Import</button>
          <button class="btn-sm" onclick="document.getElementById('importForm').className='hide'">Cancel</button>
        </div>
      </div>
    </div>
    <!-- Search -->
    <div class="pe-search"><input id="playerSearch" placeholder="🔍 Search players..." oninput="renderPlayerList()"></div>
    <!-- Header -->
    <div class="pe-grid hdr"><span>Name / Team</span><span>3PA</span><span>3P%</span><span>L10 3PA</span><span>L10 3P%</span><span>MIN</span><span>PF36</span><span></span></div>
    <!-- Player list -->
    <div id="playerList"></div>
  </div>
</div>

<!-- SETUP TAB -->
<div id="panelSetup" class="hide">
  <div class="box">
    <h3 style="color:#10b981;margin-bottom:12px">🔑 Odds API Key (for scanning props)</h3>
    <div class="box" style="border-left:3px solid #3b82f6"><b class="blue">Step 1:</b> Go to <a href="https://the-odds-api.com" target="_blank" style="color:#f59e0b;font-weight:700">the-odds-api.com</a></div>
    <div class="box" style="border-left:3px solid #3b82f6"><b class="blue">Step 2:</b> Sign up — email + password</div>
    <div class="box" style="border-left:3px solid #10b981"><b class="green">Step 3:</b> Copy API key → paste above → Save</div>
  </div>
  <div class="box">
    <h3 style="color:#8b5cf6;margin-bottom:12px">📡 Balldontlie Key (for live stats refresh)</h3>
    <div class="box" style="border-left:3px solid #8b5cf6"><b class="purple">Step 1:</b> Go to <a href="https://app.balldontlie.io" target="_blank" style="color:#f59e0b;font-weight:700">app.balldontlie.io</a></div>
    <div class="box" style="border-left:3px solid #8b5cf6"><b class="purple">Step 2:</b> Create free account → go to Account Settings</div>
    <div class="box" style="border-left:3px solid #10b981"><b class="green">Step 3:</b> Copy API key → paste above → Save. Then go to 👤 Players → <b>📡 Refresh All Stats</b></div>
    <div style="font-size:11px;color:#8b949e;margin-top:8px">Free tier = 60 requests/min. One full refresh uses ~240 requests (3 per player: search + season avg + last 10 game logs). Takes about 4 minutes. Do this once a week.</div>
  </div>
  <div class="box">
    <h3 class="purple" style="margin-bottom:8px">⚙ Model Settings</h3>
    <label>Overdispersion: <span id="odVal">1.35</span></label>
    <input type="range" id="odSlider" min="1" max="2.5" step="0.05" value="1.35" oninput="odVal.textContent=this.value" style="height:auto;padding:0;margin-bottom:12px">
    <label>Recency Weight: <span id="rwVal">30%</span></label>
    <input type="range" id="rwSlider" min="0" max="0.6" step="0.05" value="0.3" oninput="rwVal.textContent=Math.round(this.value*100)+'%'" style="height:auto;padding:0;margin-bottom:12px">
    <label>Median Correction: <span id="medVal">ON</span></label>
    <input type="range" id="medSlider" min="0" max="1" step="1" value="1" oninput="medVal.textContent=this.value==='1'?'ON':'OFF'" style="height:auto;padding:0">
  </div>
</div>

<div id="errorDisplay" class="msg msg-err hide" style="position:fixed;bottom:16px;left:16px;right:16px;max-width:700px;margin:0 auto;z-index:999"></div>

<script>
window.onerror=function(msg,src,line){var el=document.getElementById("errorDisplay");el.textContent="JS Error: "+msg+" (line "+line+")";el.className="msg msg-err";};

// ═══════ MATH ═══════
function poissonPMF(l,k){if(l<=0)return k===0?1:0;var p=-l+k*Math.log(l);for(var i=2;i<=k;i++)p-=Math.log(i);return Math.exp(p);}
function negBinPMF(m,v,k){if(m<=0)return k===0?1:0;if(v<=m)return poissonPMF(m,k);var r=(m*m)/(v-m),p=m/v,c=0;for(var i=0;i<k;i++)c+=Math.log(r+i)-Math.log(i+1);return Math.exp(c+r*Math.log(p)+k*Math.log(1-p));}
function calcProbs(l,od){var v=l*od,o=[];for(var k=0;k<=14;k++)o.push(od>1.05?negBinPMF(l,v,k):poissonPMF(l,k));return o;}
function overProb(pr,line){var c=Math.ceil(line),o=0;if(line%1!==0){for(var k=c;k<pr.length;k++)o+=pr[k];}else{for(var k=line+1;k<pr.length;k++)o+=pr[k];}return o;}
function toAm(p){if(p<=.01)return"+9999";if(p>=.99)return"-9999";return p>=.5?"-"+Math.round((p/(1-p))*100):"+"+Math.round(((1-p)/p)*100);}
function parseAm(s){if(!s)return null;var n=parseInt(String(s).replace(/[^0-9\-+]/g,""));if(isNaN(n))return null;return n>0?100/(n+100):Math.abs(n)/(Math.abs(n)+100);}

function medianCorr(lam,od){if(lam<=0.3||od<=1.05)return lam;var v=lam*od;return Math.max(lam-(v-lam)/(3*lam),lam*0.85);}
function blowProb(sp){var s=1/(1+Math.exp(-(sp-10)/4));return Math.min(0.07+0.58*s,0.70);}
function blowMinFrac(m){return Math.max(0.55,(m-10)/m);}
var LAT=224;
function gtMult(t){if(!t||t<180||t>270)return 1;return 1+(t-LAT)*0.003;}

// ═══════ TEAMS ═══════
var T={ATL:{n:"Hawks",pa:102.1,d:115.7},BOS:{n:"Celtics",pa:95.2,d:113.4},BRK:{n:"Nets",pa:96.6,d:118.3},CHA:{n:"Hornets",pa:97.8,d:115.8},CHI:{n:"Bulls",pa:101.5,d:118.4},CLE:{n:"Cavaliers",pa:101.0,d:114.3},DAL:{n:"Mavericks",pa:101.7,d:114.3},DEN:{n:"Nuggets",pa:97.3,d:118.2},DET:{n:"Pistons",pa:99.7,d:109.3},GSW:{n:"Warriors",pa:99.8,d:113.5},HOU:{n:"Rockets",pa:96.0,d:112.9},IND:{n:"Pacers",pa:100.7,d:117.2},LAC:{n:"Clippers",pa:95.8,d:116.6},LAL:{n:"Lakers",pa:98.7,d:117.6},MEM:{n:"Grizzlies",pa:101.1,d:115.8},MIA:{n:"Heat",pa:104.0,d:112.4},MIL:{n:"Bucks",pa:97.7,d:117.3},MIN:{n:"Timberwolves",pa:100.8,d:113.2},NOP:{n:"Pelicans",pa:99.9,d:119.4},NYK:{n:"Knicks",pa:97.8,d:113.8},OKC:{n:"Thunder",pa:99.4,d:107.9},ORL:{n:"Magic",pa:99.8,d:114.8},PHI:{n:"76ers",pa:98.7,d:115.7},PHX:{n:"Suns",pa:98.0,d:113.9},POR:{n:"Trail Blazers",pa:101.1,d:116.6},SAC:{n:"Kings",pa:99.3,d:120.8},SAS:{n:"Spurs",pa:100.1,d:111.8},TOR:{n:"Raptors",pa:98.4,d:113.2},UTA:{n:"Jazz",pa:101.7,d:122.5},WAS:{n:"Wizards",pa:100.9,d:121.6}};
var LP=0,LD=0,tk;for(tk in T){LP+=T[tk].pa;LD+=T[tk].d;}LP/=30;LD/=30;

// ═══════ DEFAULT PLAYER DATABASE ═══════
// Rule #1: NO ESTIMATED DATA. Stats are blank until API-verified.
// Only names and teams here. Stats come from "Refresh All Stats" only.
var DEFAULT_PLAYERS = [
  {n:"Stephen Curry",t:"GSW"},{n:"Luka Doncic",t:"LAL"},{n:"James Harden",t:"CLE"},
  {n:"Anthony Edwards",t:"MIN"},{n:"Donovan Mitchell",t:"CLE"},{n:"Tyrese Maxey",t:"PHI"},
  {n:"Trae Young",t:"WAS"},{n:"Michael Porter Jr.",t:"BRK"},{n:"Kon Knueppel",t:"CHA"},
  {n:"LaMelo Ball",t:"CHA"},{n:"Damian Lillard",t:"POR"},{n:"Kyrie Irving",t:"DAL"},
  {n:"Desmond Bane",t:"ORL"},{n:"Anfernee Simons",t:"CHI"},{n:"CJ McCollum",t:"ATL"},
  {n:"Buddy Hield",t:"GSW"},{n:"Sam Merrill",t:"CLE"},{n:"Dillon Brooks",t:"PHX"},
  {n:"Jalen Green",t:"PHX"},{n:"Derrick White",t:"BOS"},{n:"Jaylen Brown",t:"BOS"},
  {n:"Jayson Tatum",t:"BOS"},{n:"Jalen Brunson",t:"NYK"},{n:"Jamal Murray",t:"DEN"},
  {n:"Donte DiVincenzo",t:"MIN"},{n:"A.J. Green",t:"MIL"},{n:"Norman Powell",t:"MIA"},
  {n:"Klay Thompson",t:"DAL"},{n:"Duncan Robinson",t:"DET"},{n:"Payton Pritchard",t:"BOS"},
  {n:"Reed Sheppard",t:"HOU"},{n:"Shai Gilgeous-Alexander",t:"OKC"},
  {n:"Bobby Portis",t:"MIL"},{n:"De'Aaron Fox",t:"SAS"},{n:"Devin Booker",t:"PHX"},
  {n:"Paul George",t:"PHI"},{n:"Jalen Johnson",t:"ATL"},{n:"Franz Wagner",t:"ORL"},
  {n:"Cade Cunningham",t:"DET"},{n:"Jalen Williams",t:"OKC"},
  {n:"Tyrese Haliburton",t:"IND"},{n:"Tyler Herro",t:"MIA"},{n:"Coby White",t:"CHA"},
  {n:"Kevin Durant",t:"HOU"},{n:"Mikal Bridges",t:"NYK"},{n:"RJ Barrett",t:"TOR"},
  {n:"Scottie Barnes",t:"TOR"},{n:"Cam Thomas",t:"MIL"},{n:"Gradey Dick",t:"TOR"},
  {n:"Malik Monk",t:"SAC"},{n:"Fred VanVleet",t:"HOU"},{n:"Darius Garland",t:"LAC"},
  {n:"Immanuel Quickley",t:"TOR"},{n:"Jrue Holiday",t:"POR"},
  {n:"Austin Reaves",t:"LAL"},{n:"D'Angelo Russell",t:"DAL"},
  {n:"Khris Middleton",t:"DAL"},{n:"Bogdan Bogdanovic",t:"LAC"},
  {n:"Marcus Smart",t:"LAL"},{n:"Josh Hart",t:"NYK"},{n:"Nikola Jokic",t:"DEN"},
  {n:"LeBron James",t:"LAL"},{n:"Tobias Harris",t:"DET"},{n:"Max Strus",t:"CLE"},
  {n:"Keldon Johnson",t:"SAS"},{n:"Jordan Poole",t:"NOP"},{n:"Luguentz Dort",t:"OKC"},
  {n:"Tre Jones",t:"CHI"},{n:"Keyonte George",t:"UTA"},{n:"Collin Sexton",t:"CHI"},
  {n:"Lauri Markkanen",t:"UTA"},{n:"Karl-Anthony Towns",t:"NYK"},
  {n:"Jonas Valanciunas",t:"WAS"},{n:"Victor Wembanyama",t:"SAS"},
  {n:"Zach LaVine",t:"SAC"},{n:"Brandon Ingram",t:"TOR"},{n:"Dejounte Murray",t:"ATL"},
  {n:"Chet Holmgren",t:"OKC"},{n:"Jabari Smith Jr.",t:"HOU"},
  {n:"Paolo Banchero",t:"ORL"},{n:"Jalen Suggs",t:"ORL"},
  {n:"Grayson Allen",t:"PHX"},{n:"OG Anunoby",t:"NYK"},{n:"Landry Shamet",t:"NYK"},
  {n:"Dorian Finney-Smith",t:"HOU"},{n:"Royce O'Neale",t:"PHX"},
  {n:"Kelly Oubre Jr.",t:"PHI"},{n:"Quentin Grimes",t:"PHI"},
  {n:"Caris LeVert",t:"DET"},{n:"Patrick Williams",t:"CHI"},
  {n:"Matas Buzelis",t:"CHI"},{n:"Isaac Okoro",t:"CHI"},
  {n:"Tristan da Silva",t:"ORL"},{n:"Moe Wagner",t:"ORL"},{n:"Herb Jones",t:"NOP"},
  {n:"Tari Eason",t:"HOU"},{n:"Amen Thompson",t:"HOU"},{n:"Alperen Sengun",t:"HOU"},
  {n:"Anthony Black",t:"ORL"},{n:"Jalen Smith",t:"CHI"},
  {n:"Josh Giddey",t:"CHI"},{n:"Giannis Antetokounmpo",t:"MIL"},
  {n:"Deni Avdija",t:"POR"}
];

// ═══════ PLAYER DATA MANAGEMENT ═══════
var P = [];

function loadPlayers() {
  try {
    var saved = localStorage.getItem("3pt_players_v8");
    if (saved) { P = JSON.parse(saved); return; }
  } catch(e) {}
  // Initialize with blank stats — Rule #1: no estimates
  P = DEFAULT_PLAYERS.map(function(d){
    return {n:d.n, t:d.t, a:0, p:0, ra:0, rp:0, m:0, pf36:0, ha:0.008, v:false};
  });
  savePlayers();
}
function savePlayers() {
  try { localStorage.setItem("3pt_players_v8", JSON.stringify(P)); } catch(e) {}
  rebuildIndex();
}
function resetDefaults() {
  if (!confirm("Reset to default " + DEFAULT_PLAYERS.length + " players?\n\nAll stats will be cleared. You must run Refresh to get real data.\nRule #1: No estimates.")) return;
  P = DEFAULT_PLAYERS.map(function(d){
    return {n:d.n, t:d.t, a:0, p:0, ra:0, rp:0, m:0, pf36:0, ha:0.008, v:false};
  });
  // Clear refresh log and ID cache so everything re-fetches
  try{localStorage.removeItem("bdl_refresh_log");localStorage.removeItem("bdl_id_cache");}catch(e){}
  savePlayers();
  renderPlayerList();
}

// ═══════ PLAYER INDEX (for matching) ═══════
var PI = {};
function rebuildIndex() {
  PI = {};
  P.forEach(function(p) {
    PI[p.n.toLowerCase()] = p;
    var parts = p.n.toLowerCase().split(" ");
    // Index by last name
    var last = parts[parts.length - 1];
    // Only index by last name if unique, otherwise full name needed
    if (!PI[last]) PI[last] = p;
    // Index by first name + last name without dots/periods
    PI[p.n.toLowerCase().replace(/\./g, "")] = p;
  });
  // Common aliases
  if(PI["curry"])PI["steph"]=PI["curry"],PI["steph curry"]=PI["curry"];
  if(PI["gilgeous-alexander"])PI["sga"]=PI["gilgeous-alexander"],PI["shai"]=PI["gilgeous-alexander"];
  if(PI["edwards"])PI["ant"]=PI["edwards"];
  if(PI["michael porter jr."])PI["mpj"]=PI["michael porter jr."];else if(PI["michael porter jr"])PI["mpj"]=PI["michael porter jr"];
  if(PI["white"])PI["d. white"]=PI["white"],PI["d white"]=PI["white"];
  if(PI["green"])PI["aj green"]=PI["green"],PI["a.j. green"]=PI["green"];
  if(PI["wembanyama"])PI["wemby"]=PI["wembanyama"],PI["victor wembanyama"]=PI["wembanyama"];
  if(PI["gilgeous-alexander"])PI["shai gilgeous-alexander"]=PI["gilgeous-alexander"];
  if(PI["ball"])PI["lamelo"]=PI["ball"],PI["lamelo ball"]=PI["ball"];
  if(PI["james"])PI["lebron"]=PI["james"],PI["lebron james"]=PI["james"];
  if(PI["towns"])PI["kat"]=PI["towns"];
  if(PI["lillard"])PI["dame"]=PI["lillard"];
  if(PI["vanvleet"])PI["fvv"]=PI["vanvleet"];
  if(PI["durant"])PI["kd"]=PI["durant"];
  if(PI["brunson"])PI["jb"]=PI["brunson"];
  if(PI["og anunoby"])PI["og"]=PI["og anunoby"];
  if(PI["dorian finney-smith"])PI["dfs"]=PI["dorian finney-smith"],PI["doe doe"]=PI["dorian finney-smith"];
  if(PI["kelly oubre jr."])PI["oubre"]=PI["kelly oubre jr."];else if(PI["kelly oubre jr"])PI["oubre"]=PI["kelly oubre jr"];
  if(PI["jalen green"])PI["jalen green"]=PI["jalen green"];
  if(PI["grayson allen"])PI["g. allen"]=PI["grayson allen"];
  document.getElementById("playerCount").textContent = P.length + " players | Stats updated 2/21/26 (ESPN/StatMuse/BBRef verified)";
}

function matchPlayer(raw) {
  if (!raw) return null;
  var q = raw.toLowerCase().trim().replace(/\./g, "").replace(/'/g, "");
  if (PI[q]) return PI[q];
  // Try last name
  var parts = q.split(" ");
  var last = parts[parts.length - 1];
  if (PI[last]) return PI[last];
  // Fuzzy: substring match
  for (var i = 0; i < P.length; i++) {
    var pn = P[i].n.toLowerCase();
    if (pn.indexOf(q) >= 0) return P[i];
    if (q.length >= 4 && pn.split(" ").pop().indexOf(q.split(" ").pop()) >= 0) return P[i];
  }
  // Try matching first initial + last name (e.g. "S. Curry", "J. Brunson")
  if (parts.length >= 2 && parts[0].length <= 2) {
    var initial = parts[0].charAt(0);
    var lastName = parts.slice(1).join(" ");
    for (var i = 0; i < P.length; i++) {
      var pp = P[i].n.toLowerCase().split(" ");
      if (pp[0].charAt(0) === initial && pp[pp.length-1] === lastName) return P[i];
    }
  }
  return null;
}

var TM={};for(tk in T){TM[T[tk].n.toLowerCase()]=tk;TM[tk.toLowerCase()]=tk;}
TM["cavaliers"]="CLE";TM["cavs"]="CLE";TM["mavs"]="DAL";TM["wolves"]="MIN";TM["blazers"]="POR";TM["sixers"]="PHI";TM["clips"]="LAC";TM["dubs"]="GSW";
function matchTeam(raw){if(!raw)return null;var q=raw.toLowerCase().trim();if(TM[q])return TM[q];for(var k in TM){if(q.indexOf(k)>=0||k.indexOf(q)>=0)return TM[k];}return null;}

// ═══════ PLAYER EDITOR UI ═══════
function renderPlayerList() {
  var search = (document.getElementById("playerSearch").value || "").toLowerCase();
  var container = document.getElementById("playerList");
  var html = "";
  var shown = 0;
  var verified = 0, total = 0;
  P.forEach(function(p){ total++; if(p.v) verified++; });
  // Show verification status banner
  var bannerColor = verified===0 ? "#ef4444" : verified<total ? "#f59e0b" : "#10b981";
  html += '<div style="padding:8px 12px;margin-bottom:8px;border-radius:6px;background:'+bannerColor+'22;border:1px solid '+bannerColor+'55;font-size:12px;color:'+bannerColor+'">';
  if(verified===0) html += '⛔ No players have API-verified data. Run 📡 Refresh All Stats before scanning.';
  else if(verified<total) html += '⚠️ '+verified+'/'+total+' players verified. '+(total-verified)+' still need API refresh.';
  else html += '✅ All '+total+' players have API-verified data.';
  html += '</div>';
  P.forEach(function(p, idx) {
    if (search && p.n.toLowerCase().indexOf(search) < 0 && p.t.toLowerCase().indexOf(search) < 0) return;
    shown++;
    var isVerified = p.v;
    var rowOpacity = isVerified ? "1" : "0.4";
    var badge = isVerified ? '<span style="color:#10b981;font-size:9px" title="API-verified">✓</span>' : '<span style="color:#ef4444;font-size:9px" title="NOT verified — needs refresh">✗</span>';
    // Color L10 stats: green if trending up, red if down, amber if similar
    var raDiff=(p.ra||p.a)-p.a, rpDiff=(p.rp||p.p)-p.p;
    var raC=Math.abs(raDiff)<0.3?"#8b949e":raDiff>0?"#10b981":"#ef4444";
    var rpC=Math.abs(rpDiff)<1.0?"#f59e0b":rpDiff>0?"#10b981":"#ef4444";
    // Show arrow indicator for meaningful L10 shifts
    var raArrow=Math.abs(raDiff)<0.3?"":raDiff>0?"↑":"↓";
    var rpArrow=Math.abs(rpDiff)<1.0?"":rpDiff>0?"↑":"↓";
    html += '<div class="pe-grid pe-row" style="opacity:'+rowOpacity+'">' +
      '<span style="font-size:12px">'+badge+' <b>' + p.n + '</b> <span style="color:#484f58">' + p.t + '</span></span>' +
      '<span style="text-align:center;color:#8b949e">' + (isVerified?p.a:"—") + '</span>' +
      '<span style="text-align:center;color:#10b981">' + (isVerified?p.p:"—") + '</span>' +
      '<span style="text-align:center;color:'+raC+'">' + (isVerified?(p.ra||p.a)+raArrow:"—") + '</span>' +
      '<span style="text-align:center;color:'+rpC+'">' + (isVerified?(p.rp||p.p)+rpArrow:"—") + '</span>' +
      '<span style="text-align:center;color:#8b949e">' + (isVerified?p.m:"—") + '</span>' +
      '<span style="text-align:center;color:#8b949e">' + (isVerified?p.pf36:"—") + '</span>' +
      '<span><button class="btn-sm red" style="height:24px;padding:0 6px;font-size:9px" onclick="deletePlayer(' + idx + ')">✕</button></span></div>';
  });
  if (shown === 0) html = '<div style="padding:20px;text-align:center;color:#484f58">No players match "' + search + '"</div>';
  container.innerHTML = html;
}

function showAddForm() {
  document.getElementById("addForm").className = "";
  // Populate team dropdown
  var sel = document.getElementById("addT");
  if (sel.options.length <= 1) {
    sel.innerHTML = "";
    for (var k in T) {
      var opt = document.createElement("option");
      opt.value = k; opt.textContent = k + " - " + T[k].n;
      sel.appendChild(opt);
    }
  }
}
function hideAddForm() { document.getElementById("addForm").className = "hide"; }

function addPlayer() {
  var name = document.getElementById("addN").value.trim();
  var team = document.getElementById("addT").value;
  var a = parseFloat(document.getElementById("addA").value);
  var p = parseFloat(document.getElementById("addP").value);
  var ra = parseFloat(document.getElementById("addRA").value);
  var rp = parseFloat(document.getElementById("addRP").value);
  var m = parseFloat(document.getElementById("addM").value);
  var pf = parseFloat(document.getElementById("addPF").value);

  if (!name || !team || isNaN(a) || isNaN(p) || isNaN(m)) {
    alert("Fill in at least: Name, Team, 3PA, 3P%, and Minutes");
    return;
  }
  // Check for duplicate
  for (var i = 0; i < P.length; i++) {
    if (P[i].n.toLowerCase() === name.toLowerCase()) {
      if (!confirm(name + " already exists. Update their stats?")) return;
      P[i] = { n:name, t:team, a:a, p:p, ra:ra||a, rp:rp||p, m:m, pf36:pf||2.2, ha:.008 };
      savePlayers();
      renderPlayerList();
      hideAddForm();
      return;
    }
  }
  P.push({ n:name, t:team, a:a, p:p, ra:ra||a, rp:rp||p, m:m, pf36:pf||2.2, ha:.008 });
  P.sort(function(a,b) { return b.a - a.a; }); // sort by 3PA desc
  savePlayers();
  renderPlayerList();
  hideAddForm();
  // Clear form
  ["addN","addA","addP","addRA","addRP","addM","addPF"].forEach(function(id){document.getElementById(id).value="";});
}

function deletePlayer(idx) {
  if (!confirm("Remove " + P[idx].n + "?")) return;
  P.splice(idx, 1);
  savePlayers();
  renderPlayerList();
}

function exportPlayers() {
  var data = JSON.stringify(P, null, 2);
  var blob = new Blob([data], {type:"application/json"});
  var url = URL.createObjectURL(blob);
  var a = document.createElement("a");
  a.href = url; a.download = "3pt-players.json"; a.click();
  URL.revokeObjectURL(url);
}

function importPlayersPrompt() {
  document.getElementById("importForm").className = "";
}
function importPlayers() {
  var text = document.getElementById("importData").value.trim();
  try {
    var data = JSON.parse(text);
    if (!Array.isArray(data)) throw "Not an array";
    if (data.length === 0) throw "Empty array";
    if (!data[0].n || !data[0].t) throw "Invalid format";
    var action = confirm("Import " + data.length + " players?\n\nOK = Replace all players\nCancel = Add to existing");
    if (action) { P = data; } else { P = P.concat(data); }
    savePlayers();
    renderPlayerList();
    document.getElementById("importForm").className = "hide";
    document.getElementById("importData").value = "";
  } catch(e) {
    alert("Import failed: " + e + "\n\nMake sure you paste valid JSON from the Export function.");
  }
}

// ═══════ TEAMMATE ROLES DATABASE ═══════
// For each team: playmaker, lead shooter(s), star driver, key bigs
// role: PM=primary playmaker, S1/S2=top 3PT shooters, DR=star driver/paint attacker, B=key big
// This lets us classify injuries by archetype and adjust λ accordingly
var ROLES={
  ATL:[{n:"Nickeil Alexander-Walker",r:"PM"},{n:"Jalen Johnson",r:"DR"}],
  BOS:[{n:"Anfernee Simons",r:"PM"},{n:"Derrick White",r:"S1"},{n:"Payton Pritchard",r:"S2"},{n:"Jaylen Brown",r:"DR"}],
  BRK:[{n:"Ben Simmons",r:"PM"},{n:"Michael Porter Jr.",r:"S1"},{n:"Cam Thomas",r:"DR"}],
  CHA:[{n:"LaMelo Ball",r:"PM"},{n:"Kon Knueppel",r:"S1"},{n:"Brandon Miller",r:"DR"}],
  CHI:[{n:"Josh Giddey",r:"PM"},{n:"Anfernee Simons",r:"S1"},{n:"Matas Buzelis",r:"S2"},{n:"Josh Giddey",r:"DR"}],
  CLE:[{n:"James Harden",r:"PM"},{n:"Donovan Mitchell",r:"S1"},{n:"Max Strus",r:"S2"},{n:"Evan Mobley",r:"DR"}],
  DAL:[{n:"Kyrie Irving",r:"PM"},{n:"Klay Thompson",r:"S1"},{n:"Spencer Dinwiddie",r:"S2"}],
  DEN:[{n:"Nikola Jokic",r:"PM"},{n:"Jamal Murray",r:"S1"},{n:"Nikola Jokic",r:"DR"}],
  DET:[{n:"Cade Cunningham",r:"PM"},{n:"Duncan Robinson",r:"S1"},{n:"Tobias Harris",r:"S2"}],
  GSW:[{n:"Draymond Green",r:"PM"},{n:"Stephen Curry",r:"S1"},{n:"Kristaps Porzingis",r:"B"},{n:"Draymond Green",r:"DR"}],
  HOU:[{n:"Fred VanVleet",r:"PM"},{n:"Kevin Durant",r:"S1"},{n:"Reed Sheppard",r:"S2"},{n:"Kevin Durant",r:"DR"}],
  IND:[{n:"Tyrese Haliburton",r:"PM"},{n:"Bennedict Mathurin",r:"S1"},{n:"Pascal Siakam",r:"DR"}],
  LAC:[{n:"Darius Garland",r:"PM"},{n:"Bogdan Bogdanovic",r:"S1"},{n:"Kawhi Leonard",r:"DR"}],
  LAL:[{n:"LeBron James",r:"PM"},{n:"Austin Reaves",r:"S1"},{n:"Luka Doncic",r:"S2"},{n:"LeBron James",r:"DR"},{n:"Anthony Davis",r:"B"}],
  MEM:[{n:"Ja Morant",r:"PM"},{n:"Marcus Smart",r:"S2"},{n:"Ja Morant",r:"DR"}],
  MIA:[{n:"Terry Rozier",r:"PM"},{n:"Tyler Herro",r:"S1"},{n:"Norman Powell",r:"S2"},{n:"Jimmy Butler",r:"DR"},{n:"Bam Adebayo",r:"B"}],
  MIL:[{n:"Damian Lillard",r:"PM"},{n:"A.J. Green",r:"S1"},{n:"Giannis Antetokounmpo",r:"DR"},{n:"Brook Lopez",r:"B"}],
  MIN:[{n:"Anthony Edwards",r:"PM"},{n:"Donte DiVincenzo",r:"S1"},{n:"Anthony Edwards",r:"DR"},{n:"Rudy Gobert",r:"B"}],
  NOP:[{n:"Trey Murphy III",r:"S1"},{n:"Herb Jones",r:"S2"},{n:"Zion Williamson",r:"DR"}],
  NYK:[{n:"Jalen Brunson",r:"PM"},{n:"Mikal Bridges",r:"S1"},{n:"Josh Hart",r:"S2"},{n:"Julius Randle",r:"DR"},{n:"Karl-Anthony Towns",r:"B"}],
  OKC:[{n:"Shai Gilgeous-Alexander",r:"PM"},{n:"Jalen Williams",r:"S1"},{n:"Luguentz Dort",r:"S2"},{n:"Shai Gilgeous-Alexander",r:"DR"},{n:"Chet Holmgren",r:"B"}],
  ORL:[{n:"Jalen Suggs",r:"PM"},{n:"Desmond Bane",r:"S1"},{n:"Franz Wagner",r:"S2"},{n:"Paolo Banchero",r:"DR"}],
  PHI:[{n:"Tyrese Maxey",r:"PM"},{n:"Paul George",r:"S1"},{n:"Joel Embiid",r:"DR"},{n:"Joel Embiid",r:"B"}],
  PHX:[{n:"Devin Booker",r:"PM"},{n:"Jalen Green",r:"S1"},{n:"Dillon Brooks",r:"S2"},{n:"Devin Booker",r:"DR"}],
  POR:[{n:"Shaedon Sharpe",r:"PM"},{n:"Deni Avdija",r:"S1"},{n:"Jerami Grant",r:"DR"}],
  SAC:[{n:"Malik Monk",r:"PM"},{n:"Zach LaVine",r:"S1"},{n:"Malik Monk",r:"S2"},{n:"Domantas Sabonis",r:"DR"}],
  SAS:[{n:"Tre Jones",r:"PM"},{n:"De'Aaron Fox",r:"S1"},{n:"Victor Wembanyama",r:"DR"},{n:"Victor Wembanyama",r:"B"}],
  TOR:[{n:"Immanuel Quickley",r:"PM"},{n:"Gradey Dick",r:"S1"},{n:"RJ Barrett",r:"S2"},{n:"Scottie Barnes",r:"DR"},{n:"Brandon Ingram",r:"S1"}],
  UTA:[{n:"Keyonte George",r:"PM"},{n:"Lauri Markkanen",r:"S1"},{n:"Lauri Markkanen",r:"DR"}],
  WAS:[{n:"Trae Young",r:"PM"},{n:"Jordan Poole",r:"S1"},{n:"Kyle Kuzma",r:"DR"}]
};

// ═══════ TEAMMATE EFFECT ENGINE ═══════
// Takes a player, their team, and the injury list → returns λ multiplier + explanation
// Uses 6 archetypes from the teammate effects research with calibrated multipliers

// Player shooting type classifications from research
// CS=catch-and-shoot (most affected), HY=hybrid, SC=self-creating (least affected)
var PLAYER_TYPES={
  // Catch-and-shoot: pure off-ball, rely on teammates for looks
  "duncan robinson":"CS","a.j. green":"CS","klay thompson":"CS","derrick white":"CS",
  "payton pritchard":"CS","bobby portis":"CS","kon knueppel":"CS","norman powell":"CS",
  "donte divincenzo":"CS","reed sheppard":"CS","buddy hield":"CS","max strus":"CS",
  "josh hart":"CS","bogdan bogdanovic":"CS","gradey dick":"CS",
  "grayson allen":"CS","landry shamet":"CS","dorian finney-smith":"CS","royce o'neale":"CS",
  "quentin grimes":"CS","isaac okoro":"CS","sam merrill":"CS","moe wagner":"CS",
  "herb jones":"CS","tari eason":"CS","jalen smith":"CS",
  // Self-creating: generate own shots off the dribble
  "stephen curry":"SC","james harden":"SC","luka doncic":"SC","shai gilgeous-alexander":"SC",
  "trae young":"SC","damian lillard":"SC","kyrie irving":"SC","devin booker":"SC",
  "cade cunningham":"SC","jordan poole":"SC","de'aaron fox":"SC","lamelo ball":"SC",
  "jalen green":"SC","caris levert":"SC",
  // Hybrid: mix of both
  "donovan mitchell":"HY","anthony edwards":"HY","tyrese maxey":"HY","michael porter jr.":"HY",
  "jamal murray":"HY","jalen brunson":"HY","jayson tatum":"HY","jaylen brown":"HY",
  "anfernee simons":"HY","tyler herro":"HY","coby white":"HY","kevin durant":"HY",
  "paul george":"HY","franz wagner":"HY","jalen williams":"HY","tyrese haliburton":"HY",
  "cam thomas":"HY","cj mccollum":"HY","mikal bridges":"HY","rj barrett":"HY",
  "fred vanvleet":"HY","darius garland":"HY","austin reaves":"HY","zach lavine":"HY",
  "malik monk":"HY","terry rozier":"HY","victor wembanyama":"HY","collin sexton":"HY",
  "og anunoby":"HY","kelly oubre jr.":"HY","patrick williams":"HY","matas buzelis":"HY",
  "tristan da silva":"HY","anthony black":"HY","dillon brooks":"HY","josh giddey":"HY",
  "amen thompson":"HY","alperen sengun":"HY"
};

function calcTeammateAdj(pl, teamAbbr, injuredOut) {
  if (!injuredOut || injuredOut.length === 0) return { mult: 1.0, effects: [] };
  var roles = ROLES[teamAbbr];
  if (!roles) return { mult: 1.0, effects: [] };

  // Determine player type: CS=catch-and-shoot, HY=hybrid, SC=self-creating
  var pType = PLAYER_TYPES[pl.n.toLowerCase()] || "HY"; // default hybrid if not classified

  // Classify injured players by role
  var pmOut = false, s1Out = false, s2Out = false, driverOut = false, bigOut = false;
  var pmName = "", driverName = ""; // track names to avoid double-counting same player
  var effects = [];

  injuredOut.forEach(function(injName) {
    var injLower = injName.toLowerCase();
    // Don't apply effects if the injured player IS the modeled player
    if (injLower === pl.n.toLowerCase()) return;

    roles.forEach(function(role) {
      var roleName = role.n.toLowerCase();
      // Match: exact full name, or last name match (but only if last name is 4+ chars to avoid false positives)
      var lastRole = roleName.split(" ").pop();
      var isMatch = (roleName === injLower) || (lastRole.length >= 4 && injLower.indexOf(lastRole) >= 0 && injLower.indexOf(lastRole.charAt(0)) >= 0);
      if (isMatch) {
        if (role.r === "PM" && !pmOut) { pmOut = true; pmName = roleName; }
        if (role.r === "S1" && !s1Out) s1Out = true;
        if (role.r === "S2" && !s2Out) s2Out = true;
        if (role.r === "DR" && !driverOut) { driverOut = true; driverName = roleName; }
        if (role.r === "B" && !bigOut) bigOut = true;
      }
    });
  });

  var mult = 1.0;

  // Archetype 1: Primary playmaker out — worst for CS guys
  if (pmOut) {
    var m = pType === "CS" ? 0.85 : pType === "HY" ? 0.90 : 0.935;
    mult *= m;
    effects.push({ l: "PM OUT", v: m, c: "neg" });
  }

  // Archetype 2 & 3: Lead shooter(s) out
  if (s1Out && s2Out) {
    // Both top shooters out — compounds non-linearly (Archetype 3)
    var m = pType === "CS" ? 0.815 : pType === "HY" ? 0.87 : 0.875;
    mult *= m;
    effects.push({ l: "S1+S2 OUT", v: m, c: "neg" });
  } else if (s1Out) {
    // Just #1 shooter out (Archetype 2)
    var m = pType === "CS" ? 0.905 : pType === "HY" ? 0.93 : 0.945;
    mult *= m;
    effects.push({ l: "S1 OUT", v: m, c: "neg" });
  } else if (s2Out) {
    // #2 shooter out — smaller effect
    var m = pType === "CS" ? 0.94 : pType === "HY" ? 0.96 : 0.97;
    mult *= m;
    effects.push({ l: "S2 OUT", v: m, c: "neg" });
  }

  // Archetype 6: Star driver/paint attacker out — defense stays home on shooters
  // Only skip if the SAME player triggered both PM and DR (e.g. LeBron fills both)
  if (driverOut && !(pmOut && driverName === pmName)) {
    var m = pType === "CS" ? 0.885 : pType === "HY" ? 0.92 : 0.955;
    mult *= m;
    effects.push({ l: "DRIVER OUT", v: m, c: "neg" });
  }

  // Archetype 4: Non-shooting big out — slight BOOST (better spacing likely)
  if (bigOut) {
    var m = pType === "CS" ? 1.05 : pType === "HY" ? 1.03 : 1.02;
    mult *= m;
    effects.push({ l: "BIG OUT", v: m, c: "pos" });
  }

  // Cap the total adjustment to avoid extreme values
  mult = Math.max(0.70, Math.min(1.20, mult));

  return { mult: mult, effects: effects };
}

// Helper: extract "OUT" player names from injury data for a specific team
function getTeamOuts(injuries, teamAbbr) {
  var outs = [];
  if (!injuries || injuries.length === 0) return outs;
  var teamName = T[teamAbbr] ? T[teamAbbr].n.toLowerCase() : "";

  injuries.forEach(function(inj) {
    var status = (inj.status || inj.Status || inj.current_status || "").toLowerCase();
    if (status !== "out" && status !== "doubtful") return; // only definite absences
    var team = (inj.team || inj.Team || "").toLowerCase();
    // Match by team name or abbreviation
    if (team.indexOf(teamName) >= 0 || team.indexOf(teamAbbr.toLowerCase()) >= 0 || teamName.indexOf(team) >= 0) {
      var name = inj.player || inj.name || inj.Player || "";
      if (name) outs.push(name);
    }
  });
  return outs;
}

// ═══════ v8 CORE ENGINE ═══════
function runV8(pl,ctx){
  var od=parseFloat(document.getElementById("odSlider").value)||1.35;
  var rw=parseFloat(document.getElementById("rwSlider").value)||0.3;
  var useMed=document.getElementById("medSlider").value==="1";
  var bP=((1-rw)*pl.p+rw*(pl.rp||pl.p))/100;
  var bA=(1-rw)*pl.a+rw*(pl.ra||pl.a);
  if(!pl.m||pl.m<=0)return{lam:0,rawLam:0,pace:1,oppD:1,projMins:0,blowoutProb:0,adjustments:[{l:"NO MINS",v:0,c:"neg"}],tpm:0,tmAdj:1};
  var tpm=bA*bP/pl.m;
  var pm=pl.m;
  var adj=[];
  var opp=ctx.opp;
  var oppD=1+((T[opp].d-LD)*0.006);
  var pace=((T[pl.t].pa+T[opp].pa)/2)/LP;
  var hA=1.0;
  if(ctx.isHome===true){hA=1+(pl.ha||.008);adj.push({l:"HOME",v:hA,c:"pos"});}
  else if(ctx.isHome===false){hA=1-(pl.ha||.008)*0.6;adj.push({l:"AWAY",v:hA,c:"neg"});}
  var b2b=1.0;
  if(ctx.isB2B){b2b=0.97;pm-=2;adj.push({l:"B2B",v:0.97,c:"neg"});}
  var env=1.0;
  if(ctx.total){env=gtMult(ctx.total);if(Math.abs(env-1)>=.005)adj.push({l:"TOTAL "+ctx.total,v:env,c:env>=1?"pos":"neg"});}
  var bAdj=1.0,bPr=0;
  if(ctx.spread!=null){var as=Math.abs(ctx.spread);bPr=blowProb(as);if(bPr>.10){var bf=blowMinFrac(pm);var em=(1-bPr)*pm+bPr*(pm*bf);bAdj=em/pm;pm=em;if(as>=6)adj.push({l:"SPREAD "+as.toFixed(1),v:bAdj,c:"neg"});}}
  var fA=1.0;
  if(pl.pf36>=3.0){fA=0.97;adj.push({l:"FOUL RISK",v:0.97,c:"neg"});}
  else if(pl.pf36>=2.7){fA=0.985;}
  // ── TEAMMATE EFFECTS (new in v8.3) ──
  var tmAdj=1.0;
  if(ctx.injuries){
    var teamOuts=getTeamOuts(ctx.injuries, pl.t);
    if(teamOuts.length>0){
      var te=calcTeammateAdj(pl, pl.t, teamOuts);
      tmAdj=te.mult;
      te.effects.forEach(function(e){adj.push(e);});
    }
  }
  var raw=tpm*pm*pace*oppD*hA*b2b*env*fA*tmAdj;
  var lam=raw;
  if(useMed&&od>1.05){lam=medianCorr(raw,od);if(Math.abs(lam-raw)>.02)adj.push({l:"MEDIAN",v:lam/raw,c:"neg"});}
  return{lam:lam,rawLam:raw,pace:pace,oppD:oppD,projMins:pm,blowoutProb:bPr,adjustments:adj,tpm:tpm,tmAdj:tmAdj};
}

// ═══════ UI ═══════
var logLines=[];
function addLog(s){logLines.push(s);var el=document.getElementById("logContent");el.textContent=logLines.join("\n");el.scrollTop=el.scrollHeight;document.getElementById("logArea").className="";}
function showMsg(id,msg,type){var el=document.getElementById(id);el.textContent=msg;el.className="msg msg-"+(type||"info");}
function hideEl(id){document.getElementById(id).className="hide";}
function showTab(t){
  ["scan","manual","players","setup"].forEach(function(x){
    document.getElementById("panel"+x.charAt(0).toUpperCase()+x.slice(1)).className=(x===t)?"":"hide";
    document.getElementById("tab"+x.charAt(0).toUpperCase()+x.slice(1)).className=(x===t)?"tab active":"tab";
  });
  if(t==="players")renderPlayerList();
}
function saveKey(){var k=document.getElementById("keyInput").value.trim();if(k){localStorage.setItem("odds_api_key",k);showMsg("scanMsg","Key saved!","ok");}}
function getKey(){return document.getElementById("keyInput").value.trim()||localStorage.getItem("odds_api_key")||"";}
try{var sk=localStorage.getItem("odds_api_key");if(sk)document.getElementById("keyInput").value=sk;}catch(e){}

function proxyUrl(u){return"https://corsproxy.io/?"+encodeURIComponent(u);}
async function safeFetch(url){
  try{addLog("  Trying direct...");var r=await fetch(url);if(r.ok){addLog("  ✓ Direct OK");return r;}}catch(e){addLog("  Direct failed, trying proxy...");}
  try{var r2=await fetch(proxyUrl(url));if(r2.ok){addLog("  ✓ Proxy OK");return r2;}addLog("  Proxy returned "+r2.status);}catch(e){addLog("  Proxy failed: "+e.message);}
  throw new Error("Could not connect.");
}

// ═══════ SCAN ═══════
async function doScan(){
  var apiKey=getKey();
  if(!apiKey){showMsg("scanMsg","You need an API key! See ⚙ Setup tab.","err");return;}
  
  // Rule #1 enforcement: check for verified players
  var verifiedCount=P.filter(function(p){return p.v;}).length;
  if(verifiedCount===0){
    showMsg("scanMsg","⛔ No API-verified player data. You must run 📡 Refresh All Stats before scanning. Rule #1: No estimates, ever.","err");
    return;
  }
  
  document.getElementById("scanBtn").disabled=true;
  document.getElementById("scanBtn").textContent="⏳ Scanning...";
  document.getElementById("board").innerHTML="";hideEl("scanSummary");logLines=[];

  try{
    addLog("Fetching NBA events + spreads + totals...");
    var evUrl="https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey="+apiKey+"&regions=us&markets=spreads,totals&oddsFormat=american";
    var evRes=await safeFetch(evUrl);var evText=await evRes.text();addLog("Response: "+evText.length+" chars");
    var events;
    try{events=JSON.parse(evText);}catch(e){showMsg("scanMsg","Invalid API response. Check your key.","err");return;}
    if(events.message){showMsg("scanMsg","API error: "+events.message,"err");return;}

    var now=Date.now();
    var upcoming=events.filter(function(e){var t=new Date(e.commence_time).getTime();return t>now-7200000&&t<now+86400000;});
    addLog("Found "+upcoming.length+" games in next 24h");
    if(upcoming.length===0){showMsg("scanSummary","No NBA games found. Try again on a game day!","info");return;}

    var gameCtx={};
    upcoming.forEach(function(ev){
      var ctx={home:ev.home_team,away:ev.away_team,spread:null,total:null};
      (ev.bookmakers||[]).forEach(function(bk){(bk.markets||[]).forEach(function(mkt){
        if(mkt.key==="spreads"&&ctx.spread==null)(mkt.outcomes||[]).forEach(function(o){if(o.name===ev.home_team&&o.point!=null)ctx.spread=o.point;});
        if(mkt.key==="totals"&&ctx.total==null)(mkt.outcomes||[]).forEach(function(o){if(o.name==="Over"&&o.point!=null)ctx.total=o.point;});
      });});
      gameCtx[ev.id]=ctx;
      addLog("  🏀 "+ev.away_team+" @ "+ev.home_team+" — "+(ctx.spread!=null?"spread "+(ctx.spread>0?"+":"")+ctx.spread:"no spread")+", "+(ctx.total!=null?"total "+ctx.total:"no total"));
    });

    addLog("\nFetching injury report...");
    var injuries=[];
    try{var injRes=await safeFetch("https://api.fantasynerds.com/v1/nba/injuries?apikey=TEST");var injText=await injRes.text();
      try{var injData=JSON.parse(injText);if(Array.isArray(injData))injuries=injData;else if(injData&&injData.injuries)injuries=injData.injuries;
      else if(injData&&typeof injData==="object"){for(var tKey in injData){if(Array.isArray(injData[tKey]))injuries=injuries.concat(injData[tKey]);}}
      addLog("  → "+injuries.length+" injury entries");}catch(pe){addLog("  Could not parse injuries");}
    }catch(ie){addLog("  Injury API unavailable");}
    renderInjuries(injuries);

    var allProps=[];
    for(var gi=0;gi<upcoming.length;gi++){
      var ev=upcoming[gi];addLog("\nFetching 3PT props: "+ev.away_team+" @ "+ev.home_team+"...");
      try{var pUrl="https://api.the-odds-api.com/v4/sports/basketball_nba/events/"+ev.id+"/odds?apiKey="+apiKey+"&regions=us&markets=player_threes,player_threes_alternate&oddsFormat=american";
        var pRes=await safeFetch(pUrl);var pData=JSON.parse(await pRes.text());
        var bks=pData.bookmakers||[];var home=pData.home_team||"";var away=pData.away_team||"";var gp=[];
        bks.forEach(function(bk){(bk.markets||[]).forEach(function(mkt){if(mkt.key!=="player_threes"&&mkt.key!=="player_threes_alternate")return;var byPL={};
          (mkt.outcomes||[]).forEach(function(o){
            // Main market: name=player, description=Over/Under
            // Alt market: name=Over/Under, description=player
            var pName,side;
            if(o.name==="Over"||o.name==="Under"){pName=o.description;side=o.name;}
            else{pName=o.name;side=o.description;}
            if(!pName||!side)return;
            var key=pName+"||"+o.point;
            if(!byPL[key])byPL[key]={player:pName,line:o.point,home:home,away:away,book:bk.title||bk.key,eventId:ev.id,mkt:mkt.key==="player_threes_alternate"?"alt":"main"};
            if(side==="Over")byPL[key].over=""+o.price;if(side==="Under")byPL[key].under=""+o.price;});
          for(var pn in byPL)gp.push(byPL[pn]);});});
        var bn={};gp.forEach(function(p){bn[p.book]=true;});
        var nMain=gp.filter(function(p){return p.mkt==="main"}).length;
        var nAlt=gp.filter(function(p){return p.mkt==="alt"}).length;
        addLog("  → "+gp.length+" lines ("+nMain+" main, "+nAlt+" alt) from "+Object.keys(bn).length+" books");
        if(gp.length>0){var pn2={};gp.forEach(function(p){pn2[p.player]=true;});addLog("  → "+Object.keys(pn2).join(", "));}
        allProps=allProps.concat(gp);
      }catch(e){addLog("  ⚠ "+e.message);}
    }

    addLog("\nTotal: "+allProps.length+" prop lines");
    var od=parseFloat(document.getElementById("odSlider").value)||1.35;
    var board=[],matched=0,unmatched=0,unmatchedNames={};

    allProps.forEach(function(prop){
      var pl=matchPlayer(prop.player);
      if(!pl){unmatched++;unmatchedNames[prop.player]=true;return;}
      // Rule #1: NEVER use unverified data
      if(!pl.v){unmatched++;unmatchedNames[prop.player+" (not API-verified — run Refresh first)"]=true;return;}
      var homeK=matchTeam(prop.home),awayK=matchTeam(prop.away);
      // Verify player's team matches one of the event teams
      if(pl.t!==homeK&&pl.t!==awayK){unmatched++;unmatchedNames[prop.player+" (team mismatch: "+pl.t+" not in "+homeK+"/"+awayK+")"]=true;return;}
      matched++;
      var opp=(pl.t===homeK)?awayK:homeK;
      if(!opp||!T[opp])return;
      var gCtx=gameCtx[prop.eventId]||{};var isHome=(pl.t===homeK);
      var teamSpread=gCtx.spread!=null?(isHome?gCtx.spread:-gCtx.spread):null;
      var ctx={opp:opp,spread:teamSpread,total:gCtx.total||null,isHome:isHome,isB2B:false,injuries:injuries};
      var md=runV8(pl,ctx);var probs=calcProbs(md.lam,od);
      var op=overProb(probs,prop.line);
      // For whole-number lines, exclude push probability from under
      var pushP=(prop.line%1===0&&prop.line>=0&&prop.line<=14)?probs[prop.line]:0;
      var up=1-op-pushP;
      var bO=parseAm(prop.over),bU=parseAm(prop.under);
      var oE=bO?(op-bO)*100:null,uE=bU?(up-bU)*100:null;
      var hold=0;if(bO&&bU)hold=((bO+bU)-1)*100;
      var hps=hold/2;var oEa=oE!=null?oE-hps:null,uEa=uE!=null?uE-hps:null;
      var bestE=Math.max(oE||-999,uE||-999),bestEa=Math.max(oEa||-999,uEa||-999);
      var best=(oE||-999)>=(uE||-999)?"OVER":"UNDER";
      var div=Math.abs(prop.line-md.lam),divR=md.lam>0?prop.line/md.lam:99;
      var sus=(divR>1.6||divR<0.55)&&div>1.0;
      // If teammate effects already explain part of the gap, raise CAUTION threshold
      if(md.tmAdj&&md.tmAdj<0.95){sus=(divR>1.8||divR<0.45)&&div>1.2;}
      var warn="";
      if(sus&&prop.line>md.lam)warn="ROLE BOOST? Book expects way more — possible expanded role or model missing context";
      else if(sus)warn="ROLE DROP? Book expects way less — possible minutes limit or model missing context";
      // If teammate adj is active, note it
      if(md.tmAdj&&md.tmAdj<0.95&&!sus)warn="";
      var sig;if(sus)sig="CAUTION";else sig=bestEa>=5?"STRONG":bestEa>=3?"MOD":bestEa>=1?"LEAN":"NONE";
      board.push({name:pl.n,team:pl.t,opp:opp,book:prop.book,line:prop.line,over:prop.over,under:prop.under,
        lam:md.lam,rawLam:md.rawLam,modelO:op,modelU:up,oEdge:oE,uEdge:uE,oEadj:oEa,uEadj:uEa,
        bestE:bestE,bestEadj:bestEa,best:best,sig:sig,suspicious:sus,warning:warn,divergence:div.toFixed(1),
        adjustments:md.adjustments,projMins:md.projMins,blowoutProb:md.blowoutProb,hold:hold,
        isHome:isHome,total:gCtx.total,spread:teamSpread,mkt:prop.mkt||"main"});
    });

    // ── Consolidate: group by player+line, collect all books ──
    var grouped={};
    board.forEach(function(e){
      var gk=e.name+"||"+e.line;
      if(!grouped[gk]){
        grouped[gk]={name:e.name,team:e.team,opp:e.opp,line:e.line,
          lam:e.lam,rawLam:e.rawLam,modelO:e.modelO,modelU:e.modelU,
          sig:e.sig,suspicious:e.suspicious,warning:e.warning,divergence:e.divergence,
          adjustments:e.adjustments,projMins:e.projMins,blowoutProb:e.blowoutProb,
          isHome:e.isHome,total:e.total,spread:e.spread,
          bestEadj:e.bestEadj,bestE:e.bestE,best:e.best,
          books:[]};
      }
      var g=grouped[gk];
      g.books.push({book:e.book,over:e.over,under:e.under,oEdge:e.oEdge,uEdge:e.uEdge,
        oEadj:e.oEadj,uEadj:e.uEadj,hold:e.hold,bestEadj:e.bestEadj,mkt:e.mkt});
      // Update group-level best edge
      if(e.bestEadj>g.bestEadj){g.bestEadj=e.bestEadj;g.bestE=e.bestE;g.best=e.best;g.sig=e.sig;}
    });
    var cBoard=[];for(var gk in grouped){
      var g=grouped[gk];
      // Sort books: best edge first
      g.books.sort(function(a,b){return b.bestEadj-a.bestEadj;});
      cBoard.push(g);
    }
    cBoard.sort(function(a,b){if(a.suspicious&&!b.suspicious)return 1;if(!a.suspicious&&b.suspicious)return-1;return b.bestEadj-a.bestEadj;});

    addLog("\nMatched "+matched+" to model, "+unmatched+" unrecognized");
    addLog("Consolidated into "+cBoard.length+" unique player+line cards");
    var uNames=Object.keys(unmatchedNames);
    if(uNames.length>0)addLog("Unrecognized: "+uNames.slice(0,15).join(", ")+(uNames.length>15?" + "+(uNames.length-15)+" more":""));
    var nS=cBoard.filter(function(e){return e.sig==="STRONG"}).length;
    var nM=cBoard.filter(function(e){return e.sig==="MOD"}).length;
    var nL=cBoard.filter(function(e){return e.sig==="LEAN"}).length;
    var nC=cBoard.filter(function(e){return e.sig==="CAUTION"}).length;

    if(allProps.length===0)showMsg("scanSummary","No prop lines found. Props post 2-6h before tip.","info");
    else if(matched===0)showMsg("scanSummary","Found "+allProps.length+" props but none matched our "+P.length+"-player database. Unmatched: "+uNames.slice(0,5).join(", "),"info");
    else showMsg("scanSummary","✅ "+cBoard.length+" results · "+nS+" STRONG · "+nM+" MOD · "+nL+" LEAN"+(nC>0?" · "+nC+" ⚠":"")+(unmatched>0?" · "+unmatched+" unmatched":""),"ok");

    renderBoard(cBoard);
  }catch(e){
    var msg=e.message;if(msg.indexOf("connect")>=0||msg.indexOf("fetch")>=0)msg="Couldn't connect. Check your internet.";
    showMsg("scanMsg",msg,"err");addLog("ERROR: "+e.message);
  }finally{document.getElementById("scanBtn").disabled=false;document.getElementById("scanBtn").textContent="🚀 Scan All 3PT Props";}
}

// ═══════ RENDER ═══════
function renderBoard(board){
  var c=document.getElementById("board");c.innerHTML="";
  board.forEach(function(e){
    var card=document.createElement("div");
    card.className="card "+(e.sig==="CAUTION"?"caution":e.bestEadj>=3?"strong":e.bestEadj>=1?"mod":"");
    var bc=e.sig==="STRONG"?"badge-strong":e.sig==="MOD"?"badge-mod":e.sig==="LEAN"?"badge-lean":e.sig==="CAUTION"?"badge-caution":"badge-none";
    var on=T[e.opp]?T[e.opp].n:e.opp;
    // Context bar
    var ctx='<div class="ctx-bar">';
    if(e.isHome!=null)ctx+='<span class="ctx-chip">'+(e.isHome?'🏠 HOME':'✈ AWAY')+'</span>';
    if(e.spread!=null)ctx+='<span class="ctx-chip">📊 '+(e.spread>0?'+':'')+e.spread.toFixed(1)+'</span>';
    if(e.total!=null)ctx+='<span class="ctx-chip">🎯 O/U '+e.total+'</span>';
    if(e.projMins)ctx+='<span class="ctx-chip">⏱ '+e.projMins.toFixed(0)+'min</span>';
    if(e.blowoutProb>.15)ctx+='<span class="ctx-chip" style="color:#ef4444;border-color:#ef444433">💨 '+Math.round(e.blowoutProb*100)+'%</span>';
    ctx+='</div>';
    // Adjustment pills
    var adjH='';if(e.adjustments&&e.adjustments.length>0){adjH='<div class="adj-row">';e.adjustments.forEach(function(a){var pct=((a.v-1)*100).toFixed(1);adjH+='<span class="adj-pill '+a.c+'">'+a.l+' '+(a.v>=1?'+':'')+pct+'%</span>';});adjH+='</div>';}
    // Warning
    var warnH=e.warning?'<div style="padding:8px 10px;background:#ef444412;border:1px solid #ef444433;border-radius:6px;margin-bottom:8px;font-size:11px;color:#ef4444;line-height:1.5">⚠ '+e.warning+'</div>':'';
    // Book odds table
    var booksH='<div style="margin-top:6px">';
    booksH+='<div style="display:grid;grid-template-columns:1fr 90px 90px;gap:0;font-size:9px;color:#484f58;padding:0 4px;margin-bottom:2px"><span>BOOK</span><span style="text-align:center">OVER</span><span style="text-align:center">UNDER</span></div>';
    e.books.forEach(function(bk,i){
      var oEc=bk.oEadj!=null?(bk.oEadj>2?"#10b981":bk.oEadj>0?"#f59e0b":"#ef4444"):"#484f58";
      var uEc=bk.uEadj!=null?(bk.uEadj>2?"#10b981":bk.uEadj>0?"#f59e0b":"#ef4444"):"#484f58";
      var oEs=bk.oEdge!=null?(bk.oEdge>0?"+":"")+bk.oEdge.toFixed(1)+"%":"";
      var uEs=bk.uEdge!=null?(bk.uEdge>0?"+":"")+bk.uEdge.toFixed(1)+"%":"";
      var bg=i===0?"rgba(16,185,129,0.06)":"transparent";
      var altTag=bk.mkt==="alt"?' <span style="font-size:7px;padding:0 3px;border-radius:2px;background:#8b5cf620;color:#8b5cf6;font-weight:700">ALT</span>':'';
      booksH+='<div style="display:grid;grid-template-columns:1fr 90px 90px;gap:0;padding:4px;border-radius:4px;background:'+bg+';align-items:center">';
      booksH+='<span style="font-size:11px;color:#c9d1d9;font-weight:'+(i===0?'700':'400')+'">'+bk.book+altTag+'</span>';
      booksH+='<span style="text-align:center">'+(bk.over?'<span style="font-size:13px;font-weight:700;color:'+(i===0&&bk.oEadj>0?'#10b981':'#c9d1d9')+'">'+bk.over+'</span> <span style="font-size:10px;color:'+oEc+'">'+oEs+'</span>':'<span style="color:#484f58">—</span>')+'</span>';
      booksH+='<span style="text-align:center">'+(bk.under?'<span style="font-size:13px;font-weight:700;color:'+(i===0&&bk.uEadj>0?'#10b981':'#c9d1d9')+'">'+bk.under+'</span> <span style="font-size:10px;color:'+uEc+'">'+uEs+'</span>':'<span style="color:#484f58">—</span>')+'</span>';
      booksH+='</div>';
    });
    booksH+='<div style="font-size:9px;color:#484f58;margin-top:4px;text-align:center">fair: over '+toAm(e.modelO)+' / under '+toAm(e.modelU)+'</div>';
    booksH+='</div>';

    card.innerHTML=
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">'+
      '<div><div style="font-size:14px;font-weight:700">'+e.name+' <span style="font-size:18px;font-weight:800;color:#f59e0b;margin-left:6px">'+e.line+'</span></div>'+
      '<div style="font-size:10px;color:#8b949e">'+e.team+' vs '+on+'</div></div>'+
      '<div style="text-align:right"><span class="badge '+bc+'">'+e.sig+'</span>'+
      '<div style="font-size:10px;color:#484f58;margin-top:2px">λ '+e.lam.toFixed(2)+
      (e.rawLam&&Math.abs(e.rawLam-e.lam)>.02?' <span style="font-size:9px">(raw '+e.rawLam.toFixed(2)+')</span>':'')+
      (e.suspicious?' · gap '+e.divergence:'')+'</div></div></div>'+
      ctx+warnH+booksH+adjH;
    c.appendChild(card);
  });
}

function renderInjuries(injuries){
  var panel=document.getElementById("injuryPanel");
  if(!injuries||injuries.length===0){panel.className="hide";return;}
  var rel=injuries.filter(function(inj){var s=(inj.status||inj.Status||inj.current_status||"").toLowerCase();return s==="out"||s==="doubtful"||s==="questionable"||s==="gtd"||s==="day-to-day";});
  if(rel.length===0){panel.className="hide";return;}
  var html='<div class="box" style="border-color:#ef444433"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px"><span style="font-size:12px;font-weight:700;color:#ef4444">🏥 INJURY REPORT</span><span style="font-size:10px;color:#484f58">'+rel.length+' players</span></div>';
  var by={out:[],doubtful:[],questionable:[]};
  rel.forEach(function(inj){var n=inj.player||inj.name||inj.Player||"Unknown",t=inj.team||inj.Team||"",s=(inj.status||inj.Status||inj.current_status||"").toLowerCase(),r=inj.injury||inj.reason||"";
    var e={name:n,team:t,reason:r};if(s==="out")by.out.push(e);else if(s==="doubtful")by.doubtful.push(e);else by.questionable.push(e);});
  function rg(l,c,items){if(!items.length)return"";var h='<div style="margin-bottom:8px"><span style="font-size:10px;font-weight:700;color:'+c+'">'+l+' ('+items.length+')</span>';
    items.slice(0,15).forEach(function(p){h+='<div style="font-size:11px;color:#8b949e;padding:2px 0">'+p.name+(p.team?' <span style="color:#484f58">('+p.team+')</span>':"")+(p.reason?' — <span style="color:#484f58">'+p.reason+'</span>':"")+'</div>';});
    return h+'</div>';}
  html+=rg("OUT","#ef4444",by.out)+rg("DOUBTFUL","#f97316",by.doubtful)+rg("QUESTIONABLE","#f59e0b",by.questionable)+'</div>';
  panel.innerHTML=html;panel.className="";
}

// ═══════ MANUAL ═══════
function parseManual(){
  var text=document.getElementById("manualInput").value.trim();if(!text)return;
  var lines=text.split("\n"),od=parseFloat(document.getElementById("odSlider").value)||1.35,board=[];
  lines.forEach(function(raw){
    var tokens=raw.trim().split(/\s+/);var lineIdx=-1,propLine=null;
    for(var i=0;i<tokens.length;i++){var v=parseFloat(tokens[i]);if(!isNaN(v)&&v>=0.5&&v<=12&&!/^[+-]\d/.test(tokens[i])){lineIdx=i;propLine=v;break;}}
    if(propLine===null)return;
    var playerName=tokens.slice(0,lineIdx).join(" ");var pl=matchPlayer(playerName);if(!pl)return;
    var oddsParts=tokens.slice(lineIdx+1);var over=null,under=null;
    oddsParts.forEach(function(t){var c=t.replace(/[()]/g,"");if(/^[+-]?\d{2,4}$/.test(c)){if(!over)over=c;else if(!under)under=c;}});
    var ctx={opp:"OKC",spread:null,total:null,isHome:null,isB2B:false};
    var md=runV8(pl,ctx);var probs=calcProbs(md.lam,od);
    var op=overProb(probs,propLine);
    var pushP=(propLine%1===0&&propLine>=0&&propLine<=14)?probs[propLine]:0;
    var up=1-op-pushP;
    var bO=parseAm(over),bU=parseAm(under);
    var oE=bO?(op-bO)*100:null,uE=bU?(up-bU)*100:null;
    var hold=(bO&&bU)?((bO+bU)-1)*100:0;var hps=hold/2;
    var oEa=oE!=null?oE-hps:null,uEa=uE!=null?uE-hps:null;
    var bestE=Math.max(oE||-999,uE||-999),bestEa=Math.max(oEa||-999,uEa||-999);
    board.push({name:pl.n,team:pl.t,opp:"OKC",book:"Manual",line:propLine,over:over,under:under,
      lam:md.lam,rawLam:md.rawLam,modelO:op,modelU:up,oEdge:oE,uEdge:uE,oEadj:oEa,uEadj:uEa,
      bestE:bestE,bestEadj:bestEa,best:(oE||-999)>=(uE||-999)?"OVER":"UNDER",
      sig:bestEa>=5?"STRONG":bestEa>=3?"MOD":bestEa>=1?"LEAN":"NONE",
      suspicious:false,warning:"",divergence:"0",adjustments:md.adjustments,projMins:md.projMins,
      blowoutProb:0,hold:hold,isHome:null,total:null,spread:null});
  });
  board.sort(function(a,b){return b.bestEadj-a.bestEadj;});
  showTab("scan");
  showMsg("scanSummary","Parsed "+board.length+" lines (manual — no spread/total context)","ok");
  renderBoard(board);
}

// ═══════ BALLDONTLIE API ═══════
function saveBDL(){var k=document.getElementById("bdlKey").value.trim();if(k){try{localStorage.setItem("bdl_key",k)}catch(e){}showMsg("scanMsg","Balldontlie key saved!","ok");}}
function getBDL(){return document.getElementById("bdlKey").value.trim()||(function(){try{return localStorage.getItem("bdl_key")||""}catch(e){return""}}());}
try{var bk=localStorage.getItem("bdl_key");if(bk)document.getElementById("bdlKey").value=bk;}catch(e){}

var BDL_BASE="https://api.balldontlie.io";
var BDL_PATHS=["/nba/v1","/v1"]; // Try new path first, fallback to old
var BDL_ACTIVE_PATH=null; // Will be set after first successful call

var TEAM_ABBR_MAP={"Hawks":"ATL","Celtics":"BOS","Nets":"BRK","Hornets":"CHA","Bulls":"CHI","Cavaliers":"CLE","Mavericks":"DAL","Nuggets":"DEN","Pistons":"DET","Warriors":"GSW","Rockets":"HOU","Pacers":"IND","Clippers":"LAC","Lakers":"LAL","Grizzlies":"MEM","Heat":"MIA","Bucks":"MIL","Timberwolves":"MIN","Pelicans":"NOP","Knicks":"NYK","Thunder":"OKC","Magic":"ORL","76ers":"PHI","Suns":"PHX","Trail Blazers":"POR","Kings":"SAC","Spurs":"SAS","Raptors":"TOR","Jazz":"UTA","Wizards":"WAS"};
var ABBR_FIX={"BKN":"BRK","PHO":"PHX","NOR":"NOP","NOH":"NOP","GS":"GSW","SA":"SAS","NY":"NYK","NO":"NOP"};
function bdlTeamAbbr(t){if(!t)return"UNK";if(t.abbreviation){var a=t.abbreviation;return ABBR_FIX[a]||a;}if(t.name&&TEAM_ABBR_MAP[t.name])return TEAM_ABBR_MAP[t.name];return"UNK";}

function parseMinutes(m){if(!m)return 0;if(typeof m==="number")return m;var s=String(m);if(s.indexOf(":")>=0){var p=s.split(":");return parseInt(p[0])+(parseInt(p[1]||0)/60);}return parseFloat(s)||0;}

async function bdlFetch(endpoint){
  var key=getBDL();
  if(!key)throw new Error("No balldontlie API key.");

  // If we already found a working path, use it
  var pathsToTry=BDL_ACTIVE_PATH?[BDL_ACTIVE_PATH]:BDL_PATHS;

  for(var pi=0;pi<pathsToTry.length;pi++){
    var base=BDL_BASE+pathsToTry[pi];
    try{
      var r=await fetch(base+endpoint,{headers:{"Authorization":key}});
      if(r.ok){
        BDL_ACTIVE_PATH=pathsToTry[pi]; // Remember working path
        return r.json();
      }
      if(r.status===401)throw new Error("401 Unauthorized — check your API key and tier (ALL-STAR needed).");
      if(r.status===429)throw new Error("Rate limited — wait 60 seconds.");
      // 404 or other — try next path
    }catch(e){
      if(e.message.indexOf("401")>=0||e.message.indexOf("Rate")>=0)throw e;
      // Network/CORS error — try proxy
      try{
        var r2=await fetch(proxyUrl(base+endpoint),{headers:{"Authorization":key}});
        if(r2.ok){
          BDL_ACTIVE_PATH=pathsToTry[pi];
          return r2.json();
        }
      }catch(e2){}
    }
  }
  throw new Error("API unreachable on all paths. CORS may be blocking — try from localhost or use proxy.");
}

// ═══════ TEST API CONNECTION ═══════
async function testBDL(){
  var key=getBDL();
  if(!key){alert("Paste your balldontlie API key first.");return;}
  var results=[];
  var paths=["/nba/v1","/v1"];
  for(var pi=0;pi<paths.length;pi++){
    var base=BDL_BASE+paths[pi];
    results.push("--- Testing "+base+" ---");
    // Test 1: Players search
    try{
      var r=await fetch(base+"/players?search=Curry&per_page=3",{headers:{"Authorization":key}});
      var txt=await r.text();
      results.push("Players: HTTP "+r.status+" | "+txt.substring(0,200));
    }catch(e){
      results.push("Players: FAILED ("+e.message+")");
      // Try proxy
      try{
        var r2=await fetch(proxyUrl(base+"/players?search=Curry&per_page=3"),{headers:{"Authorization":key}});
        var txt2=await r2.text();
        results.push("Players (proxy): HTTP "+r2.status+" | "+txt2.substring(0,200));
      }catch(e2){results.push("Players (proxy): FAILED ("+e2.message+")");}
    }
    // Test 2: Stats endpoint
    try{
      var r3=await fetch(base+"/stats?player_ids[]=115&seasons[]=2025&per_page=3",{headers:{"Authorization":key}});
      var txt3=await r3.text();
      results.push("Stats: HTTP "+r3.status+" | "+txt3.substring(0,200));
    }catch(e){
      results.push("Stats: FAILED ("+e.message+")");
      try{
        var r4=await fetch(proxyUrl(base+"/stats?player_ids[]=115&seasons[]=2025&per_page=3"),{headers:{"Authorization":key}});
        var txt4=await r4.text();
        results.push("Stats (proxy): HTTP "+r4.status+" | "+txt4.substring(0,200));
      }catch(e2){results.push("Stats (proxy): FAILED ("+e2.message+")");}
    }
  }
  alert(results.join("\n\n"));
}

// ═══════ AUTO-REFRESH ALL PLAYERS (ALL-STAR TIER — uses game logs) ═══════
function r1(v){return Math.round(v*10)/10;}
function delay(ms){return new Promise(function(r){setTimeout(r,ms)});}

// Cache player IDs in localStorage so we only search once per player
function getIdCache(){try{return JSON.parse(localStorage.getItem("bdl_id_cache")||"{}") }catch(e){return{};}}
function saveIdCache(c){try{localStorage.setItem("bdl_id_cache",JSON.stringify(c))}catch(e){}}

async function bdlFetchAllPages(endpoint){
  // Fetch all pages of a paginated BDL endpoint
  var all=[];
  var nextCursor=null;
  var pages=0;
  while(pages<10){
    var url=endpoint;
    if(nextCursor)url+="&cursor="+nextCursor;
    var data=await bdlFetch(url);
    all=all.concat(data.data||[]);
    if(data.meta&&data.meta.next_cursor){
      nextCursor=data.meta.next_cursor;
      await delay(600);
    }else{break;}
    pages++;
  }
  return all;
}

async function resolvePlayerId(name,team,idCache){
  if(idCache[name])return idCache[name];
  
  var parts=name.split(" ");
  var fname=parts[0].toLowerCase();
  var lname=parts.slice(1).join(" ").toLowerCase();
  var season=new Date().getMonth()>=9?new Date().getFullYear():new Date().getFullYear()-1;
  var allFound=[];
  
  // STRATEGY 1: Search full name
  var s1=await bdlFetch("/players?search="+encodeURIComponent(name)+"&per_page=25");
  allFound=allFound.concat(s1.data||[]);
  
  // STRATEGY 2: Search last name only
  if(allFound.length===0||!allFound.some(function(p){return p.first_name.toLowerCase()===fname;})){
    await delay(1500);
    var s2=await bdlFetch("/players?search="+encodeURIComponent(parts.slice(1).join(" "))+"&per_page=25");
    allFound=allFound.concat(s2.data||[]);
  }
  
  // STRATEGY 3: Search FIRST name (key for "Jalen", "Keldon", "Gradey" etc.)
  if(!allFound.some(function(p){return p.first_name.toLowerCase()===fname&&p.last_name.toLowerCase()===lname;})){
    await delay(1500);
    var s3=await bdlFetch("/players?search="+encodeURIComponent(parts[0])+"&per_page=25");
    allFound=allFound.concat(s3.data||[]);
  }
  
  // STRATEGY 4: Multi-word last name fallback
  if(parts.length>2&&!allFound.some(function(p){return p.first_name.toLowerCase()===fname;})){
    await delay(1500);
    var s4=await bdlFetch("/players?search="+encodeURIComponent(parts[1])+"&per_page=25");
    allFound=allFound.concat(s4.data||[]);
  }
  
  // Deduplicate by ID
  var seen={};var found=[];
  for(var j=0;j<allFound.length;j++){
    if(!seen[allFound[j].id]){seen[allFound[j].id]=true;found.push(allFound[j]);}
  }
  if(found.length===0)return null;
  
  // Score candidates: exact name + team match = best
  var candidates=[];
  for(var j=0;j<found.length;j++){
    var fn=found[j].first_name.toLowerCase();
    var ln=found[j].last_name.toLowerCase();
    var score=0;
    if(fn===fname)score+=10;
    if(ln===lname)score+=10;
    if(found[j].team&&bdlTeamAbbr(found[j].team)===team)score+=5;
    if(score>=10)candidates.push({p:found[j],s:score});
  }
  candidates.sort(function(a,b){return b.s-a.s;});
  if(candidates.length===0)candidates=[{p:found[0],s:0}];
  
  // Perfect match (exact name + team = 25): use immediately
  if(candidates[0].s>=25){
    idCache[name]=candidates[0].p.id;saveIdCache(idCache);return candidates[0].p.id;
  }
  
  // Test top candidates' stats to find who actually plays this season
  for(var c=0;c<Math.min(candidates.length,4);c++){
    await delay(1500);
    try{
      var ts=await bdlFetch("/stats?player_ids[]="+candidates[c].p.id+"&seasons[]="+season+"&per_page=5");
      var tg=(ts.data||[]).filter(function(g){return g.min&&parseMinutes(g.min)>3;});
      if(tg.length>0){
        idCache[name]=candidates[c].p.id;saveIdCache(idCache);return candidates[c].p.id;
      }
    }catch(e){}
  }
  
  // No one had games — return highest-scored candidate anyway
  idCache[name]=candidates[0].p.id;saveIdCache(idCache);return candidates[0].p.id;
}

async function autoRefreshAll(){
  var key=getBDL();
  if(!key){alert("Paste your balldontlie API key at the top of the page first.\n\nGet one at app.balldontlie.io (ALL-STAR tier or higher).");return;}
  if(!confirm("Refresh live stats for "+P.length+" players?\n\nPlayers refreshed in the last 4 hours will be skipped.\nFirst run: ~5 min. Retry runs: much faster."))return;

  var btn=document.getElementById("refreshAllBtn");
  btn.disabled=true;btn.textContent="⏳ Refreshing...";
  document.getElementById("refreshStatus").className="";

  // Season: if Oct+ → current year, else previous year (NBA season convention)
  var now=new Date();
  var season=now.getMonth()>=9?now.getFullYear():now.getFullYear()-1;
  var updated=0,errors=0,skipped=0;
  var errorNames=[];
  var idCache=getIdCache();
  var ratePause=1500; // ms between API calls (safe for 60/min)

  // Quick test: make sure API works before looping 102 players
  try{
    var testData=await bdlFetch("/players?search=Curry&per_page=3");
    if(!testData||!testData.data){
      alert("API returned unexpected format. Response: "+JSON.stringify(testData).substring(0,300));
      btn.disabled=false;btn.textContent="📡 Refresh All Stats";
      return;
    }
    document.getElementById("refreshProgText").textContent="✓ API connected (using "+BDL_ACTIVE_PATH+"). Starting refresh...";
  }catch(e){
    alert("API connection failed: "+e.message);
    btn.disabled=false;btn.textContent="📡 Refresh All Stats";
    return;
  }
  await delay(ratePause);

  // Track which players were successfully refreshed recently
  var refreshLog={};
  try{refreshLog=JSON.parse(localStorage.getItem("bdl_refresh_log")||"{}");}catch(e){}
  var nowMs=Date.now();
  var SKIP_IF_WITHIN=4*60*60*1000; // skip if refreshed within 4 hours

  for(var i=0;i<P.length;i++){
    var pl=P[i];
    // Skip players already marked OUT (minutes=0)
    if(pl.m===0&&pl.a===0){skipped++;continue;}

    // Skip players refreshed within last 4 hours
    if(refreshLog[pl.n]&&(nowMs-refreshLog[pl.n])<SKIP_IF_WITHIN){
      updated++;continue; // count as updated since they have fresh data
    }

    var pct=Math.round(((i+1)/P.length)*100);
    document.getElementById("refreshProgFill").style.width=pct+"%";
    document.getElementById("refreshProgPct").textContent=pct+"%";
    document.getElementById("refreshProgText").textContent="("+(i+1)+"/"+P.length+") "+pl.n+(idCache[pl.n]?" (cached ID)":"")+"...";

    try{
      // 1) Resolve player ID (cached = no API call needed)
      var wasCached=!!idCache[pl.n];
      var pid=await resolvePlayerId(pl.n,pl.t,idCache);
      if(!pid){skipped++;errorNames.push(pl.n+": not found in API");continue;}
      document.getElementById("refreshProgText").textContent="("+(i+1)+"/"+P.length+") "+pl.n+" → ID:"+pid+(wasCached?" (cached)":"");

      await delay(idCache[pl.n]?100:ratePause); // short delay if cached, full if searched

      // 2) Get ALL game logs for the season (per_page=100 covers most players in 1 call)
      var allGames=await bdlFetchAllPages("/stats?player_ids[]="+pid+"&seasons[]="+season+"&per_page=100");

      await delay(ratePause);

      // 3) Filter to games where player actually played (>3 min)
      var played=allGames.filter(function(g){return g.min&&parseMinutes(g.min)>3;});
      if(played.length<3){
        // If player is marked as OUT (m=0, a=0), skip silently
        if(pl.m===0&&pl.a===0){skipped++;continue;}
        // Otherwise, player SHOULD have games — likely wrong ID cached. Clear it.
        delete idCache[pl.n];
        saveIdCache(idCache);
        skipped++;errorNames.push(pl.n+": only "+played.length+" games (ID "+pid+" cleared from cache)");
        continue;
      }

      // 4) Calculate SEASON averages from game logs
      var totFg3a=0,totFg3m=0,totMin=0,totPf=0;
      played.forEach(function(g){
        totFg3a+=(g.fg3a||0);
        totFg3m+=(g.fg3m||0);
        totMin+=parseMinutes(g.min);
        totPf+=(g.pf||0);
      });
      var gp=played.length;
      var seasonA=totFg3a/gp;
      var seasonP=totFg3a>0?(totFg3m/totFg3a)*100:0;
      var seasonMin=totMin/gp;
      var seasonPf36=totMin>0?(totPf/totMin)*36:2.0;

      // 5) Sort by date descending → calculate L10 averages
      played.sort(function(a,b){
        var da=a.game&&a.game.date?a.game.date:"";
        var db=b.game&&b.game.date?b.game.date:"";
        return db.localeCompare(da);
      });
      var l10=played.slice(0,10);
      var l10fg3a=0,l10fg3m=0,l10min=0;
      l10.forEach(function(g){
        l10fg3a+=(g.fg3a||0);
        l10fg3m+=(g.fg3m||0);
        l10min+=parseMinutes(g.min);
      });
      var recentA=l10fg3a/l10.length;
      var recentP=l10fg3a>0?(l10fg3m/l10fg3a)*100:seasonP;
      var recentMin=l10min/l10.length;

      // 6) Get current team from most recent game
      var newTeam=played[0]&&played[0].team?bdlTeamAbbr(played[0].team):pl.t;

      // 7) Update player with REAL stats (v:true = API-verified)
      P[i]={
        n:pl.n,
        t:newTeam!=="UNK"?newTeam:pl.t,
        a:r1(seasonA),
        p:r1(seasonP),
        ra:r1(recentA),
        rp:r1(recentP),
        m:r1(recentMin),  // L10 minutes (more current for injury returns etc.)
        pf36:r1(seasonPf36),
        ha:pl.ha||0.008,
        v:true
      };
      updated++;
      refreshLog[pl.n]=Date.now();

    }catch(e){
      errors++;
      errorNames.push(pl.n+": "+e.message);
      if(e.message.indexOf("Rate")>=0){
        document.getElementById("refreshProgText").textContent="⏳ Rate limited — waiting 65s...";
        await delay(65000);
      }
    }
  }

  // Save everything
  savePlayers();
  renderPlayerList();
  try{localStorage.setItem("bdl_refresh_log",JSON.stringify(refreshLog));}catch(e){}

  // Record last refresh time
  var ts=new Date().toLocaleString();
  try{localStorage.setItem("3pt_last_refresh",ts);}catch(e){}
  showLastRefresh();

  // Show summary
  var summary="✅ Updated "+updated+"/"+P.length+" players · Season "+season+"-"+(season+1);
  if(skipped>0)summary+=" · "+skipped+" skipped";
  if(errors>0)summary+=" · "+errors+" errors";
  document.getElementById("refreshProgText").textContent=summary;
  document.getElementById("refreshProgFill").style.width="100%";
  document.getElementById("refreshProgPct").textContent="✓";

  if(errorNames.length>0){
    document.getElementById("refreshProgText").textContent+="\n⚠ "+errorNames.slice(0,10).join(", ")+(errorNames.length>10?" + "+(errorNames.length-10)+" more":"");
  }

  btn.disabled=false;btn.textContent="📡 Refresh All Stats";
}

function showLastRefresh(){
  try{
    var last=localStorage.getItem("3pt_last_refresh");
    if(last)document.getElementById("lastRefresh").textContent="Last refreshed: "+last;
  }catch(e){}
}

// ═══════ INIT ═══════
loadPlayers();
showLastRefresh();
</script>
</body>
</html>
