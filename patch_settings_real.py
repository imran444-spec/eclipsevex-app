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
    assert len(matches) == 1, f"[{label}] regex matched {len(matches)} times (expected 1)"
    content = content[:matches[0].start()] + new + content[matches[0].end():]

# ─────────────────────────────────────────────
# 1. CSS additions
# ─────────────────────────────────────────────
css_anchor = ".cap-toggle-row:last-child{border-bottom:none}"
css_add = """
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
do_replace(css_anchor, css_anchor + css_add, "css")

# ─────────────────────────────────────────────
# 2. Replace the whole settings-body block with the premium structure
# ─────────────────────────────────────────────
new_body = '''<div class="settings-body">
          <div class="settings-account-card">
            <div class="settings-account-left">
              <div class="settings-account-avatar" id="settings-account-avatar">?</div>
              <div>
                <div class="settings-account-email" id="settings-email">user@example.com</div>
                <div class="settings-account-plan"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>Free Plan</div>
              </div>
            </div>
          </div>

          <div class="settings-upgrade-card">
            <div class="settings-upgrade-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#04040f" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:18px;height:18px"><path d="M2 20h20M4 20V10l4 3 4-7 4 7 4-3v10"/></svg></div>
            <div class="settings-upgrade-text">
              <div class="settings-upgrade-title">Unlock Premium</div>
              <div class="settings-upgrade-sub">Get more tokens, advanced features & priority access.</div>
            </div>
            <button class="settings-upgrade-btn" onclick="openBillingInfo()">Upgrade</button>
          </div>

          <div class="settings-section-label">Quick Access</div>
          <div class="settings-quick-row">
            <button class="settings-quick-btn" onclick="closeSettings();newChat()">
              <span class="settings-quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span>
              New Chat
            </button>
            <button class="settings-quick-btn" onclick="openFavorites()">
              <span class="settings-quick-icon"><svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15 9 22 9.5 17 14.5 18.5 22 12 18 5.5 22 7 14.5 2 9.5 9 9"/></svg></span>
              Favorites
            </button>
            <button class="settings-quick-btn" onclick="openHistoryPanel()">
              <span class="settings-quick-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="12 7 12 12 15 15"/><path d="M21 12a9 9 0 1 1-3-6.7"/><polyline points="21 3 21 9 15 9"/></svg></span>
              History
            </button>
          </div>

          <div class="settings-section-label">Core Settings</div>
          <div class="settings-group">
            <div class="settings-item" onclick="openProfileEditor()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Profile</div><div class="settings-item-sub">Manage your personal info</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" onclick="openCapabilities()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="4" y1="21" x2="4" y2="14"/><line x1="4" y1="10" x2="4" y2="3"/><line x1="12" y1="21" x2="12" y2="12"/><line x1="12" y1="8" x2="12" y2="3"/><line x1="20" y1="21" x2="20" y2="16"/><line x1="20" y1="12" x2="20" y2="3"/><line x1="1" y1="14" x2="7" y2="14"/><line x1="9" y1="8" x2="15" y2="8"/><line x1="17" y1="16" x2="23" y2="16"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Capabilities</div><div class="settings-item-sub" id="settings-cap-sub">3 enabled</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" onclick="openConnectorsInfo()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 3v6M15 3v6M6 9h12l-1 5a5 5 0 0 1-10 0Z"/><path d="M12 17v4"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Connectors</div><div class="settings-item-sub">Manage integrations</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" onclick="openAppearance()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><circle cx="9" cy="9.5" r="1"/><circle cx="15" cy="9.5" r="1"/><circle cx="9" cy="14.5" r="1"/><path d="M15 14.5a1 1 0 1 1-2 0"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Appearance</div><div class="settings-item-sub">Color mode, font style</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" style="cursor:default">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Haptic feedback</div></div>
              <div class="settings-toggle on" id="haptic-toggle" onclick="toggleHaptic(event)"><div class="settings-toggle-knob"></div></div>
            </div>
            <div class="settings-item" onclick="openQuietHours()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 12.5A9 9 0 1 1 11.5 3 7 7 0 0 0 21 12.5Z"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Time & focus</div><div class="settings-item-sub">Manage reminders & focus</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" onclick="openPrivacy()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2 4 5v6c0 5 3.5 8.5 8 11 4.5-2.5 8-6 8-11V5Z"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Privacy & data</div><div class="settings-item-sub">Control your data & privacy</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" onclick="openNotifications()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Notifications</div><div class="settings-item-sub">Manage alerts & updates</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
          </div>

          <div class="settings-section-label">Support</div>
          <div class="settings-group">
            <div class="settings-item" onclick="openHelpCenter()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 0 1 5 0c0 1.5-2.5 2-2.5 3.5"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Help center</div><div class="settings-item-sub">FAQs & guides</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
            <div class="settings-item" onclick="openFeedback()">
              <div class="settings-item-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></div>
              <div class="settings-item-text"><div class="settings-item-title">Feedback</div><div class="settings-item-sub">Share your thoughts</div></div>
              <svg class="settings-item-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>
            </div>
          </div>

          <button class="settings-logout-btn" onclick="closeSettings();signOut()">Log out</button>
        </div>'''

do_regex(r'<div class="settings-body">.*?Log out</button>\s*</div>', new_body, "settings-body")

# ─────────────────────────────────────────────
# 3. Update openSettings() to fill the account avatar too
# ─────────────────────────────────────────────
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
  const avEl = document.getElementById('settings-account-avatar');
  if(avEl && currentUser) avEl.textContent = currentUser.initials || '?';""",
    "open-settings-avatar")

