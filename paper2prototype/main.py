import requests
import arxiv

def get_arxiv_abstract(paper_id):
    search = arxiv.Search(id_list=[paper_id.split('/')[-1]])
    for result in search.results():
        return {
            "title": result.title,
            "summary": result.summary,
            "url": result.entry_id
        }
    return None

def summary(summary):
    url = "https://ai.hackclub.com/chat/completions"
    user_prompt = f"""You are a helpful assistant that writes code summaries of papers. A user will provide an arXiv paper ID, and you will generate a summary of the code in the paper with comments and explanations. Please make sure your summary accurately represents all parts of the paper the user provides. Abstract: {summary}"""
    system_prompt = f"""You are a helpful assistant that writes the accurate code summaries of a paper given to you from arXiv."""
   
    headers = {
        'Content-Type': 'application/json'
    }

    data = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating summary. {e}")
        return None