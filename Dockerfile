FROM nerfstudio/nerfstudio
WORKDIR /workspace/
USER root
# Install git
RUN apt-get update && apt-get install -y git
# Install pixi
RUN curl -fsSL https://pixi.sh/install.sh | bash
# Add pixi to PATH
ENV PATH="/root/.pixi/bin:${PATH}"
# Clone the repository and run the application
COPY . /workspace/InstantSplat
WORKDIR /workspace/InstantSplat
# Download MASt3R model checkpoint
RUN mkdir -p mast3r/checkpoints/ && \
    wget https://download.europe.naverlabs.com/ComputerVision/MASt3R/MASt3R_ViTLarge_BaseDecoder_512_catmlpdpt_metric.pth -P mast3r/checkpoints/
EXPOSE 7860
RUN pixi install 
CMD ["pixi", "run", "--environment", "default", "app"]