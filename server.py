import requests
from datetime import datetime
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")
from pydantic import BaseModel, Field
from typing import Union
from typing import Annotated

mcp = FastMCP('linkedin-data-api')

@mcp.tool()
def get_profile_data(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get all profile data, including experience, skills, language, education, course, and companies, **open to work** status, hiring status, location. Check **Example Responses** for more details'''
    url = 'https://linkedin-data-api.p.rapidapi.com/'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_data_by_url(url: Annotated[str, Field(description='')]) -> dict: 
    '''Get all profile data, including experience, skills, language, education, course, and companies, **open to work** status, hiring status, location. Check **Example Responses** for more details'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-data-by-url'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_people(keywords: Annotated[str, Field(description='')] = None,
                  start: Annotated[str, Field(description='it could be one of these; 0, 10, 20, 30, etc.')] = None,
                  geo: Annotated[str, Field(description='please follow this link to find location id')] = None,
                  schoolId: Annotated[str, Field(description='')] = None,
                  firstName: Annotated[str, Field(description='')] = None,
                  lastName: Annotated[str, Field(description='')] = None,
                  keywordSchool: Annotated[str, Field(description='')] = None,
                  keywordTitle: Annotated[str, Field(description='')] = None,
                  company: Annotated[str, Field(description='Company name')] = None) -> dict: 
    '''Search LinkedIn profiles by a keyword. You may see less than 10 results per page. This is because LinkedIn does not return all profiles as public, sometimes hiding profiles and these profiles appear as "LinkedIn Member" in the result. The endpoint automatically filters these profiles from the result'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-people'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keywords': keywords,
        'start': start,
        'geo': geo,
        'schoolId': schoolId,
        'firstName': firstName,
        'lastName': lastName,
        'keywordSchool': keywordSchool,
        'keywordTitle': keywordTitle,
        'company': company,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_people_by_url() -> dict: 
    '''Search People by URL. You may see less than 10 results per page. This is because LinkedIn does not return all profiles as public, sometimes hiding profiles and these profiles appear as "LinkedIn Member" in the result. The endpoint automatically filters these profiles from the result'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-people-by-url'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_recent_activity_time(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get the time of the profile's last activity'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-recent-activity-time'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_sposts(username: Annotated[str, Field(description='')],
                       start: Annotated[str, Field(description='use this param to get posts in next results page: 0 for page 1, 50 for page 2 100 for page 3, etc.')] = None,
                       paginationToken: Annotated[str, Field(description='It is required when fetching the next results page. The token from the previous call must be used.')] = None,
                       postedAt: Annotated[str, Field(description='It is not an official filter. It filters posts after fetching them from LinkedIn and returns posts that are newer than the given date. Example value: 2024-01-01 00:00')] = None) -> dict: 
    '''Get last 50 posts of a profile. 1 credit per call'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-posts'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'start': start,
        'paginationToken': paginationToken,
        'postedAt': postedAt,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_post_and_comments(urn: Annotated[str, Field(description='URN value of the post. Example URL: https://www.linkedin.com/posts/andy-jassy-8b1615_amazon-bedrock-customers-have-more-choice-activity-7181285160586211328-Idxl/?utm_source=share&utm_medium=member_desktop Example URN: 7181285160586211328')]) -> dict: 
    '''Get profile post and comments of the post'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-post-and-comments'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'urn': urn,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_post_comment(urn: Annotated[str, Field(description='Post urn value')],
                             sort: Annotated[str, Field(description='it could be one of these; mostRelevant, mostRecent')],
                             page: Annotated[str, Field(description='')] = None,
                             paginationToken: Annotated[str, Field(description='It is required when fetching the next results page. The token from the previous call must be used.')] = None) -> dict: 
    '''Get 50 comments of a profile post (activity)'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-posts-comments'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'urn': urn,
        'sort': sort,
        'page': page,
        'paginationToken': paginationToken,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_scomments(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get last 50 comments of a profile. 1 credit per call'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-comments'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_connection_follower_count(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Profile Connection & Follower Count'''
    url = 'https://linkedin-data-api.p.rapidapi.com/connection-count'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_data_and_connection_follower_count(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Profile Data and Connection & Follower Count'''
    url = 'https://linkedin-data-api.p.rapidapi.com/data-connection-count'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_given_recommendations(username: Annotated[str, Field(description='')],
                              start: Annotated[str, Field(description='')] = None) -> dict: 
    '''To scrape all recommendations from a profile, increase the start value to +100 for each request until you reach the total recommendations count. You can find the total recommendations count in the response'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-given-recommendations'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'start': start,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_reactions(username: Annotated[str, Field(description='')],
                          start: Annotated[str, Field(description='for pagination, increase +100 to parse next result until you see less than 100 results. it could be one of these; 0, 100, 200, 300, 400, etc.')] = None,
                          paginationToken: Annotated[str, Field(description='It is required when fetching the next results page. The token from the previous call must be used.')] = None) -> dict: 
    '''Find out what posts a profile reacted to'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-profile-likes'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'start': start,
        'paginationToken': paginationToken,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def about_the_profile(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get profile verification details, profile’s joined, contact information updated, and profile photo updated date'''
    url = 'https://linkedin-data-api.p.rapidapi.com/about-this-profile'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_data_connection_follower_count_and_posts(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Profile Data, Connection & Follower Count and Posts. 2 credits per call'''
    url = 'https://linkedin-data-api.p.rapidapi.com/profile-data-connection-count-posts'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def profile_data_recommendations(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Profile Data, Given and Received Recommendations. **2 credits per call**'''
    url = 'https://linkedin-data-api.p.rapidapi.com/all-profile-data'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_similar_profiles(url: Annotated[str, Field(description='')]) -> dict: 
    '''Returns profiles that are similar to the provided LinkedIn profile'''
    url = 'https://linkedin-data-api.p.rapidapi.com/similar-profiles'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_positions_with_skills(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Profile Positions With Skills'''
    url = 'https://linkedin-data-api.p.rapidapi.com/profiles/position-skills'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_company_interest() -> dict: 
    '''Get the profile's company interests up to 50 results per page.'''
    url = 'https://linkedin-data-api.p.rapidapi.com/profiles/interests/companies'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_top_position(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get profile top position'''
    url = 'https://linkedin-data-api.p.rapidapi.com/profiles/positions/top'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_details(username: Annotated[str, Field(description='')]) -> dict: 
    '''The endpoint returns full details of the LinkedIn company details + Crunchbase url in JSON format'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-details'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_details_by_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''The endpoint returns full details of the LinkedIn company details + Crunchbase url in JSON format'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-details-by-id'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_companies() -> dict: 
    '''Search companies'''
    url = 'https://linkedin-data-api.p.rapidapi.com/companies/search'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_jobs() -> dict: 
    '''Get company jobs'''
    url = 'https://linkedin-data-api.p.rapidapi.com/company-jobs'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_by_domain(domain: Annotated[str, Field(description='')]) -> dict: 
    '''Get a company's LinkedIn data by domain. **1 credit per successful request.**'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-by-domain'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_insights_premium(username: Annotated[str, Field(description='')]) -> dict: 
    '''Get Company Insight Details & Company Details in a single request. **5 credit per call.** If the request fails, you don't pay.'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-insights'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_employees_count() -> dict: 
    '''Get company employees count (location filter possible)'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-employees-count'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_jobs_count(companyId: Annotated[str, Field(description='')]) -> dict: 
    '''Get total number of opening jobs the company'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-jobs-count'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'companyId': companyId,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_pages_people_also_viewed(username: Annotated[str, Field(description='')] = None) -> dict: 
    '''Get Company Pages People Also Viewed'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-pages-people-also-viewed'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_spost(username: Annotated[str, Field(description='')],
                      start: Annotated[str, Field(description='use this param to get posts in next results page: 0 for page 1, 50 for page 2, 100 for page 3, etc.')] = None,
                      paginationToken: Annotated[str, Field(description='It is required when fetching the next results page. The token from the previous call must be used.')] = None) -> dict: 
    '''Get last 50 posts of a company. 1 credit per call'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-posts'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
        'start': start,
        'paginationToken': paginationToken,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_company_post_comments(urn: Annotated[str, Field(description='')],
                              sort: Annotated[str, Field(description='')],
                              page: Annotated[str, Field(description='')] = None) -> dict: 
    '''Get comments of a company post'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-company-post-comments'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'urn': urn,
        'sort': sort,
        'page': page,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def find_email_address(url: Annotated[str, Field(description='')]) -> dict: 
    '''Find email address of a LinkedIn profile by LinkedIn profile URL. Initiating the request costs **2 credits**. If there is an email in the result **+1 credit** will be consumed.'''
    url = 'https://linkedin-data-api.p.rapidapi.com/linkedin-to-email'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_jobs(keywords: Annotated[str, Field(description='')],
                locationId: Annotated[Union[int|float], Field(description='please follow this link to find location id')] = None,
                companyIds: Annotated[str, Field(description='please follow this link to find company id')] = None,
                datePosted: Annotated[str, Field(description='it could be one of these; anyTime, pastMonth, pastWeek, past24Hours')] = None,
                salary: Annotated[str, Field(description='it could be one of these; 40k+, 60k+, 80k+, 100k+, 120k+, 140k+, 160k+, 180k+, 200k+ Example: 80k+')] = None,
                jobType: Annotated[str, Field(description='it could be one of these; fullTime, partTime, contract, internship Example: contract')] = None,
                experienceLevel: Annotated[str, Field(description='it could be one of these; internship, associate, director, entryLevel, midSeniorLevel. executive example: executive')] = None,
                titleIds: Annotated[str, Field(description='please follow this link to find title id by title')] = None,
                functionIds: Annotated[str, Field(description='please follow this link to find function id')] = None,
                start: Annotated[str, Field(description='it could be one of these; 0, 25, 50, 75, 100, etc. The maximum number of start is 975')] = None,
                industryIds: Annotated[str, Field(description='please follow this link to find industry id')] = None,
                onsiteRemote: Annotated[str, Field(description='it could be one of these;')] = None,
                sort: Annotated[str, Field(description='it could be one of these; mostRelevant, mostRecent')] = None) -> dict: 
    '''Search Jobs'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-jobs'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keywords': keywords,
        'locationId': locationId,
        'companyIds': companyIds,
        'datePosted': datePosted,
        'salary': salary,
        'jobType': jobType,
        'experienceLevel': experienceLevel,
        'titleIds': titleIds,
        'functionIds': functionIds,
        'start': start,
        'industryIds': industryIds,
        'onsiteRemote': onsiteRemote,
        'sort': sort,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_job_details(id: Annotated[Union[int|float], Field(description='Default: 4090994054')]) -> dict: 
    '''Get the full job details, including the job skills and the company information'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-job-details'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_jobs_v2(keywords: Annotated[str, Field(description='')],
                   locationId: Annotated[Union[int|float], Field(description='please follow this link to find location id')] = None,
                   companyIds: Annotated[str, Field(description='please follow this link to find company id')] = None,
                   datePosted: Annotated[str, Field(description='it could be one of these; anyTime, pastMonth, pastWeek, past24Hours')] = None,
                   salary: Annotated[str, Field(description='it could be one of these; 40k+, 60k+, 80k+, 100k+, 120k+, 140k+, 160k+, 180k+, 200k+ Example: 80k+')] = None,
                   jobType: Annotated[str, Field(description='it could be one of these; fullTime, partTime, contract, internship Example: contract')] = None,
                   experienceLevel: Annotated[str, Field(description='it could be one of these; internship, associate, director, entryLevel, midSeniorLevel. executive example: executive')] = None,
                   titleIds: Annotated[str, Field(description='please follow this link to find title id by title')] = None,
                   functionIds: Annotated[str, Field(description='please follow this link to find function id')] = None,
                   start: Annotated[str, Field(description='it could be one of these; 0, 50, 100, 150, 200, etc. The maximum number of start is 975')] = None,
                   industryIds: Annotated[str, Field(description='please follow this link to find industry id')] = None,
                   onsiteRemote: Annotated[str, Field(description='it could be one of these;')] = None,
                   sort: Annotated[str, Field(description='it could be one of these; mostRelevant, mostRecent')] = None,
                   distance: Annotated[str, Field(description='0 = 0km')] = None) -> dict: 
    '''Search Jobs'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-jobs-v2'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keywords': keywords,
        'locationId': locationId,
        'companyIds': companyIds,
        'datePosted': datePosted,
        'salary': salary,
        'jobType': jobType,
        'experienceLevel': experienceLevel,
        'titleIds': titleIds,
        'functionIds': functionIds,
        'start': start,
        'industryIds': industryIds,
        'onsiteRemote': onsiteRemote,
        'sort': sort,
        'distance': distance,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_hiring_team(id: Annotated[str, Field(description='LinkedIn job id')] = None,
                    url: Annotated[str, Field(description='LinkedIn job url')] = None) -> dict: 
    '''Get hiring team/job poster profile details. You can use either a job id or a job URL. One of these is required.'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-hiring-team'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_profile_sposted_jobs(username: Annotated[str, Field(description='LinkedIn job id')]) -> dict: 
    '''Get profile's posted jobs.'''
    url = 'https://linkedin-data-api.p.rapidapi.com/profiles/posted-jobs'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_posts() -> dict: 
    '''Search Posts'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-posts'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_post_by_hashtag() -> dict: 
    '''Search Post by Hashtag'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-posts-by-hashtag'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post(url: Annotated[str, Field(description='')]) -> dict: 
    '''Get post details'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-post'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_reposts() -> dict: 
    '''Get post reposts by post url'''
    url = 'https://linkedin-data-api.p.rapidapi.com/posts/reposts'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_post_reactions() -> dict: 
    '''Get profiles that reacted to the post'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-post-reactions'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.post(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_user_articles(url: Annotated[str, Field(description='')] = None,
                      username: Annotated[str, Field(description='')] = None) -> dict: 
    '''Get user articles by profile with url or username'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-user-articles'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'username': username,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_article(url: Annotated[str, Field(description='')]) -> dict: 
    '''Get article with url'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-article'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_article_comments(url: Annotated[str, Field(description='')],
                         page: Annotated[str, Field(description='')] = None,
                         sort: Annotated[str, Field(description='')] = None) -> dict: 
    '''Get article comments with url'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-article-comments'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'page': page,
        'sort': sort,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def get_article_reactions(url: Annotated[str, Field(description='')],
                          page: Annotated[str, Field(description='')] = None) -> dict: 
    '''Get article reactions with url'''
    url = 'https://linkedin-data-api.p.rapidapi.com/get-article-reactions'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'page': page,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search_locations(keyword: Annotated[str, Field(description='')]) -> dict: 
    '''Search locations by keyword'''
    url = 'https://linkedin-data-api.p.rapidapi.com/search-locations'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def health_check() -> dict: 
    '''Health Check'''
    url = 'https://linkedin-data-api.p.rapidapi.com/health'
    headers = {'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")