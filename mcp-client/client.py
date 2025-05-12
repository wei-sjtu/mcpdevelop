import asyncio
import os
from openai import OpenAI
from dotenv import load_dotenv
from contextlib import AsyncExitStack, asynccontextmanager

load_dotenv()

class MCPClient:
    def __init__(self):
        self.exit_stack = AsyncExitStack()
        self.openai_api_key=os.getenv('OPENAI_API_KEY')
        self.base_url=os.getenv('BASE_URL')
        self.model=os.getenv('MODEL')

        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables")
        self.client = OpenAI(
            api_key=self.openai_api_key,
            base_url=self.base_url,
        )
    async def process_query(self, query:str)->str:
        messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ]
        try:
            response = await asyncio.get_event_loop().run_in_executor(
                None, 
                lambda: self.client.chat.completions.create( 
                    model=self.model, 
                    messages=messages
                )
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error processing query: {e}")
            return "An error occurred while processing your request."


    async def chat_loop(self):
        print("MCP CLient is starting! Type 'exit' to quit.")
        while True:
            try:
                query=input("\n你: ").strip()
                if query.lower()=='exit':
                    print("Exiting chat...")
                    break

                response=await self.process_query(query)
            except Exception as e:
                print(f"Error in chat loop: {e}")
                break
            print(f"\nAI: {response}")
        
    async def close(self):
        await self.exit_stack.aclose()

async def main():
    client=MCPClient()
    try:
        await client.chat_loop()
    finally:
        await client.close()

if __name__=='__main__':
    asyncio.run(main())