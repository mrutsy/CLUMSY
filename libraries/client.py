import os

import system


os.system("clear")
system.Language("system").word("logo").console()
system.Language().word("sub-logo", system.Settings().version(), "").console()

os.system("docker ps")