# ─────────────────────────────────────────────
# 4. Add favorite star to sidebar chat items
# ─────────────────────────────────────────────
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
  const container = document.getElementById('sidebar-chats');
  if(chatHistory.length===0){ container.innerHTML='<div style="padding:10px 12px;font-size:.8rem;color:var(--fg3)">No chats yet</div>'; return; }
  container.innerHTML = chatHistory.map(ch=>`
    <button class="chat-item${ch.id===activeChatId?' active':''}" onclick="loadChat('${ch.id}')" style="position:relative">
      <svg class="chat-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
      <span class="chat-item-text">${ch.title}</span>
      <span class="chat-item-time">${ch.time}</span>
      <button class="fav-star-btn${ch.favorite?' active':''}" onclick="toggleFavorite('${ch.id}', event)" title="Favorite">
        <svg viewBox="0 0 24 24" fill="${ch.favorite?'currentColor':'none'}" stroke="currentColor" stroke-width="2"><polygon points="12 2 15 9 22 9.5 17 14.5 18.5 22 12 18 5.5 22 7 14.5 2 9.5 9 9"/></svg>
      </button>
      <span onclick="deleteChat('${ch.id}', event)" style="margin-left:2px;padding:2px 6px;color:var(--fg3);cursor:pointer;font-size:.85rem" title="Delete chat">&times;</span>
    </button>`).join('');
}
function toggleFavorite(id, evt){
  if(evt) evt.stopPropagation();
  const ch = chatHistory.find(c=>c.id===id);
  if(!ch) return;
  ch.favorite = !ch.favorite;
  persistChatHistory();
  renderSidebarChats();
}'''

do_replace(old_render, new_render, "render-sidebar-chats")

# ─────────────────────────────────────────────
# 5. New JS: Favorites / History / Appearance / Notifications / Help / Feedback
# ─────────────────────────────────────────────
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

/* ══════════════ FAVORITES (real — reads/writes actual chat history) ══════════════ */
function openFavorites(){
  const favs = chatHistory.filter(c=>c.favorite);
  const rows = favs.length
    ? favs.map(c=>`<div class="fav-list-item" onclick="closeSettingsModal();closeSettings();loadChat('${c.id}')">
        <svg viewBox="0 0 24 24" fill="currentColor" style="width:14px;height:14px;color:#f59e0b;flex-shrink:0"><polygon points="12 2 15 9 22 9.5 17 14.5 18.5 22 12 18 5.5 22 7 14.5 2 9.5 9 9"/></svg>
        <span style="font-size:.88rem">${c.title}</span>
      </div>`).join('')
    : `<p style="font-size:.85rem;color:var(--fg3)">No favorites yet — tap the star on any chat in the sidebar to add one.</p>`;
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Favorites</h3>
    ${rows}
  `);
}

/* ══════════════ HISTORY (real — reuses sidebar) ══════════════ */
function openHistoryPanel(){
  closeSettings();
  const sb = document.getElementById('sidebar');
  if(window.innerWidth <= 768){
    sb.classList.add('open');
    document.getElementById('sidebar-overlay').classList.add('open');
    document.getElementById('sidebar-close-btn').style.display = 'flex';
  } else if(sb.style.display === 'none'){
    toggleSidebar();
  }
}

/* ══════════════ APPEARANCE (real — merges color mode + font) ══════════════ */
function openAppearance(){
  const isLight = document.documentElement.getAttribute('data-theme') === 'light';
  const current = localStorage.getItem('evx-font') || 'default';
  const fontRows = Object.keys(FONT_OPTIONS).map(k =>
    `<div class="settings-font-opt${k===current?' active':''}" onclick="applyFont('${k}');openAppearance()">
      <span style="font-family:${FONT_OPTIONS[k].stack}">${FONT_OPTIONS[k].label}</span>
      <span>${k===current?'✓':''}</span>
    </div>`).join('');
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Appearance</h3>
    <div class="settings-modal-row">
      <label style="display:flex;align-items:center;justify-content:space-between">Dark mode
        <input type="checkbox" ${!isLight?'checked':''} onchange="toggleTheme();openAppearance()"/>
      </label>
    </div>
    <div class="settings-modal-row"><label>Font style</label>${fontRows}</div>
  `);
}

/* ══════════════ NOTIFICATIONS (real — uses installed @capacitor/local-notifications) ══════════════ */
async function openNotifications(){
  const enabled = localStorage.getItem('evx-notify-enabled') === '1';
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Notifications</h3>
    <div class="settings-modal-row">
      <label style="display:flex;align-items:center;justify-content:space-between">Enable reminders
        <input type="checkbox" ${enabled?'checked':''} onchange="toggleNotifications(this.checked)"/>
      </label>
    </div>
    <button class="settings-modal-btn secondary" onclick="sendTestNotification()">Send test notification</button>
  `);
}
async function toggleNotifications(val){
  const { LocalNotifications } = (window.Capacitor && window.Capacitor.Plugins) || {};
  if(!LocalNotifications){ toast('Notifications plugin not available in this build'); return; }
  if(val){
    const perm = await LocalNotifications.requestPermissions();
    if(perm.display !== 'granted'){ toast('Permission denied'); return; }
  }
  localStorage.setItem('evx-notify-enabled', val ? '1':'0');
  toast(val ? 'Notifications enabled' : 'Notifications disabled');
}
async function sendTestNotification(){
  const { LocalNotifications } = (window.Capacitor && window.Capacitor.Plugins) || {};
  if(!LocalNotifications){ toast('Notifications plugin not available in this build'); return; }
  const perm = await LocalNotifications.checkPermissions();
  if(perm.display !== 'granted'){
    const req = await LocalNotifications.requestPermissions();
    if(req.display !== 'granted'){ toast('Permission denied'); return; }
  }
  await LocalNotifications.schedule({ notifications: [{
    title: 'ECLIPSEVEX AI',
    body: 'This is a test notification.',
    id: Date.now() % 100000,
    schedule: { at: new Date(Date.now() + 2000) },
  }]});
  toast('Test notification scheduled');
}

/* ══════════════ HELP CENTER (real — static FAQ, no backend needed) ══════════════ */
function openHelpCenter(){
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Help center</h3>
    <div style="font-size:.85rem;color:var(--fg3);line-height:1.6">
      <p style="margin-bottom:10px"><strong style="color:var(--fg)">How do I start a new chat?</strong><br/>Tap "New Chat" from Quick Access or the sidebar.</p>
      <p style="margin-bottom:10px"><strong style="color:var(--fg)">How do I attach a photo?</strong><br/>Tap the + button next to the message box.</p>
      <p><strong style="color:var(--fg)">How do I delete my data?</strong><br/>Go to Privacy & data → Clear all chat history.</p>
    </div>
  `);
}

/* ══════════════ FEEDBACK (real — opens native email client) ══════════════ */
function openFeedback(){
  openSettingsModal(`
    <button class="settings-modal-close" onclick="closeSettingsModal()">&times;</button>
    <h3>Feedback</h3>
    <div class="settings-modal-row">
      <label>Your message</label>
      <textarea id="feedback-text" rows="4" style="padding:10px 12px;border-radius:10px;background:var(--surface2);border:1px solid var(--border2);color:var(--fg);font-size:.9rem;font-family:inherit;resize:vertical" placeholder="What's on your mind?"></textarea>
    </div>
    <button class="settings-modal-btn" onclick="sendFeedback()">Send via email</button>
  `);
}
function sendFeedback(){
  const msg = document.getElementById('feedback-text').value.trim();
  if(!msg){ toast('Write something first'); return; }
  const subject = encodeURIComponent('ECLIPSEVEX AI Feedback');
  const body = encodeURIComponent(msg + '\\n\\n— from ' + (currentUser ? currentUser.name : 'a user'));
  window.location.href = `mailto:hello@eclipsevex.ai?subject=${subject}&body=${body}`;
  closeSettingsModal();
}
