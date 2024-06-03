let nextPageUrl = '/api/books/';
let isLoading = false;

async function fetchBooks(url) {
  if (isLoading || !url) return;
  isLoading = true;
  document.getElementById('loading').style.display = 'block';

  try {
    const response = await fetch(url);
    if (!response.ok) {
      console.error('Failed to fetch books:', response.statusText);
      return;
    }
    const data = await response.json();
    displayBooks(data.results);
    nextPageUrl = data.next; // Assuming your API returns a `next` field for pagination
  } catch (error) {
    console.error('Error fetching books:', error);
  } finally {
    isLoading = false;
    document.getElementById('loading').style.display = 'none';
  }
}

function displayBooks(books) {
  const container = document.getElementById('books-container');
  books.forEach(book => {
    const bookElement = document.createElement('div');
    bookElement.className = 'book';

    const titleElement = document.createElement('h2');
    titleElement.textContent = book.title;
    bookElement.appendChild(titleElement);

    const authorElement = document.createElement('p');
    authorElement.textContent = `Author: ${book.author}`;
    bookElement.appendChild(authorElement);

    if (book.cover) {
      const coverElement = document.createElement('img');
      coverElement.src = book.cover;
      coverElement.alt = `${book.title} cover`;
      bookElement.appendChild(coverElement);
    }

    const genreElement = document.createElement('p');
    genreElement.textContent = `Genre: ${book.genre}`;
    bookElement.appendChild(genreElement);

    const linkElement = document.createElement('a');
    linkElement.href = book.book_file;
    linkElement.target = "_blank";
    linkElement.textContent = 'Download PDF';
    bookElement.appendChild(linkElement);

    container.appendChild(bookElement);
  });
}

function onScroll() {
  if ((window.innerHeight + window.scrollY) >= document.documentElement.scrollHeight - 10 && !isLoading) {
    fetchBooks(nextPageUrl);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  fetchBooks(nextPageUrl);
  window.addEventListener('scroll', onScroll);
});