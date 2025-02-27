import Header from "../Header/Header";
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Footer from "../Footer/Footer";

function CreateBlog(){
    const TodayDate = new Date();
    const assignedDate = TodayDate.toISOString().split('T')[0];
    return(
        <>
        <Header>

        </Header>
        <div className="container mt-5 p-5" style={{border : '1px solid black'}}> 
            <h1 className="text-center">Crear Blog</h1>   
                <Form className="p-5">
                <Form.Group className="mb-2" controlId="exampleForm.ControlInput1">
                    <Form.Label class>Titulo</Form.Label>
                    <Form.Control type="text" />
                    <Form.Label class>Texto</Form.Label>
                    <Form.Control type="text"/>
                    <Form.Label class>Autor</Form.Label>
                    <Form.Control type="text" />
                    
                </Form.Group>

                <Button variant="outline-success">Crear</Button>

                </Form>
        </div>
        <Footer></Footer>
        </>
    )
}

export default CreateBlog;