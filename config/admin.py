from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Ishchi, Foydalanuvchi

# ==========================================
#  TIZIM BOSHQARUVI — ZAMONAVIY DIZAYN
# ==========================================
admin.site.site_header = mark_safe('🛡 Tizim Boshqaruvi')
admin.site.site_title = "Tizim Admin"
admin.site.index_title = "Xush kelibsiz"

PREMIUM_CSS = """
<style>
    /* =============================================
       1. ASOSIY FONT VA ANIMATSIYA SOZLAMALARI
    ============================================= */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    *, *::before, *::after {
        transition:
            background-color 0.22s cubic-bezier(0.4, 0, 0.2, 1),
            border-color 0.22s cubic-bezier(0.4, 0, 0.2, 1),
            color 0.22s cubic-bezier(0.4, 0, 0.2, 1),
            transform 0.18s cubic-bezier(0.4, 0, 0.2, 1),
            box-shadow 0.22s cubic-bezier(0.4, 0, 0.2, 1),
            opacity 0.2s ease !important;
    }

    /* Sahifa yuklanganda yuqoridan pastga silliq tushish */
    @keyframes fadeSlideDown {
        from { opacity: 0; transform: translateY(-10px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(0, 113, 227, 0.25); }
        50%       { box-shadow: 0 0 0 6px rgba(0, 113, 227, 0); }
    }

    /* =============================================
       2. RANG PALITASI (CSS O'ZGARUVCHILAR)
    ============================================= */
    :root {
        --blue:          #0071e3;
        --blue-hover:    #0077ed;
        --blue-light:    #e8f0fc;
        --blue-shadow:   rgba(0, 113, 227, 0.22);

        --bg-page:       #f0f2f5;
        --bg-card:       #ffffff;
        --bg-row-alt:    #fbfbfd;
        --bg-hover:      rgba(0, 113, 227, 0.04);

        --text-primary:  #1c1c1e;
        --text-muted:    #86868b;
        --text-light:    #aeaeb2;

        --border:        #e5e5ea;
        --border-soft:   #f2f2f7;

        --header-bg:     #0a0a0f;
        --sidebar-bg:    #ffffff;

        --radius-sm:     8px;
        --radius-md:     12px;
        --radius-lg:     16px;

        --shadow-card:   0 1px 4px rgba(0,0,0,0.04), 0 4px 16px rgba(0,0,0,0.05);
        --shadow-hover:  0 4px 20px rgba(0,0,0,0.09);
        --shadow-btn:    0 1px 3px rgba(0, 113, 227, 0.25);
        --shadow-btn-hover: 0 4px 14px rgba(0, 113, 227, 0.35);
    }

    /* =============================================
       3. ASOSIY FONGA
    ============================================= */
    body, html {
        background-color: var(--bg-page) !important;
        color: var(--text-primary) !important;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
        font-size: 14px !important;
        line-height: 1.55 !important;
        -webkit-font-smoothing: antialiased !important;
    }

    #container, #content, #content-main {
        background-color: var(--bg-page) !important;
    }

    /* =============================================
       4. YUQORI PANEL (HEADER)
    ============================================= */
    #header {
        background: var(--header-bg) !important;
        border-bottom: 1px solid rgba(255,255,255,0.07) !important;
        padding: 0 28px !important;
        height: 54px !important;
        display: flex !important;
        align-items: center !important;
        animation: fadeSlideDown 0.4s ease both !important;
        position: sticky !important;
        top: 0 !important;
        z-index: 100 !important;
    }

    #branding h1 {
        font-size: 16px !important;
        font-weight: 500 !important;
        letter-spacing: -0.01em !important;
        color: #ffffff !important;
    }

    #user-tools {
        font-size: 12.5px !important;
        color: rgba(255,255,255,0.5) !important;
    }
    #user-tools a {
        color: rgba(255,255,255,0.75) !important;
        text-decoration: none !important;
        padding: 4px 8px !important;
        border-radius: var(--radius-sm) !important;
    }
    #user-tools a:hover {
        color: #ffffff !important;
        background: rgba(255,255,255,0.1) !important;
    }

    /* =============================================
       5. CHAP MENYU (SIDEBAR)
    ============================================= */
    #nav-sidebar, .nav-sidebar {
        background: var(--sidebar-bg) !important;
        border-right: 1px solid var(--border) !important;
        padding-top: 12px !important;
    }

    #nav-sidebar .module caption,
    #nav-sidebar th {
        background: transparent !important;
        color: var(--text-light) !important;
        font-size: 10.5px !important;
        font-weight: 600 !important;
        letter-spacing: 0.07em !important;
        text-transform: uppercase !important;
        padding: 12px 16px 5px !important;
    }

    #nav-sidebar td a {
        display: block !important;
        color: var(--text-primary) !important;
        font-size: 13.5px !important;
        padding: 8px 12px !important;
        margin: 2px 8px !important;
        border-radius: var(--radius-sm) !important;
        text-decoration: none !important;
        background: transparent !important;
    }

    #nav-sidebar td a:hover {
        background: var(--bg-page) !important;
        color: var(--blue) !important;
    }

    .current-model td a {
        background: var(--blue-light) !important;
        color: var(--blue) !important;
        font-weight: 500 !important;
    }

    #nav-sidebar tr { background: transparent !important; }

    /* =============================================
       6. BREADCRUMBS
    ============================================= */
    div.breadcrumbs {
        background: var(--bg-card) !important;
        border-bottom: 1px solid var(--border) !important;
        padding: 11px 28px !important;
        font-size: 12.5px !important;
        color: var(--text-muted) !important;
        animation: fadeSlideDown 0.35s ease 0.05s both !important;
    }
    div.breadcrumbs a {
        color: var(--text-muted) !important;
        text-decoration: none !important;
    }
    div.breadcrumbs a:hover { color: var(--blue) !important; }

    /* =============================================
       7. JADVAL BLOKI (CHANGELIST)
    ============================================= */
    #changelist-form {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        box-shadow: var(--shadow-card) !important;
        overflow: hidden !important;
        animation: fadeUp 0.38s ease 0.1s both !important;
    }

    /* Toolbar (qidiruv va tugmalar satri) */
    #toolbar {
        background: var(--bg-card) !important;
        border-bottom: 1px solid var(--border-soft) !important;
        padding: 16px 18px !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
    }

    /* Qidiruv paneli */
    #searchbar {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 7px 13px !important;
        font-size: 13.5px !important;
        font-family: inherit !important;
        background: var(--bg-page) !important;
        color: var(--text-primary) !important;
        min-width: 220px !important;
    }
    #searchbar:focus {
        background: var(--bg-card) !important;
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.14) !important;
        outline: none !important;
    }

    /* Jadval sarlavhalari */
    #result_list thead th {
        background: #fafafa !important;
        color: var(--text-light) !important;
        font-weight: 600 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
        padding: 11px 16px !important;
        border-bottom: 1px solid var(--border-soft) !important;
    }

    /* Jadval qatorlari */
    #result_list tbody tr {
        border-bottom: 1px solid var(--border-soft) !important;
        animation: fadeUp 0.3s ease both !important;
    }
    #result_list tbody tr:nth-child(1) { animation-delay: 0.12s !important; }
    #result_list tbody tr:nth-child(2) { animation-delay: 0.17s !important; }
    #result_list tbody tr:nth-child(3) { animation-delay: 0.22s !important; }
    #result_list tbody tr:nth-child(4) { animation-delay: 0.27s !important; }
    #result_list tbody tr:nth-child(5) { animation-delay: 0.32s !important; }
    #result_list tbody tr:nth-child(6) { animation-delay: 0.37s !important; }

    tr.row1 { background: var(--bg-card) !important; }
    tr.row2 { background: var(--bg-row-alt) !important; }

    tbody tr:hover {
        background: var(--bg-hover) !important;
        transform: translateX(2px) !important;
    }

    #result_list tbody td {
        padding: 12px 16px !important;
        font-size: 13.5px !important;
        color: var(--text-primary) !important;
        border-bottom: none !important;
    }

    #result_list tbody td a {
        color: var(--blue) !important;
        text-decoration: none !important;
        font-weight: 500 !important;
    }
    #result_list tbody td a:hover { text-decoration: underline !important; }

    /* =============================================
       8. TUGMALAR
    ============================================= */
    .button, input[type=submit], input[type=button],
    .submit-row input, .submit-row button {
        background: var(--blue) !important;
        border: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 8px 18px !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
        font-family: inherit !important;
        color: #ffffff !important;
        box-shadow: var(--shadow-btn) !important;
        text-shadow: none !important;
        cursor: pointer !important;
        letter-spacing: -0.01em !important;
    }
    .button:hover, input[type=submit]:hover, input[type=button]:hover {
        background: var(--blue-hover) !important;
        transform: translateY(-1px) scale(1.015) !important;
        box-shadow: var(--shadow-btn-hover) !important;
    }
    .button:active, input[type=submit]:active {
        transform: translateY(0) scale(0.985) !important;
        box-shadow: var(--shadow-btn) !important;
    }
    .button:focus-visible, input[type=submit]:focus-visible {
        animation: pulse 1.5s infinite !important;
    }

    /* "Qo'shish" tugmasi (object-tools) */
    .object-tools a {
        background: var(--blue) !important;
        border-radius: var(--radius-sm) !important;
        padding: 7px 16px !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #ffffff !important;
        text-decoration: none !important;
        box-shadow: var(--shadow-btn) !important;
    }
    .object-tools a:hover {
        background: var(--blue-hover) !important;
        transform: translateY(-1px) !important;
        box-shadow: var(--shadow-btn-hover) !important;
    }

    /* "Bekor qilish" tugmasi */
    .submit-row a.closelink {
        background: transparent !important;
        border: 1px solid var(--border) !important;
        color: var(--text-muted) !important;
        box-shadow: none !important;
        border-radius: var(--radius-sm) !important;
        padding: 7px 16px !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
    }
    .submit-row a.closelink:hover {
        border-color: var(--text-muted) !important;
        color: var(--text-primary) !important;
        transform: none !important;
    }

    /* "O'chirish" tugmasi — qizil */
    .deletelink, input.default.deletelink {
        background: #ff3b30 !important;
        box-shadow: 0 1px 3px rgba(255,59,48,0.3) !important;
    }
    .deletelink:hover {
        background: #e0342a !important;
        box-shadow: 0 4px 14px rgba(255,59,48,0.35) !important;
    }

    /* =============================================
       9. FORMALAR VA INPUT MAYDONLAR
    ============================================= */
    .module {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: var(--shadow-card) !important;
        overflow: hidden !important;
        margin-bottom: 16px !important;
        animation: fadeUp 0.38s ease 0.1s both !important;
    }
    .module h2, .module caption {
        background: #fafafa !important;
        color: var(--text-muted) !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
        padding: 11px 16px !important;
        border-bottom: 1px solid var(--border-soft) !important;
    }

    .form-row {
        padding: 14px 18px !important;
        border-bottom: 1px solid var(--border-soft) !important;
    }
    .form-row:last-child { border-bottom: none !important; }

    label {
        color: var(--text-muted) !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        margin-bottom: 5px !important;
        display: block !important;
    }

    input[type=text], input[type=email], input[type=password],
    input[type=number], input[type=url], textarea, select {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-sm) !important;
        padding: 8px 13px !important;
        font-size: 14px !important;
        font-family: inherit !important;
        background: var(--bg-page) !important;
        color: var(--text-primary) !important;
        width: 100% !important;
        max-width: 500px !important;
    }
    input[type=text]:focus, input[type=email]:focus, input[type=password]:focus,
    input[type=number]:focus, textarea:focus, select:focus {
        background: var(--bg-card) !important;
        border-color: var(--blue) !important;
        box-shadow: 0 0 0 3px rgba(0, 113, 227, 0.13) !important;
        outline: none !important;
    }

    /* =============================================
       10. O'NG TOMONDAGI FILTR
    ============================================= */
    #changelist-filter {
        background: var(--bg-card) !important;
        border-left: 1px solid var(--border) !important;
        border-radius: 0 var(--radius-lg) var(--radius-lg) 0 !important;
        padding-bottom: 12px !important;
    }
    #changelist-filter h2 {
        background: #fafafa !important;
        color: var(--text-light) !important;
        font-size: 10.5px !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.07em !important;
        padding: 11px 16px !important;
        border-bottom: 1px solid var(--border-soft) !important;
        margin: 0 !important;
    }
    #changelist-filter h3 {
        font-size: 12px !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        padding: 12px 16px 6px !important;
        margin: 0 !important;
    }
    #changelist-filter ul { padding: 0 8px !important; margin: 0 !important; list-style: none !important; }
    #changelist-filter li { padding: 2px 0 !important; }
    #changelist-filter li a {
        display: block !important;
        padding: 6px 10px !important;
        border-radius: 7px !important;
        font-size: 13px !important;
        color: var(--text-primary) !important;
        text-decoration: none !important;
    }
    #changelist-filter li a:hover { background: var(--bg-page) !important; color: var(--blue) !important; }
    #changelist-filter li.selected a {
        color: var(--blue) !important;
        font-weight: 500 !important;
        background: var(--blue-light) !important;
    }

    /* =============================================
       11. SUBMIT ROW (SAQLASH PANELI)
    ============================================= */
    .submit-row {
        background: var(--bg-card) !important;
        border-top: 1px solid var(--border) !important;
        border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
        padding: 14px 18px !important;
        display: flex !important;
        gap: 8px !important;
        align-items: center !important;
    }

    /* =============================================
       12. XABARLAR (MESSAGES)
    ============================================= */
    .messagelist {
        padding: 0 28px !important;
        margin-bottom: 16px !important;
        list-style: none !important;
    }
    .messagelist li {
        padding: 12px 16px !important;
        border-radius: var(--radius-sm) !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
        margin-bottom: 8px !important;
        animation: fadeSlideDown 0.35s ease both !important;
    }
    .messagelist li.success {
        background: #e5f8ed !important;
        color: #1d8348 !important;
        border: 1px solid #abebc6 !important;
    }
    .messagelist li.error {
        background: #fce8e6 !important;
        color: #c0392b !important;
        border: 1px solid #f5b7b1 !important;
    }
    .messagelist li.warning {
        background: #fef9e7 !important;
        color: #b7770d !important;
        border: 1px solid #f9e79f !important;
    }

    /* =============================================
       13. PAGINATION
    ============================================= */
    .paginator {
        padding: 14px 18px !important;
        font-size: 13px !important;
        color: var(--text-muted) !important;
        border-top: 1px solid var(--border-soft) !important;
        display: flex !important;
        align-items: center !important;
        gap: 4px !important;
    }
    .paginator a, .paginator span.this-page {
        padding: 5px 11px !important;
        border-radius: 7px !important;
        font-size: 13px !important;
        text-decoration: none !important;
    }
    .paginator a { color: var(--blue) !important; }
    .paginator a:hover { background: var(--blue-light) !important; }
    .paginator span.this-page {
        background: var(--blue) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* =============================================
       14. CHECKBOX VA TANLASH
    ============================================= */
    input[type=checkbox] {
        accent-color: var(--blue) !important;
        width: 15px !important;
        height: 15px !important;
        cursor: pointer !important;
    }

    /* =============================================
       15. INDEX SAHIFASI (BOSH SAHIFA KARTALAR)
    ============================================= */
    .app-auth.module, .app-ishchilar.module {
        border-radius: var(--radius-lg) !important;
        overflow: hidden !important;
        animation: fadeUp 0.38s ease both !important;
    }

    #content-main .module table {
        width: 100% !important;
    }
    #content-main .module table td a {
        font-size: 14px !important;
        color: var(--blue) !important;
        text-decoration: none !important;
        display: block !important;
        padding: 8px 16px !important;
    }
    #content-main .module table td a:hover {
        background: var(--blue-light) !important;
        border-radius: 6px !important;
    }
    #content-main .module table td.addlink a,
    #content-main .module table td.changelink a {
        font-size: 12.5px !important;
        color: var(--text-muted) !important;
    }
    #content-main .module table td.addlink a:hover,
    #content-main .module table td.changelink a:hover {
        color: var(--blue) !important;
        background: transparent !important;
    }

    /* =============================================
       16. SCROLLBAR (ZAMONAVIY STIL)
    ============================================= */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--text-light); }

    /* =============================================
       17. SELECTION VA FOCUS
    ============================================= */
    ::selection { background: rgba(0, 113, 227, 0.15); color: var(--text-primary); }
</style>
"""


