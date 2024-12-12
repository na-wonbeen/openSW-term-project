import React from 'react';
import { Row, Col } from 'antd';
import ContentBox from './ContentBox';

const cities = [
  { id: 1, city: 'Seoul' },
  { id: 2, city: 'Tokyo' },
  { id: 3, city: 'New York' },
  { id: 4, city: 'Beijing' },
  { id: 5, city: 'London' },
  { id: 6, city: 'Sydney' },
];

function Container() {
  return (
    <div style={{ padding: '20px' }}>
      <Row gutter={[16, 16]}>
        {cities.map((data) => (
          <Col key={data.id} xs={12} sm={12} md={8} lg={8}>
            <ContentBox city={data.city} />
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default Container;
