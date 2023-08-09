import {Table} from "reactstrap";
import ModalSoftware from "../appModalSoftware/ModalSoftware";
import AppRemoveSoftware from "../appRemoveSoftware/RemoveSoftware";
// import ModalPhoto from "../appPhotoModal/ModalPhoto";

const ListSoftware = (props) => {
    const {software} = props
    return (
        <Table dark>
            <thead>
            <tr>
                <th>Title</th>
                <th>Price</th>
                <th>Currency</th>
                <th>Count</th>
                <th></th>
            </tr>
            </thead>
            <tbody>
            {!software || software.length <= 0 ? (
                <tr>
                    <td colSpan="4" align="center">
                        <b>Пока ничего нет</b>
                    </td>
                </tr>
            ) : software.map(software => (
                    <tr key={software.id}>
                        <td>{software.title}</td>
                        <td>{software.price}</td>
                        <td>{software.currency}</td>
                        <td>{software.count}</td>
                        <td>
                            <ModalSoftware
                                create={false}
                                software={software}
                                resetState={props.resetState}
                                newSoftware={props.newSoftware}
                            />
                            &nbsp;&nbsp;
                            <AppRemoveSoftware
                                id={software.id}
                                resetState={props.resetState}
                            />
                        </td>
                    </tr>
                )
            )}
            </tbody>
        </Table>
    )
}

export default ListSoftware