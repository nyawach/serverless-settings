const AWS = require("aws-sdk")

AWS.config.update({region: "ap-northeast-1"})

const sqs = new AWS.SQS({apiVersion: '2012-11-05'})

const QueueUrl = process.env.QUEUE_URL

exports.handler = async (event, context) => {
  const MessageBody = JSON.stringify({
    'staus': 'success!',
  })
  const params = {
    MessageBody,
    QueueUrl,
  }
  const res = await sqs.sendMessage(params).promise()
  console.log(res)
  return {
    statusCode: 200,
    body: res,
    headers: {
      'Content-Type': 'application/json',
    },
  }
}
