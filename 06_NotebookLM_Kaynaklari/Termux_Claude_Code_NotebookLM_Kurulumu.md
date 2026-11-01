# Telefonda (Termux) Claude Code + NotebookLM — Kurulum ve Günlük Kullanım

Bu not, 1 Kasım 2026 gecesi telefonda (Android, Termux) yapılan kurulumun özetidir. Burada hiçbir şifre, çerez ya da token yoktur; olmamalıdır da.

## Günlük kullanım (kurulum bittikten sonra)

| Ne yapmak istiyorum? | Termux'a yaz |
|---|---|
| Claude Code'u hipnoz klasöründe aç | `hipnoz` |
| Son Claude Code konuşmasına devam et | `hipnoz-devam` |
| NotebookLM girişi hâlâ geçerli mi? | `nlm-kontrol` |
| NotebookLM girişini yenile (çerez süresi dolunca) | `nlm-yenile` |

Claude Code'dan çıkmak: `/exit` yaz ya da **CTRL + c**'ye iki kez bas.

**Açılış menüsü:** Termux açılınca bir menü çıkar: **1** = Claude Code (yeni konuşma), **2** = son konuşmaya devam, **3** = NotebookLM girişini yenile, **Enter** = normal terminal. Menü `~/.bashrc` dosyasının sonundaki `HIPNOZ_MENU` bloğundadır.

**Neden widget yok:** Termux Play Store'dan kurulu. Termux:Widget Play Store'da yayında değil; F-Droid'deki sürüm ise Play Store Termux'uyla çalışmıyor (imzalar farklı). Play Store'daki "Termux Tools/Toolbox" gibi uygulamalar resmî değil, kurulmamalı. `~/.shortcuts/` scriptleri ileride widget kurulursa diye duruyor.

### NotebookLM girişi düşerse (`nlm-kontrol` "error" derse)
1. Firefox → notebook.google.com (Masaüstü sitesi açık) → 1-2 dk bekle, sayfayı yenile.
2. Cookie-Editor → listede `__Secure-1PSIDTS` var mı bak → **Export**.
3. Bu sohbete uğramadan Termux'a dön, `nlm-yenile` yaz.
4. ">>> SIMDI JSON'U YAPISTIR" yazısını görünce: uzun bas → Yapıştır → Enter → **CTRL + d**.
5. Sonda `"status": "ok"` görünmeli.

**Güvenlik:** Çerez JSON'u hesabın anahtarıdır. Kimseye (Claude'a da) gönderme, ekran görüntüsü alma. Script, işi bitince dosyayı ve komut geçmişini siler. Bir sorun olursa: Google Hesabı → Güvenlik → Cihazların → Firefox oturumunu kapat.

---

## Kurulumda neler yapıldı (bir daha gerekirse diye)

1. **Paketler:** `pkg install -y python nodejs-lts git ripgrep`, ardından `pip install notebooklm-py`.
2. **NotebookLM girişi:** Telefonda `notebooklm login` çalışmaz (Playwright/Chromium yok). Bunun yerine Firefox + Cookie-Editor ile çerezler JSON olarak alınıp `notebooklm auth import-cookies` ile içeri aktarıldı. Bunu `~/imp.sh` scripti yapıyor.
   - Zorunlu çerez `__Secure-1PSIDTS` ancak Firefox'ta **masaüstü sitesi** açıkken ve giriş yaptıktan biraz sonra oluşuyor.
   - Termux'ta yapıştırma, JSON'un başına görünmez karakter ekleyebiliyor; script bunu temizliyor.
3. **Claude Code:** Güncel sürümlerin Android için derlenmiş hali yok. Bu yüzden saf JavaScript olan son sürüm kuruldu:
   `npm install -g @anthropic-ai/claude-code@2.1.112`
   - Otomatik güncelleme kapalı: `~/.bashrc` içinde `export DISABLE_AUTOUPDATER=1`.
   - Sistem ripgrep'i kullanılıyor: `export USE_BUILTIN_RIPGREP=0`.
   - **Güncelleme yapma.** `npm update -g` ya da `claude update` çalıştırırsan kurulum bozulur, Claude Code açılmaz.
