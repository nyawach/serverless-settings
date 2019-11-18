exports.handler = async (event, context) => {
  console.log(event)
  event.Records.forEach(record => {
    const { body } = record;
    console.log(body);
  });
  return {};
}
