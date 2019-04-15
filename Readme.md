# Project description:  

Cart tracker.  

## Project configuration:  

(a) Clone repository.  
(b) Install docker and docker-compose.  

## Running application:  

```bash
sudo docker-compose up --build
```

## Running tests:  

```bash
sudo docker-compose run web pytest
```

## API:

### Item endpoint:  

* **URL**  

	localhost:8000/v1/trackers/item

* **Method POST**

* **Data**    

```json
{    
	"external_id": <string>,    
	"name": <string|optional>,    
	"value": <integer|optional>    
}    
```    

* **Success Response:**  

	* **Code:** 204  