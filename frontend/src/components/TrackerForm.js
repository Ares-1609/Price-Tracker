import React, { useState } from "react";
import axios from "axios";
import "./TrackerForm.css";

const TrackerForm = () => {
  const [form, setForm] = useState({
    name: "",
    url: "",
    target_price: "",
    email: "",
  });

  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse(null);
    try {
      const res = await axios.post("http://localhost:5000/track", form);
      setResponse(res.data);
    } catch (err) {
      setResponse({ message: "❌ Something went wrong. Try again later." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>🛍️ Price Tracker</h1>
      <p className="tagline">Track product prices & get alerts when deals hit!</p>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Your Name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <input
          type="url"
          name="url"
          placeholder="Product URL (Amazon/Flipkart)"
          value={form.url}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="target_price"
          placeholder="Target Price (₹)"
          value={form.target_price}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Your Email"
          value={form.email}
          onChange={handleChange}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "⏳ Tracking..." : "Track Price"}
        </button>
      </form>

      {response && (
        <div className="result-box">
          {response.image && (
            <img
              src={response.image}
              alt="Product"
              className="product-image"
            />
          )}
          {response.title && (
            <h2 className="product-title">{response.title}</h2>
          )}
          {response.price && (
            <p className="price">Current Price: ₹{response.price}</p>
          )}
          <p
            className={`message ${
              response.message.includes("✅")
                ? "green"
                : response.message.includes("❌")
                ? "red"
                : "orange"
            }`}
          >
            {response.message}
          </p>
        </div>
      )}
    </div>
  );
};

export default TrackerForm;
