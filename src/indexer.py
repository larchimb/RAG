class Indexer():
    '''To create the index for .py or .md files'''

    def load_files(self) -> None:
        '''Find the files, check if they are available'''
        ...

    def chunk_python(self) -> None:
        '''Chunk a python file in functions'''
        ...

    def chunk_text(self) -> None:
        '''Chunk a md or text file in chunks'''
        ...

    def build_index(self) -> None:
        '''Build the index depending of the BM25 method'''
        ...

    def save_index(self) -> None:
        '''Save the index to the right path'''