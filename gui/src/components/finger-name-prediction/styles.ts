import styled from 'styled-components';


export namespace styles {

    export const Wrapper = styled.div`
      flex: 4;
      background-color: transparent;
      padding: 20px;
      display: flex;
    `
    export const PredictionWindow = styled.div`
      flex: 1;
      background-color: #FDFDFD;
      display: flex;
      flex-direction: column;
      box-shadow: 0px 3px 6px #00000017;
      border-radius: 10px;
      overflow: hidden;
    `

    export const Header = styled.div`
      flex: 1;
      padding: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      background-color: #FDFDFD;
      box-shadow: 0px 3px 6px #00000017;
      z-index: 1;
    `

    export const Content = styled.div`
      flex: 7;
      padding: 10px;
      background-color: #FDFDFD;
      z-index: 0;
      display: flex;
      flex-direction: column;
    `


}

export default styles