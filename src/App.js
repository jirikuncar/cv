import React from 'react';
import logo from './logo.svg';
import { Value, List, useLDflex } from '@solid/react';
import './App.css';


function Name({ tag = 'h1', source = '.' }) {
  const expression = `[${source}].label`;
  const [name, pending, error] = useLDflex(expression);

  if (pending)
    return <span>loading ...</span>;
  if (error)
    return <span>loading failed: {error.message}</span>;

  window.console.log(name);
  return React.createElement(tag, {}, name.toString());
}

class App extends React.Component {
  state = {profile: 'http://profiles.kuncar.dev/jiri/#me'};
  // state = {profile: "https://ruben.verborgh.org/profile/#me"};

  getMetaContentByName(name,content){
    var content = (content==null)?'content':content;
    return document.querySelector("meta[name='"+name+"']").getAttribute(content);
  }

  render() {
    const {profile} = this.state;

    return (
      <Name source={profile} />
    );
  };
}

export default App;
