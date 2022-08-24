import React from 'react';
import Header from './Header';
import Footer from './Footer';
import ConnectApi from '../services/ConnectApi';

const Home = () => {
    const API_URL = "http://127.0.0.1:8000/personality/";
    const [dataState] = ConnectApi(API_URL);

    console.log(dataState)

  return (
    <div>
        <Header/>
        <Footer/>
    </div>
  )
}

export default Home