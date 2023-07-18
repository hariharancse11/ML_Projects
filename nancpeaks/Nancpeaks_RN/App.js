import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Button, View, TextInput, Platform } from 'react-native';

export default function App() {
  const [text, setText] = useState('');
  const [language, setLanguage] = useState('');
  const [speed, setSpeed] = useState('');

  const postToAPI = async () => {
    const url = ' http://127.0.0.1:8000/';

    const requestBody = {
      text,
      language,
      speed,
    };

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
      });

      if (response.ok) {
        // Request succeeded
        const result = await response.json();
        console.log(result);
      } else {
        // Request failed
        console.log('Request failed:', response.status);
      }
    } catch (error) {
      console.log('Error:', error.message);
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Enter text"
        value={text}
        onChangeText={setText}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter language"
        value={language}
        onChangeText={setLanguage}
      />
      <TextInput
        style={styles.input}
        placeholder="Enter speed"
        value={speed}
        onChangeText={setSpeed}
      />
      <Button title="POST to API" onPress={postToAPI} />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});
