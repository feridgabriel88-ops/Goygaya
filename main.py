import flet as ft

def main(page: ft.Page):
    page.title = "Göy Qaya - Ağıllı Arıçılıq Asistenti"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20
    
    ACCENT_COLOR = "#FFB300"
    BG_CARD = "#1A2F1A"
    
    header = ft.Container(
        content=ft.Column([
            ft.Text("🐝 GÖY QAYA ARIDARLIQ", size=26, weight=ft.FontWeight.BOLD, color=ACCENT_COLOR),
            ft.Text("Mövqe, İqlim və Yeşik İstiqaməti Təyin Edici Sistem", size=13, italic=True, color="white70"),
            ft.Divider(color=ACCENT_COLOR, thickness=1.5)
        ])
    )
    
    bolge_data = {
        "Laçın (Yaylaq)": {
            "iqlim": "Dağlıq və sərindir. Şimal və şimal-qərb küləkləri güclüdür.",
            "sos": "🚨 QIRMIZI SOS: Gecələr temperatur kəskin düşə bilər. Uçuş dəliklərini daralt!",
            "sos_color": "#4A1515",
            "istiqamet": "🧭 CƏNUB-ŞƏRQƏ BAXMALIDIR! Səbəb: Səhər günəşini tez görüb arılar erkən oyansın."
        },
        "Kəlbəcər (Yaylaq)": {
            "iqlim": "Yüksək dağ iqlimi, qəfil duman və güclü qərb küləkləri xarakterikdir.",
            "sos": "⚠️ SARI SOS: Yüksək rütubət və duman gözlənilir, yeşiklərin havalandırmasını yoxla.",
            "sos_color": "#4A3B15",
            "istiqamet": "🧭 DÜZ CƏNUBA BAXMALIDIR! Səbəb: Dağ daşqınlarından qorunmaq üçün."
        },
        "Aran Bölgəsi (Qışlaq)": {
            "iqlim": "İsti və quru iqlim. Yayda ekstremal istilər, qışda mülayim hava.",
            "sos": "✅ NORMAL: Hava sabitdir. Kölgəlikləri təmin etmək kifayətdir.",
            "sos_color": "#154A1A",
            "istiqamet": "🧭 ŞƏRQƏ VƏ YA ŞİMAL-ŞƏRQƏ BAXMALIDIR! Səbəb: İsti leyis küləklərindən qorunmaq üçün."
        }
    }
    
    iqlim_txt = ft.Text(size=14, color="white")
    sos_txt = ft.Text(size=14, weight=ft.FontWeight.BOLD, color="white")
    istiqamet_txt = ft.Text(size=15, weight=ft.FontWeight.BOLD, color=ACCENT_COLOR)
    
    sos_container = ft.Container(
        content=ft.Column([
            ft.Text("📊 REGİONAL İQLİM VƏ SƏMT TƏYİNATI", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_COLOR),
            iqlim_txt, ft.Divider(color="white24"),
            sos_txt, ft.Divider(color="white24"),
            istiqamet_txt
        ]),
        padding=15, border_radius=10, bgcolor=BG_CARD, visible=False
    )
    
    def bolge_deyisdi(e):
        secilen = bolge_dropdown.value
        if secilen in bolge_data:
            data = bolge_data[secilen]
            iqlim_txt.value = f"🌍 İqlim: {data['iqlim']}"
            sos_txt.value = data['sos']
            sos_container.bgcolor = data['sos_color']
            istiqamet_txt.value = data['istiqamet']
            sos_container.visible = True
            page.update()

    bolge_dropdown = ft.Dropdown(
        label="📍 Arıların Hazırkı Yerləşməsini Seç",
        options=[ft.dropdown.Option("Laçın (Yaylaq)"), ft.dropdown.Option("Kəlbəcər (Yaylaq)"), ft.dropdown.Option("Aran Bölgəsi (Qışlaq)")],
        on_change=bolge_deyisdi, border_color=ACCENT_COLOR
    )
    
    mualice_chk = ft.Checkbox(label="💊 60 Yeşiyin hamısında gənə dərmanı verildi ✅", value=False)
    sire_chk = ft.Checkbox(label="🍯 Şirə və vitamin qidalandırılması tamamlandı ✅", value=False)
    
    tasks_container = ft.Container(
        content=ft.Column([
            ft.Text("📋 GÜNDƏLİK TƏDBİRLƏR PLANLARI", size=16, weight=ft.FontWeight.BOLD, color=ACCENT_COLOR),
            mualice_chk, sire_chk
        ]),
        padding=15, border_radius=10, bgcolor=BG_CARD, margin=ft.margin.only(top=15)
    )
    
    page.add(header, ft.Container(height=15), bolge_dropdown, ft.Container(height=10), sos_container, tasks_container)

ft.app(main)
