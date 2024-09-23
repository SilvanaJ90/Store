from langchain.text_splitter import CharacterTextSplitter


def text_splitter(
        documents,
        separator=" ",
        chunk_size=1000,
        chunk_overlap=200,
        is_separator_regex=False):
    """
        Extracts text from a list of document objects and splits
        it into chunks using the CharacterTextSplitter.

        Parameters:
        - documents (list): List of document objects,
            each with a `page_content` attribute.
        - separator (str): The separator to use for
            splitting the text. Default value is a space.
        - chunk_size (int): Size of each text chunk.
        - chunk_overlap (int): Amount of overlap between chunks.
        - is_separator_regex (bool): Whether the separator
            is a regular expression.

        Returns:
        - texts (list): List of split text chunks.
    """

    # Extraer el texto completo de cada documento
    full_text = "\n\n".join([doc.page_content for doc in documents])

    # Crear un objeto text_splitter
    text_splitter = CharacterTextSplitter(
        separator=separator,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=is_separator_regex,
    )

    # Crear documentos a partir del texto extraído
    texts = text_splitter.create_documents([full_text])

    return texts