class ZamonaviyAdmin(admin.ModelAdmin):
    """Zamonaviy premium CSS'ni har bir sahifaga qo'llash uchun asosiy klass."""

    def changelist_view(self, request, extra_context=None):
        admin.site.site_header = mark_safe(f'🛡 Tizim Boshqaruvi {PREMIUM_CSS}')
        return super().changelist_view(request, extra_context=extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        admin.site.site_header = mark_safe(f'🛡 Tizim Boshqaruvi {PREMIUM_CSS}')
        return super().changeform_view(request, object_id, form_url, extra_context)

    def delete_view(self, request, object_id, extra_context=None):
        admin.site.site_header = mark_safe(f'🛡 Tizim Boshqaruvi {PREMIUM_CSS}')
        return super().delete_view(request, object_id, extra_context)


# ==========================================
# MODELLARNI RO'YXATDAN O'TKAZISH
# ==========================================

@admin.register(Ishchi)
class IshchiAdmin(ZamonaviyAdmin):
    list_display = ('name', 'surname', 'sohasi', 'age', 'created_at')
    search_fields = ('name', 'surname', 'sohasi')
    list_filter = ('sohasi',)
    list_per_page = 25
    ordering = ('-created_at',)


@admin.register(Foydalanuvchi)
class FoydalanuvchiAdmin(ZamonaviyAdmin):
    list_display = ('name', 'surname', 'email', 'age')
    search_fields = ('name', 'surname', 'email')
    list_per_page = 25