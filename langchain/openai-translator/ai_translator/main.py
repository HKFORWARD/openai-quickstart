import sys
import os
import time
import jwt
from langchain_community.chat_models import ChatZhipuAI
from langchain_openai import ChatOpenAI


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from translator import PDFTranslator, TranslationConfig

glm_model = ChatZhipuAI(
    model_name='glm-4',
    temperature=0.5,  # (0.0, 1.0) 不能等于0
    verbose=True,
)
gpt_model = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.5,
    verbose=True,
    max_tokens=4096
)

glm_translator = PDFTranslator(glm_model)
gpt_translator = PDFTranslator(gpt_model)

if __name__ == "__main__":
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()

    # 初始化配置单例
    config = TranslationConfig()
    config.initialize(args)    
    global model_type

    # 实例化 PDFTranslator 类，并调用 translate_pdf() 方法
    if args.model_type == "OpenAIModel":
        translator = gpt_translator
    elif args.model_type == "GLMModel":
        translator = glm_translator
    else:
        raise ValueError("Invalid model_type specified. Please choose either 'GLMModel' or 'OpenAIModel'.")
    
    translator.translate_pdf(config.input_file, config.output_file_format, pages=None)
