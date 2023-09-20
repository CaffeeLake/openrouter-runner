from modal import Stub
from vllm_runner.shared.config import Config

config = Config(
    name="auxilary",
    api_key_id="AUXILARY_API_KEY",
    download_dir="/model",
    num_gpu=1,
    max_batched_tokens=4096,
    idle_timeout=5 * 60,  # 5 minutes
    concurrency=16,
)

stub = Stub(config.name)
