import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Login } from "../appLogin/login";
import Home from "../appHome/Home";
import { Navigation } from '../navigation';
import { Logout } from '../appLogout/logout';

function App() {
    return <BrowserRouter>
        <Navigation></Navigation>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/logout" element={<Logout />} />
        </Routes>
    </BrowserRouter>;
}

export default App;