import React from 'react';
import ContentBox from './ContentBox';

const contentDatas = [
  { id: 1, title: 'Box 1', content: 'This is the content of Box 1.' },
  { id: 2, title: 'Box 2', content: 'This is the content of Box 2.' },
  { id: 3, title: 'Box 3', content: 'This is the content of Box 3.' },
  { id: 4, title: 'Box 4', content: 'This is the content of Box 4.' },
];

function Container(props) {
  return (
    <>
      {contentDatas.map((data) => (
        <ContentBox key={data.id} title={data.title} content={data.content} />
      ))}
    </>
  );
}

export default Container;
