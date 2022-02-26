/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 1;        /* border pixel of windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const unsigned int gappx     = 8;        /* gaps between windows */
static const unsigned int systraypinning = 0;   /* 0: sloppy systray follows selected monitor, >0: pin systray to monitor X */
static const unsigned int systrayonleft = 0;   	/* 0: systray in the right corner, >0: systray on left of status text */
static const unsigned int systrayspacing = 2;   /* systray spacing */
static const int systraypinningfailfirst = 1;   /* 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor*/
static const int showsystray        = 1;     /* 0 means no systray */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const int horizpadbar        = 2;        /* horizontal padding for statusbar */
static const int vertpadbar         = 4;        /* vertical padding for statusbar */
static const char *fonts[]          = { "Ubuntu Mono:size=10" };
static const char dmenufont[]       = "monospace:size=10";
static const char col_gray1[]       = "#222222";
static const char col_gray2[]       = "#444444";
static const char col_gray3[]       = "#bbbbbb";
static const char col_gray4[]       = "#eeeeee";
static const char col_cyan[]        = "#005577";

static const char col_gray[]        = "#aaaaaa";
static const char col_focus[]        = "#535d6c";
static const char col_border[]      = "#c1f9f4";
static const char col_white[]      = "#ffffff";

static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray1 },
	[SchemeSel]  = { col_white, col_focus, col_border },
};

static const char *const autostart[] = {
	"picom", NULL,
	"nm-applet", NULL,
	"dwmblocks", NULL,
	"nitrogen", "--restore", NULL,
	NULL /* terminate */
};

/* tagging */
static const char *tags[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };

static const Rule rules[] = {
	/* class                        instance    title       tags mask     isfloating   fake     monitor */
	{ "Gimp",                       NULL,       NULL,       0,            1,            0,      -1 },
	{ "Steam",                      NULL,       NULL,       0,            1,            0,      -1 },
	{ "Lutris",                     NULL,       NULL,       0,            1,            0,      -1 },
	{ "Nitrogen",                   NULL,       NULL,       0,            1,            0,      -1 },
	{ "Piper",                      NULL,       NULL,       0,            1,            0,      -1 },
	{ "File-roller",                NULL,       NULL,       0,            1,            0,      -1 },
	{ "csgo_linux64",               NULL,       NULL,       0,            1,            0,      -1 },
	{ "file_progress",              NULL,       NULL,       0,            1,            0,      -1 },
	{ "st-vifm",                    NULL,       NULL,       0,            1,            0,      -1 },
	{ "Com.cisco.anyconnect.gui",   NULL,       NULL,       1 << 8,       1,            0,      -1 },
	{ "zoom",                       NULL,       NULL,       0,            1,            0,      -1 },
};

/* layout(s) */
static const float mfact     = 0.5; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */


/*
static const Layout layouts[] = {
	{ "[]=",      tile },
	{ "><>",      NULL },
	{ "[M]",      monocle },
	{ "|||",      col },
};
*/

static const Layout layouts[] = {
	{ "| tile |",      tile },
	{ "| column |",    col },
	{ "| monocle |",   monocle },
	{ "| floating |",  NULL },
};

/* key definitions */
#define MODKEY Mod4Mask
#define TAGKEYS(KEY,TAG) \
	{ MODKEY,                       KEY,      view,           {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ShiftMask,             KEY,      tag,            {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} },

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

#define XF86XK_AudioLowerVolume	0x1008FF11   /* Volume control down        */
#define XF86XK_AudioMute	    0x1008FF12   /* Mute sound from the system */
#define XF86XK_AudioRaiseVolume	0x1008FF13   /* Volume control up          */

/* Application Commands */
static char dmenumon[2] = "0";
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray4, NULL };
static const char *roficmd[] = { "rofi", "-show", "drun", NULL};

static const char *termcmd[]  = { "alacritty", NULL };
static const char *stcmd[]  = { "st", NULL };

static const char *browsercmd[]  = { "brave", NULL };
static const char *filescmd[]  = { "st", "-c", "st-vifm", "-e", "vifm", "/home/amos", NULL };
static const char *emacscmd[]  = { "emacs", NULL };
static const char *nemocmd[]  = { "nemo", NULL };
static const char *steamcmd[]  = { "steam", NULL };
static const char *spotifycmd[]  = { "spotify", NULL };

/* Scripts */
static const char *screenshot[]   = { "screenshot", NULL };
static const char *emojicmd[] = { "rofi", "-show", "emoji", "-modi", "emoji", NULL};

static const char *upvol[]   = { "volup", NULL };
static const char *downvol[]   = { "voldown", NULL };
static const char *mutevol[]   = { "volmute", NULL };

