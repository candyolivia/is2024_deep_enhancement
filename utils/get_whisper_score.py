from jiwer import wer, cer, mer
import jiwer
import string
import re
import pandas as pd

def get_scores(reference_transcript, enhanced_transcript):
  wer_score = wer(reference_transcript, enhanced_transcript)*100
  cer_score = cer(reference_transcript, enhanced_transcript)*100
  mer_score = mer(reference_transcript, enhanced_transcript)*100
  return (wer_score, cer_score, mer_score)

beep_dict_path = "beep/beep-1.0.txt"

beep_dict = pd.read_csv(beep_dict_path, delimiter='\t', names=['word','pronounce'], header=0)

def get_pronounce(word):
  pronounce = ''
  try:
    pronounce += (beep_dict[beep_dict['word']==word.strip().upper()]['pronounce'].iloc[0])
  except:
    pronounce += ''
  return pronounce.strip()

transformation = jiwer.Compose([
    jiwer.ToLowerCase(),
    jiwer.ExpandCommonEnglishContractions(),
    jiwer.RemoveWhiteSpace(replace_by_space=True),
    jiwer.RemoveMultipleSpaces(),
    jiwer.RemovePunctuation(),
    jiwer.ReduceToListOfListOfWords(word_delimiter=" ")
])

df_sentence = []

for idx in range(whisper_transcript_df_noisy.shape[0]):
  scene_id = whisper_transcript_df_noisy['wavfile'].iloc[idx].split('_')[0]
  enhanced_transcript = whisper_transcript_df_noisy['transcript'].iloc[idx]
  reference_transcript = whisper_transcript_df_clean['transcript'].iloc[idx]

  ref_transformed = transformation(reference_transcript)[0]
  reference_transcript = ' '.join(x for x in ref_transformed)

  if (enhanced_transcript != enhanced_transcript):
    enhanced_transcript = ''
  else:
    enhanced_transcript = ''.join(x for x in enhanced_transcript if x in string.ascii_letters + string.whitespace)
    enh_transformed = transformation(enhanced_transcript)[0]
    enhanced_transcript = ' '.join(x for x in enh_transformed)

  reference_words = transformation(reference_transcript)
  reference_pronounce = ' '.join(get_pronounce(word) for word in reference_words[0])

  enhanced_words = transformation(enhanced_transcript)
  enhanced_pronounce = ' '.join(get_pronounce(word) for word in enhanced_words[0])

  wer_score, cer_score, mer_score = get_scores(reference_pronounce, enhanced_pronounce)

  df_sentence.append(
        {
            'scene': scene_id,
            'reference': reference_transcript,
            'hypothesis': enhanced_transcript,
            'reference_beep': reference_pronounce,
            'enhanced_beep': enhanced_pronounce,
            'wer':  wer_score,
            'cer': cer_score,
            'mer': mer_score
        }
    )

df_sentence = pd.DataFrame(df_sentence)
df_sentence.to_csv("CEC2_Interspeech2024/whisper_score_" + transcript_filename + ".csv")
