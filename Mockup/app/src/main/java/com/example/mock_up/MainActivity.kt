package com.example.mock_up

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.widget.EditText
import android.widget.Toast
import kotlin.reflect.typeOf

class MainActivity : AppCompatActivity() {

    lateinit var passInput: EditText  // create variable for the user input

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        passInput = findViewById(R.id.passInput)  // get the value for the string from the input box
    }

    fun buttonClick(view: View?){
        println(passInput.text) // write user input to console for debugging
        if (passInput.text.toString() == "yolo") { //when password is correct
            val Intent = Intent(this,Activity2::class.java) // open activity 2
            startActivity(Intent) // open activity 2
        } else { //if password is incorrect
            //display a Toast message
            val myErrorToast = Toast.makeText(this, "wrong password", Toast.LENGTH_SHORT)
            myErrorToast.setGravity(Gravity.TOP, -400, 0)  // position tost on the top
            myErrorToast.show() // display tost
        }
        passInput.text.clear() // clear the field where the user wrote his/her input

    }
}