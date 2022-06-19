import styled from 'styled-components';


export namespace styles {

    export const App = styled.div`
      width: 100vw;
      height: 100vh;
    `

    export const Wrapper = styled.div`
      height: 100%;
      width: 100%;
      background-color: white;
      display: flex;
      flex-direction: row;
    `
    export const ImagesWrapper = styled.div`
      flex: 2;
      display: flex;
      flex-direction: column;
    `
    export const Manager = styled.div`
      flex: 1;
      display: flex;
    `

    export const ImagesSection = styled.div`
      flex: 1;
      padding: 3% 10%;
    `
    export const Dropzone = styled.div`
      width: 100%;
      min-height: 150px;
      border: 4px gray dashed;
      padding: 10px;
      align-items: center;
      justify-content: center;
    `

    export const ImagesList = styled.div`
      display: flex;
      flex-direction: row;
    `

    export const Img = styled.img`
      flex: 5;
      object-fit: cover;
      overflow: hidden;
    `

    export const ImageName = styled.div`
      flex: 1;
    `

    export const ImageCard = styled.div`
      height: 200px;
      width: 200px;
      border-radius: 5px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    `

    export const ModesList = styled.div`
      flex: 1;
      padding: 3% 10%;
    `
}

export default styles