path = "www/index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def do_replace(old, new, label):
    global content
    n = content.count(old)
    assert n == 1, f"[{label}] anchor found {n} times (expected 1)"
    content = content.replace(old, new, 1)

# 1. CSS
css_anchor = '.settings-logout-btn{background:var(--surface);border:1px solid rgba(239,68,68,.3);color:#ef4444;border-radius:14px;padding:14px;text-align:center;font-size:.88rem;font-weight:600}'
css_add = """
.settings-modal-overlay{position:fixed;inset:0;z-index:1100;background:rgba(4,4,15,.8);backdrop-filter:blur(4px);display:none;align-items:center;justify-content:center;padding:20px}
.settings-modal-overlay.open{display:flex}
.settings-modal-box{background:var(--bg);border:1px solid var(--border2);border-radius:16px;width:100%;max-width:400px;max-height:80vh;overflow-y:auto;padding:20px;position:relative}
.settings-modal-box h3{font-family:var(--raj);font-size:1.05rem;margin-bottom:14px}
.settings-modal-row{display:flex;flex-direction:column;gap:6px;margin-bottom:14px}
.settings-modal-row label{font-size:.75rem;color:var(--fg3);font-weight:600;letter-spacing:.04em}
.settings-modal-row input[type=text],.settings-modal-row input[type=email],.settings-modal-row input[type=time]{padding:10px 12px;border-radius:10px;background:var(--surface2);border:1px solid var(--border2);color:var(--fg);font-size:.9rem}
.settings-modal-row input[type=range]{width:100%}
.settings-modal-btn{width:100%;padding:12px;border-radius:10px;font-weight:600;border:none;background:linear-gradient(135deg,#7c3aed,#00e5ff);color:#04040f;margin-top:6px}
.settings-modal-btn.secondary{background:var(--surface2);color:var(--fg);border:1px solid var(--border2)}
.settings-modal-close{position:absolute;top:14px;right:14px;background:none;border:none;color:var(--fg3);font-size:1.3rem;cursor:pointer;line-height:1}
.settings-font-opt{display:flex;align-items:center;justify-content:space-between;padding:10px 12px;border-radius:10px;background:var(--surface2);margin-bottom:8px;cursor:pointer;border:1px solid var(--border2)}
.settings-font-opt.active{border-color:var(--violet);background:rgba(124,58,237,.15)}
.cap-toggle-row{display:flex;align-items:center;justify-content:space-between;padding:10px 0;border-bottom:1px solid var(--border2);gap:12px}
.cap-toggle-row:last-child{border-bottom:none}
"""
do_replace(css_anchor, css_anchor + css_add, "css")

# 2. Modal container
html_anchor = "<!-- CHAT MAIN -->"
modal_html = '''<div class="settings-modal-overlay" id="settings-modal-overlay" onclick="if(event.target===this)closeSettingsModal()">
      <div class="settings-modal-box" id="settings-modal-content"></div>
    </div>

    ''' + html_anchor
do_replace(html_anchor, modal_html, "modal-html")

# 3. Real onclick handlers
do_replace("onclick=\"settingsComingSoon('Profile')\"", 'onclick="openProfileEditor()"', "profile-click")
do_replace("onclick=\"settingsComingSoon('Billing')\"", 'onclick="openBillingInfo()"', "billing-click")

do_replace(
    '''onclick="settingsComingSoon('Capabilities')">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Capabilities</div><div class="settings-item-sub">4 enabled</div></div>''',
    '''onclick="openCapabilities()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Capabilities</div><div class="settings-item-sub" id="settings-cap-sub">3 enabled</div></div>''',
    "capabilities-click")

do_replace("onclick=\"settingsComingSoon('Connectors')\"", 'onclick="openConnectorsInfo()"', "connectors-click")

do_replace(
    '''onclick="settingsComingSoon('Font style')">
              <div class="settings-item-icon" style="font-family:var(--raj);font-weight:700;font-size:.85rem">Aa</div>
              <div class="settings-item-text"><div class="settings-item-title">Font style</div><div class="settings-item-sub">Default</div></div>''',
    '''onclick="openFontStyle()">
              <div class="settings-item-icon" style="font-family:var(--raj);font-weight:700;font-size:.85rem">Aa</div>
              <div class="settings-item-text"><div class="settings-item-title">Font style</div><div class="settings-item-sub" id="settings-font-sub">Default</div></div>''',
    "font-click")

