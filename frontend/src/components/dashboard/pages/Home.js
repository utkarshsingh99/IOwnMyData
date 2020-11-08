import React from 'react';
import axios from 'axios';
import './home.css';
// import { Timeline, Button, Card } from 'antd';
import {Card, Button, CardContent, CardHeader, CardMedia } from '@material-ui/core'
import { Timeline, TimelineItem, TimelineSeparator, TimelineConnector, TimelineDot, TimelineContent } from '@material-ui/lab';

const reddit="https://external-preview.redd.it/iDdntscPf-nfWKqzHRGFmhVxZm4hZgaKe5oyFws-yzA.png?auto=webp&s=38648ef0dc2c3fce76d5e1d8639234d8da0152b2"
const twitter="https://assets.stickpng.com/images/580b57fcd9996e24bc43c53e.png";

export default class MainPanel extends React.Component {
  constructor(props) {
    super(props)
    this.state={
      reverse: false,
      activity: []
    }
  }
  async componentDidMount() {
    const response = await axios.get('http://127.0.0.1:1244/allactivity?username=utkarshsingh369@gmail.com')
    this.setState({activity: response})
  }

  reverser = (e) => {
    this.setState({reverse: !this.state.reverse})
  }

  render() {
    const activity = this.state.activity.map((post) => {
      const socialAcc = {
        cardTitle: post.social === 'reddit' ? "Reddit post" : "Twitter post",
        avatar: post.social === 'reddit' ? reddit : twitter,
        title: post.title,
        subheader: post.timestamp,
        image: post.media ? post.media : null,
        text: post.text
      }
      return (<Card title={socialAcc.cardTitle} extra={<img src={socialAcc.avatar}/>}>
                    <CardHeader
                      avatar={<img className="header-image" src={reddit}/>}
                      title={socialAcc.title}
                      subheader={socialAcc.subheader}
                    />
                    <CardMedia
                      image={socialAcc.image}
                      className="post-image"
                    />
                    <CardContent>
                      <p>{socialAcc.text}</p>
                    </CardContent>
                  </Card>)
    })
    return (
      <div className="container-fluid background">
        <div className="header text-center">
          <h3 className="title">I Own My Data</h3>
          <p className="category">
          I own all my data.
          </p>
          <Button onClick={this.reverser}>View {this.state.reverse ? 'from the beginning' : 'latest'}</Button>
        </div>
          <div className="parent-scroller">
            <Timeline align="alternate">
              <TimelineItem>
                <TimelineSeparator>
                  <TimelineDot />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent>
                  {activity}
                </TimelineContent>
              </TimelineItem>
            </Timeline>  
          </div>
      </div>
    );
  }
}
