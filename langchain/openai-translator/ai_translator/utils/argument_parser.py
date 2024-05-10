import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='A translation tool that supports translations in any language pair.')
        self.parser.add_argument('--config_file', type=str, default='config.yaml', help='Configuration file with model and API settings.')
        self.parser.add_argument('--model_type', type=str, default='GLMModel', choices=['GLMModel', 'OpenAIModel'], help='Name of the Large Language Model.')
        self.parser.add_argument('--model_name', help='Name of the Large Language Model.')
        self.parser.add_argument('--input_file', type=str, help='PDF file to translate.')
        self.parser.add_argument('--output_file_format', type=str, help='The file format of translated book. Now supporting PDF and Markdown')
        self.parser.add_argument('--source_language', type=str, help='The language of the original book to be translated.')
        self.parser.add_argument('--target_language', type=str, help='The target language for translating the original book.')

    def parse_arguments(self):
        args = self.parser.parse_args()
        if args.model_type == 'OpenAIModel':
            if not args.openai_model:
                print("If you haven't configure model in your configuration file, "
                      "then --openai_model is required on your command line.")
            if not args.openai_api_key:
                print("If you haven't configure api_key in your configuration file, "
                      "and haven't set the OPENAI_API_KEY environment variable, "
                      "then --openai_api_key is required on your command line.")
        return args
