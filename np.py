import numpy as np
import matplotlib.pyplot as plt
import os
import re
from tkinter import *
import warnings

warnings.filterwarnings("ignore")

folder_name = 'saved_figures'

if os.path.exists(folder_name):
    print(f"Folder '{folder_name}' exists.")
    os.chdir('saved_figures/')
else:
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")
    os.chdir('saved_figures/')

root = Tk()
root.geometry('320x250')
root.title('Julia set generator')

global m
m=0

global j
j = 0
sectext = Label(root, text=j, font=('Arial',16))
sectext.pack(padx=55, pady=10, anchor='w',side=LEFT)

global i
i = 0
ftext = Label(root, text=i, font=('Arial',16))
ftext.pack(padx=65, pady=5, anchor='e', side=RIGHT)

def upone():
    global j
    j+=0.01 
    j = round(j,3)
    sectext.configure(text=j)
def downone():
    global j
    j-=0.01 
    j = round(j,3)
    sectext.configure(text=j)

def upone2():
    global i
    i+=0.01 
    i = round(i,3)
    ftext.configure(text=i)
def downone2():
    global i
    i-=0.01 
    i = round(i,3)
    ftext.configure(text=i)

def upmore():
    global j
    j+=0.1 
    j = round(j,2)
    sectext.configure(text=j)
def downmore():
    global j
    j-=0.1 
    j = round(j,2)
    sectext.configure(text=j)

def upmore2():
    global i
    i+=0.1 
    i = round(i,2)
    ftext.configure(text=i)
def downmore2():
    global i
    i-=0.1 
    i = round(i,2)
    ftext.configure(text=i)

upButton = Button(root, text='\u2191', command=upone).place(relx=0.32, rely=0.43, anchor='w')
downButton = Button(root, text='\u2193', command=downone).place(relx=0.32, rely=0.54, anchor='w')

upButton2 = Button(root, text='\u2191', command=upone2).place(relx=0.63, rely=0.43, anchor='e')
downButton2 = Button(root, text='\u2193', command=downone2).place(relx=0.63, rely=0.54, anchor='e')

upButton3 = Button(root, text='\u21D1', command=upmore).place(relx=0.01, rely=0.43, anchor='w')
downButton3 = Button(root, text='\u21D3', command=downmore).place(relx=0.01, rely=0.54, anchor='w')

upButton4 = Button(root, text='\u21D1', command=upmore2).place(relx=0.95, rely=0.43, anchor='e')
downButton4 = Button(root, text='\u21D3', command=downmore2).place(relx=0.95, rely=0.54, anchor='e')

vals = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu',
'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r',
'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 
'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn',
'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r',
'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 
'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r',
'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r',
'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 
'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r',
'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar',
'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot',
'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r',
'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r',
'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic',
'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r',
'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted',
'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

strvar = StringVar()
strvar.set( "Accent" )
menu = OptionMenu( root , strvar , *vals ).place(relx=0.47, rely=0.25, anchor='c')


def julia_set(c,X0,N,num_iter):

    x0 = X0[0] 
    x1 = X0[1]
    y0 = X0[2]
    y1 = X0[3]

    x, y = np.meshgrid(np.linspace(x0, x1, N), 
                       np.linspace(y0, y1, N) * 1j)
    z = x + y

    F = np.zeros([N, N])

    for j in range(num_iter):
        z = z ** 2 + c
        index = np.abs(z) <= np.inf
        F[index] = F[index] + 1
    return np.linspace(x0, x1, N), np.linspace(y0, y1, N), F
    

def do():
    x, y, F = julia_set(c = j + i * 1j, num_iter = 200, 
                        N = 1000, X0 = np.array([-1.5, 1.5, -1.5, 1.5]))
    plt.figure(figsize = (10, 10))
    #rdm = random.choice(vals)
    plt.pcolormesh(x, y, F, cmap = strvar.get())
    if i >= 0:
        plt.title(f'colorscheme = {str(strvar.get())}        c = {j} +{i}i')
    else:
        plt.title(f'colorscheme = {str(strvar.get())}        c = {j} {i}i')
    plt.axis('equal')
    plt.axis('off')
    plt.show()
#interesting values: -.69 + .29; -.83 -.23; -0.15 -0.85 ;-0.3 .59; -.9 -.23; -.79 - .15 ; 0.29 - 0 ; -0.29 - 0.7 ; -0 - 1 ; 0 - 0.81 ; -0.2 - 0.87 with z**3; {-0.2 -0.9;-0.2 -0.92} ; 0.3 -0.7

f = os.listdir()

def find_fig_with_max_number(strings_list):
    pattern = r'\bfig(\d+)\b'
    max_number = float('-inf')
    for string in strings_list:
        matches = re.findall(pattern, string)
        for match in matches:
            number = int(match)
            max_number = max(max_number, number)

    return max_number

def save_protocol():
    global max_number
    max_number = find_fig_with_max_number(f)
    if max_number != float('-inf'):
        save_sec()
    else:
        save_init()

def save_sec():
    global max_number
    max_number+=1
    plt.savefig(f'fig{max_number}.png')

def save_init():
    global m
    m+=1
    plt.savefig(f'fig{m}.png')

gobutton = Button(root, text='Go', command=do).place(relx=0.39, rely=0.7, anchor='c')
savebutton = Button(root, text='Save', command=save_protocol).place(relx=0.57,rely=0.7, anchor='c')
root.mainloop()

