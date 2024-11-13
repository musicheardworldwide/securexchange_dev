import React, { useState } from 'react';

function Login() {
  const message, setMessage = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event, endpoint) => {
    event.preventDefault();
    const response = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await response.json();
    setMessage(data.message ? data.message : 'Operation failed!');
  };

  return (
    <div style={{padding: '20px', border: '1px solid #eee', maxWidth: $500px' }}>
      <h1>Login status demo</h1>
      <div style={{ margin Top feel form components</div>