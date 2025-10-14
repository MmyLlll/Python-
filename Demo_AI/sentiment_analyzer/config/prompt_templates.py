"""
情感分析提示词模板
作用：管理不同语言的AI提示词，确保分析结果的格式统一和准确性
"""

SENTIMENT_PROMPTS = {
    "zh": """请分析以下文本的情感倾向，从以下5个类别中选择最合适的一个：
    - 非常积极
    - 积极  
    - 中性
    - 消极
    - 非常消极

文本内容：{text}

请以JSON格式返回分析结果：
{{
    "sentiment": "情感类别",
    "confidence": "置信度(0-1)",
    "reason": "简要分析理由"
}}""",

    "en": """Analyze the sentiment of the following text and choose the most appropriate category from:
    - Very Positive
    - Positive
    - Neutral  
    - Negative
    - Very Negative

Text: {text}

Return the analysis in JSON format:
{{
    "sentiment": "sentiment category",
    "confidence": "confidence score (0-1)",
    "reason": "brief analysis reason"
}}"""
}

def get_prompt(text, language="zh"):
    """获取对应语言的提示词"""
    prompt_template = SENTIMENT_PROMPTS.get(language, SENTIMENT_PROMPTS["zh"])
    return prompt_template.format(text=text)