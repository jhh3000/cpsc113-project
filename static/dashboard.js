// tutorial1.js
var CommentBox = React.createClass({
  render: function() {
    return (
      <div className="info">
        Hello, world! This is ReactJS!
      </div>
    );
  }
});
ReactDOM.render(
  <CommentBox />,
  document.getElementById('content')
);