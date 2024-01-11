import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Barcode from "react-barcode";
import JSBarcode from "react-jsbarcode";

export const BarcodeExample = ({ value }) => {
  return <Barcode value={value} format="upc" />;
};

export const JSBarcodeExample = ({ value }) => {
  return <Barcode value={value} options={{ format: "UPC" }} renderer="svg" />;
};

function App() {
  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <BarcodeExample value="788909011562" />
      <br />
      <JSBarcodeExample value="788909011562" />
      <br />
      <JSBarcode value="1234567890" />
    </>
  );
}

export default App;