do_replace("onclick=\"settingsComingSoon('Voice')\"", 'onclick="openVoiceSettings()"', "voice-click")
do_replace("onclick=\"settingsComingSoon('Time & focus')\"", 'onclick="openQuietHours()"', "time-click")
do_replace("onclick=\"settingsComingSoon('Privacy')\"", 'onclick="openPrivacy()"', "privacy-click")
do_replace("onclick=\"settingsComingSoon('Shared links')\"", 'onclick="shareCurrentChat()"', "shared-click")

# 4. New JS functions
js_anchor = '''function openAppPermissions(){
  alert('To manage permissions, go to your device Settings > Apps > ECLIPSEVEX AI > Permissions.');
}'''

js_add = js_anchor + """

function openSettingsModal(html){
  document.getElementById('settings-modal-content').innerHTML = html;
  document.getElementById('settings-modal-overlay').classList.add('open');
}
function closeSettingsModal(){
  document.getElementById('settings-modal-overlay').classList.remove('open');
}

function openProfileEditor(){
  const name = currentUser ? currentUser.name : '';
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Edit Profile</h3>
    <div class="settings-modal-row">
      <label>Display name</label>
      <input type="text" id="profile-name-input" value="${name}" placeholder="Your name"/>
    </div>
    <button class="settings-modal-btn" onclick="saveProfileName()">Save</button>
  `);
}
function saveProfileName(){
  const val = document.getElementById('profile-name-input').value.trim();
  if(!val){ toast('Name cannot be empty'); return; }
  currentUser.name = val;
  currentUser.initials = val.split(' ').map(p=>p[0]).join('').toUpperCase().slice(0,2);
  try{ localStorage.setItem('evx-current-user', JSON.stringify(currentUser)); }catch(e){}
  document.getElementById('user-display-name').textContent = val;
  document.getElementById('user-avatar-initials').textContent = currentUser.initials;
  const emailEl = document.getElementById('settings-email');
  if(emailEl) emailEl.textContent = val;
  closeSettingsModal();
  toast('Profile updated');
}

const FONT_OPTIONS = {
  default: { label:'Default', stack:"'Inter',sans-serif" },
  rounded: { label:'Rounded', stack:"'Rajdhani',sans-serif" },
  mono:    { label:'Mono',    stack:"'JetBrains Mono',monospace" },
};
function applyFont(key){
  const opt = FONT_OPTIONS[key] || FONT_OPTIONS.default;
  document.documentElement.style.setProperty('--int', opt.stack);
  document.body.style.fontFamily = opt.stack;
  try{ localStorage.setItem('evx-font', key); }catch(e){}
  const sub = document.getElementById('settings-font-sub');
  if(sub) sub.textContent = opt.label;
}
(function(){
  const saved = localStorage.getItem('evx-font');
  if(saved) applyFont(saved);
})();
function openFontStyle(){
  const current = localStorage.getItem('evx-font') || 'default';
  const rows = Object.keys(FONT_OPTIONS).map(k =>
    `<div class="settings-font-opt${k===current?' active':''}" onclick="applyFont('${k}');openFontStyle()">
      <span style="font-family:${FONT_OPTIONS[k].stack}">${FONT_OPTIONS[k].label}</span>
      <span>${k===current?'✓':''}</span>
    </div>`).join('');
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Font style</h3>
    ${rows}
  `);
}

function openVoiceSettings(){
  const rate = parseFloat(localStorage.getItem('evx-voice-rate')||'1');
  const pitch = parseFloat(localStorage.getItem('evx-voice-pitch')||'1');
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Voice</h3>
    <div class="settings-modal-row">
      <label id="voice-rate-label">Speech rate (${rate.toFixed(2)}x)</label>
      <input type="range" min="0.5" max="2" step="0.05" value="${rate}" oninput="updateVoiceRate(this.value)"/>
    </div>
    <div class="settings-modal-row">
      <label id="voice-pitch-label">Pitch (${pitch.toFixed(2)})</label>
      <input type="range" min="0" max="2" step="0.05" value="${pitch}" oninput="updateVoicePitch(this.value)"/>
    </div>
    <button class="settings-modal-btn secondary" onclick="speakRaw('This is how I will sound when I reply.')">Test voice</button>
  `);
}
function updateVoiceRate(v){
  localStorage.setItem('evx-voice-rate', v);
  document.getElementById('voice-rate-label').textContent = 'Speech rate ('+parseFloat(v).toFixed(2)+'x)';
}
function updateVoicePitch(v){
  localStorage.setItem('evx-voice-pitch', v);
  document.getElementById('voice-pitch-label').textContent = 'Pitch ('+parseFloat(v).toFixed(2)+')';
}
function speakRaw(text){
  if(!('speechSynthesis' in window)){ toast('Speech synthesis not supported on this device'); return; }
  const rate = parseFloat(localStorage.getItem('evx-voice-rate')||'1');
  const pitch = parseFloat(localStorage.getItem('evx-voice-pitch')||'1');
  window.speechSynthesis.cancel();
  const u = new SpeechSynthesisUtterance(text);
  u.rate = rate; u.pitch = pitch;
  window.speechSynthesis.speak(u);
}

function isQuietHoursActive(){
  if(localStorage.getItem('evx-quiet-enabled') !== '1') return false;
  const start = localStorage.getItem('evx-quiet-start') || '22:00';
  const end   = localStorage.getItem('evx-quiet-end')   || '07:00';
  const now = new Date();
  const cur = now.getHours()*60 + now.getMinutes();
  const [sh,sm] = start.split(':').map(Number);
  const [eh,em] = end.split(':').map(Number);
  const s = sh*60+sm, e = eh*60+em;
  return s < e ? (cur>=s && cur<e) : (cur>=s || cur<e);
}
function openQuietHours(){
  const enabled = localStorage.getItem('evx-quiet-enabled') === '1';
  const start = localStorage.getItem('evx-quiet-start') || '22:00';
  const end   = localStorage.getItem('evx-quiet-end')   || '07:00';
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Time & focus</h3>
    <div class="settings-modal-row">
      <label style="display:flex;align-items:center;justify-content:space-between">
        Quiet hours (mutes spoken replies)
        <input type="checkbox" ${enabled?'checked':''} onchange="localStorage.setItem('evx-quiet-enabled', this.checked?'1':'0')"/>
      </label>
    </div>
    <div class="settings-modal-row"><label>Start</label><input type="time" value="${start}" onchange="localStorage.setItem('evx-quiet-start', this.value)"/></div>
    <div class="settings-modal-row"><label>End</label><input type="time" value="${end}" onchange="localStorage.setItem('evx-quiet-end', this.value)"/></div>
    <button class="settings-modal-btn" onclick="closeSettingsModal();toast('Quiet hours saved')">Done</button>
  `);
}

function openPrivacy(){
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Privacy</h3>
    <button class="settings-modal-btn secondary" onclick="exportMyData()">Export my data (.json)</button>
    <button class="settings-modal-btn secondary" style="margin-top:10px;color:#ef4444" onclick="clearAllChats()">Clear all chat history</button>
  `);
}
function exportMyData(){
  const payload = { user: currentUser, chats: chatHistory, exportedAt: new Date().toISOString() };
  const blob = new Blob([JSON.stringify(payload,null,2)], {type:'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = 'eclipsevex-data-export.json';
  document.body.appendChild(a); a.click(); document.body.removeChild(a);
  URL.revokeObjectURL(url);
  toast('Export downloaded');
}
function clearAllChats(){
  if(!confirm('Delete ALL chat history? This cannot be undone.')) return;
  chatHistory = []; messages = []; activeChatId = null;
  persistChatHistory();
  renderSidebarChats();
  document.getElementById('chat-messages').style.display='none';
  document.getElementById('chat-welcome').style.display='flex';
  closeSettingsModal();
  toast('All chats cleared');
}

async function shareCurrentChat(){
  if(!messages || messages.length===0){ toast('No active chat to share'); return; }
  const text = messages.map(m => (m.role==='user'?'You: ':'ECLIPSEVEX: ') + m.text).join('\\n\\n');
  if(navigator.share){
    try{ await navigator.share({ title:'ECLIPSEVEX chat', text }); }
    catch(e){ }
  } else if(navigator.clipboard){
    await navigator.clipboard.writeText(text);
    toast('Chat copied to clipboard');
  } else {
    toast('Sharing not supported on this device');
  }
}

const CAPABILITY_KEYS = ['markdown','codeHighlight','mathRender'];
const CAPABILITY_LABELS = { markdown:'Markdown formatting', codeHighlight:'Code syntax highlighting', mathRender:'Math rendering (LaTeX)' };
function getCapability(key){
  const v = localStorage.getItem('evx-cap-'+key);
  return v === null ? true : v === '1';
}
function setCapability(key, val){
  localStorage.setItem('evx-cap-'+key, val ? '1' : '0');
  const sub = document.getElementById('settings-cap-sub');
  if(sub) sub.textContent = CAPABILITY_KEYS.filter(getCapability).length + ' enabled';
}
function openCapabilities(){
  const rows = CAPABILITY_KEYS.map(k => `
    <div class="cap-toggle-row">
      <span>${CAPABILITY_LABELS[k]}</span>
      <div class="settings-toggle${getCapability(k)?' on':''}" onclick="this.classList.toggle('on');setCapability('${k}', this.classList.contains('on'))"><div class="settings-toggle-knob"></div></div>
    </div>`).join('');
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Capabilities</h3>
    ${rows}
  `);
}

function openBillingInfo(){
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Billing</h3>
    <p style="font-size:.85rem;color:var(--fg3);line-height:1.5;margin-bottom:14px">
      You're on the <strong>Free</strong> plan. Paid plans aren't connected to a
      payment processor yet, so upgrading isn't available in-app.
    </p>
    <div class="settings-modal-row"><label>Notify me when upgrades launch</label>
      <input type="email" id="billing-notify-email" placeholder="you@email.com"/>
    </div>
    <button class="settings-modal-btn" onclick="saveBillingNotify()">Save</button>
  `);
}
function saveBillingNotify(){
  const em = document.getElementById('billing-notify-email').value.trim();
  if(!em || !em.includes('@')){ toast('Enter a valid email'); return; }
  try{
    const list = JSON.parse(localStorage.getItem('evx-billing-waitlist')||'[]');
    list.push({ email: em, at: new Date().toISOString() });
    localStorage.setItem('evx-billing-waitlist', JSON.stringify(list));
  }catch(e){}
  closeSettingsModal();
  toast('Saved on this device — connect a backend to actually notify users');
}

function openConnectorsInfo(){
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Connectors</h3>
    <p style="font-size:.85rem;color:var(--fg3);line-height:1.5">
      No connectors are configured. Connecting real services (Drive, Slack, etc.)
      requires OAuth credentials and a token exchange on your server —
      this can't be turned on from the app alone.
    </p>
  `);
}
"""
do_replace(js_anchor, js_add, "js-functions")

