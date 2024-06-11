from transformers import WhisperProcessor, WhisperForConditionalGeneration
from datasets import load_dataset, Audio

# directory location
dir_path = "/is2024_deep_enhancement/dataset/CEC2/eval/set1/noisy"

# load model and processor
processor = WhisperProcessor.from_pretrained("openai/whisper-medium.en")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-medium.en")
model.config.forced_decoder_ids = None

# load dataset from directory
dataset = load_dataset(dir_path)
dataset = dataset.cast_column("audio", Audio(sampling_rate=16000))

for i in range(dataset["train"].num_rows):

	# load dummy dataset and read audio files
	sample = dataset["train"][i]["audio"]
	input_features = processor(sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt").input_features

	# generate token ids
	predicted_ids = model.generate(input_features)

	# decode token ids to text
	transcription = processor.batch_decode(predicted_ids, skip_special_tokens=False)
	transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

	print(dataset["train"][i]["audio"]["path"].split('/')[-1] + ';' + transcription[0])
