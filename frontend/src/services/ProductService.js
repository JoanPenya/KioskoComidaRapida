import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ProductService{

    constructor(){}


    getProducts() {
        const url = `${API_URL}/api/product/`;
        return axios.get(url).then(response => response.data);
    }

    getProductByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getProduct(id) {
        const url = `${API_URL}/api/product/${id}`;
        return axios.get(url).then(response => response.data);
    }
    deleteProduct(product){
        const url = `${API_URL}/api/product/${product.id}`;
        return axios.delete(url);
    }
    createProduct(product){
        const url = `${API_URL}/api/product/`;
        return axios.post(url,product);
    }
    updateProduct(product){
        const url = `${API_URL}/api/product/${product.id}`;
        return axios.put(url,product);
    }
}