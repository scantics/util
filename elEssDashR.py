def elEssDashR(root,ext):
    paths = [os.path.join(root,name) for name in os.listdir(root)
             if fnmatch(name,'*.xscade')]
    dirnames = [os.path.join(root,name) for name in os.listdir(root)
                if os.path.isdir(os.path.join(root,name))]
    for directory in dirnames:
        paths += elEssDashR(directory,ext)
    return paths
