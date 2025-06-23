from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from agent_executor import WeatherAgentExecutor

app = FastAPI()
agent = WeatherAgentExecutor()

# ✅ Mount static files at /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Serve index.html manually
@app.get("/", response_class=HTMLResponse)
async def index():
    return FileResponse("static/index.html")

# ✅ Working POST endpoint
@app.post("/execute", response_class=HTMLResponse)
async def execute(request: Request):
    form = await request.form()
    query = form.get("query")
    result = agent.run(query)

    return f"""
    <html>
        <head>
            <title>🌤️ Weather Agent</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="flex items-center justify-center min-h-screen bg-gradient-to-br from-blue-100 to-white">
            <form action="/execute" method="post" class="bg-white p-8 rounded-xl shadow-md w-full max-w-lg space-y-6">
                <h2 class="text-3xl font-bold text-center text-blue-600">🌤️ Weather Agent</h2>

                <input name="query" value="{query}" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-200"/>

                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-lg">
                  Get Weather
                </button>

                <div class="mt-4 bg-gray-50 p-4 rounded-lg border text-gray-800 whitespace-pre-line">
                    <strong>🌦️ Response</strong><br>{result}
                </div>
            </form>
        </body>
    </html>
    """
