/**
 * Material Design 3 Design System - Light Theme
 * Focuses on clean elevation, refined tonal surfaces, and high-readability typography.
 */

const m3 = {
    // Standard M3 Light Mode Palette
    primary: '#6750A4',      // Primary (Deep Purple)
    onPrimary: '#FFFFFF',
    secondary: '#625B71',    // Secondary (Muted Purple)
    onSecondary: '#FFFFFF',
    tertiary: '#7D5260',     // Tertiary (Deep Rose)
    surface: '#FFFBFE',      // Light Surface
    onSurface: '#1C1B1F',
    surfaceVariant: '#E7E0EB',
    onSurfaceVariant: '#49454F',
    outline: '#79747E',
    error: '#B3261E',
    background: '#FFFBFE',
};

const styles = {
    // Global App Container
    app: {
        minHeight: '100vh',
        background: m3.background,
        color: m3.onSurface,
        fontFamily: "'Outfit', sans-serif",
        position: 'relative',
    },

    // Main Content Area
    main: {
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '2rem',
        position: 'relative',
        zIndex: 1,
    },

    // Navigation (Material Top AppBar style)
    nav: {
        position: 'sticky',
        top: 0,
        background: m3.surface,
        borderBottom: `1px solid ${m3.outline}33`,
        zIndex: 100,
    },
    navInner: {
        maxWidth: '1200px',
        margin: '0 auto',
        padding: '0.75rem 2rem',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
    },
    logo: {
        display: 'flex',
        alignItems: 'center',
        gap: '0.75rem',
    },
    logoIcon: {
        fontSize: '1.75rem',
        color: m3.primary,
    },
    logoText: {
        fontSize: '1.5rem',
        fontWeight: '700',
        color: m3.onSurface,
        letterSpacing: '-0.5px',
    },
    navTabs: {
        display: 'flex',
        background: m3.surfaceVariant,
        padding: '4px',
        borderRadius: '100px',
        gap: '4px',
    },
    navTab: {
        background: 'transparent',
        border: 'none',
        color: m3.onSurfaceVariant,
        padding: '0.6rem 1.5rem',
        borderRadius: '100px',
        cursor: 'pointer',
        fontSize: '0.9rem',
        fontWeight: '600',
        display: 'flex',
        alignItems: 'center',
        gap: '0.5rem',
        transition: 'all 0.2s cubic-bezier(0.4, 0, 0.2, 1)',
    },
    navTabActive: {
        background: m3.primary,
        color: m3.onPrimary,
        boxShadow: '0 2px 8px rgba(103, 80, 164, 0.3)',
    },

    // M3 Card System
    card: {
        background: m3.surface,
        borderRadius: '24px',
        padding: '1.5rem',
        border: `1px solid ${m3.outline}22`,
        transition: 'transform 0.2s ease, box-shadow 0.2s ease',
    },
    elevatedCard: {
        background: '#FFFFFF',
        borderRadius: '28px',
        padding: '2rem',
        boxShadow: '0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24)',
        border: `1px solid ${m3.outline}11`,
    },

    // Hero Section
    hero: {
        textAlign: 'center',
        padding: '5rem 0 4rem',
    },
    heroTitle: {
        fontSize: '4rem',
        fontWeight: '800',
        color: m3.onSurface,
        letterSpacing: '-1.5px',
        margin: 0,
        lineHeight: '1.1',
    },
    heroAccent: {
        color: m3.primary,
    },
    heroSubtitle: {
        fontSize: '1.25rem',
        color: m3.onSurfaceVariant,
        marginTop: '1.5rem',
        maxWidth: '650px',
        marginInline: 'auto',
        lineHeight: '1.6',
        fontWeight: '400',
    },

    // Layout Grids
    homeGrid: {
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(380px, 1fr))',
        gap: '2rem',
        marginTop: '2rem',
    },

    // Material 3 Buttons
    primaryBtn: {
        background: m3.primary,
        color: m3.onPrimary,
        border: 'none',
        padding: '1rem 2.5rem',
        borderRadius: '100px',
        fontSize: '1rem',
        fontWeight: '700',
        cursor: 'pointer',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: '0.75rem',
        boxShadow: '0 4px 12px rgba(103, 80, 164, 0.2)',
        transition: 'all 0.2s ease',
    },
    secondaryBtn: {
        background: m3.surfaceVariant,
        color: m3.onSurfaceVariant,
        border: 'none',
        padding: '1rem 2.5rem',
        borderRadius: '100px',
        fontSize: '1rem',
        fontWeight: '700',
        cursor: 'pointer',
        transition: 'all 0.2s ease',
    },

    // Form Elements
    uploadZone: {
        marginTop: '1.5rem',
        padding: '4rem 2rem',
        border: `2px dashed ${m3.outline}44`,
        borderRadius: '24px',
        background: m3.surfaceVariant + '33',
        textAlign: 'center',
        cursor: 'pointer',
        transition: 'all 0.2s ease',
    },

    // Stats and Analytics
    statsGrid: {
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
        gap: '1.5rem',
        marginBottom: '3rem',
    },
    statCard: {
        borderRadius: '28px',
        padding: '2rem',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '0.5rem',
        background: m3.surfaceVariant,
        border: 'none',
    },
    statValue: {
        fontSize: '2.5rem',
        fontWeight: '800',
        color: m3.primary,
        letterSpacing: '-1px',
    },
    statLabel: {
        fontSize: '0.9rem',
        color: m3.onSurfaceVariant,
        fontWeight: '600',
        textTransform: 'uppercase',
        letterSpacing: '1px',
    },

    // Page Header
    pageTitle: {
        fontSize: '2.5rem',
        fontWeight: '800',
        color: m3.onSurface,
        textAlign: 'left',
        marginBottom: '2.5rem',
        display: 'flex',
        alignItems: 'center',
        gap: '1.25rem',
        letterSpacing: '-1px',
    },

    // Components specific to tabs
    howPage: { padding: '2rem 0' },
    analyticsPage: { padding: '2rem 0' },
    aboutPage: { padding: '2rem 0' },
    stepCard: {
        display: 'flex',
        gap: '1.5rem',
        padding: '2rem',
        background: '#FFFFFF',
        borderRadius: '24px',
        marginBottom: '1.5rem',
        alignItems: 'center',
        boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
        border: `1px solid ${m3.outline}11`,
    },

    // Loader
    loaderSpinner: {
        width: '56px',
        height: '56px',
        border: `5px solid ${m3.surfaceVariant}`,
        borderTop: `5px solid ${m3.primary}`,
        borderRadius: '50%',
        animation: 'spin 1s linear infinite',
    },

    // Footer
    footer: {
        marginTop: '6rem',
        padding: '4rem 2rem',
        borderTop: `1px solid ${m3.outline}11`,
        textAlign: 'center',
        background: m3.surface,
    },
    footerText: {
        color: m3.onSurfaceVariant,
        fontSize: '1rem',
        lineHeight: '1.6',
    }
};

export default styles;
export { m3 };
