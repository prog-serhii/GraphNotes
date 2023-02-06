import http from "@/http-common";


class NotesDataService {
  getAll() {
    return http.get("/notes");
  }

  get(id) {
    return http.get(`/notes/${id}`)
  }
}

export default new NotesDataService();