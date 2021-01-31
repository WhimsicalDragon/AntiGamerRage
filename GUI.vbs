Dim FSO
Set FSO = CreateObject("Scripting.FileSystemObject")

intAnswer = _
    Msgbox("Whoa gamer you're being kinda loud there. Are you ok?", _
        vbYesNo, "Are you ok")
If intAnswer = vbYes Then
    Set OutPutFile = FSO.OpenTextFile("answer.txt" ,2 , True)
    OutPutFile.WriteLine("Yes")
    Set FSO= Nothing

Else
    Set OutPutFile = FSO.OpenTextFile("answer.txt" ,2 , True)
    OutPutFile.WriteLine("No")
    Set FSO= Nothing
End If