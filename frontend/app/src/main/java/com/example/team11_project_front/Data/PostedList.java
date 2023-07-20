package com.example.team11_project_front.Data;

public class PostedList {
    private String id;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    private String title;
    private String contents;
    private String created_at;
    private String updated_at;
    private String pictureid;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContents() {
        return contents;
    }

    public void setContents(String contents) {
        this.contents = contents;
    }

    public String getCreated_at() {
        return created_at;
    }

    public void setCreated_at(String created_at) {
        this.created_at = created_at;
    }

    public String getUpdated_at() {
        return updated_at;
    }

    public void setUpdated_at(String updated_at) {
        this.updated_at = updated_at;
    }

    public String getPictureid() {
        return pictureid;
    }

    public void setPictureid(String pictureid) {
        this.pictureid = pictureid;
    }

    public PostedList(String id,String title, String contents, String created_at, String updated_at, String pictureid) {
        this.id = id;
        this.title = title;
        this.contents = contents;
        this.created_at = created_at;
        this.updated_at = updated_at;
        this.pictureid = pictureid;
    }


}
