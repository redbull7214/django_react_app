import {Container, Row, Col} from "reactstrap";
import ListSoftware from "../appListSoftware/ListSoftware";
import axios from "axios";
import {useEffect, useState} from "react";
import ModalSoftware from "../appModalSoftware/ModalSoftware";
import {API_URL} from "../../index";

const Home = () => {
    const [software, setSoftware] = useState([])

    useEffect(()=>{
        if(localStorage.getItem('access_token') === null){
            window.location.href = '/login'  
        }
        else{
        getSoftware()
        }
    },[])
        
    const getSoftware = (data)=>{
        axios.get(API_URL).then(data => setSoftware(data.data))
    }

    const resetState = () => {
        getSoftware();
    };

    return (
        <Container style={{marginTop: "20px"}}>
            <Row>
                <Col>
                    <ListSoftware software={software} resetState={resetState} newSoftware={false}/>
                </Col>
            </Row>
            <Row>
                <Col>
                    <ModalSoftware
                    create={true}
                    resetState={resetState}
                    newSoftware={true}/>
                </Col>
            </Row>
        </Container>
    )
}

export default Home;