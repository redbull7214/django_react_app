import {Fragment, useState} from "react";
import {Button, Modal, ModalHeader, ModalBody} from "reactstrap";
import SoftwareForm from "../appSoftwareForm/SoftwareForm";

const ModalSoftware = (props) => {
    const [visible, setVisible] = useState(false)
    var button = <Button onClick={() => toggle()}>Edit</Button>;

    const toggle = () => {
        setVisible(!visible)
    }

    if (props.create) {
        button = (
            <Button
                color="primary"
                className="float-right"
                onClick={() => toggle()}
                style={{minWidth: "200px"}}>
                Add Software
            </Button>
        )
    }
    return (
        <Fragment>
            {button}
            <Modal isOpen={visible} toggle={toggle}>
                <ModalHeader
                    style={{justifyContent: "center"}}>{props.create ? "Add Software" : "Edit Software"}</ModalHeader>
                <ModalBody>
                    <SoftwareForm
                        software={props.software ? props.software : []}
                        resetState={props.resetState}
                        toggle={toggle}
                        newSoftware={props.newSoftware}
                    />
                </ModalBody>
            </Modal>
        </Fragment>
    )
}
export default ModalSoftware;