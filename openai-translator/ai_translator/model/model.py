from book import ContentType

class Model:
    def make_text_prompt(self, text: str, target_language: str) -> str:
        return f"翻译为{target_language}：{text}"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        # return f"翻译为{target_language}，保持间距（空格，分隔符），以表格形式返回：\n{table}"
        return f"translate into {target_language},return in table format, keep row counts and column counts the same, keep distance the same, return in table format: \n{table}. Please double check and ensure the table rows and columns are the same. Please double check and every column should be the {target_language}. If there is table translation error please double check and ensure the columns passed and data passed are consistent."

    def translate_prompt(self, content, target_language: str) -> str:
        if content.content_type == ContentType.TEXT:
            return self.make_text_prompt(content.original, target_language)
        elif content.content_type == ContentType.TABLE:
            return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
