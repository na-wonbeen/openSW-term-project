import React, { useState, useEffect } from 'react';
import { Card, notification } from 'antd';

function ContentBox(props) {
  const { city } = props;
  // useState Hook으로 날씨 데이터 상태 관리
  const [weatherData, setWeatherData] = useState(null);

  // useEffect Hook으로 openWeathermap API 호출
  useEffect(() => {
    const fetchWeatherData = async () => {
      const API_KEY = process.env.REACT_APP_OPENWEATHERMAP_API_KEY;
      const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;

      try {
        const response = await fetch(url);
        const data = await response.json();
        if (data.cod === 200) {
          // 날씨 데이터 업데이트
          setWeatherData(data);
        } else {
          // API 호출 성공 but, 응답 상태 코드가 올바르지 않은 경우
          throw new Error(data.message || 'Failed to fetch weather data');
        }
      } catch (error) {
        // API 호출 실패
        console.error('Error fetching weather data:', error.message);
        notification.error({
          message: 'Weather Data Fetch Failed',
          description: error.message,
          placement: 'bottom',
          duration: 3,
        });
      }
    };

    // 날씨 데이터 호출
    fetchWeatherData();

    // 1분 간격으로 날씨 업데이트
    const interval = setInterval(() => {
      fetchWeatherData();
    }, 60000);

    // clean-up 함수
    return () => clearInterval(interval);
  }, [city]);

  // 날씨 아이콘 URL 생성
  const weatherIcon = weatherData ? weatherData.weather[0].icon : '';
  const iconUrl = `https://openweathermap.org/img/wn/${weatherIcon}@2x.png`;

  return (
    <Card title={props.title} bordered={true} style={{ borderColor: 'grey' }}>
      <p style={{ fontWeight: 'bolder' }}>도시: {city}</p>
      {weatherData ? (
        <>
          <img
            src={iconUrl}
            alt="data:image/png;base64,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"
          />
          <p>온도: {weatherData.main.temp}°C</p>
          <p>습도: {weatherData.main.humidity}%</p>
          <p>풍속: {weatherData.wind.speed}m/s</p>
        </>
      ) : (
        <p>Weather data is not available.</p>
      )}
    </Card>
  );
}

export default ContentBox;
