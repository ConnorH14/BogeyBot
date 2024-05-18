class SearchPage:
    def __init__(self, page):
        self.page = page

    async def selectCourse(self, course):
        print(course)

        await self.page.locator("#secondarycode_vm_1_button").click()

        match course:
            case "1":
                await self.page.get_by_title("Quail Hollow Golf Club").click()
            case "2":
                await self.page.get_by_title("Warm Springs Golf Course").click()

        print("ping")
        return
