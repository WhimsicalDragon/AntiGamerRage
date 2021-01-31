intAnswer = _
    Msgbox("Whoa gamer you're being kinda loud there. Are you ok?", _
        vbYesNo, "Are you ok")
If intAnswer = vbYes Then
    Msgbox "You answered yes."
Else
    Msgbox "You answered no."
End If