4. **Claude Code girişi:** Giriş bağlantısı ekranda birkaç satıra bölünüyor. Tam bağlantıyı almak için: ekrana uzun bas → **More… → Select URL**.
5. **NotebookLM skill'i:** `notebooklm skill install` (Claude Code bunu `~/.claude/skills/notebooklm` altında görür).

### Kalıcı olanlar (her açılışta yeniden yapmana gerek yok)
- Claude Code girişi: `~/.claude/` içinde saklı.
- NotebookLM oturumu: `~/.notebooklm/profiles/default/storage_state.json` (çerezlerin süresi dolunca `nlm-yenile`).
- Kısayollar ve ayarlar: `~/.bashrc`.

### Bilinen sınırlar
- Claude Code 2.1.112 eski bir sürüm; yeni özelliklerin bir kısmı yok. Anthropic eski sürümleri kabul etmemeye başlarsa çalışmaz. O zaman çözüm: Termux içinde `proot-distro` ile Ubuntu kurup güncel sürümü orada çalıştırmak.
- `notebooklm-py` resmî değil; Google arayüzünü değiştirirse bozulabilir. Güncellemek için: `pip install -U notebooklm-py`.

---

## Yeni bir cihaza hızlı kurulum (ör. tablet)

Termux'u kur ve aç. Aşağıdaki iki bloğu **sırayla** yapıştır. Bir blok bitmeden (yani `~ $` geri gelmeden) diğerine geçme.

### Blok A — paketler (5-10 dk)
```
yes | pkg update && yes | pkg upgrade && pkg install -y python nodejs-lts git ripgrep && pip install notebooklm-py && npm install -g @anthropic-ai/claude-code@2.1.112 && notebooklm skill install && echo "=== BLOK A TAMAM ==="
```

### Blok B — ayarlar, kısayollar, menü
```
mkdir -p ~/hipnoz
cat > ~/imp.sh <<'EOF'
clear
echo ">>> SIMDI JSON'U YAPISTIR, sonra Enter, sonra CTRL+d"
cat > ~/c.json
clear
python -c "import re,os,sys;p=os.path.expanduser('~/c.json');s=open(p,errors='ignore').read();m=re.search(r'\[\s*\{',s);m or sys.exit('JSON bulunamadi');open(p,'w').write(s[m.start():s.rfind(']')+1])" && notebooklm auth import-cookies ~/c.json
rm -f ~/c.json ~/.bash_history
notebooklm auth check --test --json
EOF
cat > ~/hipnoz/CLAUDE.md <<'EOF'
# Hipnoz SEP (mobil)
- Dil: Türkçe. Cevaplar kısa ve akıcı olsun.
- Kullanıcı Tıbbi Hipnoz SEP eğitimi alıyor (Medipol, 2026).
- NotebookLM'e `notebooklm` komutuyla eriş (notebooklm skill'i yüklü).
- Giriş hatası olursa kullanıcıya Termux'ta `nlm-yenile` yazmasını söyle.
- Cihazdaki dosyalar: ~/storage/downloads (önce `termux-setup-storage` gerekir).
- Claude Code'u güncelleme (`claude update`, `npm update -g` yasak; Android'de bozulur).
EOF
cat >> ~/.bashrc <<'EOF'
export USE_BUILTIN_RIPGREP=0
export DISABLE_AUTOUPDATER=1
alias hipnoz='cd ~/hipnoz && claude'
alias hipnoz-devam='cd ~/hipnoz && claude -c'
alias nlm-yenile='sh ~/imp.sh'
alias nlm-kontrol='notebooklm auth check --test --json | grep -E "\"status\"|notebook_count" | head -2'
# HIPNOZ_MENU
if [ -z "$HIPNOZ_MENU" ] && [ -t 0 ]; then
  export HIPNOZ_MENU=1
  echo "1) Claude Code  2) Devam et  3) NLM-Yenile  Enter) Terminal"
  read -n1 -p "Secim: " s; echo
  case $s in
    1) cd ~/hipnoz && claude ;;
    2) cd ~/hipnoz && (claude -c || claude) ;;
    3) sh ~/imp.sh ;;
  esac
fi
EOF
termux-setup-storage
echo "=== BLOK B TAMAM — Termux'u kapatip ac ==="
```

Sonra: Termux'u kapatıp aç → **3** (NotebookLM girişi, Firefox + Cookie-Editor ile) → **1** (Claude Code girişi; bağlantıyı **More… → Select URL** ile kopyala).
