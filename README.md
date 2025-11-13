<div align="center">

# N

<p align="center">
	<img src="res/example_plate.jpg" width="400px">
	<img src="res/scan.gif" width="400px">
</p>

<p align="center">
	<a href="https://arxiv.org/pdf/2103.03375.pdf"><b>Paper</b></a> •
	<a href="#download-data"><b>Download Data</b></a> •
	<a href="#dataset-contents"><b>Dataset Contents</b></a> •
	<a href="#license--contact"><b>License & Contact</b></a>
</p>

</div>

## Live Production API

**GitHub**: https://github.com/leolorence12345/-nutrition-video-analysis  
**Live Demo**: http://18.214.98.110:8000  
**API Docs**: http://18.214.98.110:8000/docs  
**Health Check**: http://18.214.98.110:8000/health

**Production Deployment**: AWS EC2 (t3.xlarge)

This repository includes a **production-ready nutrition analysis API** that uses:
- **Florence-2**: Automatic food detection from images
- **SAM2**: Video object tracking with continuous IDs
- **Metric3D**: Depth & volume estimation
- **RAG System**: Calorie & nutrition database (FNDDS + CoFID)
- **Gemini API**: Fallback for unknown food items

See [`Grounded-SAM-2/deploy/README.md`](Grounded-SAM-2/deploy/README.md) for deployment guide.

## Research & Analysis

The project includes comprehensive analysis documents in the `analysis/` directory:

- **Methods Comparison**: Detailed comparison of different detection and segmentation approaches
- **Cost Analysis**: API cost analysis for Gemini and video processing
- **3D Volume Estimation**: Analysis of depth and volume estimation methods

See `WHY_DETECTIONS_ARE_WRONG.md` for insights into model limitations and solutions.

---

<b>Nutrition5k</b> is a dataset of visual and nutritional data for ~5k realistic plates of food captured from Google cafeterias using a custom scanning rig. We are releasing this dataset alongside our recent <a href="https://arxiv.org/abs/2103.03375">CVPR 2021 paper</a> to help promote research in visual nutrition understanding. Please see the paper for more details on the dataset and follow-up experiments.

### Key Features
<ul>
	<li>Scans data for 5,006 plates of food, each containing:
		<ul>
			<li>4 rotating side-angle videos</li>
			<li>Overhead RGB-D images <i>(when available)</i></li>
			<li>Fine-grained list of ingredients</li>
			<li>Per-ingredient mass</li>
			<li>Total dish mass and calories</li>
			<li>Fat, protein, and carbohydrate macronutrient masses</li>
		</ul></li>
	<li>Official train/test split</li>
	<li>Nutrition regression eval scripts</li>
</ul>

### Project Capabilities

This repository extends the Nutrition5k dataset with:

- **Multi-Model Detection**: Support for YOLO-World, Grounding DINO, OWL-ViT, Detectron2, and Gemini
- **Video Tracking**: DeepSORT, ByteTrack, and SAM2-based tracking systems
- **Segmentation**: SAM, SAM2, and CLIP-based segmentation methods
- **3D Analysis**: Metric3D integration for depth and volume estimation (in Grounded-SAM-2/deploy)
- **Nutrition Database**: RAG system with FNDDS and CoFID databases (in Grounded-SAM-2/deploy)
- **Model Fine-tuning**: Scripts for fine-tuning Grounding DINO on custom food datasets

<i>→ [Also, see our related <a href="https://tfhub.dev/google/seefood/segmenter/mobile_food_segmenter_V1/1">Mobile Food Segmentation model on TensorFlow Hub</a>]</i>

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

