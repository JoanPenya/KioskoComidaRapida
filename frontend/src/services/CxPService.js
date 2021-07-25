import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class CxPService{

    constructor(){}


    getCxP() {
        const url = `${API_URL}/api/customers/`;
        return axios.get(url).then(response => response.data);
    }
    getCxPByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getCxP(pk) {
        const url = `${API_URL}/api/customers/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteCxP(customer){
        const url = `${API_URL}/api/customers/${customer.pk}`;
        return axios.delete(url);
    }
    createCxP(customer){
        const url = `${API_URL}/api/customers/`;
        return axios.post(url,customer);
    }
    updateCxP(customer){
        const url = `${API_URL}/api/customers/${customer.pk}`;
        return axios.put(url,customer);
    }
}