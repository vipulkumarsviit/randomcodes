### Enabling Auditing in Spring Boot
#### 1. AuditModel
```
    package com.example.jpa.model;
    import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
    import org.springframework.data.annotation.CreatedDate;
    import org.springframework.data.annotation.LastModifiedDate;
    import org.springframework.data.jpa.domain.support.AuditingEntityListener;
    import javax.persistence.*;
    import javax.validation.constraints.NotNull;
    import java.io.Serializable;
    import java.util.Date;

    @MappedSuperclass
    @EntityListeners(AuditingEntityListener.class)
    @JsonIgnoreProperties(
            value = {"createdAt", "updatedAt"},
            allowGetters = true
    )
    public abstract class AuditModel implements Serializable {
        @Temporal(TemporalType.TIMESTAMP)
        @Column(name = "created_at", nullable = false, updatable = false)
        @CreatedDate
        private Date createdAt;
    
        @Temporal(TemporalType.TIMESTAMP)
        @Column(name = "updated_at", nullable = false)
        @LastModifiedDate
        private Date updatedAt;
    
        public Date getCreatedAt() {
            return createdAt;
        }
    
        public void setCreatedAt(Date createdAt) {
            this.createdAt = createdAt;
        }
    
        public Date getUpdatedAt() {
            return updatedAt;
        }
    
        public void setUpdatedAt(Date updatedAt) {
            this.updatedAt = updatedAt;
        }
    }
```
#### 2. Enabling JPA Auditing
```
    package com.example.jpa;
    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.data.jpa.repository.config.EnableJpaAuditing;
    
    @SpringBootApplication
    @EnableJpaAuditing
    public class DemoApplication {
        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }
    }
```

#### 3. Post model 
```
    @Entity
    @Table(name = "posts")
    public class Model1 extends AuditModel {}
```

```
    @Entity
    @Table(name = "comments")
    public class Model2 extends AuditModel {}
```



    
