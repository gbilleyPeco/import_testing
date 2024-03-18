class Database():
    def __init__(self):
        # The checks we want to perform
        self.check_names = ['CheckOne']
    
    def apply_checks(self):
        import importlib
        import checks
        all_checks = [getattr(checks,i) for i in self.check_names]
        for c in all_checks:
            c().apply_()