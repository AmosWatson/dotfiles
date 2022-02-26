call plug#begin('~/.vim/plugged')

    Plug 'sainnhe/sonokai',
    Plug 'morhetz/gruvbox',

    Plug 'lilydjwg/colorizer',
    Plug 'itchyny/lightline.vim',
    Plug 'vifm/vifm.vim',
    Plug 'tpope/vim-fugitive',

call plug#end()

" set guifont=Source Code Pro:h15

set relativenumber
set nu
set smartindent
set noswapfile
set nobackup
set undodir=~/.nvim/undodir
set undofile
set incsearch
set nohlsearch
" set colorcolumn=80
set scrolloff=8
set mouse=a

set path+=**    " Searches current directory recursively
set wildmenu    " Display all matches when tab complete
set clipboard=unnamedplus   "Copy/Paste between vim and other programs

" Tab Changes
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab

let mapleader = " "
let g:netrw_banner = 0
let g:netrw_browse_split = 2
let g:netrw_winsize = 25

" Split Navigation
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>l :wincmd l<CR>

" Vifm
map <leader>vv :Vifm<CR>
map <leader>vs :VsplitVifm<CR>
map <leader>ss :SplitVifm<CR>

" Run current python file
nnoremap <leader>pp :!python %<CR>

" lightline statusBar + theme
set noshowmode
" let g:lightline = { 'colorscheme': 'material', }
let g:lightline = { 'colorscheme': 'jellybeans', }

let g:sonokai_style = 'atlantis'

" ColorScheme
syntax on
" colorscheme sonokai
colorscheme gruvbox
set termguicolors

fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun

augroup MOSS
    autocmd!
    autocmd BufWritePre * : call TrimWhitespace()
augroup END
