


with open("core/rx.txt") as install_requires_file:
    install_requires = install_requires_file.read().strip().split("\n")


print(install_requires)