static Key keys[] = {
	/* modifier                     key        function        argument */

    /* Rofi and Dmenu Launcher */
	{ MODKEY|ShiftMask,             XK_Return, spawn,          {.v = roficmd } },
	{ MODKEY,                       XK_p,      spawn,          {.v = dmenucmd } },

    /* Launch Applications */
	{ MODKEY,                       XK_Return, spawn,          {.v = termcmd } },
	{ MODKEY|ShiftMask,             XK_t,      spawn,          {.v = stcmd } },
	{ MODKEY,                       XK_b,      spawn,          {.v = browsercmd } },
	{ MODKEY|ShiftMask,             XK_m,      spawn,          {.v = spotifycmd } },
	{ MODKEY|ShiftMask,             XK_g,      spawn,          {.v = steamcmd } },
	{ MODKEY,                       XK_f,      spawn,          {.v = filescmd } },
	{ MODKEY|ShiftMask,             XK_f,      spawn,          {.v = nemocmd } },
	{ MODKEY,                       XK_e,      spawn,          {.v = emacscmd } },

    /* Quit Application */
	{ MODKEY,                       XK_q,      killclient,     {0} },

    /* Scripts */
	{ MODKEY|Mod1Mask,              XK_e,      spawn,          {.v = emojicmd } },
	{ MODKEY|Mod1Mask,              XK_s,      spawn,          {.v = screenshot } },

    /* Volume Keys */
	{ 0,           XF86XK_AudioLowerVolume,    spawn,          {.v = downvol } },
	{ 0,           XF86XK_AudioRaiseVolume,    spawn,          {.v = upvol } },
	{ 0,           XF86XK_AudioMute,           spawn,          {.v = mutevol } },


    /* Modifying your Layout */
	{ MODKEY,                       XK_j,      focusstack,     {.i = +1 } },
	{ MODKEY,                       XK_k,      focusstack,     {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_j,      rotatestack,    {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_k,      rotatestack,    {.i = -1 } },
	{ MODKEY,                       XK_i,      incnmaster,     {.i = +1 } },
	{ MODKEY,                       XK_d,      incnmaster,     {.i = -1 } },
	{ MODKEY,                       XK_h,      setmfact,       {.f = -0.05} },
	{ MODKEY,                       XK_l,      setmfact,       {.f = +0.05} },
	/*{ MODKEY,                       XK_Return, zoom,           {0} },*/
	/*{ MODKEY,                       XK_Tab,    view,           {0} },*/

    /* Layouts */
	{ MODKEY,		                XK_Tab,    cyclelayout,    {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_Tab,    cyclelayout,    {.i = -1 } },
	/*{ MODKEY,                       XK_t,      setlayout,      {.v = &layouts[0]} },
	{ MODKEY,                       XK_f,      setlayout,      {.v = &layouts[1]} },
	{ MODKEY,                       XK_m,      setlayout,      {.v = &layouts[2]} },
	{ MODKEY,                       XK_c,      setlayout,      {.v = &layouts[3]} },*/
	{ MODKEY,                       XK_space,  setlayout,      {0} },
	{ MODKEY|ShiftMask,             XK_space,  togglefloating, {0} },
	{ MODKEY,                       XK_0,      view,           {.ui = ~0 } },
	{ MODKEY|ShiftMask,             XK_0,      tag,            {.ui = ~0 } },
	{ MODKEY|Mod1Mask,              XK_b,      togglebar,      {0} },

    /* Monitor Manipulation */
	{ MODKEY,                       XK_comma,  focusmon,       {.i = -1 } },
	{ MODKEY,                       XK_period, focusmon,       {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_comma,  tagmon,         {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_period, tagmon,         {.i = +1 } },

    /* Gaps */
	{ MODKEY,                       XK_minus,  setgaps,        {.i = -1 } },
	{ MODKEY,                       XK_equal,  setgaps,        {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_equal,  setgaps,        {.i = 0  } },

	TAGKEYS(                        XK_1,                      0)
	TAGKEYS(                        XK_2,                      1)
	TAGKEYS(                        XK_3,                      2)
	TAGKEYS(                        XK_4,                      3)
	TAGKEYS(                        XK_5,                      4)
	TAGKEYS(                        XK_6,                      5)
	TAGKEYS(                        XK_7,                      6)
	TAGKEYS(                        XK_8,                      7)
	TAGKEYS(                        XK_9,                      8)

	{ MODKEY|ControlMask,           XK_q,      quit,           {0} },
	{ MODKEY|ControlMask,           XK_r,      quit,           {1} },
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
	{ ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,          0,              Button2,        zoom,           {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};
