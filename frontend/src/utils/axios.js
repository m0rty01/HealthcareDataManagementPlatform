import axios from 'axios';

const instance = axios.create({
  baseURL: (process.env.REACT_APP_API_URL || 'http://localhost:8000') + '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
  // Don't override Content-Type if it's already set
  validateStatus: (status) => status < 500,
});

export default instance;