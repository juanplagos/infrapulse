import yaml

with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

def reload_page(self) -> None:
    self.notify(ptbr['notification']['reloading'], timeout=2.0)

if __name__ == '__main__':
    reload_page()