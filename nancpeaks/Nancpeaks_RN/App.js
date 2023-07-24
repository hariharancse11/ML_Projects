import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Button, View, Platform } from 'react-native';
import * as FileSystem from 'expo-file-system';
import { shareAsync } from 'expo-sharing';

export default function App() {
  const downloadFromAPI = async () => {
    const filename = "MissCoding.pdf";
    const localhost = Platform.OS === "android" ? "10.0.2.2" : "127.0.0.1";

    const payload = {
      text: "Hola Me IIamo Gus Fring, soy de chile",
      language: "es",
      speed: 5.5
    };

    const queryParameters = Object.entries(payload)
      .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
      .join("&");

    const url = `http://35.173.186.103:8000/?${queryParameters}`;

    const response = await fetch(url);
    const content = await response.text();

    // Handle the content as needed
    console.log(content);
  };

  const save = async (uri, filename, mimetype) => {
    // The save function implementation
  };

  return (
    <View style={styles.container}>
      <Button title="Download From API" onPress={downloadFromAPI} />
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
});
