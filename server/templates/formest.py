$def with (form)

<form name="main" method="post"> 
$if not form.valid: <p class="error">Try again, AmeriCAN:</p>
$:form.render()
<input type="submit" />    </form>