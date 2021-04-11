# Amos - Fish Config, ~/.config/fist/config.fish, WM: qtile

set fish_greeting
set TERM "xterm-256color"
set EDITOR "nvim"

# Quit Alias (Fun)
alias :q='exit'

# nvim alias
alias vim='nvim'
alias v='nvim'

# git alias
alias config='/usr/bin/git --git-dir=$HOME/repos/dotfiles --work-tree=$HOME'
# ls aliases
alias ls='exa -al --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'

# navigation
alias ..='cd ..'
alias cd..='cd ..'

# pacman and yay
alias pacman='sudo pacman'
alias pacsyu='sudo pacman -Syu'

# Grep color
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

# Prompt before removal
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# config edit shortcuts
alias qtileconf='vim ~/.config/qtile/config.py'
alias vimconf='vim ~/.config/nvim/init.vim'
alias fishconf='vim ~/.config/fish/config.fish'

nerdfetch
echo ''
