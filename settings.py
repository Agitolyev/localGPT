from pydantic import (
    BaseSettings,
    Field,
)

class ModelSettings(BaseSettings):

####
#### (FOR HF MODELS)
####

# MODEL_ID = "TheBloke/vicuna-7B-1.1-HF"
# MODEL_BASENAME = None
# MODEL_ID = "TheBloke/Wizard-Vicuna-7B-Uncensored-HF"
# MODEL_ID = "TheBloke/guanaco-7B-HF"
# MODEL_ID = 'NousResearch/Nous-Hermes-13b' # Requires ~ 23GB VRAM. Using STransformers
# alongside will 100% create OOM on 24GB cards.
# llm = load_model(device_type, model_id=model_id)

####
#### (FOR GPTQ QUANTIZED) Select a llm model based on your GPU and VRAM GB. Does not include Embedding Models VRAM usage.
####

##### 48GB VRAM Graphics Cards (RTX 6000, RTX A6000 and other 48GB VRAM GPUs) #####

### 65b GPTQ LLM Models for 48GB GPUs (*** With best embedding model: hkunlp/instructor-xl ***)
# model_id = "TheBloke/guanaco-65B-GPTQ"
# model_basename = "model.safetensors"
# model_id = "TheBloke/Airoboros-65B-GPT4-2.0-GPTQ"
# model_basename = "model.safetensors"
# model_id = "TheBloke/gpt4-alpaca-lora_mlp-65B-GPTQ"
# model_basename = "model.safetensors"
# model_id = "TheBloke/Upstage-Llama1-65B-Instruct-GPTQ"
# model_basename = "model.safetensors"

##### 24GB VRAM Graphics Cards (RTX 3090 - RTX 4090 (35% Faster) - RTX A5000 - RTX A5500) #####

### 13b GPTQ Models for 24GB GPUs (*** With best embedding model: hkunlp/instructor-xl ***)
# model_id = "TheBloke/Wizard-Vicuna-13B-Uncensored-GPTQ"
# model_basename = "Wizard-Vicuna-13B-Uncensored-GPTQ-4bit-128g.compat.no-act-order.safetensors"
# model_id = "TheBloke/vicuna-13B-v1.5-GPTQ"
# model_basename = "model.safetensors"
# model_id = "TheBloke/Nous-Hermes-13B-GPTQ"
# model_basename = "nous-hermes-13b-GPTQ-4bit-128g.no-act.order"
# model_id = "TheBloke/WizardLM-13B-V1.2-GPTQ"
# model_basename = "gptq_model-4bit-128g.safetensors

### 30b GPTQ Models for 24GB GPUs (*** Requires using intfloat/e5-base-v2 instead of hkunlp/instructor-large as embedding model ***)
# model_id = "TheBloke/Wizard-Vicuna-30B-Uncensored-GPTQ"
# model_basename = "Wizard-Vicuna-30B-Uncensored-GPTQ-4bit--1g.act.order.safetensors"
# model_id = "TheBloke/WizardLM-30B-Uncensored-GPTQ"
# model_basename = "WizardLM-30B-Uncensored-GPTQ-4bit.act-order.safetensors"

##### 8-10GB VRAM Graphics Cards (RTX 3080 - RTX 3080 Ti - RTX 3070 Ti - 3060 Ti - RTX 2000 Series, Quadro RTX 4000, 5000, 6000) #####
### (*** Requires using intfloat/e5-small-v2 instead of hkunlp/instructor-large as embedding model ***)

### 7b GPTQ Models for 8GB GPUs
# model_id = "TheBloke/Wizard-Vicuna-7B-Uncensored-GPTQ"
# model_basename = "Wizard-Vicuna-7B-Uncensored-GPTQ-4bit-128g.no-act.order.safetensors"
# model_id = "TheBloke/WizardLM-7B-uncensored-GPTQ"
# model_basename = "WizardLM-7B-uncensored-GPTQ-4bit-128g.compat.no-act-order.safetensors"
# model_id = "TheBloke/wizardLM-7B-GPTQ"
# model_basename = "wizardLM-7B-GPTQ-4bit.compat.no-act-order.safetensors"

####
#### (FOR GGML) (Quantized cpu+gpu+mps) models - check if they support llama.cpp
####

# MODEL_ID = "TheBloke/wizard-vicuna-13B-GGML"
# MODEL_BASENAME = "wizard-vicuna-13B.ggmlv3.q4_0.bin"
# MODEL_BASENAME = "wizard-vicuna-13B.ggmlv3.q6_K.bin"
# MODEL_BASENAME = "wizard-vicuna-13B.ggmlv3.q2_K.bin"
# MODEL_ID = "TheBloke/orca_mini_3B-GGML"
# MODEL_BASENAME = "orca-mini-3b.ggmlv3.q4_0.bin"
    model_id: str = Field(..., env='MODEL_ID')
    model_basename: str = Field(..., env='MODEL_BASENAME')

model_settings = ModelSettings()
