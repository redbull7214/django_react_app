import {useEffect, useState} from "react";
import {Button, Form, FormGroup, Input, Label} from "reactstrap";
import axios from "axios";
import {API_URL} from "../../index";

const SoftwareForm = (props) => {
    const [software, setSoftware] = useState({})

    const onChange = (e) => {
        const newState = software
        if (e.target.name === "file") {
            newState[e.target.name] = e.target.files[0]
        } else newState[e.target.name] = e.target.value
        setSoftware(newState)
    }

    useEffect(() => {
        if (!props.newSoftware) {
            setSoftware(software => props.software)
        }
        // eslint-disable-next-line
    }, [props.software])


    const defaultIfEmpty = value => {
        return value === "" ? "" : value;
    }

    const submitDataEdit = async (e) => {
        e.preventDefault();
        // eslint-disable-next-line
        const result = await axios.put(API_URL + software.id, software, {headers: {'Content-Type': 'multipart/form-data'}})
            .then(() => {
                props.resetState()
                props.toggle()
            })
    }
    const submitDataAdd = async (e) => {
        e.preventDefault();
        const data = {
            title: software['title'],
            price: software['price'],
            currency: software['currency'],
            count: software['count']
        }
        // eslint-disable-next-line
        const result = await axios.post(API_URL, data, {headers: {'Content-Type': 'multipart/form-data'}})
            .then(() => {
                props.resetState()
                props.toggle()
            })
    }
    return (
        <Form onSubmit={props.newSoftware ? submitDataAdd : submitDataEdit}>
            <FormGroup>
                <Label for="title">Title:</Label>
                <Input
                    type="text"
                    name="title"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(software.title)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="price">Price:</Label>
                <Input
                    type="text"
                    name="price"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(software.price)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="currency">Currency:</Label>
                <Input
                    type="text"
                    name="currency"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(software.currency)}
                />
            </FormGroup>
            <FormGroup>
                <Label for="count">Count:</Label>
                <Input
                    type="text"
                    name="count"
                    onChange={onChange}
                    defaultValue={defaultIfEmpty(software.count)}
                />
            </FormGroup>
            <div style={{display: "flex", justifyContent: "space-between"}}>
                <Button>Send</Button> <Button onClick={props.toggle}>Cancel</Button>
            </div>
        </Form>
    )
}

export default SoftwareForm;