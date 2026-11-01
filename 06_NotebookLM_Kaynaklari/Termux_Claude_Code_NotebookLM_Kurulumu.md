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
