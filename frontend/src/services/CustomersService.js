import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ProductService{

    constructor(){}


    getProduct() {
        const url = `${API_URL}/api/customers/`;
        return axios.get(url).then(response => response.data);
    }
    getProductByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getProduct(pk) {
        const url = `${API_URL}/api/customers/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteProduct(customer){
        const url = `${API_URL}/api/customers/${customer.pk}`;
        return axios.delete(url);
    }
    createProduct(customer){
        const url = `${API_URL}/api/customers/`;
        return axios.post(url,customer);
    }
    updateProduct(customer){
        const url = `${API_URL}/api/customers/${customer.pk}`;
        return axios.put(url,customer);
    }
}