# Set Gemini API key
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
```

### Core Systems

The project includes several production-ready systems for food analysis:

#### Video Food Analysis System
```bash
# Main video analysis pipeline combining SAM segmentation + tracking + Gemini labeling
python core/video_food_analysis_system.py
```

#### Tracking Systems
- **Gemini-based tracking**: Uses Gemini API for object detection and tracking
- **DeepSORT tracking**: Multi-object tracking with DeepSORT
- **ByteTrack integration**: ByteTrack-based tracking with Gemini

#### Model Testing
```bash
# Test various detection models
python scripts/test_owlvit_detection.py
python scripts/test_detectron2_clip.py
python scripts/test_sam_clip.py
```

### Production API

The project includes a production-ready API in `Grounded-SAM-2/deploy/`:

```bash
cd Grounded-SAM-2/deploy
# See deploy/README.md for full deployment instructions
```

**Live API**: http://18.214.98.110:8000/docs

## Project Structure

```
Nutrition5k/
├── core/                    # Core tracking and analysis systems
│   ├── video_food_analysis_system.py    # Main video analysis pipeline
│   ├── gemini_*_tracking.py             # Gemini-based tracking systems
│   ├── working_*_system.py              # Production tracking implementations
│   └── live_*_visualization.py          # Real-time visualization tools
├── demos/                    # Demo scripts and examples
│   ├── simple_demo.py                   # Basic food analysis demo
│   ├── video_demo.py                    # Video processing demo
│   ├── compare_all_models.py            # Model comparison utilities
│   └── *_detection.py                   # Various detection demos
├── scripts/                  # Utility scripts
│   ├── compute_eval_statistics.py       # Nutrition evaluation metrics
│   ├── generate_*_dataset.py           # Dataset generation tools
│   ├── finetune_grounding_dino*.py      # Model fine-tuning scripts
│   └── test_*.py                        # Model testing scripts
├── Grounded-SAM-2/           # Grounded SAM-2 implementation
│   ├── deploy/                          # Production deployment
│   ├── sam2/                            # SAM2 model implementation
│   ├── grounding_dino/                  # Grounding DINO implementation
│   └── nutrition_rag_system.py          # RAG system for nutrition data
├── analysis/                 # Analysis and comparison documents
│   ├── methods_comparison.md            # Detailed method comparisons
│   ├── video_processing_cost_analysis.md
│   ├── gemini_production_cost_analysis.md
│   └── gemini_2.5_flash_3d_volume_estimation.md
├── models/                    # Pre-trained model files
│   ├── cache/                           # Model cache directory
│   ├── grounding_dino_finetuned/        # Fine-tuned models
│   └── sam_vit_*.pth                    # SAM model checkpoints
├── data/                     # Dataset files and results
│   ├── food_videos_dataset/             # Food video dataset
│   ├── food101_local/                   # Food-101 dataset
│   ├── gemini_food_dataset/             # Gemini-generated annotations
│   └── *_results/                       # Various model results
├── results/                  # Output results and visualizations
├── videos/                   # Video files for analysis
├── res/                      # Resources and sample images
├── requirements.txt          # Python dependencies
├── download_food_dataset.py  # Dataset download utility
└── README.md                # This file
```

### Download Data
All Nutrition5k data can be downloaded directly from our [Google Cloud Storage bucket](https://console.cloud.google.com/storage/browser/nutrition5k_dataset), or from the .tar.gz download link below.
<ul>
	<li><a href="https://storage.cloud.google.com/nutrition5k_dataset/nutrition5k_dataset.tar.gz">nutrition5k_dataset.tar.gz</a> (181.4 GB)
</ul>

From the Cloud Storage bucket directory, you can also browse through the dataset folders and download specific files using the `gsutil cp` command:
```
gsutil -m cp -r "gs://nutrition5k_dataset/nutrition5k_dataset/{FILE_OR_DIR_PATH}" .
```

See [here](https://cloud.google.com/storage/docs/gsutil) for instructions on installing the `gsutil` tool.

### Examples

<p align="center">
	<img src="res/plate_1.jpg">
	<img src="res/plate_2.jpg">
	<img src="res/plate_3.jpg">
	<img src="res/plate_4.jpg">
	<i><b>Example side-angle and overhead frames, with nutrition labels.</b></i>
</p>

<p align="center">
	<img src="res/incremental.jpg">
	<i><b>Example of the incremental scanning procedure.</b></i>
</p>

### Video Tracking Demo

The repository includes example videos demonstrating food tracking and analysis:

**Example Tracking Video**: [smart_tracked_WhatsApp Video 2025-09-10 at 05.16.56_9874c762.mp4](./smart_tracked_WhatsApp%20Video%202025-09-10%20at%2005.16.56_9874c762.mp4)

This video demonstrates:
- Food item detection and tracking with continuous IDs
- Segmentation masks for each tracked item
- Frame-by-frame object persistence

Additional tracking results are available in:
- `videos/` - Sample input videos
- `data/food_videos_tracking_results/` - Processed tracking videos
- `data/metric3d_results/` - Videos with depth and volume estimation

## Dataset contents

#### Side-Angle Videos
Video recordings were captured using 4 separate Raspberry Pi cameras (labeled A-D) at alternating 30 degree and 60 degree viewing angles. The cameras are positioned 90 degrees apart and sweep 90 degrees during video capture so that the dish is captured from all sides.

After downloading the Nutrition5k dataset, video files will be found in `imagery/side_angles/` and organized by dish id. To extract all 2D image frames from a video, use ffmpeg as shown below:
```
ffmpeg -i input.mp4 output_%03d.jpeg
```

The models included in the Nutrition5k paper were trained and evaluated on every fifth frame sampled from each video. The repository includes `scripts/extract_frames.sh` and `scripts/extract_frames_sampled.sh` to help with frame extraction from the downloaded dataset.

#### Overhead RGB-D Images
After downloading the dataset, the `imagery/realsense_overhead/` directory contains RGB, raw depth, and colorized depth images organized by dish ID. Raw depth images are encoded as 16-bit integer images with depth units of 10,000 (i.e. 1 meter = 10,000 units). The colorized depth images provide a human-readable visualization of the depth map, with closer objects in blue and further objects in red. All depth values are rounded to a maximum of 0.4m (4,000 depth units), which exceeds the height of our food scanning rig.

#### Ingredient Metadata
After downloading the dataset, the ingredient metadata CSV (`metadata/ingredient_metadata.csv`) contains a list of all ingredients covered in the dataset's dishes, their unique IDs, and per-gram nutritional information sourced from the USDA Food and Nutrient Database. Ingredient IDs take the following form: `ingr_[ingredient number padded to 10 digits]`.

#### Dish Metadata
After downloading the dataset, the dish metadata CSVs (`metadata/dish_metadata_cafe1.csv` and `metadata/dish_metadata_cafe2.csv`) contain all nutrition metadata at the dish-level, as well as per-ingredient mass and macronutrients. For each dish ID `dish_[10 digit timestamp]`, there is a CSV entry containing the following fields: 

<i>dish_id, total_calories, total_mass, total_fat, total_carb, total_protein, num_ingrs, (ingr_1_id, ingr_1_name, ingr_1_grams, ingr_1_calories, ingr_1_fat, ingr_1_carb, ingr_1_protein, ...)</i>

with the last 8 fields repeated for every ingredient present in the dish.

#### Train/Test Splits
After downloading the dataset, dish IDs for the training and testing splits used in the experiments are in the `dish_ids/splits/` directory. All incremental scans that compose a unique plate are held within the same split, to avoid overlap between the train and test splits. See Section 3.6 of the paper for more details on incremental scanning.

#### Evaluation Script
To help evaluate nutrition prediction methods, we provide `scripts/compute_eval_statistics.py`. This script can be used to calculate absolute and percentage mean average error from a CSV of per-dish nutrition values. This tool can be used to generate regression results that can be directly compared to those reported in the paper. See the header file for usage instructions.

## Dataset Bias Disclaimer
The dataset does not cover all food cuisines, as it was only collected in a few select cafeterias in California, USA. Nutrition5k does not claim to completely solve the food understanding problem, but rather aims to provide a unique level of detailed annotations and depth data to further advance the space.

## License & Contact
We release all Nutrition5k data under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons V4.0</a> license. You are free to share and adapt this data for any purpose, even commercially. If you found this dataset useful, please consider citing our [CVPR 2021 paper](https://arxiv.org/pdf/2103.03375.pdf).
```
@inproceedings{thames2021nutrition5k,
  title={Nutrition5k: Towards Automatic Nutritional Understanding of Generic Food},
  author={Thames, Quin and Karpur, Arjun and Norris, Wade and Xia, Fangting and Panait, Liviu and Weyand, Tobias and Sim, Jack},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={8903--8911},
  year={2021}
}
```

If you have any questions about the Nutrition5k dataset or paper, please send an email to the authors at <a href="mailto:nutrition5k@google.com">nutrition5k@google.com</a>.


Thank you to Ben Goldberger, Caitlin O'Brien, and the Google LAX/PLV Cafeteria teams for their contributions!
