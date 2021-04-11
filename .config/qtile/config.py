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
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 2%+"),
        desc="Volume Up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 2%-"),
        desc="Volume Down"),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master 1+ toggle"),
        desc="Volumue Mute Toggle"),

    # Terminal Launch
    Key([mod], "Return", lazy.spawn("alacritty -e fish"), 
        desc="Launch terminal"),

    # Rofi Launcher
    Key([mod, "shift"], "Return", lazy.spawn("rofi -show drun"),
        desc="Rofi Launcher"),
    
    Key([mod, "shift"], "e", lazy.spawn("rofi -show emoji -modi emoji"),
        desc="Rofi emoji"),

    # Program Launchers

    # File Manager - Vifm
    Key([mod], "f", lazy.spawn("alacritty -e vifm"),
        desc="Launch File Manager"),
    # Qutebrowser
    Key([mod], "w", lazy.spawn("qutebrowser"),
        desc="Launch Brave Browser"),
    # Brave Browser
    Key([mod], "b", lazy.spawn("brave"),
        desc="Launch Brave Browser"),
    # File Manager - Nemo
    Key([mod, "shift"], "f", lazy.spawn("nemo"),
        desc="Launch Nemo File Manager"),
]

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": "c1f9f4",
                "border_normal": "000000",
               }
        
layouts = [
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.Tile(**layout_theme),
    layout.Floating(**layout_theme),
]

colors = [["#000000", "#000000"],
          ["#B19CD9", "#B19CD9"], 
          ["#ff8b94", "#ff8b94"], 
          ["#ffaaa5", "#ffaaa5"], 
          ["#ffd3b6", "#ffd3b6"], 
          ["#dcedc1", "#dcedc1"], 
          ["#a8e6cf", "#a8e6cf"]]

widget_defaults = dict(
    font='Droid Sans Mono Bold',
    fontsize=13,
    padding=2,
    background='#222222',
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=10, foreground='#222222'),

                # Shows WorkSpaces
                widget.GroupBox(
                    disable_drag=True,
                    use_mouse_wheel=False,
                    inactive='#949494',
                    spacing=8,
                    highlight_method='block',
                    this_current_screen_border='#227db5',
                ),

                # Focused Window Name
                widget.Sep(
                    padding=10,
                    foreground='#909090',
                    linewidth=0,
                ),
                widget.WindowName(),

                ####################
                # MID POINT
                ####################

                widget.TextBox('',
                    fontsize=24,
                    foreground=colors[6],
                    padding=0,
                ),

                # Current Layout Mode
                widget.Sep(
                    padding=10,
                    background=colors[6],
                    linewidth=0,
                ),
                widget.CurrentLayout(
                    background=colors[6],
                    foreground=colors[0],
                ),
                widget.Sep(
                    padding=10,
                    background=colors[6],
                    linewidth=0,
                ),

                widget.TextBox('',
                    fontsize=24,
                    background=colors[6],
                    foreground=colors[5],
                    padding=0,
                ),

                # Package Updates
                widget.Sep(
                    padding=10,
                    background=colors[5],
                    linewidth=0,
                ),
                widget.TextBox('↻',
                    fontsize=16,
                    background=colors[5],
                    foreground=colors[0],
                ),
                widget.CheckUpdates(
                    distro='Arch_checkupdates',
                    no_update_string='0',
                    display_format='{updates}',
                    background=colors[5],
                    foreground=colors[0],
                    colour_have_updates=colors[0],
                    colour_no_updates=colors[0],
                ),
                widget.Sep(
                    padding=10,
                    background=colors[5],
                    linewidth=0,
                ),

                widget.TextBox('',
                    fontsize=24,
                    background=colors[5],
                    foreground=colors[4],
                    padding=0,
                ),

                # Memory Usage
                widget.Sep(
                    padding=10,
                    background=colors[4],
                    linewidth=0,
                ),
                widget.TextBox('🧠',
                    background=colors[4],
                ),
                widget.Memory(
                    background=colors[4],
                    foreground=colors[0],
                ),
                widget.Sep(
                    padding=10,
                    background=colors[4],
                    linewidth=0,
                ),

                widget.TextBox('',
                    fontsize=24,
                    background=colors[4],
                    foreground=colors[3],
                    padding=0,
                ),
                
                # Volume
                widget.Sep(
                    padding=10,
                    background=colors[3],
                    linewidth=0,
                ),
                widget.TextBox('🔉',
                    background=colors[3],
                ),
                widget.Volume(
                    background=colors[3],
                    foreground=colors[0],
                ),
                widget.Sep(
                    padding=10,
                    background=colors[3],
                    linewidth=0,
                ),

                widget.TextBox('',
                    fontsize=24,
                    background=colors[3],
                    foreground=colors[2],
                    padding=0,
                ),

                # Clock
                widget.Sep(
                    padding=10,
                    background=colors[2],
                    linewidth=0,
                ),
                widget.TextBox('🕐',
                    background=colors[2],
                ),
                widget.Clock(format='%I:%M %p %a %d %B',
                    background=colors[2],
                    foreground=colors[0],
                ),
                widget.Sep(
                    padding=10,
                    background=colors[2],
                    linewidth=0,
                ),

                widget.TextBox('',
                    fontsize=24,
                    background=colors[2],
                    foreground=colors[1],
                    padding=0,
                ),

                # Systray
                widget.Sep(
                    padding=10,
                    background=colors[1],
                    linewidth=0,
                ),
                widget.Systray(
                    background=colors[1],
                ),
                widget.Sep(
                    padding=10,
                    background=colors[1],
                    linewidth=0,
                ),

                # END
                widget.Sep(
                    padding=10,
                    background=colors[1],
                    linewidth=0,
                ),
            ],
            20,
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
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
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
