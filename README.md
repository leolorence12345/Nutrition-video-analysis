<div align="center">

# Nutrition5k: A Comprehensive Nutrition Dataset

<p align="center">
	<img src="res/example_plate.jpg" width="400px">
	<img src="res/scan.gif" width="400px">
</p>

<p align="center">
	<a href="https://arxiv.org/pdf/2103.03375.pdf"><b>Paper</b></a> •
	<a href="#download-data"><b>Download Data</b></a> •
	<a href="#dataset-contents"><b>Dataset Contents</b></a> •
	# Nutrition5k — Visual Nutrition Dataset and Tools

	Nutrition5k is a dataset and toolkit for visual nutrition understanding. It contains thousands of plates with side-angle videos, overhead RGB-D captures (when available), ingredient-level metadata, and per-dish nutrition labels. This repo also includes demo scripts and analysis tools used to reproduce parts of the Nutrition5k project.

	This README focuses on quick setup, running demos, and where to find the data and code in this repository.

	## Quick links
	- Paper: https://arxiv.org/abs/2103.03375
	- Dataset (Google Cloud): https://console.cloud.google.com/storage/browser/nutrition5k_dataset

	## Quick start (Windows PowerShell)
	1. Create and activate a virtualenv (recommended):

	```powershell
	python -m venv venv
	venv\Scripts\Activate.ps1
	```

	2. Install dependencies:

	```powershell
	pip install -r requirements.txt
	```

	3. Run a demo:

	```powershell
See [here](https://cloud.google.com/storage/docs/gsutil) for instructions on installing the `gsutil` tool.

### Examples

<p align="center">
	<img src="res/plate_1.jpg">
	<img src="res/plate_2.jpg">
	<img src="res/plate_3.jpg">
	```

	## Files and folders of interest
	- `demos/` — runnable demo scripts (detection, video, visualization).  
	- `core/` — core analysis pipelines and tracking systems.  
	- `data/` — dataset slices and supporting metadata (when present).  
	- `videos/` and root-level `smart_tracked_...mp4` — example/sample videos used for demos.  
	- `requirements.txt` — Python dependencies for running demos and tools.

	## Data (download)
	Full Nutrition5k data is hosted on Google Cloud Storage. You can download the full archive or specific folders using `gsutil`:

	```powershell
	<img src="res/plate_4.jpg">
	<i><b>Example side-angle and overhead frames, with nutrition labels.</b></i>
</p>

<!--### Dish Ingredient Label
	```

	Note: dataset is large (~180GB). Download only the parts you need.

	## Contributing / Updating this README
	- To update the README and push changes, push to your fork and open a pull request against the `google-research-datasets/Nutrition5k` upstream repository. You can add your fork as a remote and push:

	```powershell
<img src="res/ingredients_table.png" width="200px">
<img src="res/example_plate.jpg" width="400px">
-->
	```

	If you would like help creating a fork, setting up Git LFS for large media, or preparing a pull request, tell me which option you prefer and I can run the commands for you locally.

	## License & citation
	This dataset and associated materials are released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. If you use the dataset in published work, please cite:

	Thames, Quin et al., "Nutrition5k: Towards Automatic Nutritional Understanding of Generic Food", CVPR 2021.

	BibTeX:

	```
	@inproceedings{thames2021nutrition5k,
	  title={Nutrition5k: Towards Automatic Nutritional Understanding of Generic Food},
	  author={Thames, Quin and Karpur, Arjun and Norris, Wade and Xia, Fangting and Panait, Liviu and Weyand, Tobias and Sim, Jack},
	  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
	  pages={8903--8911},
	  year={2021}
	}
	```

	Contact: nutrition5k@google.com

	---

	Last updated: 2025-11-12


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
