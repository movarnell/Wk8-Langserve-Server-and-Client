import os
import uvicorn
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


model1 = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key= os.environ["OPENAI_API_KEY"])
prompt1 = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt1 | model1,
    path="/joke",
)


# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)