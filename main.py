import re
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def define_env(env):
    @env.macro
    def add_search_input_to_md(content):
        input_html = '<input type="text" class="searchInput" data-table-id="dataTable" placeholder="カラム名で検索" style="margin-left: 10px;">\n'
                
        # HTML for the table list link
        link_html = '\n[テーブル定義一覧に戻る](../database-design)\n'
        
        table_pattern = re.compile(r'(^|\n# .+?\n)(\|[^|]+\|\n\|[-| :]+\|)', re.DOTALL)

        def add_input_and_link(match):
            logger.info("add_input_and_link called")
            # Insert the search input after the table header and append the link at the end of the table
            return f'{match.group(1)}{input_html}\n{match.group(2)}{link_html}'

        # Apply the regex pattern and add the input field and link to the content
        content = table_pattern.sub(add_input_and_link, content)
        return content

    def on_page_markdown(markdown, page, config, files):
        logger.info(f"on_page_markdown called for {page.file.src_path}")
        target_folder = 'detailed/tables/'  # Adjust the target folder path as needed
        if page.file.src_path.startswith(target_folder):
            return add_search_input_to_md(markdown)
        return markdown

    env.page_markdown = on_page_markdown
