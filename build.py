# Generates the Solfeggio privacy policy and terms pages (6 languages) for GitHub Pages.
import os, html
LANGS = ['en', 'pl', 'de', 'es', 'fr', 'pt']
NAMES = {'en': 'English', 'pl': 'Polski', 'de': 'Deutsch', 'es': 'Español', 'fr': 'Français', 'pt': 'Português'}
UPDATED = {'en': 'Last updated: November 20, 2026', 'pl': 'Ostatnia aktualizacja: 20 listopada 2026',
           'de': 'Zuletzt aktualisiert: 20. November 2026', 'es': 'Última actualización: 20 de noviembre de 2026',
           'fr': 'Dernière mise à jour : 20 novembre 2026', 'pt': 'Última atualização: 20 de novembro de 2026'}
T = {}
T['en'] = {
 'privacy_title': 'Privacy Policy', 'terms_title': 'Terms of Use',
 'privacy': [
  ('Who we are', 'Solfeggio (“the app”) is published by chocho apps. This policy explains what happens to your information when you use the app on iPhone, iPad or Android.'),
  ('No account, no ads, no tracking', 'The app has no sign-up and contains no advertising, analytics or tracking SDKs. We do not sell or share personal data.'),
  ('Microphone', 'The microphone is used only while you run a Voice Aura Scan or the Mantra Tuner. Audio is analyzed in real time in your device’s memory. It is never recorded, saved or sent anywhere.'),
  ('Data stored on your device', 'Your sessions, streaks, challenges, scan results and settings are stored only on your device. Deleting the app deletes them. We have no server that receives this data.'),
  ('Purchases', 'Subscriptions and one-time purchases are processed by Apple (App Store) or Google (Google Play). To validate purchases we use RevenueCat, which receives an anonymous app user ID and your purchase receipts. We do not receive your name, email address or payment details. RevenueCat’s privacy policy: https://www.revenuecat.com/privacy'),
  ('Notifications', 'Daily reminders are scheduled locally by your device. No push server is involved, and you can turn them off at any time in the app or in your device settings.'),
  ('Children', 'The app is not directed at children under 13 and does not knowingly collect information from them.'),
  ('Changes and contact', 'If this policy changes, the new version will be published on this page with a new date. Questions: https://chocho.io/'),
 ],
 'terms': [
  ('Agreement', 'By downloading or using Solfeggio you agree to these terms. If you got the app from the App Store, Apple’s Licensed Application End User License Agreement also applies: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
  ('Wellness, not medicine', 'Solfeggio is designed for relaxation, meditation and self-reflection. It is not a medical device and does not diagnose, treat, cure or prevent any condition. Talk to a doctor about any health concern.'),
  ('Solfeggio Pro', 'Some features require Solfeggio Pro, available as a yearly subscription with a 7-day free trial, a monthly subscription, or a one-time lifetime purchase. Prices are shown in the app before you buy and may vary by country.'),
  ('Billing and renewal', 'Payment is charged to your Apple Account or Google Play account at confirmation of purchase. Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period; the account is charged for renewal within 24 hours before the period ends. Any unused part of a free trial is forfeited when you buy a subscription.'),
  ('Managing and cancelling', 'You can manage or cancel subscriptions in your App Store account settings or in Google Play › Subscriptions. Refunds are handled by Apple or Google under their policies.'),
  ('Your use', 'Use the app for personal, non-commercial purposes. Don’t copy, resell or reverse-engineer it. Content, sounds and design remain the property of chocho apps and its licensors.'),
  ('Liability', 'The app is provided “as is”. To the extent permitted by law, we are not liable for indirect or consequential damages arising from its use.'),
  ('Changes and contact', 'We may update these terms; the current version is always on this page. Questions: https://chocho.io/'),
 ]}
T['pl'] = {
 'privacy_title': 'Polityka prywatności', 'terms_title': 'Warunki korzystania',
 'privacy': [
  ('Kim jesteśmy', 'Aplikację Solfeggio („aplikacja”) wydaje chocho apps. Ta polityka wyjaśnia, co dzieje się z Twoimi informacjami, gdy korzystasz z aplikacji na iPhonie, iPadzie lub Androidzie.'),
  ('Bez konta, reklam i śledzenia', 'Aplikacja nie wymaga rejestracji i nie zawiera reklam ani narzędzi analitycznych czy śledzących. Nie sprzedajemy ani nie udostępniamy danych osobowych.'),
  ('Mikrofon', 'Mikrofon działa tylko podczas Skanu aury głosu i w Stroiku mantr. Dźwięk jest analizowany na bieżąco w pamięci Twojego urządzenia. Nigdy nie jest nagrywany, zapisywany ani nigdzie wysyłany.'),
  ('Dane na Twoim urządzeniu', 'Sesje, serie, wyzwania, wyniki skanów i ustawienia są przechowywane wyłącznie na Twoim urządzeniu. Usunięcie aplikacji je usuwa. Nie mamy serwera, który odbiera te dane.'),
  ('Zakupy', 'Subskrypcje i zakupy jednorazowe obsługuje Apple (App Store) lub Google (Google Play). Do weryfikacji zakupów używamy RevenueCat, który otrzymuje anonimowy identyfikator użytkownika aplikacji i potwierdzenia zakupów. Nie otrzymujemy Twojego imienia, adresu e-mail ani danych płatniczych. Polityka prywatności RevenueCat: https://www.revenuecat.com/privacy'),
  ('Powiadomienia', 'Codzienne przypomnienia planuje samo urządzenie. Nie korzystamy z serwera powiadomień, a przypomnienia możesz w każdej chwili wyłączyć w aplikacji lub w ustawieniach urządzenia.'),
  ('Dzieci', 'Aplikacja nie jest skierowana do dzieci poniżej 13 lat i świadomie nie zbiera od nich informacji.'),
  ('Zmiany i kontakt', 'Jeśli polityka się zmieni, nowa wersja pojawi się na tej stronie z nową datą. Pytania: https://chocho.io/'),
 ],
 'terms': [
  ('Akceptacja', 'Pobierając lub używając Solfeggio, akceptujesz te warunki. Jeśli aplikacja pochodzi z App Store, obowiązuje też Umowa licencyjna Apple dla aplikacji licencjonowanych: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
  ('Dobre samopoczucie, nie medycyna', 'Solfeggio służy relaksowi, medytacji i autorefleksji. Nie jest wyrobem medycznym i nie diagnozuje, nie leczy ani nie zapobiega żadnym schorzeniom. W sprawach zdrowia skonsultuj się z lekarzem.'),
  ('Solfeggio Pro', 'Niektóre funkcje wymagają Solfeggio Pro, dostępnego jako subskrypcja roczna z 7-dniowym bezpłatnym okresem próbnym, subskrypcja miesięczna lub jednorazowy zakup dożywotni. Ceny są widoczne w aplikacji przed zakupem i mogą się różnić w zależności od kraju.'),
  ('Płatności i odnawianie', 'Płatność jest pobierana z konta Apple lub Google Play w chwili potwierdzenia zakupu. Subskrypcje odnawiają się automatycznie, chyba że zostaną anulowane co najmniej 24 godziny przed końcem bieżącego okresu; opłata za odnowienie jest pobierana w ciągu 24 godzin przed końcem okresu. Niewykorzystana część bezpłatnego okresu próbnego przepada po zakupie subskrypcji.'),
  ('Zarządzanie i anulowanie', 'Subskrypcjami zarządzasz i anulujesz je w ustawieniach konta App Store lub w Google Play › Subskrypcje. Zwroty obsługuje Apple lub Google zgodnie ze swoimi zasadami.'),
  ('Korzystanie', 'Używaj aplikacji do celów osobistych i niekomercyjnych. Nie kopiuj jej, nie odsprzedawaj ani nie poddawaj inżynierii wstecznej. Treści, dźwięki i projekt należą do chocho apps i licencjodawców.'),
  ('Odpowiedzialność', 'Aplikacja jest udostępniana „tak jak jest”. W granicach dozwolonych prawem nie odpowiadamy za szkody pośrednie lub wtórne wynikające z jej używania.'),
  ('Zmiany i kontakt', 'Możemy aktualizować te warunki; aktualna wersja jest zawsze na tej stronie. Pytania: https://chocho.io/'),
 ]}
T['de'] = {
 'privacy_title': 'Datenschutzerklärung', 'terms_title': 'Nutzungsbedingungen',
 'privacy': [
  ('Wer wir sind', 'Solfeggio („die App“) wird von chocho apps herausgegeben. Diese Erklärung beschreibt, was mit deinen Informationen geschieht, wenn du die App auf iPhone, iPad oder Android nutzt.'),
  ('Kein Konto, keine Werbung, kein Tracking', 'Die App braucht keine Registrierung und enthält keine Werbung sowie keine Analyse- oder Tracking-SDKs. Wir verkaufen oder teilen keine personenbezogenen Daten.'),
  ('Mikrofon', 'Das Mikrofon wird nur während eines Stimm-Aura-Scans oder im Mantra-Tuner verwendet. Der Ton wird in Echtzeit im Speicher deines Geräts analysiert. Er wird nie aufgenommen, gespeichert oder irgendwohin gesendet.'),
  ('Daten auf deinem Gerät', 'Sitzungen, Serien, Challenges, Scan-Ergebnisse und Einstellungen werden nur auf deinem Gerät gespeichert. Wenn du die App löschst, werden sie gelöscht. Wir haben keinen Server, der diese Daten empfängt.'),
  ('Käufe', 'Abos und Einmalkäufe werden von Apple (App Store) oder Google (Google Play) abgewickelt. Zur Prüfung der Käufe nutzen wir RevenueCat; es erhält eine anonyme App-Nutzer-ID und deine Kaufbelege. Wir erhalten weder deinen Namen noch deine E-Mail-Adresse oder Zahlungsdaten. Datenschutz bei RevenueCat: https://www.revenuecat.com/privacy'),
  ('Benachrichtigungen', 'Tägliche Erinnerungen plant dein Gerät lokal. Es ist kein Push-Server beteiligt, und du kannst sie jederzeit in der App oder in den Geräteeinstellungen abschalten.'),
  ('Kinder', 'Die App richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine Informationen von ihnen.'),
  ('Änderungen und Kontakt', 'Wenn sich diese Erklärung ändert, erscheint die neue Fassung mit neuem Datum auf dieser Seite. Fragen: https://chocho.io/'),
 ],
 'terms': [
  ('Zustimmung', 'Mit dem Herunterladen oder der Nutzung von Solfeggio stimmst du diesen Bedingungen zu. Wenn du die App aus dem App Store hast, gilt zusätzlich Apples Endbenutzer-Lizenzvertrag für lizenzierte Apps: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
  ('Wohlbefinden, keine Medizin', 'Solfeggio dient der Entspannung, Meditation und Selbstreflexion. Es ist kein Medizinprodukt und diagnostiziert, behandelt, heilt oder verhindert keine Erkrankungen. Wende dich bei gesundheitlichen Fragen an eine Ärztin oder einen Arzt.'),
  ('Solfeggio Pro', 'Einige Funktionen erfordern Solfeggio Pro, erhältlich als Jahresabo mit 7 Tagen kostenloser Testphase, als Monatsabo oder als einmaliger Lifetime-Kauf. Die Preise werden vor dem Kauf in der App angezeigt und können je nach Land variieren.'),
  ('Abrechnung und Verlängerung', 'Die Zahlung wird bei Bestätigung des Kaufs deinem Apple-Account bzw. Google-Play-Konto belastet. Abos verlängern sich automatisch, sofern sie nicht mindestens 24 Stunden vor Ende des aktuellen Zeitraums gekündigt werden; die Verlängerung wird innerhalb von 24 Stunden vor Ende des Zeitraums abgerechnet. Ein ungenutzter Teil der kostenlosen Testphase verfällt beim Kauf eines Abos.'),
  ('Verwalten und kündigen', 'Abos verwaltest und kündigst du in den Einstellungen deines App-Store-Accounts oder unter Google Play › Abos. Erstattungen bearbeiten Apple bzw. Google nach ihren Richtlinien.'),
  ('Nutzung', 'Nutze die App für persönliche, nicht kommerzielle Zwecke. Kopiere, verkaufe oder dekompiliere sie nicht. Inhalte, Klänge und Design bleiben Eigentum von chocho apps und seinen Lizenzgebern.'),
  ('Haftung', 'Die App wird „wie besehen“ bereitgestellt. Soweit gesetzlich zulässig, haften wir nicht für indirekte oder Folgeschäden aus ihrer Nutzung.'),
  ('Änderungen und Kontakt', 'Wir können diese Bedingungen aktualisieren; die aktuelle Fassung steht immer auf dieser Seite. Fragen: https://chocho.io/'),
 ]}
T['es'] = {
 'privacy_title': 'Política de privacidad', 'terms_title': 'Términos de uso',
 'privacy': [
  ('Quiénes somos', 'Solfeggio (“la app”) está publicada por chocho apps. Esta política explica qué ocurre con tu información cuando usas la app en iPhone, iPad o Android.'),
  ('Sin cuenta, sin anuncios, sin rastreo', 'La app no requiere registro y no contiene publicidad ni SDK de análisis o rastreo. No vendemos ni compartimos datos personales.'),
  ('Micrófono', 'El micrófono solo se usa mientras haces un Escaneo del aura de voz o usas el Afinador de mantras. El audio se analiza en tiempo real en la memoria de tu dispositivo. Nunca se graba, se guarda ni se envía a ningún sitio.'),
  ('Datos guardados en tu dispositivo', 'Tus sesiones, rachas, retos, resultados de escaneos y ajustes se guardan solo en tu dispositivo. Si eliminas la app, se eliminan. No tenemos ningún servidor que reciba estos datos.'),
  ('Compras', 'Las suscripciones y compras únicas las procesa Apple (App Store) o Google (Google Play). Para validar las compras usamos RevenueCat, que recibe un ID de usuario anónimo de la app y tus recibos de compra. No recibimos tu nombre, tu correo ni tus datos de pago. Política de privacidad de RevenueCat: https://www.revenuecat.com/privacy'),
  ('Notificaciones', 'Tu dispositivo programa los recordatorios diarios de forma local. No interviene ningún servidor de notificaciones y puedes desactivarlos cuando quieras en la app o en los ajustes del dispositivo.'),
  ('Menores', 'La app no está dirigida a menores de 13 años y no recopila información de ellos de forma consciente.'),
  ('Cambios y contacto', 'Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha. Preguntas: https://chocho.io/'),
 ],
 'terms': [
  ('Aceptación', 'Al descargar o usar Solfeggio aceptas estos términos. Si obtuviste la app en el App Store, también se aplica el Contrato de licencia de usuario final de Apple para apps con licencia: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
  ('Bienestar, no medicina', 'Solfeggio está pensada para la relajación, la meditación y la autorreflexión. No es un dispositivo médico y no diagnostica, trata, cura ni previene ninguna afección. Consulta a un médico ante cualquier problema de salud.'),
  ('Solfeggio Pro', 'Algunas funciones requieren Solfeggio Pro, disponible como suscripción anual con 7 días de prueba gratis, suscripción mensual o compra única de por vida. Los precios se muestran en la app antes de comprar y pueden variar según el país.'),
  ('Cobro y renovación', 'El pago se carga a tu cuenta de Apple o de Google Play al confirmar la compra. Las suscripciones se renuevan automáticamente salvo que se cancelen al menos 24 horas antes del final del periodo actual; la renovación se cobra dentro de las 24 horas previas al final del periodo. La parte no usada de la prueba gratuita se pierde al comprar una suscripción.'),
  ('Gestión y cancelación', 'Puedes gestionar o cancelar las suscripciones en los ajustes de tu cuenta del App Store o en Google Play › Suscripciones. Los reembolsos los gestionan Apple o Google según sus políticas.'),
  ('Uso', 'Usa la app con fines personales y no comerciales. No la copies, revendas ni apliques ingeniería inversa. Los contenidos, sonidos y diseño pertenecen a chocho apps y sus licenciantes.'),
  ('Responsabilidad', 'La app se ofrece “tal cual”. En la medida en que la ley lo permita, no somos responsables de daños indirectos o consecuentes derivados de su uso.'),
  ('Cambios y contacto', 'Podemos actualizar estos términos; la versión vigente está siempre en esta página. Preguntas: https://chocho.io/'),
 ]}
T['fr'] = {
 'privacy_title': 'Politique de confidentialité', 'terms_title': 'Conditions d’utilisation',
 'privacy': [
  ('Qui sommes-nous', 'Solfeggio (« l’app ») est éditée par chocho apps. Cette politique explique ce qu’il advient de tes informations lorsque tu utilises l’app sur iPhone, iPad ou Android.'),
  ('Sans compte, sans pub, sans suivi', 'L’app ne demande aucune inscription et ne contient ni publicité, ni SDK d’analyse ou de suivi. Nous ne vendons ni ne partageons de données personnelles.'),
  ('Micro', 'Le micro n’est utilisé que pendant un Scan de l’aura vocale ou dans l’Accordeur de mantras. Le son est analysé en temps réel dans la mémoire de ton appareil. Il n’est jamais enregistré, sauvegardé ni envoyé où que ce soit.'),
  ('Données stockées sur ton appareil', 'Tes séances, séries, défis, résultats de scan et réglages sont stockés uniquement sur ton appareil. Supprimer l’app les supprime. Aucun serveur ne reçoit ces données.'),
  ('Achats', 'Les abonnements et achats uniques sont traités par Apple (App Store) ou Google (Google Play). Pour valider les achats, nous utilisons RevenueCat, qui reçoit un identifiant utilisateur anonyme et tes reçus d’achat. Nous ne recevons ni ton nom, ni ton e-mail, ni tes données de paiement. Politique de confidentialité de RevenueCat : https://www.revenuecat.com/privacy'),
  ('Notifications', 'Les rappels quotidiens sont programmés localement par ton appareil. Aucun serveur de notifications n’intervient, et tu peux les désactiver à tout moment dans l’app ou dans les réglages de l’appareil.'),
  ('Enfants', 'L’app ne s’adresse pas aux enfants de moins de 13 ans et ne collecte pas sciemment d’informations les concernant.'),
  ('Modifications et contact', 'Si cette politique change, la nouvelle version sera publiée sur cette page avec une nouvelle date. Questions : https://chocho.io/'),
 ],
 'terms': [
  ('Acceptation', 'En téléchargeant ou en utilisant Solfeggio, tu acceptes ces conditions. Si tu as obtenu l’app sur l’App Store, le Contrat de licence utilisateur final d’Apple pour les apps sous licence s’applique également : https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
  ('Bien-être, pas médecine', 'Solfeggio est conçue pour la détente, la méditation et l’introspection. Ce n’est pas un dispositif médical : elle ne diagnostique, ne traite, ne guérit ni ne prévient aucune affection. Consulte un médecin pour toute question de santé.'),
  ('Solfeggio Pro', 'Certaines fonctions nécessitent Solfeggio Pro, disponible en abonnement annuel avec 7 jours d’essai gratuit, en abonnement mensuel ou en achat unique à vie. Les prix sont affichés dans l’app avant l’achat et peuvent varier selon le pays.'),
  ('Facturation et renouvellement', 'Le paiement est débité de ton compte Apple ou Google Play à la confirmation de l’achat. Les abonnements se renouvellent automatiquement, sauf résiliation au moins 24 heures avant la fin de la période en cours ; le renouvellement est facturé dans les 24 heures précédant la fin de la période. Toute partie inutilisée de l’essai gratuit est perdue à l’achat d’un abonnement.'),
  ('Gérer et résilier', 'Tu peux gérer ou résilier tes abonnements dans les réglages de ton compte App Store ou dans Google Play › Abonnements. Les remboursements sont gérés par Apple ou Google selon leurs règles.'),
  ('Utilisation', 'Utilise l’app à des fins personnelles et non commerciales. Ne la copie pas, ne la revends pas et ne la décompile pas. Les contenus, sons et design appartiennent à chocho apps et à ses concédants.'),
  ('Responsabilité', 'L’app est fournie « en l’état ». Dans les limites permises par la loi, nous ne sommes pas responsables des dommages indirects ou consécutifs liés à son utilisation.'),
  ('Modifications et contact', 'Nous pouvons mettre à jour ces conditions ; la version en vigueur figure toujours sur cette page. Questions : https://chocho.io/'),
 ]}
T['pt'] = {
 'privacy_title': 'Política de privacidade', 'terms_title': 'Termos de uso',
 'privacy': [
  ('Quem somos', 'O Solfeggio (“o app”) é publicado pela chocho apps. Esta política explica o que acontece com suas informações quando você usa o app no iPhone, iPad ou Android.'),
  ('Sem conta, sem anúncios, sem rastreamento', 'O app não exige cadastro e não contém publicidade nem SDKs de análise ou rastreamento. Não vendemos nem compartilhamos dados pessoais.'),
  ('Microfone', 'O microfone só é usado durante um Escaneamento da aura da voz ou no Afinador de mantras. O áudio é analisado em tempo real na memória do seu dispositivo. Ele nunca é gravado, salvo ou enviado para lugar nenhum.'),
  ('Dados salvos no seu dispositivo', 'Suas sessões, sequências, desafios, resultados de escaneamentos e configurações ficam salvos apenas no seu dispositivo. Excluir o app os exclui. Não temos servidor que receba esses dados.'),
  ('Compras', 'Assinaturas e compras únicas são processadas pela Apple (App Store) ou pelo Google (Google Play). Para validar as compras usamos o RevenueCat, que recebe um ID anônimo de usuário do app e seus recibos de compra. Não recebemos seu nome, e-mail nem dados de pagamento. Política de privacidade do RevenueCat: https://www.revenuecat.com/privacy'),
  ('Notificações', 'Os lembretes diários são agendados localmente pelo seu dispositivo. Nenhum servidor de notificações é usado, e você pode desativá-los a qualquer momento no app ou nas configurações do dispositivo.'),
  ('Crianças', 'O app não é direcionado a menores de 13 anos e não coleta intencionalmente informações deles.'),
  ('Alterações e contato', 'Se esta política mudar, a nova versão será publicada nesta página com uma nova data. Dúvidas: https://chocho.io/'),
 ],
 'terms': [
  ('Aceitação', 'Ao baixar ou usar o Solfeggio, você concorda com estes termos. Se você obteve o app na App Store, também se aplica o Contrato de Licença de Usuário Final da Apple para apps licenciados: https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
  ('Bem-estar, não medicina', 'O Solfeggio foi feito para relaxamento, meditação e autorreflexão. Não é um dispositivo médico e não diagnostica, trata, cura nem previne nenhuma condição. Procure um médico para qualquer questão de saúde.'),
  ('Solfeggio Pro', 'Alguns recursos exigem o Solfeggio Pro, disponível como assinatura anual com 7 dias de teste grátis, assinatura mensal ou compra vitalícia única. Os preços aparecem no app antes da compra e podem variar conforme o país.'),
  ('Cobrança e renovação', 'O pagamento é cobrado na sua conta Apple ou Google Play ao confirmar a compra. As assinaturas são renovadas automaticamente, a menos que sejam canceladas pelo menos 24 horas antes do fim do período atual; a renovação é cobrada nas 24 horas anteriores ao fim do período. Qualquer parte não usada do teste grátis é perdida ao comprar uma assinatura.'),
  ('Gerenciar e cancelar', 'Você pode gerenciar ou cancelar assinaturas nos ajustes da sua conta da App Store ou em Google Play › Assinaturas. Reembolsos são tratados pela Apple ou pelo Google conforme suas políticas.'),
  ('Uso', 'Use o app para fins pessoais e não comerciais. Não o copie, revenda nem faça engenharia reversa. Conteúdos, sons e design pertencem à chocho apps e a seus licenciadores.'),
  ('Responsabilidade', 'O app é fornecido “no estado em que se encontra”. Na medida permitida por lei, não nos responsabilizamos por danos indiretos ou consequenciais decorrentes do seu uso.'),
  ('Alterações e contato', 'Podemos atualizar estes termos; a versão atual está sempre nesta página. Dúvidas: https://chocho.io/'),
 ]}
CSS = """:root{--ink:#07060d;--moon:#f4efe6;--gold:#e9cb8e;--mist:#bdb6cc;--card:#14121e}
*{box-sizing:border-box}body{margin:0;background:var(--ink);color:var(--moon);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
main{max-width:720px;margin:0 auto;padding:40px 20px 80px}h1{font-family:Georgia,serif;font-weight:600;font-size:34px;margin:8px 0 4px}
.eyebrow{color:var(--gold);letter-spacing:.2em;font-size:12px;font-weight:600;text-transform:uppercase}.date{color:var(--mist);font-size:14px;margin-bottom:28px}
section{background:var(--card);border:1px solid #ffffff14;border-radius:16px;padding:18px 20px;margin:12px 0}h2{font-size:18px;margin:0 0 6px}
p{margin:0;color:#e6e0d6}a{color:var(--gold);word-break:break-word}nav{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:14px;margin-bottom:24px}
nav a{color:var(--mist);text-decoration:none}nav a.on{color:var(--gold)}"""
import re
def linkify(t):
    return re.sub(r'(https://[^\s]+?)([.,;:)]?(?:\s|$))', lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>{m.group(2)}', html.escape(t, quote=False))
def prefix(lang): return '' if lang == 'en' else lang + '/'
def page(lang, kind):
    t = T[lang]; title = t[kind + '_title']
    depth = '../' * (2 if lang != 'en' else 1)
    nav = ' '.join(f'<a class="{"on" if l == lang else ""}" href="{depth}{prefix(l)}{kind}/">{NAMES[l]}</a>' for l in LANGS)
    other = 'terms' if kind == 'privacy' else 'privacy'
    body = ''.join(f'<section><h2>{html.escape(h)}</h2><p>{linkify(p)}</p></section>' for h, p in t[kind])
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Solfeggio · {html.escape(title)}</title><style>{CSS}</style></head><body><main>
<nav>{nav}</nav><div class="eyebrow">Solfeggio</div><h1>{html.escape(title)}</h1><div class="date">{UPDATED[lang]} · <a href="{depth}{prefix(lang)}{other}/">{html.escape(t[other + "_title"])}</a></div>
{body}</main></body></html>'''
for lang in LANGS:
    for kind in ('privacy', 'terms'):
        d = os.path.join(prefix(lang), kind); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(lang, kind))
open('index.html', 'w', encoding='utf-8').write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=privacy/"><title>Solfeggio</title><a href="privacy/">Privacy Policy</a> · <a href="terms/">Terms of Use</a>')
open('.nojekyll', 'w').write('')
print('ok')
