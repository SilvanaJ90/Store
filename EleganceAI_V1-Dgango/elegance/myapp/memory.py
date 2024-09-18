from langchain.memory import ConversationBufferMemory

class Memory:
    def __init__(self):
        self.memory = ConversationBufferMemory(memory_key='chat_history')

    def get_memory(self):
        return self.memory

    def save_context(self, inputs, outputs):
        # Asume que 'content' es el mensaje principal que queremos guardar
        input_message = inputs.get('content', '')
        output_message = outputs.get('content', '')
        self.memory.save_context({'input': input_message}, {'output': output_message})

    def load_memory(self):
        return self.memory.load_memory_variables({})

    def clear_memory(self):
        self.memory.clear()
