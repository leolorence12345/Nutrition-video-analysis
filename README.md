# Food Tracking and Analysis System

A comprehensive food detection, tracking, and nutrition analysis system using multiple AI models including Gemini, YOLO-World, Grounding DINO, SAM2, and more.

## Live Production API

**GitHub**: https://github.com/leolorence12345/-nutrition-video-analysis  
**Live Demo**: http://18.214.98.110:8000  
**API Docs**: http://18.214.98.110:8000/docs  
**Health Check**: http://18.214.98.110:8000/health

**Production Deployment**: AWS EC2 (t3.xlarge)

## Features

- **Multi-Model Detection**: Support for Gemini, YOLO-World, Grounding DINO, OWL-ViT, Detectron2, and YOLOE
- **Video Tracking**: DeepSORT, ByteTrack, and SAM2-based tracking systems with continuous object IDs
- **Segmentation**: SAM, SAM2, and CLIP-based segmentation methods
- **Live Visualization**: Real-time tracking and detection visualization tools
- **Production API**: FastAPI-based REST API for video analysis (see `deploy/` directory)
- **3D Analysis**: Metric3D integration for depth and volume estimation
- **Nutrition Database**: RAG system with FNDDS and CoFID databases
- **Model Fine-tuning**: Scripts for fine-tuning Grounding DINO on custom food datasets

## Quick Start

### Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set Gemini API key (required for Gemini-based demos)
export GEMINI_API_KEY='your_api_key_here'  # Linux/Mac
$env:GEMINI_API_KEY="your_api_key_here"   # Windows PowerShell
```

### Run Demos

```bash
# Simple food analysis demo
python demos/simple_demo.py

# Video analysis demo
python demos/video_demo.py

# Visualize existing results
python demos/view_visualizations.py

# Compare different detection models
python demos/compare_all_models.py

