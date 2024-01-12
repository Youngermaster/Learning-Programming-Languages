import React, { useEffect, useRef } from "react";
import bwipjs from "bwip-js";

function BwipJsExample({ text }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    bwipjs.toCanvas(canvasRef.current, {
      bcid: "upca", // Barcode type
      text: text, // Text to encode
      scale: 3, // 3x scaling factor
      height: 15, // Bar height, in millimeters
      includetext: true, // Show human-readable text
      textxalign: "center", // Always good to set this
    });
  }, [text]);

  return <canvas ref={canvasRef} />;
}

export default BwipJsExample;
