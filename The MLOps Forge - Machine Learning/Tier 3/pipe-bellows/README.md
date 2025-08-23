# Project: Pipe-Bellows

### The MLOps Forge - Tier 3

---

## 1. Project Overview

Pipe-Bellows is a complete, end-to-end CI/CD pipeline for a machine learning model. Built upon the "Training Crucible" project, it uses **DVC (Data Version Control)** and **GitHub Actions** to create a fully automated workflow.

When triggered, the pipeline automatically pulls versioned data from cloud storage, retrains a model, validates its performance against a set threshold, and if successful, versions the new model artifact and pushes it back to storage. This project demonstrates a foundational MLOps workflow for ensuring reproducible and quality-controlled model updates.

### Workflow Diagram
`Git Push` -> `GitHub Action Trigger` -> `Setup Environment` -> `DVC Pull` -> `Train Model` -> `Validate` -> `DVC Push` -> `Git Commit`

## 2. Technologies Used

- **CI/CD:** GitHub Actions
- **Data Version Control:** DVC
- **Cloud Storage:** Amazon S3
- **ML Framework:** Scikit-learn
- **Utilities:** Pandas, Joblib, AWS CLI

## 3. Setup and Installation

This project is part of a larger monorepo. For instructions on how to clone only this specific project, please refer to the **[main repository's README.md](../../../README.md)**.

### 3.1. DVC Remote Setup (Amazon S3)

This project requires a cloud storage backend for DVC. Follow these steps to configure your own S3 bucket.

1.  **Create an AWS Free Tier Account:** You will need an AWS account.
2.  **Create an S3 Bucket:**
    - In the AWS Console, navigate to S3 and create a **General Purpose** bucket with a **globally unique name** (e.g., `yourname-pipe-bellows-storage`).
    - **Uncheck "Block all public access"** and acknowledge the warning.
3.  **Set Bucket Policy:**
    - Go to your bucket's "Permissions" tab, edit the "Bucket policy," and paste the following, replacing `YOUR_BUCKET_NAME_HERE` with your bucket's name. This makes the data publicly readable.
      ```json
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "PublicReadGetObject",
                  "Effect": "Allow",
                  "Principal": "*",
                  "Action": "s3:GetObject",
                  "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME_HERE/*"
              }
          ]
      }
      ```
4.  **Create a Secure IAM User:**
    - In the AWS Console, navigate to IAM and create a new user (e.g., `pipe-bellows-dvc-user`).
    - Create a new policy with JSON, pasting the code below (replace `YOUR_BUCKET_NAME_HERE` again). This gives the user permission to manage files *only* in that specific bucket.
      ```json
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "AllowDvcAccess",
                  "Effect": "Allow",
                  "Action": [
                      "s3:GetObject",
                      "s3:PutObject",
                      "s3:DeleteObject",
                      "s3:ListBucket"
                  ],
                  "Resource": [
                      "arn:aws:s3:::YOUR_BUCKET_NAME_HERE/*",
                      "arn:aws:s3:::YOUR_BUCKET_NAME_HERE"
                  ]
              }
          ]
      }
      ```
    - Attach this new policy to the user you created.
    - Generate an **Access key** for the user (select "Command Line Interface (CLI)" as the use case) and save the **Access key ID** and **Secret access key**.

### 3.2. Local Environment Setup

1.  **Navigate to the project directory.**
2.  **Create and activate a virtual environment.**
3.  **Install dependencies:** `pip install -r requirements.txt`.
4.  **Install AWS CLI:**
    - **(macOS/Linux Recommended)**: Use Homebrew: `brew install awscli`. This avoids potential "bad interpreter" errors if your project path contains spaces.
    - **(Pip)**: `pip install awscli`.
5.  **Configure AWS Credentials:** Run `aws configure` and enter the Access Key ID, Secret Access Key, and your bucket's region.
6.  **Configure DVC Remote:** Run the following command, replacing the bucket name with your own:
    ```bash
    dvc remote add -d myremote s3://YOUR_BUCKET_NAME_HERE
    ```

## 4. Usage

The pipeline is defined in `.github/workflows/pipe-bellows.yml` and is designed to be run manually.

1.  Make changes to the code or data.
2.  Commit and push your changes to GitHub.
3.  Navigate to the "Actions" tab of the repository.
4.  Select the "MLOps Pipeline for Pipe-Bellows" workflow and click "Run workflow".
