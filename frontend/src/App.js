// src/App.js
import React, { createContext } from 'react';
import NavBar from './components/NavBar';
import styles from './App.module.css';
import Container from 'react-bootstrap/Container';
import { Route, Switch } from 'react-router-dom';
import SignUpForm from './pages/auth/SignUpForm';
import SignInForm from './pages/auth/SignInForm';
import PostCreateForm from './pages/recipe-posts/PostCreateForm';
import RecipePostPage from './pages/recipe-posts/RecipePostPage';
import PostsPage from './pages/recipe-posts/PostsPage';
import { useCurrentUser } from './contexts/CurrentUserContext';



function App() {
  const currentUser = useCurrentUser();
  const profile_id = currentUser?.profile?.id || "";


  return (
    <div className={styles.App}>
      <NavBar />
      <Container className={styles.Main}>
        <Switch>
          <Route exact path="/"
            render={() => (
              <PostsPage
                message='No results found. Adjust keyword' />
            )}
          />
          <Route exact path="/feed"
            render={() => (
              <PostsPage
                message='No results found. Adjust keyword or follow a user'
                filter={`user__followed__user__profile=${profile_id}&`} />
            )}
          />
          <Route exact path="/favorites"
            render={() => (
              <PostsPage
                message='No results found. Adjust keyword or like a post'
                filter={`likes__owner__profile=${profile_id}&ordering=-likes__created_at&`} />
            )}
          />
          <Route exact path="/signin" render={() => <SignInForm />} />
          <Route exact path="/signup" render={() => <SignUpForm />} />
          < Route exact path="/recipe-posts/create" render={() => <PostCreateForm />} />
          <Route exact path="/recipe-posts/:id" render={() => <RecipePostPage />} />
          <Route render={() => <h3>Page not found!</h3>} />
        </Switch>
      </Container>
    </div>

  );
}

export default App;
