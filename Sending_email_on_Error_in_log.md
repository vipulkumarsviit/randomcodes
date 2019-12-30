## SMTPAppender for Gmail

```<appender name="emailAppender" class="ch.qos.logback.classic.net.SMTPAppender">
    <smtpHost>smtp.gmail.com</smtpHost>
    <smtpPort>587</smtpPort>
    <STARTTLS>true</STARTTLS>
    <asynchronousSending>false</asynchronousSending>
    <username>SENDER-EMAIL@gmail.com</username>
    <password>GMAIL-ACCT-PASSWORD</password>
    <to>EMAIL-RECIPIENT</to>
    <from>SENDER-EMAIL@gmail.com</from>
    <subject>BAELDUNG: %logger{20} - %msg</subject>
    <layout class="ch.qos.logback.classic.html.HTMLLayout"/>
</appender>```

https://www.baeldung.com/logback-send-email
