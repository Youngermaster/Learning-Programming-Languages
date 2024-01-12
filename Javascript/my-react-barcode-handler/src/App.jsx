import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Barcode from "react-barcode";
import JSBarcode from "react-jsbarcode";
import BwipJsExample from "./BwipJsExample";
import QuaggaReader from "./QuaggaReader";

export const BarcodeExample = ({ value }) => {
  return <Barcode value={value} format="upc" />;
};

export const JSBarcodeExample = ({ value }) => {
  return <Barcode value={value} options={{ format: "UPC" }} renderer="svg" />;
};

function App() {
  const handleDetected = (code) => {
    console.log(`Detected barcode: ${code}`);
  };

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
      <h1>Vite + React BarCode usage (Generation & Reading)</h1>
      <BwipJsExample text="788909011562" />
      <br />
      <BarcodeExample value="788909011562" />
      <br />
      <JSBarcodeExample value="788909011562" />
      <br />
      <JSBarcode value="1234567890" />

      <div>
        <QuaggaReader onDetected={handleDetected} />
      </div>
    </>
  );
}

export default App;
