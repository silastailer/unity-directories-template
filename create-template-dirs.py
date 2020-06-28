import os;

base_path = "/mnt/c/unity"

dirs = {
    "Audio": None,
    "Character": ["Animations", "Sprites"],
    "Documents":None,
    "Editor": None,
    "Environment": ["Sprites", "Tiles"],
    "Mod Assets": ["2D Props", "Bounce Effect Prefabs", "Custom Materials", "Environment Sprites Colored", "Mod Resources", "Particle Prefabs", "Powerup Prefabs", "Trail Prefabs"],
    "Prefabs": None,
    "Scenes": None,
    "Scripts": ["Core", "Gameplay", "Mechanics", "Model", "UI", "View"],
    "TextMesh Pro": ["Documentation", "Resources", "Sprites"],
    "Tiles": None
}

def main():
    for dir, subdirs in dirs.items():
        try:
            if(subdirs is not None):
                for subdir in subdirs:
                    path = base_path + "/" + dir + "/" + subdir
                    os.makedirs(path)
            else:
                path = base_path + "/" + dir
                os.makedirs(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

if __name__ == '__main__':
    main()