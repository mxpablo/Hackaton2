import React, { Component } from 'react';
import DatePicker from 'react-datepicker';
import moment from 'moment'

class EssayForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            mensaje: '',
            datetime: moment(),
            nombre: '',
            colonia: '',
            estado: '',
            telefono: '',
            street: '',
            imagen: ''

        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({
            mensaje: event.target.value
        });
    }

    handleChangeNombre = (event) => {
        this.setState({
            nombre: event.target.value
        });
    }

    handleChangeStreet = (event) => {
        this.setState({
            street: event.target.value
        });
    }

    handleChangeColonia = (event) => {
        this.setState({
            colonia: event.target.value
        })
    }

    handleChangeEstado = (event) => {
        this.setState({
            estado: event.target.value
        })
    }

    handleChangeTelefono = (event) => {
        this.setState({
            telefono: event.target.value
        })
    }


    handleChangeDate = (event) => {
        this.setState({
            datetime: event.target.value
        })
    }

    handleChangeImagen = (event) => {
        this.setState({
            imagen: event.target.value
        })
    }

    handleSubmit(event) {

        let json = {
            nombre: this.state.nombre,
            lugar: this.state.street + ' ' + this.state.colonia + ' ' + this.state.estado,
            telefono: this.state.telefono,
            mensaje: this.state.mensaje,
            datetime: this.state.datetime,
            imagen: this.state.imagen
        };
        alert('An essay was submitted: ' + this.state.mensaje);
        console.log(JSON.stringify(json))

        fetch('http://f4a27278.ngrok.io/api/v1/posada/',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(json)
            })

        event.preventDefault();

    }

    render() {
        return (
            <form onSubmit={this.handleSubmit} class="form-horizontal">
                <div class="form-group">
                    <label for="name">Ponle nombre a tu posada:</label>
                    <input type="text" class="form-control" value={this.state.nombre} onChange={this.handleChangeNombre} />
                </div>

                <div class="form-group">
                    <label for="date">¿Cuándo será?</label>
                    <input type="text" class="form-control" value={this.state.datetime} onChange={this.handleChangeDate} />
                </div>

                <h3><label for="place">¿Donde será?</label></h3>
                <div class="form-group">
                    <label for="place">Calle</label>
                    <input type="text" class="form-control" value={this.state.street} onChange={this.handleChangeStreet} />
                </div>

                <div class="form-group">
                    <label for="colonia">Colonia</label>
                    <input type="text" class="form-control" value={this.state.colonia} onChange={this.handleChangeColonia} />
                </div>

                <div class="form-group">
                    <label for="state">Estado</label>
                    <input type="text" class="form-control" value={this.state.estado} onChange={this.handleChangeEstado} />
                </div>

                <div class="form-group">
                    <label for="state">URL de imágen</label>
                    <input type="text" class="form-control" value={this.state.imagen} onChange={this.handleChangeImagen} />
                </div>

                <div class="form-group">
                    <label for="place">Teléfono de contacto</label>
                    <input type="number" class="form-control" value={this.state.telefono} onChange={this.handleChangeTelefono} />
                </div>

                <div class="form-group" >
                    <label>Mensaje</label>
                    <textarea class="form-control" rows="5" id="comment" value={this.state.mensaje} onChange={this.handleChange} />
                </div>
                <button type="submit" class="btn btn-default">Crear</button>
            </form>
        );
    }
}

export default EssayForm