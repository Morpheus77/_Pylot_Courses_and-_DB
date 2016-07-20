from system.core.model import Model
class Course(Model):
	def__init__(self):
		super(Course,self).__init__()

	def get_all_courses(self):
		return self.db.query_db("SELECT * FROM courses")
	
	def get_course_by_id(self,course_id):
		#pass data to the query like so
		query = "select * from courses where id = :course_id"
		data = { 'course_id':course_id}
		return self.db.query_db(query,data)

	def add_course(self,course):
		#build the query first and then the data that goes in the query
		query = "insert into courses(title, description,created_at) values (:title, :description, now())"
		data = { 'title': course['title'], 'description': course['descripttion, '}
		return self.db.query_db(query,data)

	def update_course(self,course):
		#building the query for the update
		query = "update course set title=:title, description=:description where id =:course_id"
		data = {'title': course['title'], 'description' : course['description'],'course_id' : course[id]}
		#run the update
		return self.db.query_db(query,data)

		def delete_course(self,course_id):
			query = "delete from course where id = :course_id"
			data = {"course_id": course_id}
			return self.db.query_db(query,data

