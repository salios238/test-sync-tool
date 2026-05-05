class VolumeLogger:
    def __init__(self, filename, env):
        self.filename = filename
        self.env = env
    
    def log(self, message):
        print(f"[{self.env}] {message}") # 無料版学習用に出力するだけ