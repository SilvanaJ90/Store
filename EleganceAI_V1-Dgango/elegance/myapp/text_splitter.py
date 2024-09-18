from langchain.text_splitter import CharacterTextSplitter

def split_text_into_chunks(raw_text, chunk_size=1000, chunk_overlap=200, separator="\n"):
    """
    Function to split raw text into chunks based on the given parameters.
    
    :param raw_text: The full text to split
    :param chunk_size: The size of each chunk (default 1000 characters)
    :param chunk_overlap: The overlap between chunks (default 200 characters)
    :param separator: The separator to split the text (default "\n")
    :return: A list of text chunks
    """
    text_splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    
    return text_splitter.split_text(raw_text)
