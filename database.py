class Database():
    def __init__(self):
        # The checks we want to perform
        self.check_names = ['CheckOne']
    
    def apply_checks(self):
        import importlib
        checks = [importlib.import_module(f'checks.{i}') for i in self.check_names]
        for c in checks:
            c().apply_()