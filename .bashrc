#
# ~/.bashrc
#

set -o vi

PS1='[\u@\h \W]\$ '
# export PS1=' \W\[\e[01;31m\] ❯\[\e[01;33m\]❯\[\e[01;32m\]❯ \[\e[m\]'

export EDITOR='nvim'
export TERMINAL='st'
export BROWSER='brave'

# Adding my scripts to $PATH
export PATH="$HOME/.local/scripts:$PATH"

# Adding emacs bin to $PATH
export PATH="$HOME/.emacs.d/bin:$PATH"

# Neovim
alias vim='nvim'
alias v='nvim'

# Alacritty Theming
alias at='alacritty-themes'

# Vim quit bash
alias :q='exit'

# Ignore upper and lowercase when TAB completion
bind "set completion-ignore-case on"

# List
alias ls='exa -al --color=always --group-directories-first'
alias la='exa -al --color=always --group-directories-first'

# Config Shortcuts
alias brc='nvim ~/.bashrc'
alias xconf='nvim ~/.xmonad/xmonad.hs'
alias awconf='nvim ~/.config/awesome/rc.lua'
alias qconf='nvim ~/.config/qtile/config.py'
alias vconf='nvim ~/.config/nvim/init.vim'
alias termconf='nvim ~/.config/alacritty/alacritty.yml'

alias todo='nvim ~/Documents/semester2/todo.txt'
alias readinglist='nvim ~/Documents/files/books/readinglist'

# Prompt before removal or overwrite
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# Free command
alias free='free -h'

# scrot alias
alias ss='maim -s ~/Pictures/screenshots/$(date +%s).png'

# Config Git Alias
alias config='/usr/bin/git --git-dir=$HOME/repos/dotfiles/ --work-tree=$HOME'

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"
