import textstat

def get_text_stats(text):
    return {
        "word_count": len(text.split()),
        "sentence_count": text.count('.'),
        "read_time": round(len(text.split()) / 200),  # 200 wpm
        "grade_level": textstat.flesch_kincaid_grade(text)
    }
