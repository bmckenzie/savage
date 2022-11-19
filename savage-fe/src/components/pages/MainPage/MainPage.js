import logo from "../../atoms/logo.png";

import Image from "react-bootstrap/Image";
import Stack from "react-bootstrap/Stack";
import Button from "react-bootstrap/Button";
import RegisterForm from "../../molecules/RegisterForm/RegisterForm";

import { useState } from "react";

function MainPage() {
  const [showRegModal, setRegModal] = useState(false);

  const toggleModal = () => {
    setRegModal(showRegModal => !showRegModal);
  };

  return (
    <div>
      <Image src={logo} alt="logo" className="mx-auto d-block" />
      <Stack gap={2} className="col-md-5 mx-auto">
        <RegisterForm show={showRegModal} onShow={toggleModal}/>
        <Button variant="primary" onClick={toggleModal}>
          Register
        </Button>
        <Button variant="primary">Log In</Button>
      </Stack>
    </div>
  );
}

export default MainPage;
