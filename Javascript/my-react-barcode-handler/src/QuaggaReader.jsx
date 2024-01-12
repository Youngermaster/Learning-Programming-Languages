import React, { useEffect, useRef } from "react";
import Quagga from "quagga";

function QuaggaReader({ onDetected }) {
  const scannerRef = useRef(null);

  useEffect(() => {
    Quagga.init(
      {
        inputStream: {
          type: "LiveStream",
          constraints: {
            width: 640,
            height: 480,
            facingMode: "environment", // or user
          },
          target: scannerRef.current, // Pass the DOM node of your choice
        },
        decoder: {
          readers: ["code_128_reader"], // List of active readers
        },
      },
      (err) => {
        if (err) {
          console.log(err);
          return;
        }
        // Start the scanner
        Quagga.start();
      }
    );

    // Register a callback for when a barcode is detected
    Quagga.onDetected((data) => {
      onDetected(data.codeResult.code);
    });

    // Stop the scanner when the component is unmounted
    return () => {
      Quagga.stop();
    };
  }, [onDetected]);

  return <div id="scanner" ref={scannerRef} />;
}

export default QuaggaReader;
