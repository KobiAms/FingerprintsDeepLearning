import styled from 'styled-components';


export namespace styles {

    export const Wrapper = styled.div`
      width: 100%;
      height: min-content;
      background-color: transparent;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
    `
    export const ResultAndIcon = styled.div`
      flex: 1;
      padding: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: start;
    `
    export const Title = styled.div`
      flex: 1;
      padding: 10px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: end;
      font-size: 20px;
      color: black;
      
    `
}

export default styles