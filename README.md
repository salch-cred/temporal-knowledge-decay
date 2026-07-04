# Temporal Knowledge Decay

An ML algorithm to model and predict the expiration probability (decay rate) of dynamic facts stored in static knowledge graphs.

Useful for keeping large linguistic models and semantic systems synchronized with real-world transitions.

## Usage
```bash
python examples/evaluate_decay.py
```


## FastAPI API Service
The project includes a FastAPI server wrapper. 

### Running the API
```bash
uvicorn src.api:app --host 0.0.0.0 --port 8000
```
- **Interactive docs**: Navigate to `/docs` for swagger documentation.
- **POST `/survival`**: Forecast semantic relationship validation status over time.
