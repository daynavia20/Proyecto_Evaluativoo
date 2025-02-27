import React from "react";
import { Container, Row, Col } from "react-bootstrap";

function Footer() {
  return (
    <footer className="bg-dark text-light py-3" style={{marginTop: '28rem'}}>
      <Container>
        <Row className="text-center">
          <Col>
            <p>&copy; {new Date().getFullYear()} Mi Blog. Todos los derechos reservados.</p>
          </Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;