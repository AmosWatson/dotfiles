" set runtimepath^=~/.vim runtimepath+=~/.vim/after
" let &packpath = &runtimepath
" source ~/.vimrc

call plug#begin('~/.vim/plugged')
    
    "ColorSchemes
    Plug 'joshdick/onedark.vim',
    Plug 'senran101604/neotrix.vim',
    Plug 'ajmwagar/vim-deus',

    " Statusbar
    Plug 'itchyny/lightline.vim',

call plug#end()

set relativenumber
set nu
set nohlsearch
set nowrap
set smartindent
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set colorcolumn=80
set scrolloff=8

" Tab Changes
set tabstop=4
set shiftwidth=4
set expandtab

" lightline statusBar + theme
set noshowmode
let g:lightline = {
    \ 'colorscheme': 'deus',
    \ }

" Set neotrix contrast, options: retro, retro_hard, galaxy, galaxy_hard
let g:neotrix_dark_contrast = 'retro'

" ColorScheme
syntax on
colorscheme neotrix
set termguicolors
