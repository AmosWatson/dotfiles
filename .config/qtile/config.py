from typing import List

from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy

import os, subprocess

mod = "mod4"
terminal = "alacritty"

keys = [
    # System Controls
    Key([mod, "control"], "r", lazy.restart(), 
        desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), 
        desc="Shutdown qtile"),
    Key([mod], "Tab", lazy.next_layout(), 
        desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), 
        desc="Kill focused window"),


    # monadtall Bindings
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(),
        desc="Expand master window (monadtall)"),
    Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(),
        desc="Expand master window (monadtall)"),
    Key([mod, "shift"], "space", lazy.layout.flip(),
        desc="Switch Master Window Side"),

    # max Bindings
    Key([mod], "j", lazy.layout.up(),
        desc="Switch Master Window Side"),

    Key([mod], "k", lazy.layout.down(),
        desc="Switch Master Window Side"),

    # Volume Controls
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 1%+"),
        desc="Volume Up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 1%-"),
        desc="Volume Down"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master 1+ toggle"),
        desc="Volumue Mute Toggle"),

    # Terminal Launch
    Key([mod], "Return", lazy.spawn("alacritty"), 
        desc="Launch terminal"),
    Key([mod], "t", lazy.spawn("st"),
        desc="Launch st Terminal"),

    # # Dmenu
    # Key([mod, "shift"], "Return", lazy.spawn("dmenu_run"),
    #     desc="Dmenu Launcher"),

    # Rofi Launcher
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show run"),
        desc="Rofi Launcher"),
    
    # Rofi Emojis
    # Key([mod, "shift"], "e", lazy.spawn("rofi -show emoji -modi emoji"),
    #     desc="Rofi emoji"),

    # Program Launchers

    # DOOM EMACS
    Key([mod], "e", lazy.spawn("emacs"),
        desc="Launch Emacs"),

    # File Manager - Vifm
    Key([mod], "f", lazy.spawn("alacritty -e vifm"),
        desc="Launch File Manager"),

    # Qutebrowser
    Key([mod], "w", lazy.spawn("qutebrowser"),
        desc="Launch qutebrowser"),

    # Brave Browser
    Key([mod], "b", lazy.spawn("brave"),
        desc="Launch Brave Browser"),

    # File Manager - pcmanfm
    # Key([mod, "shift"], "f", lazy.spawn("pcmanfm"),
    #     desc="Launch pcmanfm File Manager"),
    # File Manager - nemo
    Key([mod, "shift"], "f", lazy.spawn("nemo"),
        desc="Launch nemo File Manager"),

    # Steam
    Key([mod, "shift"], "g", lazy.spawn("steam"),
        desc="Launch steam"),
    # Spotify 
    Key([mod, "shift"], "m", lazy.spawn("spotify"),
        desc="Launch spotify"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 1,
                "margin": 12,
                "border_focus": "c1f9f4",
                "border_normal": "000000",
               }
        
layouts = [
    # layout.Bsp(**layout_theme),
    # layout.Columns(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.Stack(num_stacks=3, margin=10, border_focus='#c1f9f4', border_normal='#000000'),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
]

# colors = [["#000000", "#000000"],
#           ["#B19CD9", "#B19CD9"], 
#           ["#ff8b94", "#ff8b94"], 
#           ["#ffaaa5", "#ffaaa5"], 
#           ["#ffd3b6", "#ffd3b6"], 
#           ["#dcedc1", "#dcedc1"], 
#           ["#a8e6cf", "#a8e6cf"]]

widget_defaults = dict(
    # font='Droid Sans Mono',
    font='Ubuntu Mono',
    fontsize=15,
    padding=0,
    background='#222222',
    foreground='#aaaaaa',
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                # Shows WorkSpaces
                widget.GroupBox(
                    disable_drag=True,
                    use_mouse_wheel=False,
                    highlight_method='block',
                    this_current_screen_border='#535d6c',
                    rounded=False,
                    active='#aaaaaa',
                ),

                # Current Layout Mode
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                widget.CurrentLayout(
                ),

                # Focused Window Name
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                widget.WindowName(
                    foreground='#ffffff',
                ),

                ####################
                # MID POINT
                ####################

                # Crypto Price
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                widget.GenPollText(
                    update_interval=600,
                    func=lambda: subprocess.check_output("/home/amos/scripts/crypto").decode('utf-8').strip(),
                ),

                # Package Updates
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                # widget.CheckUpdates(
                #     distro='Arch_checkupdates',
                #     no_update_string='Updates: 0',
                #     display_format='Updates: {updates}',
                #     color_no_updates='#aaaaaa',
                #     color_have_updates='#aaaaaa',
                # ),
                widget.GenPollText(
                    update_interval=3600,
                    func=lambda: subprocess.check_output("/home/amos/scripts/pacupdates").decode('utf-8').strip(),
                ),

                # Memory Usage
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                widget.GenPollText(
                    update_interval=10,
                    func=lambda: subprocess.check_output("/home/amos/scripts/temperature").decode('utf-8').strip(),
                ),

                # Memory Usage
                widget.TextBox (
                    text=' |',
                    foreground='#5e5e5e',
                ),
                widget.Memory(
                    format='{MemUsed: .0f}Mbs',
                ),

                # Volume
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                widget.Volume(
                    fmt='Vol: {}',
                ),

                # Clock
                widget.TextBox (
                    text=' | ',
                    foreground='#5e5e5e',
                ),
                widget.Clock(format='%I:%M %p %a %d %B',
                ),


                # Systray
                widget.TextBox (
                    text=' |',
                    foreground='#5e5e5e',
                ),
                widget.Systray(
                ),
                widget.TextBox (
                    text='|',
                    foreground='#5e5e5e',
                ),
            ],
            22,
        ),
    ),
]

# Drag floating layouts.  
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'csgo_linux64'},
    {'wmclass': 'Cisco AnyConnect Secure Mobility Client'},
    {'wmclass': 'zoom'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'VirtualBox Manager'},
    {'wmclass': 'VirtualBox Machine'},
    {'wmclass': 'VirtualBoxVM'},
    {'wmclass': 'notification'},
    {'wmclass': 'transmission-gtk'},
    {'wmclass': 'minecraft-launcher'},
    {'wmclass': 'splash'},
    {'wmclass': 'Steam'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def startup():
   home = os.path.expanduser('~')
   subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
