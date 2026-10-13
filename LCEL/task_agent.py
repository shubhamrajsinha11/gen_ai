from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash',
    api_key='',
    temperature=0
)

prompt=ChatPromptTemplate.from_messages([
    ('system', 'you are a helpful assistant.'),
    MessagesPlaceholder(variable_name='history'),
    ('human','{input}')
])

chain=prompt | llm | StrOutputParser()
store={}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id]=[]
        
  
  
        
session_id=1
print('-----START-----')
while True:
    user_input=input('''
                     Enter your query....
                     or
                     For exit type => exit
                     query : > ''').lower()
    if user_input=='exit':
        print('Thank you 😊👌')
        break
    try:
        history=get_session_history(session_id)
        history.append({'user_query':user_input})
        response= chain.ivoke({'history':history})
        print(f'''
              user input => {user_input}
              Rreponse =>{response}
              ''')
    except Exception as e:
        print(f' error=> {e}')
        break
    new_session=input('''
                      if you want to continue the same session type anything except no ==> yes
                      for new session type => no
                      ''')
    if new_session== 'no':
        session_id+=1