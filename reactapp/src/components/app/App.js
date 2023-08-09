import './App.css';
// import {Fragment} from "react";
// import Header from "../appHeader/Header";
// import Home from "../appHome/Home";


import {BrowserRouter, Routes, Route} from 'react-router-dom';
import {Login} from "../appLogin/login";
import Home from "../appHome/Home";
import {Navigation} from '../navigation';
import {Logout} from '../appLogout/logout';

// function App() {
//     return (
//         <Fragment>
//             <Header/>
//             <Home/>
//         </Fragment>
//     );
// }
function App() {
    return <BrowserRouter>
    <Navigation></Navigation>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/logout" element={<Logout/>}/>
        </Routes>
    </BrowserRouter>;
}

export default App;