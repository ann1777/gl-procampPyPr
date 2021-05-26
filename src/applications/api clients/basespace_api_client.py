import public as public

public class BaseApiTest {
    private static RequestSpecification requestSpecification;
    private static ResponseSpecification responseSpecification;
    @BeforeClass
    public void setup() {
        requestSpecification = given().auth()
                .preemptive()
                .basic(ProjectProperties.getProperties().getProperty("name"), ProjectProperties.getProperties().getProperty("password"))
                .baseUri(BASE_URI)
                .basePath(BASE_PATH);

        RestAssured.requestSpecification = requestSpecification;

        responseSpecification = new ResponseSpecBuilder().expectStatusCode(CODE_200)
                .expectResponseTime(lessThan(3000L))
                .build();

        RestAssured.requestSpecification = requestSpecification;
        RestAssured.responseSpecification = responseSpecification;


