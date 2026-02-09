"""
Patch to add HfFolder compatibility for newer huggingface_hub versions
"""
import sys

# Try to import and patch HfFolder if it doesn't exist
try:
    from huggingface_hub import HfFolder
except ImportError:
    # If HfFolder doesn't exist, we need to provide it
    import huggingface_hub
    from pathlib import Path
    
    class HfFolder:
        """Compatibility shim for removed HfFolder class"""
        _SUBFOLDER = "huggingface"
        
        @classmethod
        def path_token(cls):
            """Return the path to the token file"""
            from huggingface_hub import HF_HOME
            return Path(HF_HOME) / "token"
        
        @classmethod
        def save_token(cls, token):
            """Save the token"""
            path = cls.path_token()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(token)
        
        @classmethod
        def get_token(cls):
            """Get the token"""
            path = cls.path_token()
            if path.exists():
                return path.read_text().strip()
            return None
        
        @classmethod
        def delete_token(cls):
            """Delete the token"""
            path = cls.path_token()
            if path.exists():
                path.unlink()
    
    # Inject HfFolder into huggingface_hub module
    huggingface_hub.HfFolder = HfFolder
    sys.modules['huggingface_hub'].HfFolder = HfFolder

print("HfFolder compatibility patch applied successfully")
