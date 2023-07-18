import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Button, View, Platform,TextInput } from 'react-native';
import * as FileSystem from 'expo-file-system';
import { shareAsync } from 'expo-sharing';
import {useState} from 'react';

export default function App() {
  const [text, setText] = useState('');
  const [language, setLanguage] = useState('');
  const [speed, setSpeed] = useState(1);
  
  const downloadFromAPI = async () => {

    const filename = "MissCoding.pdf";
    const localhost = Platform.OS === "android" ? "10.0.2.2" : "127.0.0.1";
    const requestBody = {
      text,
      language,
      speed
    };
    const result = await FileSystem.downloadAsync(
      `http://35.173.186.103:8000/`,
      FileSystem.documentDirectory + filename,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody)
      }
    );
    console.log(result);
    save(result.uri, filename, result.headers["Content-Type"]);
  };

  const save = async (uri, filename, mimetype) => {
    if (Platform.OS === "android") {
      const permissions = await FileSystem.StorageAccessFramework.requestDirectoryPermissionsAsync();
      if (permissions.granted) {
        const base64 = await FileSystem.readAsStringAsync(uri, { encoding: FileSystem.EncodingType.Base64 });
        await FileSystem.StorageAccessFramework.createFileAsync(permissions.directoryUri, filename, mimetype)
          .then(async (uri) => {
            await FileSystem.writeAsStringAsync(uri, base64, { encoding: FileSystem.EncodingType.Base64 });
          })
          .catch(e => console.log(e));
      } else {
        shareAsync(uri);
      }
    } else {
      shareAsync(uri);
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
      <Button title="POST to API" onPress={downloadFromAPI} />
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