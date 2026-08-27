import re

path = "www/index.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()


def do_replace(old, new, label):
    global content
    n = content.count(old)
    assert n == 1, f"[{label}] anchor found {n} times (expected 1)"
    content = content.replace(old, new, 1)


def do_regex(pattern, new, label, flags=re.DOTALL):
    global content
    matches = list(re.finditer(pattern, content, flags))
    assert len(matches) == 1, (
        f"[{label}] regex matched {len(matches)} times (expected 1)"
    )
    content = (
        content[:matches[0].start()]
        + new
        + content[matches[0].end():]
    )


# ============================================================
# 1. REAL SETTINGS MODAL CSS
# ============================================================

css_anchor = (
    '.settings-logout-btn{background:var(--surface);'
    'border:1px solid rgba(239,68,68,.3);color:#ef4444;'
    'border-radius:14px;padding:14px;text-align:center;'
    'font-size:.88rem;font-weight:600}'
)

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

.settings-account-left{display:flex;align-items:center;gap:12px}
.settings-account-avatar{width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,var(--violet),var(--cyan));display:flex;align-items:center;justify-content:center;font-family:var(--orb);font-weight:900;font-size:.85rem;color:#04040f;flex-shrink:0}
.settings-account-plan{display:flex;align-items:center;gap:5px;font-size:.75rem;color:#a78bfa;margin-top:2px}
.settings-account-plan svg{width:12px;height:12px}
.settings-upgrade-card{display:flex;align-items:center;gap:12px}
.settings-upgrade-icon{width:38px;height:38px;border-radius:11px;background:rgba(4,4,15,.15);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.settings-upgrade-text{flex:1;min-width:0}
.settings-upgrade-card .settings-upgrade-btn{flex-shrink:0}
.settings-section-label{font-family:var(--orb);font-size:.62rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--fg3);margin:6px 2px -2px}
.settings-quick-row{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.settings-quick-btn{display:flex;flex-direction:column;align-items:center;gap:8px;padding:14px 8px;border-radius:14px;background:var(--surface);border:1px solid var(--border2);color:var(--fg2);font-size:.78rem;font-weight:500}
.settings-quick-icon{width:38px;height:38px;border-radius:50%;background:var(--surface2);display:flex;align-items:center;justify-content:center;color:#a78bfa}
.settings-quick-icon svg{width:17px;height:17px}
.fav-star-btn{background:none;border:none;color:var(--fg3);padding:2px 4px;flex-shrink:0}
.fav-star-btn.active{color:#f59e0b}
.fav-star-btn svg{width:14px;height:14px}
.fav-list-item{display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border2);cursor:pointer}
.fav-list-item:last-child{border-bottom:none}
"""

do_replace(
    css_anchor,
    css_anchor + css_add,
    "css"
)


# ============================================================
# 2. SETTINGS MODAL CONTAINER
# ============================================================

html_anchor = "<!-- CHAT MAIN -->"

modal_html = """<div class="settings-modal-overlay" id="settings-modal-overlay" onclick="if(event.target===this)closeSettingsModal()">
      <div class="settings-modal-box" id="settings-modal-content"></div>
    </div>

    """ + html_anchor

do_replace(
    html_anchor,
    modal_html,
    "modal-html"
)


# ============================================================
# 3. REAL SETTINGS CLICK HANDLERS
# ============================================================

do_replace(
    "onclick=\"settingsComingSoon('Profile')\"",
    'onclick="openProfileEditor()"',
    "profile-click"
)

do_replace(
    "onclick=\"settingsComingSoon('Billing')\"",
    'onclick="openBillingInfo()"',
    "billing-click"
)

do_replace(
    '''onclick="settingsComingSoon('Capabilities')">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Capabilities</div><div class="settings-item-sub">4 enabled</div></div>''',

    '''onclick="openCapabilities()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Capabilities</div><div class="settings-item-sub" id="settings-cap-sub">3 enabled</div></div>''',

    "capabilities-click"
)

do_replace(
    "onclick=\"settingsComingSoon('Connectors')\"",
    'onclick="openConnectorsInfo()"',
    "connectors-click"
)

do_replace(
    '''onclick="settingsComingSoon('Font style')">
              <div class="settings-item-icon" style="font-family:var(--raj);font-weight:700;font-size:.85rem">Aa</div>
              <div class="settings-item-text"><div class="settings-item-title">Font style</div><div class="settings-item-sub">Default</div></div>''',

    '''onclick="openFontStyle()">
              <div class="settings-item-icon" style="font-family:var(--raj);font-weight:700;font-size:.85rem">Aa</div>
              <div class="settings-item-text"><div class="settings-item-title">Font style</div><div class="settings-item-sub" id="settings-font-sub">Default</div></div>''',

    "font-click"
)

do_replace(
    "onclick=\"settingsComingSoon('Voice')\"",
    'onclick="openVoiceSettings()"',
    "voice-click"
)

do_replace(
    "onclick=\"settingsComingSoon('Time & focus')\"",
    'onclick="openQuietHours()"',
    "time-click"
)

do_replace(
    "onclick=\"settingsComingSoon('Privacy')\"",
    'onclick="openPrivacy()"',
    "privacy-click"
)

do_replace(
    "onclick=\"settingsComingSoon('Shared links')\"",
    'onclick="shareCurrentChat()"',
    "shared-click"
)


# ============================================================
# 4. REAL SETTINGS MODAL FUNCTIONS
# ============================================================

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
      <input type="text"
             id="profile-name-input"
             value="${name}"
             placeholder="Your name"/>
    </div>

    <button class="settings-modal-btn"
            onclick="saveProfileName()">Save</button>
  `);
}


function saveProfileName(){
  const val = document.getElementById('profile-name-input').value.trim();

  if(!val){
    toast('Name cannot be empty');
    return;
  }

  currentUser.name = val;

  currentUser.initials = val
    .split(' ')
    .map(p=>p[0])
    .join('')
    .toUpperCase()
    .slice(0,2);

  try{
    localStorage.setItem(
      'evx-current-user',
      JSON.stringify(currentUser)
    );
  }catch(e){}

  document.getElementById('user-display-name').textContent = val;

  document.getElementById('user-avatar-initials').textContent =
    currentUser.initials;

  const emailEl =
    document.getElementById('settings-email');

  if(emailEl)
    emailEl.textContent = val;

  closeSettingsModal();

  toast('Profile updated');
}


const FONT_OPTIONS = {
  default: {
    label:'Default',
    stack:"'Inter',sans-serif"
  },

  rounded: {
    label:'Rounded',
    stack:"'Rajdhani',sans-serif"
  },

  mono: {
    label:'Mono',
    stack:"'JetBrains Mono',monospace"
  }
};


function applyFont(key){
  const opt =
    FONT_OPTIONS[key] || FONT_OPTIONS.default;

  document.documentElement.style.setProperty(
    '--int',
    opt.stack
  );

  document.body.style.fontFamily =
    opt.stack;

  try{
    localStorage.setItem(
      'evx-font',
      key
    );
  }catch(e){}

  const sub =
    document.getElementById('settings-font-sub');

  if(sub)
    sub.textContent = opt.label;
}


(function(){
  const saved =
    localStorage.getItem('evx-font');

  if(saved)
    applyFont(saved);
})();


function openFontStyle(){
  const current =
    localStorage.getItem('evx-font') || 'default';

  const rows =
    Object.keys(FONT_OPTIONS)
      .map(k =>
        `<div class="settings-font-opt${k===current?' active':''}"
              onclick="applyFont('${k}');openFontStyle()">

          <span style="font-family:${FONT_OPTIONS[k].stack}">
            ${FONT_OPTIONS[k].label}
          </span>

          <span>
            ${k===current?'✓':''}
          </span>

        </div>`
      )
      .join('');

  openSettingsModal(`
    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Font style</h3>

    ${rows}
  `);
}


function openVoiceSettings(){
  const rate =
    parseFloat(
      localStorage.getItem('evx-voice-rate') || '1'
    );

  const pitch =
    parseFloat(
      localStorage.getItem('evx-voice-pitch') || '1'
    );

  openSettingsModal(`
    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Voice</h3>

    <div class="settings-modal-row">

      <label id="voice-rate-label">
        Speech rate (${rate.toFixed(2)}x)
      </label>

      <input
        type="range"
        min="0.5"
        max="2"
        step="0.05"
        value="${rate}"
        oninput="updateVoiceRate(this.value)"
      />

    </div>

    <div class="settings-modal-row">

      <label id="voice-pitch-label">
        Pitch (${pitch.toFixed(2)})
      </label>

      <input
        type="range"
        min="0"
        max="2"
        step="0.05"
        value="${pitch}"
        oninput="updateVoicePitch(this.value)"
      />

    </div>

    <button class="settings-modal-btn secondary"
            onclick="speakRaw('This is how I will sound when I reply.')">
      Test voice
    </button>
  `);
}


function updateVoiceRate(v){
  localStorage.setItem(
    'evx-voice-rate',
    v
  );

  document.getElementById(
    'voice-rate-label'
  ).textContent =
    'Speech rate (' +
    parseFloat(v).toFixed(2) +
    'x)';
}


function updateVoicePitch(v){
  localStorage.setItem(
    'evx-voice-pitch',
    v
  );

  document.getElementById(
    'voice-pitch-label'
  ).textContent =
    'Pitch (' +
    parseFloat(v).toFixed(2) +
    ')';
}


function speakRaw(text){
  if(!('speechSynthesis' in window)){
    toast(
      'Speech synthesis not supported on this device'
    );
    return;
  }

  const rate =
    parseFloat(
      localStorage.getItem('evx-voice-rate') || '1'
    );

  const pitch =
    parseFloat(
      localStorage.getItem('evx-voice-pitch') || '1'
    );

  window.speechSynthesis.cancel();

  const u =
    new SpeechSynthesisUtterance(text);

  u.rate = rate;
  u.pitch = pitch;

  window.speechSynthesis.speak(u);
}


function isQuietHoursActive(){

  if(
    localStorage.getItem(
      'evx-quiet-enabled'
    ) !== '1'
  )
    return false;

  const start =
    localStorage.getItem(
      'evx-quiet-start'
    ) || '22:00';

  const end =
    localStorage.getItem(
      'evx-quiet-end'
    ) || '07:00';

  const now = new Date();

  const cur =
    now.getHours() * 60 +
    now.getMinutes();

  const [sh,sm] =
    start.split(':').map(Number);

  const [eh,em] =
    end.split(':').map(Number);

  const s =
    sh * 60 + sm;

  const e =
    eh * 60 + em;

  return s < e
    ? (cur >= s && cur < e)
    : (cur >= s || cur < e);
}


function openQuietHours(){

  const enabled =
    localStorage.getItem(
      'evx-quiet-enabled'
    ) === '1';

  const start =
    localStorage.getItem(
      'evx-quiet-start'
    ) || '22:00';

  const end =
    localStorage.getItem(
      'evx-quiet-end'
    ) || '07:00';

  openSettingsModal(`

    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Time & focus</h3>

    <div class="settings-modal-row">

      <label style="display:flex;align-items:center;justify-content:space-between">

        Quiet hours (mutes spoken replies)

        <input
          type="checkbox"
          ${enabled?'checked':''}
          onchange="localStorage.setItem(
            'evx-quiet-enabled',
            this.checked?'1':'0'
          )"
        />

      </label>

    </div>

    <div class="settings-modal-row">

      <label>Start</label>

      <input
        type="time"
        value="${start}"
        onchange="localStorage.setItem(
          'evx-quiet-start',
          this.value
        )"
      />

    </div>

    <div class="settings-modal-row">

      <label>End</label>

      <input
        type="time"
        value="${end}"
        onchange="localStorage.setItem(
          'evx-quiet-end',
          this.value
        )"
      />

    </div>

    <button
      class="settings-modal-btn"
      onclick="closeSettingsModal();toast('Quiet hours saved')">
      Done
    </button>

  `);
}


function openPrivacy(){

  openSettingsModal(`

    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Privacy</h3>

    <button
      class="settings-modal-btn secondary"
      onclick="exportMyData()">
      Export my data (.json)
    </button>

    <button
      class="settings-modal-btn secondary"
      style="margin-top:10px;color:#ef4444"
      onclick="clearAllChats()">
      Clear all chat history
    </button>

  `);
}


function exportMyData(){

  const payload = {
    user: currentUser,
    chats: chatHistory,
    exportedAt: new Date().toISOString()
  };

  const blob =
    new Blob(
      [JSON.stringify(payload,null,2)],
      {type:'application/json'}
    );

  const url =
    URL.createObjectURL(blob);

  const a =
    document.createElement('a');

  a.href = url;

  a.download =
    'eclipsevex-data-export.json';

  document.body.appendChild(a);

  a.click();

  document.body.removeChild(a);

  URL.revokeObjectURL(url);

  toast('Export downloaded');
}


function clearAllChats(){

  if(
    !confirm(
      'Delete ALL chat history? This cannot be undone.'
    )
  )
    return;

  chatHistory = [];
  messages = [];
  activeChatId = null;

  persistChatHistory();

  renderSidebarChats();

  document.getElementById(
    'chat-messages'
  ).style.display = 'none';

  document.getElementById(
    'chat-welcome'
  ).style.display = 'flex';

  closeSettingsModal();

  toast('All chats cleared');
}


async function shareCurrentChat(){

  if(
    !messages ||
    messages.length === 0
  ){
    toast('No active chat to share');
    return;
  }

  const text =
    messages
      .map(
        m =>
          (m.role === 'user'
            ? 'You: '
            : 'ECLIPSEVEX: ') +
          m.text
      )
      .join('\\n\\n');

  if(navigator.share){

    try{

      await navigator.share({
        title:'ECLIPSEVEX chat',
        text
      });

    }catch(e){}

  }else if(navigator.clipboard){

    await navigator.clipboard.writeText(text);

    toast(
      'Chat copied to clipboard'
    );

  }else{

    toast(
      'Sharing not supported on this device'
    );

  }
}


const CAPABILITY_KEYS = [
  'markdown',
  'codeHighlight',
  'mathRender'
];


const CAPABILITY_LABELS = {
  markdown:'Markdown formatting',
  codeHighlight:'Code syntax highlighting',
  mathRender:'Math rendering (LaTeX)'
};


function getCapability(key){

  const v =
    localStorage.getItem(
      'evx-cap-' + key
    );

  return v === null
    ? true
    : v === '1';
}


function setCapability(key,val){

  localStorage.setItem(
    'evx-cap-' + key,
    val ? '1' : '0'
  );

  const sub =
    document.getElementById(
      'settings-cap-sub'
    );

  if(sub){

    sub.textContent =
      CAPABILITY_KEYS
        .filter(getCapability)
        .length +
      ' enabled';

  }
}


function openCapabilities(){

  const rows =
    CAPABILITY_KEYS
      .map(
        k => `

        <div class="cap-toggle-row">

          <span>
            ${CAPABILITY_LABELS[k]}
          </span>

          <div
            class="settings-toggle${getCapability(k)?' on':''}"
            onclick="
              this.classList.toggle('on');
              setCapability(
                '${k}',
                this.classList.contains('on')
              )
            "
          >

            <div class="settings-toggle-knob"></div>

          </div>

        </div>

      `
      )
      .join('');

  openSettingsModal(`

    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Capabilities</h3>

    ${rows}

  `);
}


function openBillingInfo(){

  openSettingsModal(`

    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Billing</h3>

    <p
      style="font-size:.85rem;color:var(--fg3);line-height:1.5;margin-bottom:14px">

      You're on the
      <strong>Free</strong> plan.

      Paid plans aren't connected to a
      payment processor yet, so upgrading
      isn't available in-app.

    </p>

    <div class="settings-modal-row">

      <label>
        Notify me when upgrades launch
      </label>

      <input
        type="email"
        id="billing-notify-email"
        placeholder="you@email.com"
      />

    </div>

    <button
      class="settings-modal-btn"
      onclick="saveBillingNotify()">
      Save
    </button>

  `);
}


function saveBillingNotify(){

  const em =
    document
      .getElementById(
        'billing-notify-email'
      )
      .value
      .trim();

  if(
    !em ||
    !em.includes('@')
  ){
    toast('Enter a valid email');
    return;
  }

  try{

    const list =
      JSON.parse(
        localStorage.getItem(
          'evx-billing-waitlist'
        ) || '[]'
      );

    list.push({
      email: em,
      at: new Date().toISOString()
    });

    localStorage.setItem(
      'evx-billing-waitlist',
      JSON.stringify(list)
    );

  }catch(e){}

  closeSettingsModal();

  toast(
    'Saved on this device — connect a backend to actually notify users'
  );
}


function openConnectorsInfo(){

  openSettingsModal(`

    <button class="settings-modal-close"
            onclick="closeSettingsModal()">&times;</button>

    <h3>Connectors</h3>

    <p
      style="font-size:.85rem;color:var(--fg3);line-height:1.5">

      No connectors are configured.

      Connecting real services
      (Drive, Slack, etc.) requires OAuth
      credentials and a token exchange on
      your server — this can't be turned on
      from the app alone.

    </p>

  `);
}
"""

do_replace(
    js_anchor,
    js_add,
    "js-functions"
)


# ============================================================
# 5. CAPABILITY FLAGS FOR MARKDOWN / CODE / MATH
# ============================================================

do_replace(
    "el.innerHTML = (typeof marked!=='undefined') ? marked.parse(text) : text;",
    "el.innerHTML = (getCapability('markdown') && typeof marked!=='undefined') ? marked.parse(text) : text.replace(/</g,'&lt;');",
    "cap-markdown"
)

do_replace(
    "if(typeof hljs!=='undefined' && !fenceOpen) hljs.highlightElement(block);",
    "if(getCapability('codeHighlight') && typeof hljs!=='undefined' && !fenceOpen) hljs.highlightElement(block);",
    "cap-codehighlight"
)

do_replace(
    "if(typeof renderMathInElement!=='undefined' && !fenceOpen){",
    "if(getCapability('mathRender') && typeof renderMathInElement!=='undefined' && !fenceOpen){",
    "cap-mathrender"
)


# ============================================================
# 6. REAL VOICE SETTINGS + QUIET HOURS
# ============================================================

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

  if(isQuietHoursActive()){
    onSpeechDone();
    return;
  }

  const clean = cleanForSpeech(text);

  if(voiceModeOn)
    showVoiceOrb('speaking', 'Speaking…');

  const savedRate =
    parseFloat(
      localStorage.getItem('evx-voice-rate') || '1'
    );

  const savedPitch =
    parseFloat(
      localStorage.getItem('evx-voice-pitch') || '1'
    );

  if('speechSynthesis' in window){

    window.speechSynthesis.cancel();

    const utter =
      new SpeechSynthesisUtterance(clean);

    utter.rate = savedRate;
    utter.pitch = savedPitch;

    utter.onend = onSpeechDone;

    utter.onerror =
      () => speakViaServer(clean);

    window.speechSynthesis.speak(utter);

  }else{

    speakViaServer(clean);

  }
}'''

do_replace(
    old_speak,
    new_speak,
    "speak-fn"
)


# ============================================================
# 7. REPLACE ENTIRE SETTINGS BODY WITH PREMIUM STRUCTURE
# ============================================================

new_body = '''<div class="settings-body">

          <!-- ACCOUNT -->
          <div class="settings-account-card">

            <div class="settings-account-left">

              <div
                class="settings-account-avatar"
                id="settings-account-avatar">
                ?
              </div>

              <div>

                <div
                  class="settings-account-email"
                  id="settings-email">
                  user@example.com
                </div>

                <div class="settings-account-plan">

                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="3"
                    stroke-linecap="round"
                    stroke-linejoin="round">

                    <polyline points="20 6 9 17 4 12"/>

                  </svg>

                  Free Plan

                </div>

              </div>

            </div>

          </div>


          <!-- PREMIUM UPGRADE -->
          <div class="settings-upgrade-card">

            <div class="settings-upgrade-icon">

              <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="#04040f"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                style="width:18px;height:18px">

                <path d="M2 20h20M4 20V10l4 3 4-7 4 7 4-3v10"/>

              </svg>

            </div>

            <div class="settings-upgrade-text">

              <div class="settings-upgrade-title">
                Unlock Premium
              </div>

              <div class="settings-upgrade-sub">
                Get more tokens, advanced features & priority access.
              </div>

            </div>

            <button
              class="settings-upgrade-btn"
              onclick="openBillingInfo()">

              Upgrade

            </button>

          </div>


          <!-- QUICK ACCESS -->
          <div class="settings-section-label">
            Quick Access
          </div>

          <div class="settings-quick-row">

            <button
              class="settings-quick-btn"
              onclick="closeSettings();newChat()">

              <span class="settings-quick-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>

                </svg>

              </span>

              New Chat

            </button>


            <button
              class="settings-quick-btn"
              onclick="openFavorites()">

              <span class="settings-quick-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="currentColor">

                  <polygon
                    points="12 2 15 9 22 9.5 17 14.5 18.5 22 12 18 5.5 22 7 14.5 2 9.5 9 9"/>

                </svg>

              </span>

              Favorites

            </button>


            <button
              class="settings-quick-btn"
              onclick="openHistoryPanel()">

              <span class="settings-quick-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <polyline points="12 7 12 12 15 15"/>

                  <path d="M21 12a9 9 0 1 1-3-6.7"/>

                  <polyline points="21 3 21 9 15 9"/>

                </svg>

              </span>

              History

            </button>

          </div>


          <!-- CORE SETTINGS -->
          <div class="settings-section-label">
            Core Settings
          </div>

          <div class="settings-group">


            <!-- PROFILE -->
            <div
              class="settings-item"
              onclick="openProfileEditor()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <circle cx="12" cy="8" r="4"/>

                  <path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Profile
                </div>

                <div class="settings-item-sub">
                  Manage your personal info
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- CAPABILITIES -->
            <div
              class="settings-item"
              onclick="openCapabilities()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <line x1="4" y1="21" x2="4" y2="14"/>
                  <line x1="4" y1="10" x2="4" y2="3"/>
                  <line x1="12" y1="21" x2="12" y2="12"/>
                  <line x1="12" y1="8" x2="12" y2="3"/>
                  <line x1="20" y1="21" x2="20" y2="16"/>
                  <line x1="20" y1="12" x2="20" y2="3"/>
                  <line x1="1" y1="14" x2="7" y2="14"/>
                  <line x1="9" y1="8" x2="15" y2="8"/>
                  <line x1="17" y1="16" x2="23" y2="16"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Capabilities
                </div>

                <div
                  class="settings-item-sub"
                  id="settings-cap-sub">
                  3 enabled
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- CONNECTORS -->
            <div
              class="settings-item"
              onclick="openConnectorsInfo()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <path d="M9 3v6M15 3v6M6 9h12l-1 5a5 5 0 0 1-10 0Z"/>

                  <path d="M12 17v4"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Connectors
                </div>

                <div class="settings-item-sub">
                  Manage integrations
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- APPEARANCE -->
            <div
              class="settings-item"
              onclick="openAppearance()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <circle cx="12" cy="12" r="9"/>

                  <circle cx="9" cy="9.5" r="1"/>
                  <circle cx="15" cy="9.5" r="1"/>
                  <circle cx="9" cy="14.5" r="1"/>

                  <path d="M15 14.5a1 1 0 1 1-2 0"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Appearance
                </div>

                <div class="settings-item-sub">
                  Color mode, font style
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- HAPTIC -->
            <div
              class="settings-item"
              style="cursor:default">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <rect
                    x="5"
                    y="2"
                    width="14"
                    height="20"
                    rx="2"/>

                  <line
                    x1="12"
                    y1="18"
                    x2="12.01"
                    y2="18"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Haptic feedback
                </div>

              </div>

              <div
                class="settings-toggle on"
                id="haptic-toggle"
                onclick="toggleHaptic(event)">

                <div class="settings-toggle-knob"></div>

              </div>

            </div>


            <!-- TIME & FOCUS -->
            <div
              class="settings-item"
              onclick="openQuietHours()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <path d="M21 12.5A9 9 0 1 1 11.5 3 7 7 0 0 0 21 12.5Z"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Time & focus
                </div>

                <div class="settings-item-sub">
                  Manage reminders & focus
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- PRIVACY -->
            <div
              class="settings-item"
              onclick="openPrivacy()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <path d="M12 2 4 5v6c0 5 3.5 8.5 8 11 4.5-2.5 8-6 8-11V5Z"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Privacy & data
                </div>

                <div class="settings-item-sub">
                  Control your data & privacy
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- NOTIFICATIONS -->
            <div
              class="settings-item"
              onclick="openNotifications()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/>

                  <path d="M13.73 21a2 2 0 0 1-3.46 0"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Notifications
                </div>

                <div class="settings-item-sub">
                  Manage alerts & updates
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>

          </div>


          <!-- SUPPORT -->
          <div class="settings-section-label">
            Support
          </div>

          <div class="settings-group">


            <!-- HELP CENTER -->
            <div
              class="settings-item"
              onclick="openHelpCenter()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <circle
                    cx="12"
                    cy="12"
                    r="9"/>

                  <path
                    d="M9.5 9a2.5 2.5 0 0 1 5 0c0 1.5-2.5 2-2.5 3.5"/>

                  <line
                    x1="12"
                    y1="17"
                    x2="12.01"
                    y2="17"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Help center
                </div>

                <div class="settings-item-sub">
                  FAQs & guides
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>


            <!-- FEEDBACK -->
            <div
              class="settings-item"
              onclick="openFeedback()">

              <div class="settings-item-icon">

                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round">

                  <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>

                </svg>

              </div>

              <div class="settings-item-text">

                <div class="settings-item-title">
                  Feedback
                </div>

                <div class="settings-item-sub">
                  Share your thoughts
                </div>

              </div>

              <svg
                class="settings-item-chevron"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round">

                <polyline points="9 18 15 12 9 6"/>

              </svg>

            </div>

          </div>


          <!-- LOGOUT -->
          <button
            class="settings-logout-btn"
            onclick="closeSettings();signOut()">

            Log out

          </button>

        </div>'''

do_regex(
    r'<div class="settings-body">.*?Log out</button>\s*</div>',
    new_body,
    "settings-body"
)


# ============================================================
# 8. UPDATE openSettings() ACCOUNT AVATAR
# ============================================================

do_replace(
    """function openSettings(){
  const overlay = document.getElementById('settings-overlay');
  const emailEl = document.getElementById('settings-email');
  const nameEl = document.getElementById('user-display-name');
  if(emailEl && nameEl && nameEl.textContent.trim()) emailEl.textContent = nameEl.textContent.trim();""",

    """function openSettings(){
  const overlay = document.getElementById('settings-overlay');
  const emailEl = document.getElementById('settings-email');
  const nameEl = document.getElementById('user-display-name');
  if(emailEl && nameEl && nameEl.textContent.trim()) emailEl.textContent = nameEl.textContent.trim();

  const avEl =
    document.getElementById('settings-account-avatar');

  if(avEl && currentUser)
    avEl.textContent =
      currentUser.initials || '?';""",

    "open-settings-avatar"
)


# ============================================================
# 9. FAVORITE STAR IN SIDEBAR CHAT ITEMS
# ============================================================

old_render = '''function renderSidebarChats(){
  const container = document.getElementById('sidebar-chats');
  if(chatHistory.length===0){ container.innerHTML='<div style="padding:10px 12px;font-size:.8rem;color:var(--fg3)">No chats yet</div>'; return; }
  container.innerHTML = chatHistory.map(ch=>`
    <button class="chat-item${ch.id===activeChatId?' active':''}" onclick="loadChat('${ch.id}')" style="position:relative">
      <svg class="chat-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      <span class="chat-item-text">${ch.title}</span>
      <span class="chat-item-time">${ch.time}</span>
      <span onclick="deleteChat('${ch.id}', event)" style="margin-left:6px;padding:2px 6px;color:var(--fg3);cursor:pointer;font-size:.85rem" title="Delete chat">&times;</span>
    </button>`).join('');
}'''

new_render = '''function renderSidebarChats(){
  const container =
    document.getElementById('sidebar-chats');

  if(chatHistory.length===0){

    container.innerHTML =
      '<div style="padding:10px 12px;font-size:.8rem;color:var(--fg3)">No chats yet</div>';

    return;
  }

  container.innerHTML =
    chatHistory.map(ch=>`

    <button
      class="chat-item${ch.id===activeChatId?' active':''}"
      onclick="loadChat('${ch.id}')"
      style="position:relative">

      <svg
        class="chat-item-icon"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="1.8"
        stroke-linecap="round">

        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>

      </svg>

      <span class="chat-item-text">
        ${ch.title}
      </span>

      <span class="chat-item-time">
        ${ch.time}
      </span>

      <button
        class="fav-star-btn${ch.favorite?' active':''}"
        onclick="toggleFavorite('${ch.id}', event)"
        title="Favorite">

        <svg
          viewBox="0 0 24 24"
          fill="${ch.favorite?'currentColor':'none'}"
          stroke="currentColor"
          stroke-width="2">

          <polygon points="12 2 15 9 22 9.5 17 14.5 18.5 22 12 18 5.5 22 7 14.5 2 9.5 9 9"/>

        </svg>

      </button>

      <span
        onclick="deleteChat('${ch.id}', event)"
        style="margin-left:2px;padding:2px 6px;color:var(--fg3);cursor:pointer;font-size:.85rem"
        title="Delete chat">

        &times;

      </span>

    </button>

  `).join('');
}


function toggleFavorite(id, evt){

  if(evt)
    evt.stopPropagation();

  const ch =
    chatHistory.find(
      c => c.id === id
    );

  if(!ch)
    return;

  ch.favorite =
    !ch.favorite;

  persistChatHistory();

  renderSidebarChats();
}'''

do_replace(
    old_render,
    new_render,
    "render-sidebar-chats"
)


# ============================================================
# 10. FAVORITES / HISTORY / APPEARANCE / NOTIFICATIONS /
#     HELP CENTER / FEEDBACK
# ============================================================

js_anchor = '''function openConnectorsInfo(){
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Connectors</h3>
    <p style="font-size:.85rem;color:var(--fg3);line-height:1.5">
      No connectors are configured. Connecting real services (Drive, Slack, etc.)
      requires OAuth credentials and a token exchange on your server —
      this can't be turned on from the app alone.
    </p>
  `);
}'''

js_add = js_anchor + """


// ============================================================
// FAVORITES
// ============================================================

function openFavorites(){

  const favs =
    chatHistory.filter(
      c => c.favorite
    );

  const rows =
    favs.length

      ? favs.map(
          c => `

          <div
            class="fav-list-item"
            onclick="
              closeSettingsModal();
              closeSettings();
              loadChat('${c.id}')
            ">

            <svg
              viewBox="0 0 24 24"
              fill="currentColor"
              style="width:14px;height:14px;color:#f59e0b;flex-shrink:0">

              <polygon
                points="12 2 15 9 22 9.5 17 14.5 18.5 22 12 18 5.5 22 7 14.5 2 9.5 9"/>

            </svg>

            <span style="font-size:.88rem">
              ${c.title}
            </span>

          </div>

        `
        ).join('')

      : `
        <p style="font-size:.85rem;color:var(--fg3)">
          No favorites yet — tap the star on any chat in the sidebar to add one.
        </p>
      `;

  openSettingsModal(`

    <button
      class="settings-modal-close"
      onclick="closeSettingsModal()">
      &times;
    </button>

    <h3>Favorites</h3>

    ${rows}

  `);
}


// ============================================================
// HISTORY
// ============================================================

function openHistoryPanel(){

  closeSettings();

  const sb =
    document.getElementById('sidebar');

  if(window.innerWidth <= 768){

    sb.classList.add('open');

    document
      .getElementById('sidebar-overlay')
      .classList.add('open');

    document
      .getElementById('sidebar-close-btn')
      .style.display = 'flex';

  }else if(
    sb.style.display === 'none'
  ){

    toggleSidebar();

  }
}


// ============================================================
// APPEARANCE
// ============================================================

function openAppearance(){

  const isLight =
    document.documentElement
      .getAttribute('data-theme') === 'light';

  const current =
    localStorage.getItem('evx-font') ||
    'default';

  const fontRows =
    Object.keys(FONT_OPTIONS)
      .map(
        k => `

        <div
          class="settings-font-opt${k===current?' active':''}"
          onclick="applyFont('${k}');openAppearance()">

          <span
            style="font-family:${FONT_OPTIONS[k].stack}">

            ${FONT_OPTIONS[k].label}

          </span>

          <span>
            ${k===current?'✓':''}
          </span>

        </div>

      `
      )
      .join('');

  openSettingsModal(`

    <button
      class="settings-modal-close"
      onclick="closeSettingsModal()">
      &times;
    </button>

    <h3>Appearance</h3>

    <div class="settings-modal-row">

      <label
        style="display:flex;align-items:center;justify-content:space-between">

        Dark mode

        <input
          type="checkbox"
          ${!isLight?'checked':''}
          onchange="toggleTheme();openAppearance()"
        />

      </label>

    </div>

    <div class="settings-modal-row">

      <label>
        Font style
      </label>

      ${fontRows}

    </div>

  `);
}


// ============================================================
// NOTIFICATIONS
// ============================================================

async function openNotifications(){

  const enabled =
    localStorage.getItem(
      'evx-notify-enabled'
    ) === '1';

  openSettingsModal(`

    <button
      class="settings-modal-close"
      onclick="closeSettingsModal()">
      &times;
    </button>

    <h3>Notifications</h3>

    <div class="settings-modal-row">

      <label
        style="display:flex;align-items:center;justify-content:space-between">

        Enable reminders

        <input
          type="checkbox"
          ${enabled?'checked':''}
          onchange="toggleNotifications(this.checked)"
        />

      </label>

    </div>

    <button
      class="settings-modal-btn secondary"
      onclick="sendTestNotification()">

      Send test notification

    </button>

  `);
}


async function toggleNotifications(val){

  const {
    LocalNotifications
  } =
    (window.Capacitor &&
     window.Capacitor.Plugins) || {};

  if(!LocalNotifications){

    toast(
      'Notifications plugin not available in this build'
    );

    return;
  }

  if(val){

    const perm =
      await LocalNotifications
        .requestPermissions();

    if(
      perm.display !== 'granted'
    ){

      toast('Permission denied');

      return;
    }
  }

  localStorage.setItem(
    'evx-notify-enabled',
    val ? '1' : '0'
  );

  toast(
    val
      ? 'Notifications enabled'
      : 'Notifications disabled'
  );
}


async function sendTestNotification(){

  const {
    LocalNotifications
  } =
    (window.Capacitor &&
     window.Capacitor.Plugins) || {};

  if(!LocalNotifications){

    toast(
      'Notifications plugin not available in this build'
    );

    return;
  }

  const perm =
    await LocalNotifications
      .checkPermissions();

  if(
    perm.display !== 'granted'
  ){

    const req =
      await LocalNotifications
        .requestPermissions();

    if(
      req.display !== 'granted'
    ){

      toast('Permission denied');

      return;
    }
  }

  await LocalNotifications.schedule({

    notifications: [{

      title:'ECLIPSEVEX AI',

      body:'This is a test notification.',

      id:
        Date.now() % 100000,

      schedule:{
        at:
          new Date(
            Date.now() + 2000
          )
      }

    }]

  });

  toast(
    'Test notification scheduled'
  );
}


// ============================================================
// HELP CENTER
// ============================================================

function openHelpCenter(){

  openSettingsModal(`

    <button
      class="settings-modal-close"
      onclick="closeSettingsModal()">
      &times;
    </button>

    <h3>Help center</h3>

    <div
      style="font-size:.85rem;color:var(--fg3);line-height:1.6">

      <p style="margin-bottom:10px">

        <strong style="color:var(--fg)">
          How do I start a new chat?
        </strong>

        <br/>

        Tap "New Chat" from Quick Access or the sidebar.

      </p>


      <p style="margin-bottom:10px">

        <strong style="color:var(--fg)">
          How do I attach a photo?
        </strong>

        <br/>

        Tap the + button next to the message box.

      </p>


      <p>

        <strong style="color:var(--fg)">
          How do I delete my data?
        </strong>

        <br/>

        Go to Privacy & data → Clear all chat history.

      </p>

    </div>

  `);
}


// ============================================================
// FEEDBACK
// ============================================================

function openFeedback(){

  openSettingsModal(`

    <button
      class="settings-modal-close"
      onclick="closeSettingsModal()">
      &times;
    </button>

    <h3>Feedback</h3>

    <div class="settings-modal-row">

      <label>
        Your message
      </label>

      <textarea
        id="feedback-text"
        rows="4"
        style="padding:10px 12px;border-radius:10px;background:var(--surface2);border:1px solid var(--border2);color:var(--fg);font-size:.9rem;font-family:inherit;resize:vertical"
        placeholder="What's on your mind?"></textarea>

    </div>

    <button
      class="settings-modal-btn"
      onclick="sendFeedback()">

      Send via email

    </button>

  `);
}


function sendFeedback(){

  const msg =
    document
      .getElementById(
        'feedback-text'
      )
      .value
      .trim();

  if(!msg){

    toast(
      'Write something first'
    );

    return;
  }

  const subject =
    encodeURIComponent(
      'ECLIPSEVEX AI Feedback'
    );

  const body =
    encodeURIComponent(
      msg +
      '\\n\\n— from ' +
      (
        currentUser
          ? currentUser.name
          : 'a user'
      )
    );

  window.location.href =
    `mailto:hello@eclipsevex.ai?subject=${subject}&body=${body}`;

  closeSettingsModal();
}
"""

do_replace(
    js_anchor,
    js_add,
    "js-new-functions"
)


# ============================================================
# 11. WRITE FINAL COMBINED FILE
# ============================================================

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("")
print("==================================================")
print(" ECLIPSEVEX AI SETTINGS PATCH")
print("==================================================")
print("Patched successfully.")
print("")
print("Premium settings structure applied.")
print("Real settings modals enabled.")
print("Favorites / History / Appearance enabled.")
print("Notifications / Help / Feedback enabled.")
print("Voice rate / pitch / quiet hours enabled.")
print("Capabilities flags enabled.")
print("Privacy export / clear history enabled.")
print("==================================================")
