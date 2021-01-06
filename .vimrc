call plug#begin('~/.vim/plugged')

    " Colorschemes
    Plug 'sainnhe/sonokai',
    Plug 'joshdick/onedark.vim',
    Plug 'senran101604/neotrix.vim'
    Plug 'ajmwagar/vim-deus'

    " Statusbar
    Plug 'itchyny/lightline.vim',
        
call plug#end()

set nu
set nowrap
set smartindent
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set colorcolumn=80

" Tab Changes
set tabstop=4
set shiftwidth=4
set expandtab

" Color Scheme
syntax on
colorscheme sonokai