# 5. Gate real rendering by capability flags
do_replace(
    "el.innerHTML = (typeof marked!=='undefined') ? marked.parse(text) : text;",
    "el.innerHTML = (getCapability('markdown') && typeof marked!=='undefined') ? marked.parse(text) : text.replace(/</g,'&lt;');",
    "cap-markdown")
do_replace(
    "if(typeof hljs!=='undefined' && !fenceOpen) hljs.highlightElement(block);",
    "if(getCapability('codeHighlight') && typeof hljs!=='undefined' && !fenceOpen) hljs.highlightElement(block);",
    "cap-codehighlight")
do_replace(
    "if(typeof renderMathInElement!=='undefined' && !fenceOpen){",
    "if(getCapability('mathRender') && typeof renderMathInElement!=='undefined' && !fenceOpen){",
    "cap-mathrender")

# 6. Real quiet hours + rate/pitch in speak()
old_speak = '''function speak(text){
  if(!voiceModeOn || !text) return;
  const clean = cleanForSpeech(text);
  if(voiceModeOn) showVoiceOrb('speaking', 'Speaking…');

  if('speechSynthesis' in window){
    window.speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(clean);
    utter.rate = 1.0;
    utter.pitch = 1.0;
    utter.onend = onSpeechDone;
    utter.onerror = () => speakViaServer(clean);
    window.speechSynthesis.speak(utter);
  } else {
    // This WebView has no built-in speech synthesis (common in embedded
    // Android WebViews) — fall back to server-generated audio instead.
    speakViaServer(clean);
  }
}'''

new_speak = '''function speak(text){
  if(!voiceModeOn || !text) return;
  if(isQuietHoursActive()){ onSpeechDone(); return; }
  const clean = cleanForSpeech(text);
  if(voiceModeOn) showVoiceOrb('speaking', 'Speaking…');

  const savedRate = parseFloat(localStorage.getItem('evx-voice-rate')||'1');
  const savedPitch = parseFloat(localStorage.getItem('evx-voice-pitch')||'1');

  if('speechSynthesis' in window){
    window.speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(clean);
    utter.rate = savedRate;
    utter.pitch = savedPitch;
    utter.onend = onSpeechDone;
    utter.onerror = () => speakViaServer(clean);
    window.speechSynthesis.speak(utter);
  } else {
    speakViaServer(clean);
  }
}'''
do_replace(old_speak, new_speak, "speak-fn")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Patched successfully.")
