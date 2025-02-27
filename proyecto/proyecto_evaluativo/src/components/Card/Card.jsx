import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

function Card_Autor() {
  return (
    <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="holder.js/100px180"  className='position-start'/>
      <Card.Body>
        <Card.Title>Autor</Card.Title>
        <Card.Text>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure sint deserunt itaque quis delectus sunt alias laborum ipsam quod quo? Dolore consequuntur provident nisi, nam similique ipsa ut voluptatem? Necessitatibus!
        </Card.Text>
        <Button variant="primary">Ver datalles</Button>
      </Card.Body>
    </Card>
  );
}

export default Card_Autor;