# mk.io-scripts

This repository contains **small code snippets and example scripts** designed to interact with the various APIs of the **MK.IO** video platform.

## What is MK.IO?

**MK.IO** is a powerful cloud-based platform developed by **MediaKind** for building modern video applications and managing streaming media services with AI interaction. It provides comprehensive management for video, audio, and metadata (such as subtitles), converting them into various formats for distribution to customers, partners, or cloud storage. 

*   **Official Website:** [mk.io](https://mk.io)
*   **Technical Documentation:** [docs.mediakind.com/mkio](https://docs.mediakind.com/mkio)

## Repository Objective

The primary goal of this repository is to facilitate **learning and experimentation** with MK.IO's potent API ecosystem. By providing modular pieces of code, users can explore:

*   **Media API:** Managing assets, live events, and publishing content.
*   **Management API:** Resolving organizational details and user profiles.
*   **Flow API:** Orchestrating complex video processing pipelines, such as Multiview setups.
*   **Player SDK/API:** Integrating and customizing the **MKPlayer** for high-performance video playback, manifest resolution (HLS/DASH), and UI customization

## ⚠️ Important Disclaimer

These scripts are intended **strictly for educational and experimental purposes**. 

*   **Non-Production Ready:** These codes are NOT designed or intended for direct use in production environments. 
*   **User Responsibility:** Users are responsible for adapting, securing, and validating any logic before implementation in a real-world scenario.
*   **Cost Awareness:** Be aware that certain API operations (e.g., starting Live Events or Streaming Endpoints) may incur costs based on your subscription plan.

## Current Contents

The repository includes examples such as:
*   **`getOrg`**: A Python script to retrieve the organization name associated with a valid API token.
*   **`createLiveEvent`**: A Python script for provisioning a Live Event along with its corresponding DVR asset.
*   **`Mkplayer-transcriptionBox`**: An HTML/JavaScript implementation using the MKPlayer API to create a dynamic transcription box below the video player.
*   **`bulkRemoveAssets`**: A Python script for batch removing assets from a user with a basic interactivity
*   **`bulkChangeRetainPolicy`**: Python script to batch update the `containerDeletionPolicy` of multiple assets, ensuring storage preservation or cleanup.

---
*Created to experiment with the future of cloud video.*