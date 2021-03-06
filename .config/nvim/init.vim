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

    " NerdTree
    Plug 'preservim/nerdtree',

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
set mouse=a

" Tab Changes
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab

let mapleader = " "
let g:netrw_banner = 0
let g:netrw_browse_split = 2
let g:netrw_winsize = 25

" Key ReMaps
" NERDTree
nnoremap <C-n> :NERDTree <CR>
nnoremap <C-t> :NERDTreeToggle <CR>
nnoremap <C-f> :NERDTreeFind <CR>


" Split Navigation
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>l :wincmd l<CR>

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

" Exit Vim if NERDTree is the only window left.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() |
    \ quit | endif

" fun! TrimWhitespace()
"     let l:save = winsaveview()
"     keeppatterns %s/\s\+$//e
"     call winrestview(l:save)
" end fun
" 
" augroup desktop
"     autocmd!
"     autocmd BufWritePre * :call TrimWhitespace()
" augroup END
