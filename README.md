# YandexGPT Model Provider for Dify

YandexGPT Pro, Lite, and Alice AI language models from Yandex Cloud.

## Models

- **YandexGPT Pro 5.1** — flagship model for deep reasoning and document analysis (32K context)
- **YandexGPT Pro 5** — previous generation Pro model (32K context)
- **YandexGPT Lite 5** — lightweight model optimized for low-latency generation (32K context)
- **Alice AI LLM** — conversational AI model for chat scenarios (32K context)

## Installation

### From GitHub

In your Dify instance, go to **Plugins > Install from GitHub** and enter this repository URL.

### Manual

1. Clone this repository
2. Package with `dify plugin package ./`
3. Upload the `.difypkg` file via **Plugins > Install from local file**

## Setup

### 1. Create a Yandex Cloud account

Go to [Yandex Cloud Console](https://console.yandex.cloud/) and create an account.

### 2. Create an API key

Go to [Service accounts](https://console.yandex.cloud/iam/service-accounts) and create a service account with the `ai.languageModels.user` role. Then create an API key for it.

### 3. Get your Folder ID

Find your folder ID in the [Yandex Cloud Console](https://console.yandex.cloud/) — it's displayed in the folder settings.

### 4. Configure in Dify

Navigate to **Settings > Model Provider > YandexGPT** and enter your **API Key** and **Folder ID**.
