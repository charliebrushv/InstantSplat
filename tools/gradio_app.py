# Patch for HfFolder compatibility with newer huggingface_hub
try:
    from huggingface_hub import HfFolder  # noqa
except ImportError:
    import sys
    from pathlib import Path
    import huggingface_hub
    
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

# Patch for gradio_client schema handling
try:
    import gradio_client.utils
    # Patch the json_schema_to_python_type function to handle non-dict schemas
    original_json_schema = gradio_client.utils.json_schema_to_python_type
    
    def patched_json_schema(schema):
        """Patched version that handles non-dict schemas"""
        if not isinstance(schema, dict):
            return "Any"
        try:
            return original_json_schema(schema)
        except (TypeError, KeyError, ValueError):
            return "Any"
    
    gradio_client.utils.json_schema_to_python_type = patched_json_schema
except Exception:
    pass  # Silently ignore if patching fails

from instant_splat.gradio_ui.multi_img_ui import multi_img_block
import gradio as gr

title = """# InstantSplat: Unofficial Demo of Sparse-view SfM-free Gaussian Splatting in Seconds"""
description1 = """
    <a title="Website" href="https://instantsplat.github.io/" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://www.obukhov.ai/img/badges/badge-website.svg">
    </a>
    <a title="arXiv" href="https://arxiv.org/abs/2403.20309" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://www.obukhov.ai/img/badges/badge-pdf.svg">
    </a>
    <a title="Github" href="https://github.com/pablovela5620/InstantSplat" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://img.shields.io/github/stars/pablovela5620/InstantSplat?label=GitHub%20%E2%98%85&logo=github&color=C8C" alt="badge-github-stars">
    </a>
    <a title="Social" href="https://x.com/pablovelagomez1" target="_blank" rel="noopener noreferrer" style="display: inline-block;">
        <img src="https://www.obukhov.ai/img/badges/badge-social.svg" alt="social">
    </a>
"""
description2 = "Using Rerun to visualize the results of InstantSplat"

with gr.Blocks() as demo:
    gr.Markdown(title)
    gr.Markdown(description1)
    gr.Markdown(description2)
    with gr.Tab(label="Multi Image"):
        multi_img_block.render()

if __name__ == "__main__":
    # Configure for public IP access
    import os
    os.environ["GRADIO_SERVER_NAME"] = "0.0.0.0"
    os.environ["GRADIO_SERVER_PORT"] = "7860"
    
    try:
        # Launch without share to allow direct public IP access
        demo.launch(
            server_name="0.0.0.0",
            server_port=7860,
            share=False,
            show_error=True,
            allowed_paths=["/"]
        )
    except (ValueError, TypeError) as e:
        print(f"Launch error: {e}")
        # Try with share as fallback
        try:
            demo.launch(
                server_name="0.0.0.0",
                server_port=7860,
                share=True,
                show_error=True,
                allowed_paths=["/"]
            )
        except Exception as e2:
            print(f"Fallback launch error: {e2}")
            raise e
