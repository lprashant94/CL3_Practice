package com.example.lpras.trignometriccalculator;

import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Switch;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        final EditText edittext1=(EditText)findViewById(R.id.editText);
        final Switch switch1=(Switch)findViewById(R.id.switch1);
        switch1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!switch1.isChecked())
                {
                    switch1.setText("Degree");
                }
                else
                    switch1.setText("Radian");
            }
        });
       // boolean flag=switch1.getShowText();
        Button sine=(Button)findViewById(R.id.sine_button);
        assert sine != null;
        sine.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                double p=0.0;
                try{
                    if(switch1.isChecked()) {
                        Log.d("debug1","in if");
                        p=Math.sin(Double.parseDouble(edittext1.getText().toString()));
                    }
                    else
                    {
                        Log.d("debug","in else");
                        p = Math.sin(Math.toRadians(Double.parseDouble(edittext1.getText().toString())));

                    }
                }
                catch(Exception e)
                {

                }
                edittext1.setText(""+p);
            }
        });
        Button cosine=(Button)findViewById(R.id.cos_button);
        cosine.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                double p=0.0;
                try{
                    if(switch1.isChecked()) {
                        Log.d("debug1","in if");
                        p=Math.cos(Double.parseDouble(edittext1.getText().toString()));
                    }
                    else
                    {
                        Log.d("debug","in else");
                        p = Math.cos(Math.toRadians(Double.parseDouble(edittext1.getText().toString())));

                    }
                }
                catch(Exception e){}
                edittext1.setText("" + p);

            }
        });
        Button tan=(Button)findViewById(R.id.tan_button);
        tan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                double p=0.0;
                try{
                    if(switch1.isChecked()) {
                        Log.d("debug1","in if");
                        p=Math.tan(Double.parseDouble(edittext1.getText().toString()));
                    }
                    else
                    {
                        Log.d("debug","in else");
                        p = Math.tan(Math.toRadians(Double.parseDouble(edittext1.getText().toString())));

                    }
                }
                catch(Exception e){}
                edittext1.setText(""+p);
            }
        });
        Button clear=(Button)findViewById(R.id.clear_button);
        clear.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                edittext1.setText("");
            }
        });




        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
