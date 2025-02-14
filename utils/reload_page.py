from typing import Callable
import yaml


with open("resources/ptbr.yaml", "r") as f:
    ptbr = yaml.safe_load(f)

def reload_page(self, screen_name: Callable) -> None:
    self.notify(ptbr['notification']['reloading'], timeout=2.0)
    self.push_screen(screen_name)

if __name__ == '__main__':
    reload_page()