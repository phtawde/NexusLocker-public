// React to Flask API connection

export async function apiRequest(path, body = null, method = 'GET') {

  // Method to make calling the Flask API easier throughout react

  const response = await fetch(`/api${path}`, {
    method,
    headers: body ? { 'Content-Type': 'application/json' } : {},
    body: body ? JSON.stringify(body) : null,
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.error || 'Failed to fetch');
  }

  return data;
}