import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";


function RegisterForm({show, onShow}){

  const registerNewUser = () => {
    console.log("Registering...");
    onShow();
  }

  return (
    <>
      <Modal show={show} onHide={onShow} centered>
        <Modal.Header closeButton>
          <Modal.Title>Register Here!</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>

            <Form.Group className="mb-3" controlId="formUsername">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" placeholder="Enter your display name" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Email Address</Form.Label>
              <Form.Control type="email" placeholder="example@example.com" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control type="password" />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formVerifyPassword">
              <Form.Label>Verify Password</Form.Label>
              <Form.Control type="password" />
            </Form.Group>

          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={onShow}>
            Close
          </Button>
          <Button variant="primary" onClick={registerNewUser}>
            Register!
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default RegisterForm;
