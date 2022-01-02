# NotionDailyJournal
 Creating the daily entries for my Notion doc

# Motivation
In my attempt to better track and monitor my habits, I have a couple different journals which I (try to) update on a daily basis:
- Daily Journal
- Food Log
- Workout

And then have a overview database view that helps me see all of it together. Going in and creating them every day is a PITA

This is also an opportunity for me to better understand and test REST APIs (first time!) and familiarize myself with the [Notion API](https://developers.notion.com/).

# Solution
This program posts to the Notion API to create the pages in each database, and then uses the responses to link them all together in my metaJournal. Should save me precious seconds in the morning