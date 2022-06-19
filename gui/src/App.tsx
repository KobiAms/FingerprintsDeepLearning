import React, {useCallback, useState} from 'react';
import styles from './styles';
import Axios from "axios";
import axios from "axios"
import {useDropzone} from 'react-dropzone'
import ImagesZone from "./components/images-zone/ImagesZone";
import PredictionsZone from "./components/predictions-zone/PredictionsZone";

const apiURL = 'http://10.0.0.10:5000'

function App() {


    const [file, setFile] = useState<File | undefined>()


    const sendImages = () => {

        // const imagesReady = new FormData()
        // files?.forEach(file => {
        //     imagesReady.append(file.name, file)
        // })
        // console.log(Array.from(imagesReady.entries(), ([key, prop]) => (
        //     {[key]: {
        //             "ContentLength":
        //                 typeof prop === "string"
        //                     ? prop.length
        //                     : prop.size
        //         }
        //     }))
        // )
        //
        // Axios({
        //     url: apiURL+'/api/predictImages',
        //     method: 'post',
        //     withCredentials: true,
        //     data: imagesReady,
        //     headers: {'Content-Type': 'multipart/form-data'}
        // }).then(res => {
        //     console.log(res.data)
        // }).catch(err => {
        //     console.log(err)
        // })

    }


    return (
        <styles.App>
            <styles.Wrapper>
                <ImagesZone setFile={setFile} file={file}/>
                <PredictionsZone/>
            </styles.Wrapper>
        </styles.App>
    );
}

export default App;
