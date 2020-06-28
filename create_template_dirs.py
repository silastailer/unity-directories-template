""" Libraries """
import os

"""Base path for unity folder"""
BASE_PATH = "/mnt/c/unity"

"""Dictionary containing best practices folder naming and hierarchy"""
DIRS = {
    "Materials": None,
    "GUI": None,
    "Effects": None,
    "Meshes": [
        "Actors",
        "Structures/Buildings",
        "Props/Plants"
        ],
    "Plugins": None,
    "Audio": None,
    "Character": [
        "Animations",
        "Sprites"
        ],
    "Documents":None,
    "Editor": None,
    "Environment": [
        "Sprites",
        "Tiles"
        ],
    "Mod Assets": [
        "2D Props",
        "Bounce Effect Prefabs",
        "Custom Materials",
        "Environment Sprites Colored",
        "Mod Resources",
        "Particle Prefabs",
        "Powerup Prefabs",
        "Trail Prefabs"
        ],
    "Prefabs": [
        "Actors",
        "Items"
        ],
    "Resources": [
        "Actors",
        "Items"
        ],
    "Scenes": [
        "Cameras",
        "Dynamic Objects",
        "GUI/HUD",
        "GUI/PauseMenu",
        "Levels",
        "TestScenes",
        "Gameplay/Actors",
        "Gameplay/Items",
        "Management",
        "Lights",
        "World/Ground",
        "World/Structure",
        "World/Props"
        ],
    "Scripts": [
        "Core",
        "Gameplay/Actors",
        "Gameplay/Items",
        "Mechanics",
        "Model",
        "UI",
        "View",
        "ThirdParty",
        "Graphics",
        "Framework",
        "GUI"
        ],
    "Textures": None,
    "Tiles": None
}

"""Main Method"""
def main():
    """Get keys and values from dictionary"""
    for basedir, subdirs in DIRS.items():
        try:
            if(subdirs is not None):
                for subdir in subdirs:
                    path = BASE_PATH + "/" + basedir + "/" + subdir
                    os.makedirs(path)
            else:
                path = BASE_PATH + "/" + basedir
                os.makedirs(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

if __name__ == '__main__':
    main()
