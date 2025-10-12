#!/usr/bin/env python3
"""
Cleanup script to prepare codebase for Git
Removes test files, demos, and temporary files
"""

import os
import shutil
from pathlib import Path

# Files and directories to remove
TO_REMOVE = [
    # Test scripts (experimental)
    "test_continuous_tracking.py",
    "test_live_tracking.py",
    "test_live_tracking_with_redetection.py",
    "test_nutrition5k_autolabel_tracking.py",
    "test_nutrition5k_florence2.py",
    "test_nutrition5k_video_tracking.py",
    "test_rag_only.py",
    "test_smart_redetection_tracking.py",
    "test_smart_tracking_improved.py",
    "test_smart_tracking_sam2_boxes.py",
    "test_tracking_with_depth_volume.py",
    "test_tracking_with_metric_depth.py",
    # Keep test_tracking_metric3d.py - it's the main one
    
    # Demo scripts
    "grounded_sam2_dinox_demo.py",
    "grounded_sam2_florence2_autolabel_pipeline.py",
    "grounded_sam2_florence2_image_demo.py",
    "grounded_sam2_gd1.5_demo.py",
    "grounded_sam2_hf_model_demo.py",
    "grounded_sam2_local_demo.py",
    "grounded_sam2_tracking_camera_with_continuous_id.py",
    "grounded_sam2_tracking_demo_custom_video_input_dinox.py",
    "grounded_sam2_tracking_demo_custom_video_input_gd1.0_hf_model.py",
    "grounded_sam2_tracking_demo_custom_video_input_gd1.0_local_model.py",
    "grounded_sam2_tracking_demo_custom_video_input_gd1.5.py",
    "grounded_sam2_tracking_demo_with_continuous_id_gd1.5.py",
    "grounded_sam2_tracking_demo_with_continuous_id_plus.py",
    "grounded_sam2_tracking_demo_with_continuous_id.py",
    "grounded_sam2_tracking_demo_with_gd1.5.py",
    "grounded_sam2_tracking_demo.py",
    
    # Directories
    "demo/",
    "demo_images/",
    "notebooks/",
    "sav_dataset/",
    "training/",
    "assets/",
    
    # Deploy test files
    "deploy/test_simple_api.py",
    "deploy/test_api.py",
    "deploy/run_with_venv.py",
    "deploy/start_api.bat",
    "deploy/check_api.py",
    
    # Deploy extra docs (keep main ones)
    "deploy/DEPLOYMENT_SUMMARY.md",
    "deploy/FINAL_INSTRUCTIONS.md",
    "deploy/QUICKSTART.md",
    "deploy/START_HERE.txt",
    "deploy/WINDOWS_SETUP.md",
    
    # Test data
    "grounding_dino/WhatsApp Video 2025-09-10 at 05.16.56_9874c762.mp4",
    
    # Old files
    "TEST_APPROACHES_SUMMARY.md",
    "backend.Dockerfile",
    "docker-compose.yaml",
    "Dockerfile",
]

def cleanup():
    """Remove unnecessary files"""
    base_dir = Path(__file__).parent
    removed = []
    errors = []
    
    print("Cleaning up codebase for Git...")
    print("=" * 60)
    
    for item in TO_REMOVE:
        path = base_dir / item
        
        if not path.exists():
            continue
            
        try:
            if path.is_file():
                path.unlink()
                removed.append(f"[OK] Removed file: {item}")
            elif path.is_dir():
                shutil.rmtree(path)
                removed.append(f"[OK] Removed directory: {item}")
        except Exception as e:
            errors.append(f"[ERROR] Error removing {item}: {e}")
    
    # Print results
    print("\nCleanup Results:")
    print("=" * 60)
    print(f"Removed {len(removed)} items:\n")
    for msg in removed:
        print(f"  {msg}")
    
    if errors:
        print(f"\nErrors ({len(errors)}):\n")
        for msg in errors:
            print(f"  {msg}")
    
    print("\n" + "=" * 60)
    print("Cleanup complete!")
    print("\nWhat's left:")
    print("  + deploy/ - Production API")
    print("  + sam2/ - SAM2 model")
    print("  + grounding_dino/ - Detection model")
    print("  + nutrition_rag_system.py - RAG system")
    print("  + rag/ - Nutrition databases")
    print("  + test_tracking_metric3d.py - Main test script")
    print("  + checkpoints/ - Model weights (excluded in .gitignore)")
    print("\nNext steps:")
    print("  1. git init")
    print("  2. git add .")
    print("  3. git commit -m 'Initial commit - production code'")
    print("  4. Create GitHub repo and push")

if __name__ == "__main__":
    cleanup()

