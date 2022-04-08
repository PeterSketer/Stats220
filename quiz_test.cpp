public class Video{
  private Long id;
  private String title;
  private String content;
  private Set<Comment> comments = new HashWet<>();
};

public class Comment{
  private Video video;
  private String message;
};
