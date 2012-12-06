import pkg_resources

if __name__ == '__main__':
    for plugin in pkg_resources.iter_entry_points('hola_aol'):
        hello_world = plugin.load()
        hello_world()

