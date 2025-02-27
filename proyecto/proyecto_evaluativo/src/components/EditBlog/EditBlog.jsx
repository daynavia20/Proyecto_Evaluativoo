import Header from "../Header/Header"
import Footer from "../Footer/Footer"
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Aside_Card from "../Card/Card";

function EditBlog(){
    const TodayDate = new Date();
    const assignedDate = TodayDate.toISOString().split('T')[0];
    return(
        <>
        <Header></Header>
        
        <div className="container mt-5 p-5 mx-auto" style={{border: '1px solid black'}}> 
            <h1 className="text-center">Editar Blog</h1>   
                <Form className="p-5 ml-2" co>
                <Form.Group className="mb-2" controlId="exampleForm.ControlInput1">
                    <Form.Label class>Titulo</Form.Label>
                    <Form.Control type="text" className="w-50" />
                    <Form.Label className="">Texto</Form.Label>
                    <Form.Control type="text" className="w-50"/>
                    <Form.Label class>Autor</Form.Label>
                    <Form.Control type="text" className="w-50" />
                </Form.Group>

                <Button variant="outline-success" className="mt-5 mx-0">Editar</Button>

                </Form>
                <aside>
                <Aside_Card></Aside_Card>
                </aside>
        </div>



        <Footer></Footer>
        </>
    )
}

export default EditBlog;