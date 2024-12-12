import React, { useEffect } from 'react';
import { Card, Col, Row } from 'antd';

function ContentBox(props) {
  const { city } = props;
  const [weather, setWeather] = React.useState(null);

  return (
    <Row gutter={20}>
      <Col span={8}>
        <Card title={props.title} bordered={false}>
          <p>{props.content}</p>
        </Card>
      </Col>
      <Col span={8}>
        <Card title={props.title} bordered={false}>
          <p>{props.content}</p>
        </Card>
      </Col>
      <Col span={8}>
        <Card title={props.title} bordered={false}>
          <p>{props.content}</p>
        </Card>
      </Col>
    </Row>
  );
}

export default ContentBox;
