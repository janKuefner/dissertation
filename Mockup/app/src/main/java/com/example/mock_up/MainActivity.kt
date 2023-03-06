package com.example.mock_up

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import kotlin.reflect.typeOf

class MainActivity : AppCompatActivity() {

    lateinit var textInput: EditText

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        textInput = findViewById(R.id.textInput)
    }

    fun buttonClick(view: View?){
        println(textInput.text)

        if (textInput.text.toString() == "yolo") {
            println("Password korrekt")
        }

    }
}