# Test specific detection methods
python demos/gemini_bbox_detection.py
python demos/grounding_dino_detection.py
python demos/yolo_world_detection.py
python demos/yoloe_detection.py
```

### Core Systems

#### Video Food Analysis System
```bash
# Main video analysis pipeline combining SAM segmentation + tracking + Gemini labeling
python core/video_food_analysis_system.py
```

#### Tracking Systems
- **Gemini-based tracking**: `core/gemini_object_detection_tracking.py`, `core/gemini_segmentation_tracking.py`
- **DeepSORT tracking**: `core/final_deepsort_system.py`, `core/proper_deepsort_tracking.py`
- **ByteTrack integration**: `core/bytetrack_gemini_integration.py`
- **Working systems**: `core/working_gemini_detection_tracking.py`, `core/working_tracking_system.py`

#### Live Visualization
```bash
# Real-time visualization tools
python core/live_bytetrack_visualization.py
python core/live_opencv_visualization.py
python core/live_segmentation_visualization.py
```

#### Model Testing
```bash
# Test various detection models
python scripts/test_owlvit_detection.py
python scripts/test_detectron2_clip.py
python scripts/test_sam_clip.py
python scripts/test_maskrcnn_clip.py
python scripts/test_open_food_detection.py
```

### Production API

The project includes a production-ready API in `deploy/`:

```bash
cd deploy
# See deploy/README.md for full deployment instructions
python run_local.py
```

**Live API**: http://18.214.98.110:8000/docs

## Project Structure

```
Nutrition5k/
├── core/                           # Core tracking and analysis systems
│   ├── video_food_analysis_system.py      # Main video analysis pipeline
│   ├── gemini_object_detection_tracking.py
│   ├── gemini_segmentation_tracking.py
│   ├── simple_gemini_tracking.py
│   ├── simple_gemini_segmentation.py
│   ├── final_deepsort_system.py
│   ├── proper_deepsort_tracking.py
│   ├── bytetrack_gemini_integration.py
│   ├── working_gemini_detection_tracking.py
│   ├── working_tracking_system.py
│   ├── live_bytetrack_visualization.py
│   ├── live_opencv_visualization.py
│   └── live_segmentation_visualization.py
├── demos/                          # Demo scripts and examples
│   ├── simple_demo.py
│   ├── video_demo.py
│   ├── compare_all_models.py
│   ├── comprehensive_model_comparison.py
│   ├── gemini_bbox_detection.py
│   ├── gemini_2_bbox_detection.py
│   ├── grounding_dino_detection.py
│   ├── grounding_dino_hf_detection.py
│   ├── grounding_dino_multi_prompt.py
│   ├── yolo_world_detection.py
│   ├── yolo_world_enhanced.py
│   ├── yoloe_detection.py
│   ├── yoloe_prompt_free.py
│   ├── live_bbox_detection.py
│   ├── live_bbox_with_save.py
│   ├── view_visualizations.py
│   ├── view_analysis_video.py
│   └── visualize_results.py
├── scripts/                        # Utility scripts
│   ├── compute_eval_statistics.py
│   ├── generate_dataset_with_gemini.py
│   ├── generate_grounding_dino_dataset.py
│   ├── finetune_grounding_dino.py
│   ├── finetune_grounding_dino_simple.py
│   ├── finetune_grounding_dino_qlora.py
│   ├── test_owlvit_detection.py
│   ├── test_detectron2_clip.py
│   ├── test_sam_clip.py
│   ├── test_maskrcnn_clip.py
│   ├── test_open_food_detection.py
│   ├── extract_frames.sh
│   └── extract_frames_sampled.sh
├── deploy/                         # Production API deployment
│   ├── app/                        # FastAPI application
│   ├── README.md                   # Deployment guide
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
├── Grounded-SAM-2/                 # Grounded SAM-2 implementation
│   ├── deploy/                     # Alternative deployment location
│   ├── sam2/                       # SAM2 model implementation
│   ├── grounding_dino/             # Grounding DINO implementation
│   └── nutrition_rag_system.py      # RAG system for nutrition data
├── analysis/                       # Analysis and comparison documents
│   ├── methods_comparison.md
│   ├── video_processing_cost_analysis.md
│   ├── gemini_production_cost_analysis.md
│   └── gemini_2.5_flash_3d_volume_estimation.md
├── models/                         # Pre-trained model files
│   ├── cache/
│   ├── grounding_dino_finetuned/
│   └── sam_vit_*.pth
├── data/                           # Dataset files and results
│   ├── food_videos_dataset/        # Food video dataset
│   ├── food101_local/              # Food-101 dataset
│   ├── gemini_food_dataset/        # Gemini-generated annotations
│   ├── food_videos_tracking_results/
│   ├── metric3d_results/
│   └── *_results/                  # Various model results
├── results/                        # Output results and visualizations
├── videos/                         # Video files for analysis
├── res/                            # Resources and sample images
├── requirements.txt                # Python dependencies
├── download_food_dataset.py        # Dataset download utility
├── WHY_DETECTIONS_ARE_WRONG.md     # Model limitations analysis
└── README.md                       # This file
```

## Video Tracking Demo

**Example Tracking Video**: [smart_tracked_WhatsApp Video 2025-09-10 at 05.16.56_9874c762.mp4](./smart_tracked_WhatsApp%20Video%202025-09-10%20at%2005.16.56_9874c762.mp4)

This video demonstrates:
- Food item detection and tracking with continuous IDs
- Segmentation masks for each tracked item
- Frame-by-frame object persistence

Additional tracking results are available in:
- `videos/` - Sample input videos
- `data/food_videos_tracking_results/` - Processed tracking videos
- `data/metric3d_results/` - Videos with depth and volume estimation

## Supported Models

### Detection Models
- **Gemini API**: Google's Gemini for food detection and labeling
- **YOLO-World**: Open-vocabulary object detection
- **YOLOE**: YOLO with enhanced capabilities
- **Grounding DINO**: Open-set object detection
- **OWL-ViT**: Open-vocabulary vision transformer
- **Detectron2**: Facebook's detection framework
- **Mask R-CNN**: Instance segmentation

### Tracking Models
- **DeepSORT**: Multi-object tracking
- **ByteTrack**: High-performance tracking
- **SAM2**: Segment Anything Model 2 for video tracking

### Segmentation Models
- **SAM**: Segment Anything Model
- **SAM2**: Video segmentation
- **CLIP**: Zero-shot segmentation

## Research & Analysis

The project includes comprehensive analysis documents:

- **Methods Comparison** (`analysis/methods_comparison.md`): Detailed comparison of different detection and segmentation approaches
- **Cost Analysis** (`analysis/video_processing_cost_analysis.md`, `analysis/gemini_production_cost_analysis.md`): API cost analysis for Gemini and video processing
- **3D Volume Estimation** (`analysis/gemini_2.5_flash_3d_volume_estimation.md`): Analysis of depth and volume estimation methods
- **Model Limitations** (`WHY_DETECTIONS_ARE_WRONG.md`): Insights into model limitations and solutions

## Download Food Dataset

The repository includes a utility to download food video datasets:

```bash
python download_food_dataset.py
```

This downloads the food videos dataset from Kaggle for testing and development.

## Dependencies

Key dependencies include:
- `google-genai` - Gemini API client
- `opencv-python` - Computer vision operations
- `transformers` - Hugging Face transformers for Grounding DINO
- `torch`, `torchvision` - PyTorch for deep learning
- `ultralytics` - YOLO models
- `matplotlib` - Visualization
- `numpy` - Numerical operations

See `requirements.txt` for the complete list.

## License

This project extends food tracking and analysis capabilities. The Nutrition5k dataset (if used) is released under the Creative Commons V4.0 license.
